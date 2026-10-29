# Tool-Veritas Task-Family and Scorer Audit R1

**Date:** 2026-10-29  
**Status:** SOURCE AUDIT COMPLETE; SPLIT/SCORER PROTOCOL PROVISIONAL, NOT FROZEN  
**Project:** yujian777555/openissue only  
**Purpose:** Advance G1 for the Agent × EC thesis candidate without running an experiment.

## 1. Pinned source and provenance

- Repository: https://github.com/CoreThink-AI/Tool-Veritas
- Audited branch head / commit: `446764fdfb0227a692a15f8f5a2f8322b81d9238` (main; commit message "Initial public release of Tool Veritas", 2026-08-03).
- Root license file: Apache License 2.0 at https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/LICENSE.
- Case file: `examples/cases/all.jsonl`, blob SHA `970c995fc102e17bc9520c5ada0c6ab0130d2039`.
- Case file content parsed successfully: **70 JSONL rows**, all `benchmark_version = "1.0"`, 239,725 characters, zero JSON parse errors.
- Metadata: 16 distinct domain labels, including one cross-domain case (`memory+calendar`); difficulty counts are 34 medium and 36 hard.
- The repo-level Apache-2.0 license is verified. A separate data-specific provenance/license statement was not identified in the files inspected; before redistributing cases or claiming the dataset itself is separately licensed, inspect the paper and repository history.

This pin is important: do not cite "Tool-Veritas 70 cases" without the exact repository commit and case-file SHA.

## 2. What the environment can and cannot do

The README and domain documentation describe a local in-memory sandbox, 16 built-in tool domains, and deterministic state gates. The runtime records per-turn user input, tool calls/results, assistant output, and gate verdicts. This makes Tool-Veritas a useful **controlled execution substrate** for observing actual Agent tool traces.

It is not, by itself, a ready-made thesis benchmark split or a complete deterministic goal oracle for every case.

### Scorer behavior verified from source

- `BenchmarkRunner` invokes deterministic gates after each turn.
- The gate engine checks required tools, maximum tool calls, whether an empty-tool turn is allowed, and configured hard-state assertions.
- `evaluate_run` invokes the optional Maven/LLM trajectory evaluator only when evaluation is enabled and either gates pass or the configuration explicitly permits judging failed-gate traces.
- With the judge disabled, the returned task pass is effectively the deterministic-gate result; with the judge enabled, the final pass requires both gates and the judge label to succeed.
- The bundled case-level `global_evaluation` is typically only `automated_gate_success`; turn-level `grading_instructions` are natural-language criteria and are not themselves deterministic assertions.

### Quantitative case-file audit

| Check | Result |
|---|---:|
| Cases parsed | 70 / 70 |
| Mean proportion of turns containing at least one explicit hard-state assertion | 59.9% |
| Cases with hard-state assertions on every turn | 4 / 70 |
| Cases with no hard-state assertions anywhere | 3 / 70 |
| Cases with at least one listed state-changing tool turn lacking a same-turn hard-state assertion | 8 / 70 |

The last statistic is a conservative source audit, not proof that the outcome is never checked later. It identifies where an independent final-state oracle or a supplemental per-turn assertion is required. In particular:
- `research_mt_001` and `research_mt_002` have no hard-state assertions; the final `write_note` artifact is not deterministically verified.
- `web_mt_001`–`web_mt_003` use a final `write_note` step without a deterministic note-content oracle.
- `docker_mt_001`–`docker_mt_003` have at least one state-changing turn whose state is not asserted in that same turn.
- `calendar_mt_003` is a no-common-slot/conflict-avoidance case with no hard-state assertions; without an explicit no-event-created assertion, a forbidden state change can evade the deterministic oracle.

**Implication:** Do not use the raw bundled pass rate as the sole primary outcome. For the thesis pilot, create an independently specified deterministic oracle overlay that checks task-goal state after every state-changing turn and at task end. Keep LLM-judged conversational quality as a secondary metric, not the sole arbiter of task success. Do not use mock-judge scores as scientific evidence.

