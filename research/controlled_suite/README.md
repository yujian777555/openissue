# OpenIssue controlled tool suite R1

This directory contains the deterministic, in-memory pilot implementation for G1.

## Files

- `family_manifest_r1.json`: 120 planned case IDs, grouped by 12 global task families. These are planned IDs, not 120 authored tasks.
- `task_case_schema_r1.json`: task-case JSON Schema, including state-oracle and trace constraints.
- `pilot_cases_r1.jsonl`: 12 independently authored representative cases, one per family. The split is 6 train / 3 validation / 3 test because these are mechanism smoke cases, not the final 120-task dataset.
- `world_r1.py`: five isolated deterministic mock domains and their tool schemas, state transitions, error behavior, idempotency guard, event trace, and oracle evaluator.
- `agent_payload_r1.py`: allowlist helper that emits only `task.user_request` and optional `task.context`; a live Agent wrapper still needs to integrate and test this boundary.
- `test_world_r1.py`: **36 standard-library unit and smoke tests** covering budget accounting, per-tool idempotency scope, dynamic-ID oracle checks, one near-miss trajectory per pilot case, manifest split integrity, the task-payload allowlist, and batch 01 reference/near-miss validation. CI run [40887208453](https://github.com/yujian777555/openissue/actions/runs/40887208453) passed 36/36.

## Safety and determinism

No tool makes network calls, touches the host filesystem, sends real email, changes a real calendar, or moves real money. Calendar times are integer units. Ledger values are synthetic integers. Email operations only enqueue records in memory.

Tool calls validate exact argument names and primitive types. Tool schemas include nested order-item fields and positive amount/quantity bounds. State-changing operations run against a staged copy; a failed precondition does not partially commit. Mutating operations require idempotency keys scoped by tool: reusing a key with the same tool and payload returns a replay, while reusing it with a different payload in that tool is rejected. Different tools may reuse the same key. `World.call_count` counts attempts admitted under the budget; `World.attempt_count` is derived from the event log and includes budget-blocked attempts. Budget-blocked events set `schema_valid` to `null` because schema validation was not run. `World(max_tool_calls=...)` accepts only a positive plain integer and `run_case_actions(case, actions)` enforces the per-episode tool-call budget; `max_turns` remains the responsibility of a future dialogue/agent wrapper because this module executes tool calls, not dialogue turns.

## Run tests

From this directory, with Python 3.10+:

```bash
python -m unittest -v test_world_r1
```

The tests cover domain isolation, argument validation, atomic failures, half-open scheduling intervals, atomic stock reservation, per-tool idempotency, repeated budget-block accounting, all 12 pilot oracles, exact ordered-call patterns, dynamic event/email/transaction IDs, side-effect rejection, schema conformance, incorrect argument propagation, and type-safe oracle operators.

## Status boundary

The 12 pilot cases plus 12 batch-01 cases and executor are a working prototype. They do **not** establish G1 PASS. A total of 24/120 cases are authored; 96 remain unauthored. Independent human oracle review, full family-template leakage review, live prompt-wrapper integration test, and frozen hashes are still outstanding. The test reference actions are evaluator-side fixtures; they must never be exposed to the Agent under evaluation.

## Oracle audit

- [`EXECUTOR_ORACLE_AUDIT_R1.md`](EXECUTOR_ORACLE_AUDIT_R1.md) records the two earlier fixes: validating every successful consumer and type-sensitive JSON equality for `eq`.
- [`EXECUTOR_ORACLE_AUDIT_R2.md`](EXECUTOR_ORACLE_AUDIT_R2.md) records budget/idempotency and oracle corrections.
- [`PILOT_FAMILY_LEAKAGE_AUDIT_R1.md`](PILOT_FAMILY_LEAKAGE_AUDIT_R1.md) records the heuristic lexical-overlap screen, manual family comparison, and revisions to F08/F09. The revised suite is still a pilot and requires green CI plus independent review.


## Case authoring and batch 01

- [`CASE_AUTHORING_PROTOCOL_R1.md`](CASE_AUTHORING_PROTOCOL_R1.md) freezes identity/split rules, family mechanism criteria, oracle/trace requirements, near-miss expectations, and batch gates.
- `authored_cases_r1.jsonl` contains the first 12 additional cases (one per family, V1 standard difficulty) pending independent review; it does not replace the 12 original pilot fixtures.
- `reference_actions_r1.jsonl` stores evaluator-only reference and near-miss trajectories separately from task records. These actions must never be serialized into an Agent prompt.
- Batch 01 adds schema/manifest checks, reference-pass checks, near-miss rejection tests, and an explicit cross-turn context-only assertion. CI [40887208453](https://github.com/yujian777555/openissue/actions/runs/40887208453) passed 36/36. The 12 new cases remain pending independent review.
