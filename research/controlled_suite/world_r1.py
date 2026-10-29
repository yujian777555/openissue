"""Deterministic, in-memory tool environments for OpenIssue G1.

This module has no network, filesystem, email, calendar, or payment side effects.
Every domain is simulated in memory and uses deterministic rules.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any


class WorldError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class ToolSpec:
    name: str
    domain: str
    required: tuple[str, ...]
    optional: tuple[str, ...]
    arg_types: dict[str, str]
    handler: str
    idempotency_arg: str | None = None
    mutating: bool = False


TOOL_SPECS: dict[str, ToolSpec] = {
    # D1 — filesystem/repository artifacts (in-memory only)
    "fs.read_file": ToolSpec("fs.read_file", "D1", ("path",), (), {"path": "str"}, "fs_read"),
    "fs.write_file": ToolSpec("fs.write_file", "D1", ("path", "content", "idempotency_key"), ("overwrite",), {"path": "str", "content": "str", "idempotency_key": "str", "overwrite": "bool"}, "fs_write", "idempotency_key", True),
    "fs.move_file": ToolSpec("fs.move_file", "D1", ("source", "destination", "idempotency_key"), (), {"source": "str", "destination": "str", "idempotency_key": "str"}, "fs_move", "idempotency_key", True),
    "fs.delete_file": ToolSpec("fs.delete_file", "D1", ("path", "idempotency_key"), (), {"path": "str", "idempotency_key": "str"}, "fs_delete", "idempotency_key", True),
    "fs.list_files": ToolSpec("fs.list_files", "D1", (), ("prefix",), {"prefix": "str"}, "fs_list"),
    # D2 — calendar/resource scheduling
    "calendar.check_availability": ToolSpec("calendar.check_availability", "D2", ("resource", "start", "end"), (), {"resource": "str", "start": "int", "end": "int"}, "calendar_check"),
    "calendar.create_event": ToolSpec("calendar.create_event", "D2", ("event_id", "resource", "start", "end", "title", "idempotency_key"), (), {"event_id": "str", "resource": "str", "start": "int", "end": "int", "title": "str", "idempotency_key": "str"}, "calendar_create", "idempotency_key", True),
    "calendar.get_event": ToolSpec("calendar.get_event", "D2", ("event_id",), (), {"event_id": "str"}, "calendar_get"),
    "calendar.cancel_event": ToolSpec("calendar.cancel_event", "D2", ("event_id", "idempotency_key"), (), {"event_id": "str", "idempotency_key": "str"}, "calendar_cancel", "idempotency_key", True),
    # D3 — inventory and orders
    "inventory.get_stock": ToolSpec("inventory.get_stock", "D3", ("sku",), (), {"sku": "str"}, "inventory_get_stock"),
    "inventory.create_order": ToolSpec("inventory.create_order", "D3", ("order_id", "customer_id", "items", "idempotency_key"), (), {"order_id": "str", "customer_id": "str", "items": "list", "idempotency_key": "str"}, "inventory_create_order", "idempotency_key", True),
    "inventory.cancel_order": ToolSpec("inventory.cancel_order", "D3", ("order_id", "idempotency_key"), (), {"order_id": "str", "idempotency_key": "str"}, "inventory_cancel_order", "idempotency_key", True),
    "inventory.get_order": ToolSpec("inventory.get_order", "D3", ("order_id",), (), {"order_id": "str"}, "inventory_get_order"),
    # D4 — mock account ledger; no real funds or payment rails
    "ledger.get_balance": ToolSpec("ledger.get_balance", "D4", ("account_id",), (), {"account_id": "str"}, "ledger_get_balance"),
    "ledger.transfer": ToolSpec("ledger.transfer", "D4", ("from_account", "to_account", "amount", "idempotency_key"), (), {"from_account": "str", "to_account": "str", "amount": "int", "idempotency_key": "str"}, "ledger_transfer", "idempotency_key", True),
    "ledger.pay_bill": ToolSpec("ledger.pay_bill", "D4", ("account_id", "bill_id", "amount", "idempotency_key"), (), {"account_id": "str", "bill_id": "str", "amount": "int", "idempotency_key": "str"}, "ledger_pay_bill", "idempotency_key", True),
    "ledger.get_transaction": ToolSpec("ledger.get_transaction", "D4", ("transaction_id",), (), {"transaction_id": "str"}, "ledger_get_transaction"),
    # D5 — mock CRM/email; messages are queued in memory and never sent
    "crm.find_customer": ToolSpec("crm.find_customer", "D5", ("query",), (), {"query": "str"}, "crm_find_customer"),
    "crm.get_customer": ToolSpec("crm.get_customer", "D5", ("customer_id",), (), {"customer_id": "str"}, "crm_get_customer"),
    "crm.update_customer": ToolSpec("crm.update_customer", "D5", ("customer_id", "field", "value", "idempotency_key"), (), {"customer_id": "str", "field": "str", "value": "str", "idempotency_key": "str"}, "crm_update_customer", "idempotency_key", True),
    "crm.send_email": ToolSpec("crm.send_email", "D5", ("customer_id", "subject", "body", "idempotency_key"), (), {"customer_id": "str", "subject": "str", "body": "str", "idempotency_key": "str"}, "crm_send_email", "idempotency_key", True),
    "crm.get_email_status": ToolSpec("crm.get_email_status", "D5", ("email_id",), (), {"email_id": "str"}, "crm_get_email_status"),
}


def tool_profile(domain: str) -> list[dict[str, Any]]:
    """Return JSON-serializable tool schemas for one isolated domain."""
    if domain not in {"D1", "D2", "D3", "D4", "D5"}:
        raise ValueError(f"Unknown domain: {domain}")
    result = []
    for spec in TOOL_SPECS.values():
        if spec.domain != domain:
            continue
        properties: dict[str, Any] = {}
        for name, kind in spec.arg_types.items():
            schema_type = {"str": "string", "int": "integer", "bool": "boolean", "list": "array"}[kind]
            prop: dict[str, Any] = {"type": schema_type}
            if name == "idempotency_key":
                prop["minLength"] = 1
            if name == "amount" or name == "quantity":
                prop["minimum"] = 1
            if spec.name == "inventory.create_order" and name == "items":
                prop = {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["sku", "quantity"],
                        "properties": {
                            "sku": {"type": "string", "minLength": 1},
                            "quantity": {"type": "integer", "minimum": 1},
                        },
                    },
                }
            properties[name] = prop
        result.append({
            "name": spec.name,
            "description": _tool_description(spec.name),
            "input_schema": {
                "type": "object",
                "additionalProperties": False,
                "required": list(spec.required),
                "properties": properties,
            },
        })
    return result


def _tool_description(name: str) -> str:
    descriptions = {
        "fs.read_file": "Read a file from the in-memory mock filesystem.",
        "fs.write_file": "Create or overwrite a file in the in-memory mock filesystem; requires an idempotency key.",
        "fs.move_file": "Move a file to a destination that does not already exist; requires an idempotency key.",
        "fs.delete_file": "Delete an existing mock file; requires an idempotency key.",
        "fs.list_files": "List mock file paths, optionally filtered by prefix.",
        "calendar.check_availability": "Check half-open integer time interval [start,end) for a mock resource.",
        "calendar.create_event": "Create a mock calendar event if the resource interval is free.",
        "calendar.get_event": "Read a mock calendar event.",
        "calendar.cancel_event": "Cancel an active mock calendar event.",
        "inventory.get_stock": "Read available quantity for a mock SKU.",
        "inventory.create_order": "Atomically create an order and decrement stock for all listed items.",
        "inventory.cancel_order": "Cancel an active mock order and return its quantities to stock.",
        "inventory.get_order": "Read a mock order.",
        "ledger.get_balance": "Read a balance in the synthetic in-memory ledger.",
        "ledger.transfer": "Transfer integer units between synthetic accounts, rejecting overdrafts.",
        "ledger.pay_bill": "Pay a synthetic bill for its exact amount from an in-memory account.",
        "ledger.get_transaction": "Read a synthetic ledger transaction.",
        "crm.find_customer": "Find mock customer records matching a query; multiple matches are possible.",
        "crm.get_customer": "Read one mock customer record.",
        "crm.update_customer": "Update an allow-listed field on a mock customer record.",
        "crm.send_email": "Queue a mock email in memory; nothing is sent externally.",
        "crm.get_email_status": "Read the status of a queued mock email.",
    }
    return descriptions[name]


def _default_state() -> dict[str, Any]:
    return {
        "files": {},
        "calendar": {"events": {}},
        "inventory": {"stock": {}, "reservations": {}},
        "orders": {"items": {}},
        "ledger": {"accounts": {}, "transactions": {}, "bills": {}},
        "customers": {"items": {}},
        "emails": {"items": {}},
        "_meta": {"idempotency": {}},
    }


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(base)
    for key, value in override.items():
        if key == "_meta":
            continue
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _deep_merge(out[key], value)
        else:
            out[key] = deepcopy(value)
    return out


def _business_projection(state: dict[str, Any]) -> dict[str, Any]:
    return {key: deepcopy(value) for key, value in state.items() if key != "_meta"}


def _matches_type(value: Any, kind: str) -> bool:
    if kind == "str":
        return isinstance(value, str)
    if kind == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    if kind == "bool":
        return isinstance(value, bool)
    if kind == "list":
        return isinstance(value, list)
    return False


class World:
    """One task episode in one isolated, deterministic mock domain."""

    def __init__(self, domain: str, initial_state: dict[str, Any] | None = None, max_tool_calls: int | None = None):
        if domain not in {"D1", "D2", "D3", "D4", "D5"}:
            raise ValueError(f"Unknown domain: {domain}")
        if max_tool_calls is not None and max_tool_calls < 1:
            raise ValueError("max_tool_calls must be a positive integer when set.")
        self.domain = domain
        self.state = _deep_merge(_default_state(), initial_state or {})
        self.max_tool_calls = max_tool_calls
        self.call_count = 0
        self.events: list[dict[str, Any]] = []

    def snapshot(self) -> dict[str, Any]:
        """Return business state only; internal idempotency bookkeeping is excluded."""
        return _business_projection(self.state)

    def call(self, tool_name: str, args: dict[str, Any]) -> dict[str, Any]:
        event_base = {"index": len(self.events), "tool": tool_name, "args": deepcopy(args) if isinstance(args, dict) else args}
        if self.max_tool_calls is not None and self.call_count >= self.max_tool_calls:
            error = {"code": "CALL_LIMIT_REACHED", "message": "Episode tool-call limit has been reached."}
            self.events.append({**event_base, "status": "blocked", "schema_valid": True, "mutated": False,
                                "event_type": "tool_call_budget_exceeded", "result": None, "error": error})
            return {"ok": False, "error": error}
        self.call_count += 1
        if tool_name not in TOOL_SPECS or TOOL_SPECS[tool_name].domain != self.domain:
            return self._error(event_base, "TOOL_NOT_AVAILABLE", "Tool is not available in this isolated domain.", schema_valid=False)
        if not isinstance(args, dict):
            return self._error(event_base, "INVALID_ARGUMENTS", "Tool arguments must be an object.", schema_valid=False)
        spec = TOOL_SPECS[tool_name]
        missing = [name for name in spec.required if name not in args]
        allowed = set(spec.required) | set(spec.optional)
        extra = sorted(set(args) - allowed)
        if missing:
            return self._error(event_base, "MISSING_ARGUMENT", f"Missing required arguments: {missing}", schema_valid=False)
        if extra:
            return self._error(event_base, "UNEXPECTED_ARGUMENT", f"Unexpected arguments: {extra}", schema_valid=False)
        for name, value in args.items():
            kind = spec.arg_types[name]
            if not _matches_type(value, kind):
                return self._error(event_base, "INVALID_ARGUMENT_TYPE", f"Argument {name!r} must have type {kind}.", schema_valid=False)
        if spec.idempotency_arg and not args.get(spec.idempotency_arg, "").strip():
            return self._error(event_base, "INVALID_IDEMPOTENCY_KEY", "Idempotency key must be a non-empty string.", schema_valid=False)

        idem_key = args.get(spec.idempotency_arg) if spec.idempotency_arg else None
        signature_args = {k: deepcopy(v) for k, v in args.items() if k != spec.idempotency_arg}
        if idem_key:
            prior = self.state["_meta"]["idempotency"].get(idem_key)
            if prior:
                if prior["tool"] != tool_name or prior["args"] != signature_args:
                    return self._error(event_base, "IDEMPOTENCY_CONFLICT", "This idempotency key was already used for a different operation.", schema_valid=True)
                result = deepcopy(prior["result"])
                event = {**event_base, "status": "replayed", "schema_valid": True, "mutated": False,
                         "event_type": f"{tool_name}:replay", "result": deepcopy(result), "error": None}
                self.events.append(event)
                return {"ok": True, "result": result, "replayed": True}

        staged = deepcopy(self.state)
        try:
            result = self._dispatch(staged, spec.handler, args)
        except WorldError as exc:
            return self._error(event_base, exc.code, exc.message, schema_valid=True)
        changed = _business_projection(staged) != _business_projection(self.state)
        if idem_key:
            staged["_meta"]["idempotency"][idem_key] = {"tool": tool_name, "args": signature_args, "result": deepcopy(result)}
        self.state = staged
        event = {**event_base, "status": "success", "schema_valid": True, "mutated": changed,
                 "event_type": f"{tool_name}:success", "result": deepcopy(result), "error": None}
        self.events.append(event)
        return {"ok": True, "result": result, "replayed": False}

    def _error(self, base: dict[str, Any], code: str, message: str, schema_valid: bool) -> dict[str, Any]:
        event = {**base, "status": "error", "schema_valid": schema_valid, "mutated": False,
                 "event_type": "tool_schema_error" if not schema_valid else f"{base['tool']}:error",
                 "result": None, "error": {"code": code, "message": message}}
        self.events.append(event)
        return {"ok": False, "error": {"code": code, "message": message}}

    def _dispatch(self, state: dict[str, Any], handler: str, a: dict[str, Any]) -> dict[str, Any]:
        # D1 — filesystem
        if handler == "fs_read":
            if a["path"] not in state["files"]:
                raise WorldError("NOT_FOUND", "File path does not exist.")
            return {"path": a["path"], "content": state["files"][a["path"]]}
        if handler == "fs_write":
            path, content = a["path"], a["content"]
            if path in state["files"] and not a.get("overwrite", False) and state["files"][path] != content:
                raise WorldError("ALREADY_EXISTS", "Destination exists and overwrite is false.")
            created = path not in state["files"]
            changed = state["files"].get(path) != content
            state["files"][path] = content
            return {"path": path, "created": created, "changed": changed, "content_length": len(content)}
        if handler == "fs_move":
            src, dst = a["source"], a["destination"]
            if src not in state["files"]:
                raise WorldError("NOT_FOUND", "Source file does not exist.")
            if dst in state["files"]:
                raise WorldError("ALREADY_EXISTS", "Destination path already exists.")
            state["files"][dst] = state["files"].pop(src)
            return {"source": src, "destination": dst, "moved": True}
        if handler == "fs_delete":
            path = a["path"]
            if path not in state["files"]:
                raise WorldError("NOT_FOUND", "File path does not exist.")
            del state["files"][path]
            return {"path": path, "deleted": True}
        if handler == "fs_list":
            prefix = a.get("prefix", "")
            return {"paths": sorted(path for path in state["files"] if path.startswith(prefix))}

        # D2 — calendar; intervals are integer units and use [start,end).
        if handler == "calendar_check":
            start, end = a["start"], a["end"]
            if start >= end:
                raise WorldError("INVALID_INTERVAL", "start must be less than end.")
            conflicts = [e["event_id"] for e in state["calendar"]["events"].values()
                         if e["status"] == "active" and e["resource"] == a["resource"]
                         and start < e["end"] and e["start"] < end]
            return {"available": not conflicts, "conflicts": sorted(conflicts), "start": start, "end": end}
        if handler == "calendar_create":
            events = state["calendar"]["events"]
            if a["event_id"] in events:
                raise WorldError("ALREADY_EXISTS", "Event ID already exists.")
            if a["start"] >= a["end"]:
                raise WorldError("INVALID_INTERVAL", "start must be less than end.")
            conflicts = [e["event_id"] for e in events.values() if e["status"] == "active"
                         and e["resource"] == a["resource"] and a["start"] < e["end"] and e["start"] < a["end"]]
            if conflicts:
                raise WorldError("RESOURCE_CONFLICT", f"Resource interval conflicts with {sorted(conflicts)}.")
            event = {"event_id": a["event_id"], "resource": a["resource"], "start": a["start"],
                     "end": a["end"], "title": a["title"], "status": "active"}
            events[a["event_id"]] = event
            return deepcopy(event)
        if handler == "calendar_get":
            event = state["calendar"]["events"].get(a["event_id"])
            if event is None:
                raise WorldError("NOT_FOUND", "Event does not exist.")
            return deepcopy(event)
        if handler == "calendar_cancel":
            event = state["calendar"]["events"].get(a["event_id"])
            if event is None:
                raise WorldError("NOT_FOUND", "Event does not exist.")
            if event["status"] != "active":
                raise WorldError("PRECONDITION_FAILED", "Only active events can be canceled.")
            event["status"] = "canceled"
            return {"event_id": a["event_id"], "status": "canceled"}

        # D3 — inventory and order management.
        if handler == "inventory_get_stock":
            sku = a["sku"]
            if sku not in state["inventory"]["stock"]:
                raise WorldError("NOT_FOUND", "SKU does not exist.")
            return {"sku": sku, "quantity": state["inventory"]["stock"][sku]}
        if handler == "inventory_create_order":
            order_id = a["order_id"]
            if order_id in state["orders"]["items"]:
                raise WorldError("ALREADY_EXISTS", "Order ID already exists.")
            if not a["customer_id"].strip() or not a["items"]:
                raise WorldError("INVALID_ORDER", "customer_id and at least one item are required.")
            totals: dict[str, int] = {}
            for item in a["items"]:
                if not isinstance(item, dict) or set(item) != {"sku", "quantity"}:
                    raise WorldError("INVALID_ORDER_ITEM", "Each item must contain exactly sku and quantity.")
                if not isinstance(item["sku"], str) or not isinstance(item["quantity"], int) or isinstance(item["quantity"], bool) or item["quantity"] <= 0:
                    raise WorldError("INVALID_ORDER_ITEM", "Each SKU must be a string and quantity a positive integer.")
                totals[item["sku"]] = totals.get(item["sku"], 0) + item["quantity"]
            for sku, quantity in totals.items():
                if sku not in state["inventory"]["stock"]:
                    raise WorldError("NOT_FOUND", f"SKU {sku!r} does not exist.")
                if state["inventory"]["stock"][sku] < quantity:
                    raise WorldError("INSUFFICIENT_STOCK", f"Insufficient stock for {sku!r}.")
            for sku, quantity in totals.items():
                state["inventory"]["stock"][sku] -= quantity
            order = {"order_id": order_id, "customer_id": a["customer_id"],
                     "items": [{"sku": sku, "quantity": qty} for sku, qty in sorted(totals.items())],
                     "status": "active"}
            state["orders"]["items"][order_id] = order
            return deepcopy(order)
        if handler == "inventory_cancel_order":
            order = state["orders"]["items"].get(a["order_id"])
            if order is None:
                raise WorldError("NOT_FOUND", "Order does not exist.")
            if order["status"] != "active":
                raise WorldError("PRECONDITION_FAILED", "Only active orders can be canceled.")
            for item in order["items"]:
                state["inventory"]["stock"][item["sku"]] += item["quantity"]
            order["status"] = "canceled"
            return {"order_id": a["order_id"], "status": "canceled"}
        if handler == "inventory_get_order":
            order = state["orders"]["items"].get(a["order_id"])
            if order is None:
                raise WorldError("NOT_FOUND", "Order does not exist.")
            return deepcopy(order)

        # D4 — synthetic ledger.
        if handler == "ledger_get_balance":
            accounts = state["ledger"]["accounts"]
            if a["account_id"] not in accounts:
                raise WorldError("NOT_FOUND", "Account does not exist.")
            return {"account_id": a["account_id"], "balance": accounts[a["account_id"]]}
        if handler == "ledger_transfer":
            src, dst, amount = a["from_account"], a["to_account"], a["amount"]
            accounts = state["ledger"]["accounts"]
            if amount <= 0:
                raise WorldError("INVALID_AMOUNT", "amount must be a positive integer.")
            if src == dst:
                raise WorldError("INVALID_TRANSFER", "Source and destination accounts must differ.")
            if src not in accounts or dst not in accounts:
                raise WorldError("NOT_FOUND", "Source or destination account does not exist.")
            if accounts[src] < amount:
                raise WorldError("INSUFFICIENT_FUNDS", "Transfer would overdraw the source account.")
            txn_id = f"txn:{a['idempotency_key']}"
            accounts[src] -= amount
            accounts[dst] += amount
            txn = {"transaction_id": txn_id, "type": "transfer", "from_account": src,
                   "to_account": dst, "amount": amount, "status": "posted"}
            state["ledger"]["transactions"][txn_id] = txn
            return deepcopy(txn)
        if handler == "ledger_pay_bill":
            accounts, bills = state["ledger"]["accounts"], state["ledger"]["bills"]
            bill = bills.get(a["bill_id"])
            if bill is None:
                raise WorldError("NOT_FOUND", "Bill does not exist.")
            if bill.get("status") != "unpaid":
                raise WorldError("PRECONDITION_FAILED", "Bill is not unpaid.")
            if a["amount"] <= 0 or a["amount"] != bill["amount"]:
                raise WorldError("AMOUNT_MISMATCH", "Payment must equal the exact positive bill amount.")
            if a["account_id"] not in accounts:
                raise WorldError("NOT_FOUND", "Account does not exist.")
            if accounts[a["account_id"]] < a["amount"]:
                raise WorldError("INSUFFICIENT_FUNDS", "Payment would overdraw the account.")
            txn_id = f"txn:{a['idempotency_key']}"
            accounts[a["account_id"]] -= a["amount"]
            bill["status"] = "paid"
            txn = {"transaction_id": txn_id, "type": "bill_payment", "account_id": a["account_id"],
                   "bill_id": a["bill_id"], "amount": a["amount"], "status": "posted"}
            state["ledger"]["transactions"][txn_id] = txn
            return deepcopy(txn)
        if handler == "ledger_get_transaction":
            txn = state["ledger"]["transactions"].get(a["transaction_id"])
            if txn is None:
                raise WorldError("NOT_FOUND", "Transaction does not exist.")
            return deepcopy(txn)

        # D5 — customer records and simulated email queue.
        if handler == "crm_find_customer":
            query = a["query"].strip().casefold()
            if not query:
                raise WorldError("INVALID_QUERY", "query must not be empty.")
            matches = []
            for customer in state["customers"]["items"].values():
                fields = [customer.get("customer_id", ""), customer.get("name", ""), customer.get("email", "")]
                if any(query in str(value).casefold() for value in fields):
                    matches.append(deepcopy(customer))
            return {"matches": sorted(matches, key=lambda c: c["customer_id"]), "count": len(matches)}
        if handler == "crm_get_customer":
            customer = state["customers"]["items"].get(a["customer_id"])
            if customer is None:
                raise WorldError("NOT_FOUND", "Customer does not exist.")
            return deepcopy(customer)
        if handler == "crm_update_customer":
            customer = state["customers"]["items"].get(a["customer_id"])
            if customer is None:
                raise WorldError("NOT_FOUND", "Customer does not exist.")
            allowed_fields = {"name", "email", "phone", "address", "tier"}
            if a["field"] not in allowed_fields:
                raise WorldError("FIELD_NOT_ALLOWED", "Field is not on the customer update allow-list.")
            old_value = customer.get(a["field"])
            customer[a["field"]] = a["value"]
            return {"customer_id": a["customer_id"], "field": a["field"], "old_value": old_value,
                    "new_value": a["value"], "changed": old_value != a["value"]}
        if handler == "crm_send_email":
            customer = state["customers"]["items"].get(a["customer_id"])
            if customer is None:
                raise WorldError("NOT_FOUND", "Customer does not exist.")
            if not customer.get("email"):
                raise WorldError("PRECONDITION_FAILED", "Customer has no email address.")
            email_id = f"email:{a['idempotency_key']}"
            if email_id in state["emails"]["items"]:
                raise WorldError("ALREADY_EXISTS", "Email ID already exists.")
            email = {"email_id": email_id, "customer_id": a["customer_id"], "to": customer["email"],
                     "subject": a["subject"], "body": a["body"], "status": "queued"}
            state["emails"]["items"][email_id] = email
            return {"email_id": email_id, "status": "queued", "to": customer["email"]}
        if handler == "crm_get_email_status":
            email = state["emails"]["items"].get(a["email_id"])
            if email is None:
                raise WorldError("NOT_FOUND", "Email does not exist.")
            return {"email_id": a["email_id"], "status": email["status"]}
        raise RuntimeError(f"Unimplemented tool handler: {handler}")


def _pointer_get(root: Any, pointer: str) -> tuple[bool, Any]:
    """Resolve an RFC 6901-style JSON Pointer. Empty pointer means the root."""
    if pointer == "":
        return True, root
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        return False, None
    current = root
    for raw in pointer[1:].split("/"):
        key = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and key.isdigit() and int(key) < len(current):
            current = current[int(key)]
        else:
            return False, None
    return True, current


def _invariant_value(state: dict[str, Any], inv: dict[str, Any]) -> bool:
    exists, actual = _pointer_get(state, inv["state_path"])
    op = inv["operator"]
    expected = inv.get("expected")
    if op == "exists":
        return exists
    if op == "not_exists":
        return not exists
    if not exists:
        return False
    try:
        if op == "eq":
            return actual == expected
        if op == "ne":
            return actual != expected
        if op == "gte":
            return actual >= expected
        if op == "lte":
            return actual <= expected
        if op == "contains":
            return expected in actual
        if op == "not_contains":
            return expected not in actual
        if op == "subset_of":
            return set(actual).issubset(set(expected))
    except (TypeError, ValueError):
        return False
    raise ValueError(f"Unsupported invariant operator: {op}")


def _successful(event: dict[str, Any]) -> bool:
    return event.get("status") in {"success", "replayed"}


def evaluate_case(case: dict[str, Any], state: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
    """Evaluate deterministic state invariants plus optional trace constraints."""
    oracle = case["oracle"]
    required_failures = [inv for inv in oracle.get("required_invariants", []) if not _invariant_value(state, inv)]
    forbidden_violations = [inv for inv in oracle.get("forbidden_invariants", []) if _invariant_value(state, inv)]
    forbidden_events = []
    for rule in oracle.get("forbidden_events", []):
        matching = [e for e in events if e.get("event_type") == rule["event_type"]]
        if matching:
            forbidden_events.append({"rule": rule, "events": matching})

    constraints = case.get("trace_constraints", {})
    successful = [e for e in events if _successful(e)]
    trace_failures: list[dict[str, Any]] = []
    cursor = -1
    for tool_name in constraints.get("ordered_successful_tools", []):
        found = next((i for i, e in enumerate(events) if i > cursor and e.get("tool") == tool_name and _successful(e)), None)
        if found is None:
            trace_failures.append({"kind": "ordered_successful_tools", "missing_or_out_of_order": tool_name})
            break
        cursor = found
    for tool_name in constraints.get("forbidden_successful_tools", []):
        hits = [e for e in successful if e.get("tool") == tool_name]
        if hits:
            trace_failures.append({"kind": "forbidden_successful_tool", "tool": tool_name, "events": hits})
    for tool_name, maximum in constraints.get("max_successful_calls", {}).items():
        count = sum(1 for e in successful if e.get("tool") == tool_name)
        if count > maximum:
            trace_failures.append({"kind": "max_successful_calls", "tool": tool_name, "count": count, "maximum": maximum})
    for tool_name, minimum in constraints.get("min_successful_calls", {}).items():
        count = sum(1 for e in successful if e.get("tool") == tool_name)
        if count < minimum:
            trace_failures.append({"kind": "min_successful_calls", "tool": tool_name, "count": count, "minimum": minimum})
    for tool_name, maximum in constraints.get("max_mutating_successes", {}).items():
        count = sum(1 for e in events if e.get("tool") == tool_name and e.get("status") == "success" and e.get("mutated"))
        if count > maximum:
            trace_failures.append({"kind": "max_mutating_successes", "tool": tool_name, "count": count, "maximum": maximum})
    for tool_name, minimum in constraints.get("min_error_calls", {}).items():
        count = sum(1 for e in events if e.get("tool") == tool_name and e.get("status") == "error")
        if count < minimum:
            trace_failures.append({"kind": "min_error_calls", "tool": tool_name, "count": count, "minimum": minimum})
    for tool_name, minimum in constraints.get("min_replayed_calls", {}).items():
        count = sum(1 for e in events if e.get("tool") == tool_name and e.get("status") == "replayed")
        if count < minimum:
            trace_failures.append({"kind": "min_replayed_calls", "tool": tool_name, "count": count, "minimum": minimum})
    for rule in constraints.get("required_arg_match", []):
        producer = next((e for e in events if e.get("tool") == rule["producer_tool"] and _successful(e)), None)
        consumer = next((e for e in events if e.get("tool") == rule["consumer_tool"] and _successful(e)), None)
        if producer is None or consumer is None:
            trace_failures.append({"kind": "required_arg_match", "rule": rule, "reason": "producer or consumer call missing"})
            continue
        source = producer.get(rule.get("source", "result"), {})
        exists, value = _pointer_get(source, rule["source_pointer"])
        if not exists or consumer.get("args", {}).get(rule["consumer_arg"]) != value:
            trace_failures.append({"kind": "required_arg_match", "rule": rule,
                                   "expected_value": value if exists else None,
                                   "actual_value": consumer.get("args", {}).get(rule["consumer_arg"])})
    passed = not (required_failures or forbidden_violations or forbidden_events or trace_failures)
    return {
        "passed": passed,
        "required_failures": required_failures,
        "forbidden_violations": forbidden_violations,
        "forbidden_events": forbidden_events,
        "trace_failures": trace_failures,
        "event_count": len(events),
        "successful_call_count": len(successful),
        "mutating_success_count": sum(1 for e in events if e.get("status") == "success" and e.get("mutated")),
    }


def run_actions(domain: str, initial_state: dict[str, Any], actions: list[dict[str, Any]], max_tool_calls: int | None = None) -> tuple[World, list[dict[str, Any]]]:
    """Execute a deterministic action list. Each action has tool and args keys."""
    world = World(domain, initial_state, max_tool_calls=max_tool_calls)
    results = []
    for action in actions:
        if set(action) != {"tool", "args"}:
            raise ValueError("Each action must contain exactly 'tool' and 'args'.")
        results.append(world.call(action["tool"], action["args"]))
    return world, results


def run_case_actions(case: dict[str, Any], actions: list[dict[str, Any]]) -> tuple[World, list[dict[str, Any]]]:
    """Run reference actions under the task's declared tool-call budget."""
    return run_actions(case["domain_id"], case["initial_state"], actions,
                       max_tool_calls=case["limits"]["max_tool_calls"])
