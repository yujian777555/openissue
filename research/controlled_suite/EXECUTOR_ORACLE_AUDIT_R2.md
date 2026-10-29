# Executor and Oracle Independent Audit R2

**Date:** 2026-10-29  
**Repository:** `yujian777555/openissue`  
**Scope:** Budget/event accounting, idempotency-key scope, task-oracle specificity, dynamic identifiers, and adversarial trace evaluation.  
**Status:** executor changes in `14ac8634607094b720e3c96ad1bd9a786a9386f5` passed 29/29 tests; the follow-up test commit `67f831cd605d0e8f70f9e53ec5db85c430c86e04` passed 31/31 tests in [run 40878796822](https://github.com/yujian777555/openissue/actions/runs/40878796822) on Python 3.11.  
**Boundary:** This is a code-and-fixture audit, not a final benchmark validation or Agent capability experiment.

## Finding A — Budgeted calls and recorded attempts were conflated

### Observation
`World.call` intentionally blocks attempts after `max_tool_calls` is exhausted and records a `blocked` event without incrementing `call_count`. That can be a valid budget contract, but the API did not expose the distinction between budget-admitted calls and all attempts. In addition, blocked events marked `schema_valid: true` even though validation was skipped.

### Change
- `call_count` is explicitly documented as budget-admitted attempts (including schema/business errors).
- `attempt_count` is derived from the event log and includes blocked attempts; evaluator output reports attempted, budgeted, and blocked counts separately.
- Blocked events use `schema_valid: null` to mean “not evaluated”.
- `max_tool_calls` now rejects booleans and non-integers instead of accidentally accepting `True` or fractional limits.

### Regression coverage
The budget test performs repeated over-budget calls, including one with malformed arguments, and verifies event indices, counter semantics, no mutation, and skipped-schema semantics.

## Finding B — Idempotency keys collided across unrelated tools

### Counterexample
The original implementation used one episode-global dictionary keyed only by `idempotency_key`. A valid `fs.write_file(..., idempotency_key="shared-key")` followed by a valid `fs.move_file(..., idempotency_key="shared-key")` was rejected as an idempotency conflict despite being a different tool operation.

### Change
Idempotency records are scoped by tool name and then key. Same-tool key reuse with a different payload still fails; different tools may reuse the same key. This contract is documented and regression-tested.

## Finding C — Several pilot oracles were coupled to reference-only identifiers or accepted wrong actions

### C1. Booking oracle (F04)
The user request specified room, interval, and title, but the oracle only bounded start/end and hard-coded `EVT-NEW`. A booking on the wrong resource or with a different interval/title could pass some state checks, while a correct booking using an agent-chosen event ID could fail.

**Change:** the oracle checks for a booking record with the exact requested resource, interval, title, and active status without fixing the generated event ID; the trace requires the correct availability check and creation call.

### C2. Transfer/email generated IDs (F05/F06)
The oracle expected `txn:transfer-001` and `email:notify-001`, both derived from the reference action's idempotency key. A correct Agent choosing a different key could fail despite performing the requested operation.

**Change:** record-level partial matching verifies transaction fields and email recipient/content/status without depending on generated IDs. F06 now specifies the exact confirmation subject/body in the user request. Regression tests use noncanonical keys.

### C3. Ambiguous customer and cross-turn reference (F07/F10)
F07 can measure safe non-mutation under ambiguity, but the state-only scorer cannot determine whether the Agent actually asked for clarification. Its manifest goal is now explicit about this limit. F10 previously placed `ORD-200` directly in the user request, so it did not test cross-turn reference resolution.

**Change:** F07 is described as ambiguity-safe no-op for this scorer. F10's user request omits the ID and the prior-turn reference is supplied in `task.context`.

### C4. Compensation trace (F11)
The previous ordered-tool check only required two successful move calls and one failed write. A move of `summary.txt` to a temporary path, a failed write to that temporary path, and a move back could restore the same final state and pass without exercising the requested draft/final compensation path.

**Change:** added an `ordered_calls` trace contract that checks ordered tool/status/selected-argument patterns, including the exact first move, failed write to the occupied summary path, and compensating move.

### C5. Unrequested side effects
Several cases checked only selected fields, so additional file/customer/calendar/ledger mutations could escape the oracle.

**Change:** the pilot oracles now compare complete relevant state collections where identifiers are deterministic, and use partial record matching where the Agent may legitimately choose generated IDs. F01/F02/F03/F07/F08/F09/F10/F11/F12 were tightened accordingly.

## Finding D — Non-equality operators also needed explicit JSON semantics

The earlier patch fixed `eq`, but native `ne`, numeric comparisons, and membership operators could still conflate booleans with numbers or fail to match generated records. The evaluator now:
- uses type-sensitive JSON equality for `ne`;
- restricts `gte/lte` to numeric values and rejects booleans;
- defines type-aware `contains/not_contains` for strings, arrays, dictionary keys, and partial record values;
- defines `subset_of` for type-sensitive array membership or object key/value subsets.

The schema now documents these semantics.

## Per-case near-miss and split-integrity follow-up

A follow-up test commit `67f831cd605d0e8f70f9e53ec5db85c430c86e04` adds:
- one plausible near-miss trajectory for each case F01–F12; all twelve are rejected by the revised scorer;
- a manifest-integrity check confirming 120 unique planned IDs, split counts of 60/30/30, and agreement between the pilot cases and their planned family/split/domain/variant assignments.

The CI run [40878796822](https://github.com/yujian777555/openissue/actions/runs/40878796822) passed **31/31 tests**. This checks discriminability against one selected near-miss per case; it is not exhaustive proof of oracle soundness or a substitute for independent human review.

## Validation and remaining limits

- New tests were added for repeated blocked attempts, strict budget types, per-tool idempotency, generated-ID independence, wrong booking details, compensation-target counterexamples, extra side effects, cross-turn context placement, and operator semantics.
- The latest GitHub Actions run [40878796822](https://github.com/yujian777555/openissue/actions/runs/40878796822) explicitly reports `Ran 31 tests` and `OK`; the earlier implementation run [40877523811](https://github.com/yujian777555/openissue/actions/runs/40877523811) passed 29/29. No local Python execution is claimed because this session used the remote GitHub workflow for execution.
- The 12 cases remain pilot fixtures, not the final 120-case benchmark. Independent human review, family-template leakage review, actual prompt-builder allowlist testing, exact final hashes, external benchmark adapter/scorer audit, and the remaining 108 tasks are outstanding.
- G0 remains OPEN; G1 remains PARTIAL/OPEN; G2 remains NOT RUN. No LLM or paid API experiment was started.
