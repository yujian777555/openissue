"""Unit and smoke tests for the deterministic G1 controlled suite."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from world_r1 import World, evaluate_case, run_case_actions, tool_profile, _json_equal  # noqa: E402

CASES = [json.loads(line) for line in (ROOT / "pilot_cases_r1.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
BY_ID = {case["case_id"]: case for case in CASES}

def _resolve_ref(root, ref):
    current = root
    for token in ref.removeprefix("#/").split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[token]
    return current


def _validate_schema_subset(value, spec, path, root, errors):
    """Validate the JSON Schema keywords used by our pinned case schema."""
    if "$ref" in spec:
        _validate_schema_subset(value, _resolve_ref(root, spec["$ref"]), path, root, errors)
        return
    if "const" in spec and not _json_equal(value, spec["const"]):
        errors.append(f"{path}: const mismatch")
    if "enum" in spec and not any(_json_equal(value, option) for option in spec["enum"]):
        errors.append(f"{path}: enum mismatch")
    expected_types = spec.get("type")
    if expected_types:
        if not isinstance(expected_types, list):
            expected_types = [expected_types]
        def matches(kind):
            if kind == "object":
                return isinstance(value, dict)
            if kind == "array":
                return isinstance(value, list)
            if kind == "string":
                return isinstance(value, str)
            if kind == "integer":
                return type(value) is int
            if kind == "number":
                return type(value) in (int, float)
            if kind == "boolean":
                return type(value) is bool
            if kind == "null":
                return value is None
            return False
        if not any(matches(kind) for kind in expected_types):
            errors.append(f"{path}: type mismatch, expected {expected_types}")
            return
    if isinstance(value, str):
        if len(value) < spec.get("minLength", 0):
            errors.append(f"{path}: below minLength")
        if "pattern" in spec and not re.search(spec["pattern"], value):
            errors.append(f"{path}: pattern mismatch")
    if type(value) in (int, float):
        if value < spec.get("minimum", float("-inf")):
            errors.append(f"{path}: below minimum")
        if value > spec.get("maximum", float("inf")):
            errors.append(f"{path}: above maximum")
    if isinstance(value, list):
        if len(value) < spec.get("minItems", 0):
            errors.append(f"{path}: below minItems")
        if "items" in spec:
            for index, item in enumerate(value):
                _validate_schema_subset(item, spec["items"], f"{path}[{index}]", root, errors)
    if isinstance(value, dict):
        for key in spec.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required key {key}")
        properties = spec.get("properties", {})
        for key, item in value.items():
            if key in properties:
                _validate_schema_subset(item, properties[key], f"{path}.{key}", root, errors)
            elif spec.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected key {key}")
            elif isinstance(spec.get("additionalProperties"), dict):
                _validate_schema_subset(item, spec["additionalProperties"], f"{path}.{key}", root, errors)


ACTIONS = {
    "F01-D1-V1": [
        {"tool": "fs.read_file", "args": {"path": "/docs/report.txt"}},
        {"tool": "fs.write_file", "args": {"path": "/docs/report.txt", "content": "approved", "overwrite": True, "idempotency_key": "f01-write"}},
    ],
    "F02-D1-V1": [
        {"tool": "fs.read_file", "args": {"path": "/docs/source.txt"}},
        {"tool": "fs.write_file", "args": {"path": "/archive/copy.txt", "content": "approved-v7", "idempotency_key": "f02-copy"}},
    ],
    "F03-D1-V1": [
        {"tool": "fs.write_file", "args": {"path": "/docs/status.txt", "content": "verified", "overwrite": True, "idempotency_key": "f03-write"}},
        {"tool": "fs.read_file", "args": {"path": "/docs/status.txt"}},
    ],
    "F04-D2-V1": [
        {"tool": "calendar.check_availability", "args": {"resource": "room-A", "start": 12, "end": 14}},
        {"tool": "calendar.create_event", "args": {"event_id": "EVT-NEW", "resource": "room-A", "start": 12, "end": 14, "title": "Review", "idempotency_key": "f04-event"}},
    ],
    "F05-D4-V1": [
        {"tool": "ledger.transfer", "args": {"from_account": "A", "to_account": "B", "amount": 30, "idempotency_key": "transfer-001"}},
        {"tool": "ledger.transfer", "args": {"from_account": "A", "to_account": "B", "amount": 30, "idempotency_key": "transfer-001"}},
    ],
    "F06-D5-V1": [
        {"tool": "crm.update_customer", "args": {"customer_id": "C-1", "field": "tier", "value": "gold", "idempotency_key": "update-001"}},
        {"tool": "crm.send_email", "args": {"customer_id": "C-1", "subject": "Tier updated", "body": "Your tier is now gold.", "idempotency_key": "notify-001"}},
    ],
    "F07-D5-V1": [
        {"tool": "crm.find_customer", "args": {"query": "Alex Lee"}},
    ],
    "F08-D4-V1": [
        {"tool": "ledger.pay_bill", "args": {"account_id": "A", "bill_id": "BILL-1", "amount": 50, "idempotency_key": "amount-mismatch-001"}},
    ],
    "F09-D2-V1": [
        {"tool": "calendar.check_availability", "args": {"resource": "room-A", "start": 10, "end": 12}},
    ],
    "F10-D3-V1": [
        {"tool": "inventory.get_order", "args": {"order_id": "ORD-200"}},
        {"tool": "inventory.cancel_order", "args": {"order_id": "ORD-200", "idempotency_key": "cancel-order-200"}},
    ],
    "F11-D1-V1": [
        {"tool": "fs.move_file", "args": {"source": "/docs/draft.txt", "destination": "/docs/final.txt", "idempotency_key": "move-001"}},
        {"tool": "fs.write_file", "args": {"path": "/docs/summary.txt", "content": "new-summary", "idempotency_key": "write-summary-001"}},
        {"tool": "fs.move_file", "args": {"source": "/docs/final.txt", "destination": "/docs/draft.txt", "idempotency_key": "compensate-001"}},
    ],
    "F12-D5-V1": [
        {"tool": "crm.update_customer", "args": {"customer_id": "C-1", "field": "phone", "value": "555-0199", "idempotency_key": "phone-update-001"}},
    ],
}


class ToolProfileTests(unittest.TestCase):
    def test_each_domain_profile_is_isolated(self):
        expected_prefix = {"D1": "fs.", "D2": "calendar.", "D3": "inventory.", "D4": "ledger.", "D5": "crm."}
        for domain, prefix in expected_prefix.items():
            profile = tool_profile(domain)
            self.assertTrue(profile)
            self.assertTrue(all(item["name"].startswith(prefix) for item in profile))
            self.assertTrue(all(item["input_schema"]["additionalProperties"] is False for item in profile))

    def test_order_item_schema_and_positive_amount_are_exposed(self):
        d3 = {item["name"]: item["input_schema"] for item in tool_profile("D3")}
        item_schema = d3["inventory.create_order"]["properties"]["items"]
        self.assertEqual(item_schema["type"], "array")
        self.assertEqual(item_schema["minItems"], 1)
        self.assertEqual(item_schema["items"]["required"], ["sku", "quantity"])
        self.assertEqual(item_schema["items"]["properties"]["quantity"]["minimum"], 1)
        d4 = {item["name"]: item["input_schema"] for item in tool_profile("D4")}
        self.assertEqual(d4["ledger.transfer"]["properties"]["amount"]["minimum"], 1)
        self.assertEqual(d4["ledger.transfer"]["properties"]["idempotency_key"]["minLength"], 1)

    def test_unknown_domain_tool_is_rejected_without_mutation(self):
        world = World("D1", {"files": {"/a.txt": "keep"}})
        before = world.snapshot()
        result = world.call("calendar.create_event", {"event_id": "E1"})
        self.assertFalse(result["ok"])
        self.assertEqual(result["error"]["code"], "TOOL_NOT_AVAILABLE")
        self.assertEqual(world.snapshot(), before)

    def test_extra_or_mistyped_arguments_are_rejected(self):
        world = World("D1", {"files": {"/a.txt": "keep"}})
        before = world.snapshot()
        extra = world.call("fs.read_file", {"path": "/a.txt", "unexpected": 1})
        wrong_type = world.call("fs.read_file", {"path": 4})
        self.assertEqual(extra["error"]["code"], "UNEXPECTED_ARGUMENT")
        self.assertEqual(wrong_type["error"]["code"], "INVALID_ARGUMENT_TYPE")
        self.assertEqual(world.snapshot(), before)
        self.assertFalse(world.events[0]["schema_valid"])

    def test_episode_tool_call_budget_blocks_extra_calls(self):
        world = World("D1", {"files": {"/a.txt": "keep"}}, max_tool_calls=1)
        first = world.call("fs.read_file", {"path": "/a.txt"})
        before = world.snapshot()
        blocked = world.call("fs.write_file", {"path": "/a.txt", "content": "changed", "overwrite": True, "idempotency_key": "over-budget"})
        blocked_again = world.call("fs.write_file", {"path": 4, "content": "changed", "idempotency_key": "over-budget-2"})
        self.assertTrue(first["ok"])
        self.assertEqual(blocked["error"]["code"], "CALL_LIMIT_REACHED")
        self.assertEqual(blocked_again["error"]["code"], "CALL_LIMIT_REACHED")
        self.assertEqual(world.snapshot(), before)
        self.assertEqual(world.call_count, 1)  # only the budget-admitted attempt consumes budget
        self.assertEqual(world.attempt_count, 3)
        self.assertEqual(len(world.events), world.attempt_count)
        self.assertEqual([e["index"] for e in world.events], [0, 1, 2])
        self.assertEqual([e["status"] for e in world.events], ["success", "blocked", "blocked"])
        self.assertIsNone(world.events[-1]["schema_valid"])  # validation was skipped after budget rejection
        result = evaluate_case({
            "oracle": {"required_invariants": [{"state_path": "/files/~1a.txt", "operator": "eq", "expected": "keep"}]}
        }, world.snapshot(), world.events)
        self.assertTrue(result["passed"])
        self.assertEqual(result["call_attempt_count"], 3)
        self.assertEqual(result["budgeted_call_count"], 1)
        self.assertEqual(result["blocked_call_count"], 2)

    def test_budget_rejects_non_integer_limits(self):
        for invalid in (True, 1.5, 0):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    World("D1", {}, max_tool_calls=invalid)

    def test_failed_move_is_atomic(self):
        world = World("D1", {"files": {"/src": "x", "/dst": "y"}})
        before = world.snapshot()
        result = world.call("fs.move_file", {"source": "/src", "destination": "/dst", "idempotency_key": "move"})
        self.assertEqual(result["error"]["code"], "ALREADY_EXISTS")
        self.assertEqual(world.snapshot(), before)
        self.assertFalse(world.events[0]["mutated"])

    def test_calendar_uses_half_open_intervals(self):
        world = World("D2", {"calendar": {"events": {"E1": {"event_id": "E1", "resource": "R", "start": 9, "end": 10, "title": "a", "status": "active"}}}})
        adjacent = world.call("calendar.check_availability", {"resource": "R", "start": 10, "end": 11})
        overlap = world.call("calendar.check_availability", {"resource": "R", "start": 9, "end": 10})
        self.assertTrue(adjacent["result"]["available"])
        self.assertFalse(overlap["result"]["available"])

    def test_order_creation_is_atomic_on_insufficient_stock(self):
        world = World("D3", {"inventory": {"stock": {"SKU-A": 2, "SKU-B": 0}}})
        before = world.snapshot()
        result = world.call("inventory.create_order", {"order_id": "O1", "customer_id": "C1",
            "items": [{"sku": "SKU-A", "quantity": 1}, {"sku": "SKU-B", "quantity": 1}], "idempotency_key": "order-1"})
        self.assertEqual(result["error"]["code"], "INSUFFICIENT_STOCK")
        self.assertEqual(world.snapshot(), before)

    def test_idempotency_replay_prevents_duplicate_transfer(self):
        world = World("D4", {"ledger": {"accounts": {"A": 100, "B": 20}, "transactions": {}, "bills": {}}})
        args = {"from_account": "A", "to_account": "B", "amount": 25, "idempotency_key": "k1"}
        first = world.call("ledger.transfer", args)
        second = world.call("ledger.transfer", args)
        self.assertTrue(first["ok"])
        self.assertTrue(second["ok"])
        self.assertFalse(first["replayed"])
        self.assertTrue(second["replayed"])
        self.assertEqual(world.state["ledger"]["accounts"], {"A": 75, "B": 45})
        self.assertEqual(len(world.state["ledger"]["transactions"]), 1)
        self.assertEqual(sum(e["mutated"] for e in world.events), 1)

    def test_idempotency_key_reuse_with_different_payload_is_rejected(self):
        world = World("D4", {"ledger": {"accounts": {"A": 100, "B": 20, "C": 10}, "transactions": {}, "bills": {}}})
        world.call("ledger.transfer", {"from_account": "A", "to_account": "B", "amount": 10, "idempotency_key": "same"})
        result = world.call("ledger.transfer", {"from_account": "A", "to_account": "C", "amount": 10, "idempotency_key": "same"})
        self.assertEqual(result["error"]["code"], "IDEMPOTENCY_CONFLICT")
        self.assertEqual(world.state["ledger"]["accounts"], {"A": 90, "B": 30, "C": 10})

    def test_customer_search_can_return_multiple_matches_without_mutation(self):
        case = BY_ID["F07-D5-V1"]
        world, _ = run_case_actions(case, ACTIONS[case["case_id"]])
        self.assertEqual(world.events[0]["result"]["count"], 2)
        self.assertEqual(world.state["customers"]["items"]["C-11"]["tier"], "silver")
        self.assertEqual(world.state["customers"]["items"]["C-12"]["tier"], "silver")


    def test_idempotency_key_is_scoped_per_tool(self):
        world = World("D1", {"files": {"/source.txt": "v1"}})
        first = world.call("fs.write_file", {
            "path": "/new.txt", "content": "new", "idempotency_key": "shared-key"
        })
        second = world.call("fs.move_file", {
            "source": "/source.txt", "destination": "/moved.txt", "idempotency_key": "shared-key"
        })
        self.assertTrue(first["ok"])
        self.assertTrue(second["ok"])
        self.assertEqual(world.snapshot()["files"], {"/new.txt": "new", "/moved.txt": "v1"})

class PilotCaseTests(unittest.TestCase):
    def test_pilot_records_validate_against_case_schema(self):
        schema = json.loads((ROOT / "task_case_schema_r1.json").read_text(encoding="utf-8"))
        errors = []
        for case in CASES:
            _validate_schema_subset(case, schema, case["case_id"], schema, errors)
        self.assertEqual(errors, [])

    def test_manifest_of_pilot_cases_has_all_twelve_families_and_unique_ids(self):
        self.assertEqual(len(CASES), 12)
        self.assertEqual(len(BY_ID), 12)
        self.assertEqual({c["family_id"] for c in CASES}, {f"F{i:02d}" for i in range(1, 13)})
        self.assertTrue(all(re.fullmatch(r"F(0[1-9]|1[0-2])-D[1-5]-V[1-2]", c["case_id"]) for c in CASES))
        self.assertTrue(all(c["provenance"]["external_case_text_copied"] is False for c in CASES))

    def test_reference_smoke_actions_satisfy_each_case_oracle_and_trace(self):
        self.assertEqual(set(ACTIONS), set(BY_ID))
        failures = []
        for case_id, case in BY_ID.items():
            world, results = run_case_actions(case, ACTIONS[case_id])
            evaluation = evaluate_case(case, world.snapshot(), world.events)
            if not evaluation["passed"]:
                failures.append({"case_id": case_id, "evaluation": evaluation, "results": results})
        self.assertEqual(failures, [])

    def test_oracle_detects_wrong_final_state(self):
        case = BY_ID["F01-D1-V1"]
        world = World(case["domain_id"], case["initial_state"])
        world.call("fs.write_file", {"path": "/docs/report.txt", "content": "wrong", "overwrite": True, "idempotency_key": "wrong"})
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertFalse(evaluation["passed"])
        self.assertTrue(evaluation["required_failures"])
        self.assertTrue(evaluation["trace_failures"])

    def test_trace_checker_detects_wrong_result_argument_propagation(self):
        case = BY_ID["F02-D1-V1"]
        world = World(case["domain_id"], case["initial_state"])
        world.call("fs.read_file", {"path": "/docs/source.txt"})
        world.call("fs.write_file", {"path": "/archive/copy.txt", "content": "not-the-source", "idempotency_key": "bad-copy"})
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertFalse(evaluation["passed"])
        self.assertTrue(any(x["kind"] == "required_arg_match" for x in evaluation["trace_failures"]))

    def test_trace_checker_checks_every_successful_consumer_call(self):
        case = BY_ID["F02-D1-V1"]
        world = World(case["domain_id"], case["initial_state"])
        world.call("fs.read_file", {"path": "/docs/source.txt"})
        world.call("fs.write_file", {
            "path": "/archive/copy.txt", "content": "approved-v7",
            "idempotency_key": "good-copy",
        })
        world.call("fs.read_file", {"path": "/docs/source.txt"})
        world.call("fs.write_file", {
            "path": "/archive/second.txt", "content": "wrong",
            "idempotency_key": "bad-second-copy",
        })
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertFalse(evaluation["passed"])
        self.assertTrue(any(
            failure["kind"] == "required_arg_match"
            and failure.get("consumer_index") == 3
            for failure in evaluation["trace_failures"]
        ))

    def test_json_oracle_equality_does_not_conflate_boolean_and_integer(self):
        case = {
            "oracle": {
                "required_invariants": [
                    {"state_path": "/flag", "operator": "eq", "expected": 1}
                ],
                "forbidden_invariants": [],
                "forbidden_events": [],
            }
        }
        evaluation = evaluate_case(case, {"flag": True}, [])
        self.assertFalse(evaluation["passed"])
        self.assertEqual(len(evaluation["required_failures"]), 1)

    def test_state_pointer_escapes_slashes(self):
        case = BY_ID["F01-D1-V1"]
        world = World("D1", case["initial_state"])
        self.assertEqual(world.snapshot()["files"]["/docs/report.txt"], "draft")
        result = evaluate_case(case, world.snapshot(), [])
        self.assertFalse(result["passed"])


    def test_booking_oracle_accepts_agent_chosen_event_id(self):
        case = BY_ID["F04-D2-V1"]
        world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
        world.call("calendar.check_availability", {"resource": "room-A", "start": 12, "end": 14})
        world.call("calendar.create_event", {
            "event_id": "agent-chosen-event-42", "resource": "room-A", "start": 12, "end": 14,
            "title": "Review", "idempotency_key": "agent-event-key"
        })
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertTrue(evaluation["passed"], evaluation)

    def test_booking_oracle_rejects_wrong_resource_time_or_title(self):
        case = BY_ID["F04-D2-V1"]
        variants = [
            {"resource": "room-B", "start": 12, "end": 14, "title": "Review"},
            {"resource": "room-A", "start": 11, "end": 13, "title": "Review"},
            {"resource": "room-A", "start": 12, "end": 14, "title": "Wrong title"},
        ]
        for index, values in enumerate(variants):
            with self.subTest(values=values):
                world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
                world.call("calendar.check_availability", {"resource": "room-A", "start": 12, "end": 14})
                world.call("calendar.create_event", {
                    "event_id": f"agent-event-{index}", **values, "idempotency_key": f"agent-key-{index}"
                })
                self.assertFalse(evaluate_case(case, world.snapshot(), world.events)["passed"])

    def test_transfer_oracle_accepts_agent_chosen_idempotency_key(self):
        case = BY_ID["F05-D4-V1"]
        world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
        args = {"from_account": "A", "to_account": "B", "amount": 30, "idempotency_key": "agent-transfer-key"}
        world.call("ledger.transfer", args)
        world.call("ledger.transfer", args)
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertTrue(evaluation["passed"], evaluation)

    def test_email_oracle_accepts_agent_chosen_idempotency_key(self):
        case = BY_ID["F06-D5-V1"]
        world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
        world.call("crm.update_customer", {
            "customer_id": "C-1", "field": "tier", "value": "gold", "idempotency_key": "agent-update-key"
        })
        world.call("crm.send_email", {
            "customer_id": "C-1", "subject": "Tier updated", "body": "Your tier is now gold.",
            "idempotency_key": "agent-email-key"
        })
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertTrue(evaluation["passed"], evaluation)

    def test_compensation_oracle_rejects_unrelated_move_round_trip(self):
        case = BY_ID["F11-D1-V1"]
        world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
        world.call("fs.move_file", {
            "source": "/docs/summary.txt", "destination": "/docs/temp.txt", "idempotency_key": "wrong-move-1"
        })
        failed_write = world.call("fs.write_file", {
            "path": "/docs/temp.txt", "content": "unrequested", "idempotency_key": "wrong-write"
        })
        world.call("fs.move_file", {
            "source": "/docs/temp.txt", "destination": "/docs/summary.txt", "idempotency_key": "wrong-move-2"
        })
        self.assertEqual(failed_write["error"]["code"], "ALREADY_EXISTS")
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertEqual(evaluation["required_failures"], [])
        self.assertEqual(evaluation["forbidden_violations"], [])
        self.assertFalse(evaluation["passed"])
        self.assertTrue(any(f["kind"] == "ordered_calls" for f in evaluation["trace_failures"]))

    def test_oracle_rejects_unrequested_side_effects(self):
        case = BY_ID["F03-D1-V1"]
        world, _ = run_case_actions(case, ACTIONS[case["case_id"]])
        world.call("fs.write_file", {
            "path": "/docs/unrequested.txt", "content": "extra", "idempotency_key": "extra-side-effect"
        })
        evaluation = evaluate_case(case, world.snapshot(), world.events)
        self.assertFalse(evaluation["passed"])
        self.assertTrue(any(
            failure.get("state_path") == "/files" for failure in evaluation["required_failures"]
        ))

    def test_cross_turn_reference_is_in_context_not_user_request(self):
        case = BY_ID["F10-D3-V1"]
        self.assertNotIn("ORD-200", case["task"]["user_request"])
        self.assertIn("ORD-200", case["task"]["context"])

    def test_invariant_operators_are_type_safe(self):
        def passed(operator, expected, actual=True):
            case = {"oracle": {"required_invariants": [{
                "state_path": "/flag", "operator": operator, "expected": expected
            }]}}
            return evaluate_case(case, {"flag": actual}, [])["passed"]
        self.assertTrue(passed("ne", 1, True))  # JSON true is not numeric 1
        self.assertFalse(passed("lte", 10, True))  # booleans are not numeric
        self.assertFalse(passed("contains", 1, [True]))
        self.assertTrue(passed("not_contains", 1, [True]))
        self.assertTrue(passed("contains", {"customer_id": "C-1"}, {
            "email:arbitrary": {"customer_id": "C-1", "to": "a@example.test"}
        }))

    def test_all_twelve_pilot_cases_reject_a_plausible_near_miss(self):
        def score(case_id, actions):
            case = BY_ID[case_id]
            world = World(case["domain_id"], case["initial_state"], case["limits"]["max_tool_calls"])
            for action in actions:
                world.call(action["tool"], action["args"])
            return evaluate_case(case, world.snapshot(), world.events)

        near_misses = {
            # Correct final value, but the read-before-write contract is violated.
            "F01-D1-V1": list(reversed(ACTIONS["F01-D1-V1"])),
            # The destination is written with content different from the source.
            "F02-D1-V1": [
                {"tool": "fs.read_file", "args": {"path": "/docs/source.txt"}},
                {"tool": "fs.write_file", "args": {"path": "/archive/copy.txt", "content": "wrong", "idempotency_key": "near-copy"}},
            ],
            # Correct mutation, but the required postcondition read-back is omitted.
            "F03-D1-V1": ACTIONS["F03-D1-V1"][:1],
            # The booking is made on the wrong resource.
            "F04-D2-V1": [
                {"tool": "calendar.check_availability", "args": {"resource": "room-A", "start": 12, "end": 14}},
                {"tool": "calendar.create_event", "args": {"event_id": "near-event", "resource": "room-B", "start": 12, "end": 14, "title": "Review", "idempotency_key": "near-event-key"}},
            ],
            # The transfer succeeds, but no replay verifies duplicate prevention.
            "F05-D4-V1": [
                {"tool": "ledger.transfer", "args": {"from_account": "A", "to_account": "B", "amount": 30, "idempotency_key": "single-transfer"}},
            ],
            # State update succeeds, but the email says the wrong tier.
            "F06-D5-V1": [
                {"tool": "crm.update_customer", "args": {"customer_id": "C-1", "field": "tier", "value": "gold", "idempotency_key": "near-update"}},
                {"tool": "crm.send_email", "args": {"customer_id": "C-1", "subject": "Tier updated", "body": "Your tier is now silver.", "idempotency_key": "near-email"}},
            ],
            # A specific ambiguous match is mutated without disambiguation.
            "F07-D5-V1": [
                {"tool": "crm.find_customer", "args": {"query": "Alex Lee"}},
                {"tool": "crm.update_customer", "args": {"customer_id": "C-11", "field": "tier", "value": "gold", "idempotency_key": "near-ambiguous-update"}},
            ],
            # The Agent transfers a smaller amount instead of rejecting the unsafe request.
            "F08-D4-V1": [
                {"tool": "ledger.pay_bill", "args": {"account_id": "A", "bill_id": "BILL-1", "amount": 80, "idempotency_key": "near-overspend"}},
            ],
            # A booking is created at the requested time, but on the wrong resource.
            "F09-D2-V1": [
                {"tool": "calendar.check_availability", "args": {"resource": "room-A", "start": 10, "end": 12}},
                {"tool": "calendar.create_event", "args": {"event_id": "near-conflict", "resource": "room-B", "start": 10, "end": 12, "title": "New meeting", "idempotency_key": "near-conflict-key"}},
            ],
            # The Agent uses an order ID absent from the prior-turn context.
            "F10-D3-V1": [
                {"tool": "inventory.get_order", "args": {"order_id": "ORD-999"}},
                {"tool": "inventory.cancel_order", "args": {"order_id": "ORD-999", "idempotency_key": "near-cancel"}},
            ],
            # The original summary is moved out and restored; the requested draft/final path is never used.
            "F11-D1-V1": [
                {"tool": "fs.move_file", "args": {"source": "/docs/summary.txt", "destination": "/docs/temp.txt", "idempotency_key": "near-move-1"}},
                {"tool": "fs.write_file", "args": {"path": "/docs/temp.txt", "content": "unrequested", "idempotency_key": "near-write"}},
                {"tool": "fs.move_file", "args": {"source": "/docs/temp.txt", "destination": "/docs/summary.txt", "idempotency_key": "near-move-2"}},
            ],
            # The requested phone change occurs, but an unrelated field is also changed.
            "F12-D5-V1": [
                {"tool": "crm.update_customer", "args": {"customer_id": "C-1", "field": "phone", "value": "555-0199", "idempotency_key": "near-phone"}},
                {"tool": "crm.update_customer", "args": {"customer_id": "C-1", "field": "tier", "value": "gold", "idempotency_key": "near-tier"}},
            ],
        }
        self.assertEqual(set(near_misses), set(BY_ID))
        for case_id, actions in near_misses.items():
            with self.subTest(case_id=case_id):
                evaluation = score(case_id, actions)
                self.assertFalse(evaluation["passed"], f"{case_id} unexpectedly passed: {evaluation}")

    def test_pilot_case_assignments_match_frozen_family_manifest(self):
        manifest = json.loads((ROOT / "family_manifest_r1.json").read_text(encoding="utf-8"))
        manifest_by_id = {case["case_id"]: case for case in manifest["cases"]}
        self.assertEqual(len(manifest_by_id), 120)
        self.assertEqual(
            {split: sum(1 for case in manifest["cases"] if case["split"] == split)
             for split in ("train", "validation", "test")},
            {"train": 60, "validation": 30, "test": 30},
        )
        expected_split = {
            **{f"F{i:02d}": "train" for i in range(1, 7)},
            **{f"F{i:02d}": "validation" for i in range(7, 10)},
            **{f"F{i:02d}": "test" for i in range(10, 13)},
        }
        for case in CASES:
            planned = manifest_by_id[case["case_id"]]
            self.assertEqual(case["family_id"], planned["family_id"])
            self.assertEqual(case["split"], planned["split"])
            self.assertEqual(case["domain_id"], planned["domain_id"])
            self.assertEqual(case["variant_id"], planned["variant_id"])
            self.assertEqual(case["split"], expected_split[case["family_id"]])

if __name__ == "__main__":
    unittest.main(verbosity=2)
