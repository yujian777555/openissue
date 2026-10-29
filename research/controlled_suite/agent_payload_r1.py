"""Allowlisted Agent-visible task payload for the controlled tool suite.

Only the task's user request and optional conversational context may be serialized
from a case record. Evaluator state, scoring rules, split/family metadata, trace
constraints, provenance, and reference actions are intentionally excluded.
"""
from __future__ import annotations

from typing import Any

_ALLOWED_TASK_FIELDS = frozenset({"user_request", "context"})


def build_agent_task_payload(case: dict[str, Any]) -> dict[str, str]:
    """Return the minimal Agent-visible payload, rejecting unexpected task fields."""
    if not isinstance(case, dict):
        raise TypeError("case must be a dictionary")
    task = case.get("task")
    if not isinstance(task, dict):
        raise ValueError("case.task must be a dictionary")

    unexpected = set(task) - _ALLOWED_TASK_FIELDS
    if unexpected:
        names = ", ".join(sorted(str(name) for name in unexpected))
        raise ValueError(f"case.task contains non-allowlisted fields: {names}")

    request = task.get("user_request")
    if not isinstance(request, str) or not request.strip():
        raise ValueError("case.task.user_request must be a non-empty string")

    payload = {"user_request": request}
    if "context" in task:
        context = task["context"]
        if not isinstance(context, str):
            raise ValueError("case.task.context must be a string when provided")
        payload["context"] = context
    return payload