## 3. Near-duplicate and family-leakage findings

Family assignment must use goal semantics, interaction turns, available/required tool signatures, and initial/final state—not just the ID prefix.

| Related cases | Audit finding | Split rule |
|---|---|---|
| `shopping_mt_002`, `shopping_mt_004` | Same required-tool signature and highly similar simple search/add/order/status workflow | Keep in the same family and same split |
| `shopping_mt_004_distractor_skus`, `shopping_mt_005` | Near-duplicate family: same product catalog, same user-turn wording, same price-threshold removal structure, nearly identical gate sequence | Keep together; for statistical counting, treat as one task family, not two independent families |
| `shopping_hard_001`, `shopping_hard_002`, `shopping_hard_003` | Related price/budget/coupon/bulk-cart optimization family | Keep together and separate from the distractor-SKU family only if the final family review confirms that the learning target differs; conservative default is to keep all price-constrained shopping tasks in one held-out split |
| `calendar_mt_003`, `calendar_mt_004` | Both test conflict/no-common-slot reasoning and avoiding an invalid meeting | Keep together |
| `calendar_mt_006_reschedule_chain_conflict`, `memory_mt_001_reference_resolution` | Both require reference resolution across turns and safe event cancel/recreate behavior. The latter's ID prefix is misleading: metadata says domains `memory+calendar`, and its scenario is calendar-event resolution | Group by scenario/tool semantics, not ID prefix |
| `filesystem_mt_003`, `filesystem_mt_002_move_copy_tracking` | Both require multi-step move/copy/delete state tracking | Keep together |
| `banking_hard_001`, `banking_hard_003` | Both involve compound-interest savings growth and downstream funding/payment decisions | Keep together |
| `travel_hard_001`, `travel_hard_002` | Both are budget-constrained, multi-leg itinerary optimization tasks | Keep together |
| `healthcare_mt_005`, `healthcare_hard_001`, `healthcare_hard_002` | All require clinical safety constraints (allergy, dose, interaction, or safe prescribing) | Keep together for a conservative safety-family holdout |

## 4. Provisional family-held-out split candidate

This is a **candidate split, not a frozen manifest**. The exact task IDs below are a starting point for the independent oracle audit. A family must never be divided across train/validation/test, and any change must be versioned and hashed before experiments.

### Candidate training set — 38 cases

- Banking routine workflows: `banking_mt_001`, `banking_mt_002`, `banking_mt_003`, `banking_mt_004`
- Calendar simple event workflows: `calendar_mt_001`, `calendar_mt_002`
- Database CRUD/notification workflows: `database_mt_001`, `database_mt_002`, `database_mt_003`
- Email search/send/verify: `email_mt_001`, `email_mt_002`
- Filesystem backup/rename: `filesystem_mt_001`, `filesystem_mt_002`
- Git repo/commit/branch: `git_mt_001`, `git_mt_002`, `git_mt_003`
- Routine healthcare record/appointment workflows: `healthcare_mt_001`, `healthcare_mt_002`, `healthcare_mt_003`, `healthcare_mt_004`
- Basic inventory operations: `inventory_mt_001`, `inventory_mt_002`, `inventory_mt_003`
- Knowledge-graph construction: `memory_mt_001`, `memory_mt_002`, `memory_mt_003`
- Shopping basic/cart workflows: `shopping_mt_001`, `shopping_mt_002`, `shopping_mt_003`, `shopping_mt_004`
- Smart-home device/scene workflows: `smart_home_mt_001`, `smart_home_mt_002`, `smart_home_mt_003`, `smart_home_mt_004`
- SQLite schema/data workflows: `sqlite_mt_001`, `sqlite_mt_002`, `sqlite_mt_003`
- Routine travel booking/cancellation: `travel_mt_001`, `travel_mt_002`, `travel_mt_003`, `travel_mt_004`

