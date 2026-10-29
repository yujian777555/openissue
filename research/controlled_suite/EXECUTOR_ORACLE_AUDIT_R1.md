# Executor and Oracle Independent Audit R1

**Date:** 2026-10-29  
**Repository:** `yujian777555/openissue`  
**Scope:** Static review of `world_r1.py` and adversarial regression tests for `test_world_r1.py`.  
**Status:** Two evaluator correctness defects patched; post-patch CI run was queued at the time this note was drafted. Do not mark the audit accepted until the latest run completes successfully.

## Finding A — Argument propagation only checked the first consumer (fixed; regression test added)

### Defect
The old `evaluate_case` implementation selected the first successful producer and first successful consumer for each `required_arg_match` rule. If an agent made one correct consumer call followed by a second incorrect consumer call, the trace constraint could pass while ignoring the later incorrect argument. This could overstate correct data flow and weaken evaluation validity for sequential tool-use tasks.

### Patch
For every successful consumer call, the evaluator now selects the nearest preceding successful producer call, reads the configured source pointer, and compares it to that consumer's argument. It records producer/consumer event indices in failure details. A consumer with no preceding successful producer fails.

### Regression test
Added `test_trace_checker_checks_every_successful_consumer_call`: the first read→write propagation is correct; a second successful write passes the state requirement for the first copy but supplies incorrect content. The evaluator must fail the second consumer's propagation check.

## Finding B — Python equality conflated booleans and integers (fixed; regression test added)

### Defect
Python considers `True == 1` and `False == 0` true. The old state oracle's `eq` operator used native equality, so a boolean state could incorrectly satisfy an integer-valued invariant.

### Patch
Added recursive `_json_equal` semantics: booleans compare only to booleans; numeric integers/floats compare numerically; containers compare recursively and type-sensitively; other values require the same type. The `eq` invariant uses this helper.

### Regression test
Added `test_json_oracle_equality_does_not_conflate_boolean_and_integer`, requiring state `{"flag": true}` to fail an invariant expecting integer `1`.

## Validation state

- Before patch: the existing smoke workflow was passing on commit `554dd609cf0adf331d0f3ae64247e2a64558e3cb`.
- Code patch commit: `668fa46da501ce07005acdb994b2e51d854ca9b5`.
- Test patch commit: `25ecb59298e7ea12983ab70b5bc569e5b3f4fc2e`.
- Workflow for the code patch: https://github.com/yujian777555/openissue/actions/runs/40872596867 (success).
- Workflow for the test patch: https://github.com/yujian777555/openissue/actions/runs/40872647713 (was queued when this note was written; verify final status before acceptance).
- Expected total unit tests after adding two tests: 19, assuming the pre-existing 17 tests remain unchanged.

## Remaining audit limits

This is a focused evaluator audit, not a complete formal verification of all tool handlers. Further work should review tool-state schema validation, idempotency scope, budget accounting for repeated over-budget attempts, and whether every pilot case's reference action is fully independent of its oracle. The 12-case pilot remains a mechanism smoke suite, not a final 120-case benchmark; G1 stays PARTIAL/OPEN.
