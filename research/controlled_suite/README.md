# OpenIssue controlled tool suite R1

This directory contains the deterministic, in-memory pilot implementation for G1.

## Files

- `family_manifest_r1.json`: 120 planned case IDs, grouped by 12 global task families. These are planned IDs, not 120 authored tasks.
- `task_case_schema_r1.json`: task-case JSON Schema, including state-oracle and trace constraints.
- `pilot_cases_r1.jsonl`: 12 independently authored representative cases, one per family. The split is 6 train / 3 validation / 3 test because these are mechanism smoke cases, not the final 120-task dataset.
- `world_r1.py`: five isolated deterministic mock domains and their tool schemas, state transitions, error behavior, idempotency guard, event trace, and oracle evaluator.
- `test_world_r1.py`: 19 standard-library unit and smoke tests (includes regression tests for repeated consumer argument propagation and boolean/integer oracle equality).

## Safety and determinism

No tool makes network calls, touches the host filesystem, sends real email, changes a real calendar, or moves real money. Calendar times are integer units. Ledger values are synthetic integers. Email operations only enqueue records in memory.

Tool calls validate exact argument names and primitive types. Tool schemas include nested order-item fields and positive amount/quantity bounds. State-changing operations run against a staged copy; a failed precondition does not partially commit. Mutating operations require idempotency keys. Reusing a key with the same operation returns a replay; reusing it with a different operation/payload is rejected. `World(max_tool_calls=...)` and `run_case_actions(case, actions)` enforce the per-episode tool-call budget; `max_turns` remains the responsibility of a future dialogue/agent wrapper because this module executes tool calls, not dialogue turns.

## Run tests

From this directory, with Python 3.10+:

```bash
python -m unittest -v test_world_r1
```

The tests cover domain isolation, argument validation, atomic failures, half-open scheduling intervals, atomic stock reservation, idempotency, ambiguous entity lookup, all 12 pilot oracles, trace-order constraints, schema conformance, nested tool-schema shape, incorrect argument propagation, repeated consumer validation, and JSON type-sensitive equality.

## Status boundary

The 12 pilot cases and executor are a working prototype. They do **not** establish G1 PASS. The full 120 task contents, final task-family review, independent oracle review, and frozen hashes are still outstanding. The test reference actions are evaluator-side fixtures; they must never be exposed to the Agent under evaluation.

## Oracle audit

See [`EXECUTOR_ORACLE_AUDIT_R1.md`](EXECUTOR_ORACLE_AUDIT_R1.md) for two evaluator defects found and patched: (1) argument propagation previously checked only the first consumer call; (2) Python boolean/integer equality could satisfy the wrong invariant. The latest test-patch CI must be green before treating these fixes as verified.