### Candidate validation set — 8 cases across 3 families

- Compound-interest/funding family: `banking_hard_001`, `banking_hard_003`
- Docker lifecycle family: `docker_mt_001`, `docker_mt_002`, `docker_mt_003`
- Price/budget/cart family: `shopping_hard_001`, `shopping_hard_002`, `shopping_hard_003`

### Candidate test set — 16 cases across 5 held-out families

- Calendar conflict avoidance and reference/reschedule chains: `calendar_mt_003`, `calendar_mt_004`, `calendar_mt_006_reschedule_chain_conflict`, `memory_mt_001_reference_resolution`
- Filesystem multi-step move/copy tracking: `filesystem_mt_003`, `filesystem_mt_002_move_copy_tracking`
- Healthcare clinical safety: `healthcare_mt_005`, `healthcare_hard_001`, `healthcare_hard_002`
- Shopping price-constrained/distractor family: `shopping_mt_004_distractor_skus`, `shopping_mt_005`, `shopping_hard_001`, `shopping_hard_002`, `shopping_hard_003`
- Budget-constrained multi-city travel: `travel_hard_001`, `travel_hard_002`

**Important leakage correction:** The provisional split above places the shopping budget family in both validation and test, which violates the conservative family rule in Section 3. Therefore, the 38/8/16 allocation is **not admissible as currently written**. Before freezing, move the entire price-constrained shopping family into exactly one split and replace its former slot with a distinct, reviewed family. Do not run an experiment on the provisional split as written.

### Excluded from the primary split pending family expansion or oracle work — 8 cases

- No deterministic final-note oracle: `research_mt_001`, `research_mt_002`, `web_mt_001`, `web_mt_002`, `web_mt_003`.
- Singleton families needing additional variants before they can support family-level generalization claims: `database_mt_004` (identity ambiguity), `inventory_mt_004_cross_sku_dependency` (cross-SKU dependency), `banking_hard_002` (loan amortization).

These eight cases may later be used as secondary stress probes after their oracle/family design is improved. They are not to be silently dropped from the report; exclusions must be reported.

## 5. Split issue found before freeze

The first proposed split draft has a real leakage issue: shopping price/budget tasks appear in both validation and test. This was caught before any experiment. The fix must be made by reassigning whole families, not by moving individual cases. A second independent review must then verify:
1. every source case is assigned exactly once to train, validation, test, or a named exclusion;
2. no family/near-duplicate group crosses partitions;
3. all state-changing goals have deterministic state assertions;
4. task IDs, source commit, source file SHA, split manifest SHA, and oracle version are recorded;
5. the external validation subset is audited separately and never used to tune the controller.

## 6. Decision

- **Tool-Veritas is suitable as a local deterministic execution substrate, not yet approved as an unmodified benchmark/split.**
- The repository source and 70-case manifest are pinned; parsing passed 70/70.
- **G1 remains PARTIAL/OPEN** because the family split has a detected leakage issue and the independent goal-state oracle overlay is not implemented/verified.
- **G2 NOT RUN.** No Agent, API, or paid experiment was started.
- Next: repair the split candidate, complete per-case oracle coverage for the selected primary cases, then conduct a second independent read-only audit before freezing the manifest.

## 7. Source files inspected

- README and license: https://github.com/CoreThink-AI/Tool-Veritas/tree/446764fdfb0227a692a15f8f5a2f8322b81d9238
- Case manifest: https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/examples/cases/all.jsonl
- Domain documentation: https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/docs/domains.md
- Deterministic gates: https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/benchmark/gates/gating_engine.py
- Per-turn runner and scoring integration: https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/benchmark/runtime/benchmark_runner.py
- Gate/judge combination: https://github.com/CoreThink-AI/Tool-Veritas/blob/446764fdfb0227a692a15f8f5a2f8322b81d9238/evaluator/evaluator/integration/__init__.py
