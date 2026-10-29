# G1 Task-Family Split and Benchmark Protocol R1

**Date:** 2026-10-29  
**Status:** Protocol design proposed and source IDs audited; task suite not yet authored or executed. **G1 remains PARTIAL/OPEN.**  
**Repository boundary:** `yujian777555/openissue` only.  
**Purpose:** Lock the evaluation design for the thesis proposal before building the Agent-evolution controller or running model/API experiments.

## 1. Decision summary

Use a two-layer evaluation design:

1. **Primary mechanism-isolation suite:** independently author a deterministic, stateful tool environment with 120 tasks, grouped into 12 global task families. Hold out entire families (not individual paraphrases) across train/validation/test. Use an offline deterministic executor; Tool-Veritas may be reused as a code-level execution substrate only after an adapter smoke test. Do not use its bundled 70 cases as the thesis train/test suite.
2. **External realistic validation candidate:** pin `sierra-research/tau2-bench` release `v2.0.0` at commit `989d3285ae669e49503324bdb9981bf14fccedeb`. Use its source `test` IDs, not the frozen `text-v1` manifest, as a custom research evaluation. Current candidate domains are airline (20 test tasks) and retail (40 test tasks), 60 total. This is a source-split external evaluation, **not** a claim of task-family-held-out evaluation and **not** an official `text-v1` leaderboard score.
3. **New candidate requiring bounded audit:** `Δτ-Bench` (arXiv:2610.34238, posted 2026-10-25) has 1,588 tasks, 42 domains, six tool-ecosystem versions, 1,191 train / 397 test tasks, and a state-change-based success metric. Its code repo states MIT, but the dataset is distributed separately; exact dataset license/revision/checksum, family leakage, and local-model adapter feasibility have not yet been independently verified. Do not replace the pinned τ²-bench candidate or expand the thesis to dynamic tool-ecosystem evolution until this short audit is complete.

This protocol fixes the *design direction*, not a finished dataset. G1 cannot be marked PASS until the authored suite, exact case manifest, license record, oracle tests, and scorer regression tests exist and are verified.

## 2. Why Tool-Veritas's bundled 70 cases are not the primary split

Source files checked:
- Repository: https://github.com/CoreThink-AI/benchmarking-the-benchmarks
- Tool-Veritas README blob: `8c3f9dfe500062746599d169bdd59cf5d82fae2a`
- Bundled `Tool-Veritas/examples/cases/all.jsonl` blob: `970c995fc102e17bc9520c5ada0c6ab0130d2039`
- Tool-Veritas license blob: `755388835a9d6497f2809e4e30f71fcb5462a7c0` (Apache-2.0)

Source-level parse of `all.jsonl`:
- 70 cases, 16 domain labels, 20 domain/category combinations;
- 70 unique normalized `system_goal` strings;
- no explicit task-family field and no provided train/validation/test split;
- repeated/near-related patterns exist, including repeated tool signatures and additional workflow variants.

Decision: use Tool-Veritas as a candidate local execution harness/reference, not as a ready-made family-held-out benchmark. Because a separate data-specific license was not found in the files checked, author original task text, state, and goals from scratch; do not copy its case text into a redistributed thesis dataset until rights/provenance are verified. The harness's Apache-2.0 code license does not by itself certify third-party content rights.

## 3. Primary controlled suite: exact design target

### 3.1 Deterministic domains

Create five isolated mock domains with explicit tool schemas and serializable state:
- **D1 Filesystem / repository artifacts:** create, read, update, move, delete, verify.
- **D2 Calendar / resource scheduling:** inspect availability, create/cancel event, detect conflicts.
- **D3 Inventory / order management:** lookup, reserve, update quantities, order/return/cancel.
- **D4 Account ledger (mock banking):** balance, transfer, bill payment, transaction verification; no real financial systems.
- **D5 Customer records / email:** resolve identity, read/update records, send/verify notification.

No real external side effects, real accounts, credentials, or paid services. Every tool has a strict JSON schema, deterministic preconditions, and deterministic state transitions.

### 3.2 Twelve global task families and frozen split assignment

Each family is instantiated in all five domains with two variants (ordinary and harder constraint/dependency variant). Target size: `12 families × 5 domains × 2 variants = 120 tasks`. Each task gets a stable ID `Fxx-Dy-Vz`. Family assignment is global, so no variant of a held-out family appears in training.

| Family | Definition | Split | Main observable |
|---|---|---|---|
| F01 | Read-before-write: identify the correct record before changing it | Train | Correct lookup and target mutation |
| F02 | Sequential dependency: feed a prior tool result into a later action | Train | Correct argument propagation |
| F03 | Postcondition verification: read back the state after a mutation | Train | Verified final invariant |
| F04 | Numeric/threshold-constrained choice | Train | Constraint-satisfying selection |
| F05 | Idempotency / duplicate-side-effect prevention | Train | No duplicate write or transaction |
| F06 | Cross-tool handoff between two related tools/services | Train | Consistent cross-tool final state |
| F07 | Ambiguous entity resolution requiring clarification or disambiguation | Validation | No mutation before identity is resolved |
| F08 | Invalid precondition / policy conflict requiring safe refusal or no-op | Validation | Forbidden transition avoided |
| F09 | Resource conflict / availability conflict | Validation | Conflict detected; state preserved |
| F10 | Cross-turn reference resolution (e.g. “that one”, earlier item/event) | Test | Correct referent and final state |
| F11 | Partial failure requiring recovery/compensation | Test | Safe recovery without extra damage |
| F12 | Minimal sufficient action under side-effect constraints | Test | Goal achieved without unrelated mutations |

Split arithmetic:
- Train: F01–F06 = 6 families × 5 domains × 2 variants = **60 tasks**.
- Validation: F07–F09 = 3 × 5 × 2 = **30 tasks**.
- Test: F10–F12 = 3 × 5 × 2 = **30 tasks**.

The IDs above are **planned IDs, not existing task artifacts**. During authoring, if a family cannot be represented naturally in a domain, record the reason and revise the whole design before generating the test set; do not silently substitute a different family or move an individual variant across splits. A minimum of two independently authored variants per family/domain is only a pilot target; before final thesis experiments, increase variants or add a second independently authored seed suite if variance is too high.

### 3.3 Oracle and metrics

Primary oracle: deterministic goal-state invariants and forbidden-state invariants. Any valid tool trajectory that reaches the target state passes; do not require one exact reference tool sequence unless the sequence itself is part of the task objective.

Report separately:
1. **Task success:** all required state invariants hold.
2. **Hard-constraint violation rate:** any forbidden state transition, duplicate side effect, or unsafe mutation.
3. **Tool-call validity:** schema-valid calls / all attempted calls; invalid arguments and precondition failures are separately logged.
4. **Behavior displacement:** normalized Levenshtein distance between parent and offspring canonical tool-call traces on the same fixed probe task. Each trace token includes tool name plus canonicalized argument object; natural-language prose is excluded. Task-specific IDs are preserved when comparing parent and child on the same task.
5. **Search outcome:** best-so-far success and area under the best-so-far curve over the same candidate-evaluation count.
6. **Credit diagnostics:** continuation-value prediction error/ranking, calibration, and operator-ranking stability.

Do not fold behavior displacement into task success or safety violation. Do not let an LLM judge override a deterministic state failure. A qualitative judge, if used, is secondary and reported separately.

### 3.4 Fairness and leakage controls

- Use identical parent policy, task initial state, tool schemas, model checkpoint, decoding settings, and random-seed schedule for matched operator/strength probes.
- For any stochastic inference, run repeated paired trials and estimate the noise floor before interpreting trace displacement.
- Tune static EA parameters on train/validation only; freeze them before the test evaluation.
- Never inspect test outcomes to choose operators, mutation strength, credit model, metric weights, stopping rules, or hyperparameters.
- For lineage value, each sampled operator–strength action receives the same descendant-evaluation opportunities. Primary pilot target: two descendant generations with two evaluations per generation (four descendant evaluations per branch); if infeasible, reduce this symmetrically for every arm and record the change before running.
- All method comparisons share policy representation, task evaluator, seed set, evaluation budget, stop rule, and tuning data. Report any unavoidable deviation.
- Task family, not task instance, is the independent unit for held-out generalization; report task-level results plus family-clustered uncertainty.

## 4. External validation candidate A: τ²/τ³-bench v2.0.0

### 4.1 Pinned sources

- Official repository: https://github.com/sierra-research/tau2-bench
- Release: `v2.0.0`, published 2026-10-20.
- Release commit: `989d3285ae669e49503324bdb9981bf14fccedeb`.
- Repository license: MIT (license blob on the checked repository: `f0323a32227c1327820da33d2fb9d3338a27ac84`).
- Airline tasks blob: `ea4ff5e3f5e3d97ca391846a6e8dd9eb3437dc80`; split blob: `c83cce155671e66a6bf07450fd2845fe0eb1f229`.
- Retail tasks blob: `e95a9f898b2d1f6568ea8faec78edc3767ce747d`; split blob: `8b20704a17aa1940b1e58668f89dcef2ddaeeea3`.
- Version 2.0 changes prompts, communication scoring, NL assertion judging and lookup normalization; do not compare its score numerically with 1.x.

### 4.2 Exact source-test task IDs

**Airline (20):** `2, 6, 8, 13, 16, 18, 19, 22, 24, 25, 26, 29, 30, 31, 32, 35, 37, 44, 45, 48`.

**Retail (40):** `5, 9, 12, 17, 18, 26, 27, 32, 33, 36, 38, 39, 40, 42, 45, 49, 51, 53, 55, 56, 60, 61, 62, 64, 65, 68, 70, 71, 74, 77, 79, 86, 90, 94, 97, 100, 101, 102, 108, 111`.

Total: **60 source-test tasks**. These IDs are from the pinned release's source split files. The full `text-v1` frozen manifest is not the same as the source test split: its 50 tasks per domain include IDs from both source train and source test. Do not use the full `text-v1` manifest as held-out evaluation after searching on source-train tasks, and do not call this 60-task custom evaluation an official `text-v1` leaderboard result.

### 4.3 Scorer caveats and reporting

- Official evaluation docs explain that `evaluation_criteria.actions` is generally a reference trajectory used to derive target state; in airline/retail/telecom, it is not normally the only acceptable path. Score outcome state, not exact trace imitation.
- Source inspection found all 20 airline test tasks use `DB+COMMUNICATE`; only one has nonempty `communicate_info`. Retail has 39 tasks with `DB+NL_ASSERTION` and one `DB`-only task; only 11 retail test tasks have nonempty `communicate_info`, and 11 have nonempty `nl_assertions` in the parsed task file. Verify actual scorer semantics before runs; do not infer from field presence alone.
- Primary reported external metric should include the database/state component separately, alongside the full benchmark reward. Record judge/version and every reward component. If the communication/NL judge is invoked, hold its model/version fixed across all arms; prefer local model endpoints if the adapter supports them and no-paid-call policy is maintained.
- Near-duplicate or related test tasks must be clustered for uncertainty analysis. Known retail pairs to inspect as same-family candidates include `5/9`, `60/61`, and `101/102`; airline `31/32` are a related flight-change pair. This list is provisional, not a complete family audit.
- τ²-bench is a source-split external test, not a family-held-out test. The primary family-held-out claim must come from the controlled suite in Section 3.

## 5. New external candidate to audit: Δτ-Bench (not yet selected)

Primary sources:
- Paper: https://arxiv.org/abs/2610.34238 (posted 2026-10-25).
- Code: https://github.com/zjunlp/delta-tau-bench
- Dataset: https://huggingface.co/datasets/zjunlp/delta-tau-bench

The paper/repository describe 1,588 multi-turn tasks across 42 domains and six tool-ecosystem versions, with 1,191 train / 397 test tasks per version. The code repository states MIT; the data bundle is distributed separately. The paper defines state-change-based success and version-aware path-efficiency/adaptation metrics. This may be a stronger validation environment for *cross-version tool adaptation* than τ²-bench, but it changes the evaluated setting and overlaps with existing skill-maintenance methods such as Steward.

Before selecting it, verify:
1. the exact Hugging Face dataset revision, `checksums.sha256`, and explicit dataset license/third-party notices;
2. whether task-family/template groups cross the 1,191/397 split and how test tasks repeat across versions;
3. whether the EC method can be evaluated without using test rewards for evolution/control tuning;
4. whether the agent, user simulator, and embedding services can run locally (do not use the default DeepSeek-v4-pro profile; user preference is DeepSeek-Flash if a DeepSeek service is used, but no paid API is authorized);
5. whether adding version adaptation is necessary for this thesis or would broaden scope unnecessarily.

Until this audit passes, Δτ-Bench is a **candidate for comparison**, not a locked benchmark and not a new thesis direction.

## 6. Baselines and gate logic

Required baseline ladder for the controlled suite:
1. starting Agent / no evolution;
2. train/validation-tuned static EA with fixed operator mixture;
3. EvoTool or a faithful component-level comparison;
4. classical adaptive operator selection with immediate reward;
5. adaptive operator selection with diversity/parent-distance credit;
6. behavior-scale-only control (ELMER-style);
7. lineage-only control (LVPG-style);
8. naive joint operator–strength control with immediate reward;
9. naive joint operator–strength control with raw lineage return;
10. OSLVC-R1.

Gate logic:
- **G1a (design):** this split and metric protocol approved as the working design.
- **G1b (artifact):** 120 original tasks, task-family manifest, license/provenance note, deterministic oracle tests, and scorer tests created and hashed.
- **G1c (external):** τ² task adapter and reward decomposition verified; Δτ-Bench is either accepted after audit or explicitly deferred.
- **G2 (mechanism pilot):** only after G0 is sufficiently closed and G1b/G1c are passed. No paid API call before these gates.

No tasks have been authored, no adapter has been run, and no experiment was performed in writing this protocol. Current state is a concrete pre-registration/design proposal, not a completed benchmark implementation.



## 7. Cross-split lexical similarity audit of τ²-bench v2.0.0 (2026-10-29)

A source-level heuristic audit compared each source-test task against every source-train task in airline (50 tasks total; 30 train / 20 test) and retail (114 tasks total; 74 train / 40 test). Text combined task purpose, user reason-for-call, and task instructions. Long alphanumeric entity IDs and numeric identifiers were normalized; word-level TF-IDF cosine similarity was then computed. Threshold `0.45` is a **screening threshold only**, not a validated duplicate detector or a ground-truth task-family label.

Results:
- Airline: 4/20 test tasks had a nearest train-task similarity ≥0.45.
- Retail: 17/40 test tasks had a nearest train-task similarity ≥0.45.
- High-scoring examples: airline test 16 ↔ train 15 (0.695), test 2 ↔ train 38 (0.611), test 22 ↔ train 17 (0.533); retail test 94 ↔ train 93 (1.000), test 32 ↔ train 31 (0.968), test 62 ↔ train 63 (0.963), test 68 ↔ train 67 (0.954), test 5 ↔ train 6 (0.938), test 9 ↔ train 8 (0.919), test 71 ↔ train 72 (0.913), test 33 ↔ train 34 (0.909), test 12 ↔ train 13 (0.879), test 97 ↔ train 96 (0.841), test 56 ↔ train 57 (0.841), test 26 ↔ train 25 (0.819), test 86 ↔ train 85 (0.732), test 36 ↔ train 37 (0.717), test 38 ↔ train 37 (0.717).

Interpretation boundary:
- These values are automated lexical similarity, not confirmed duplicate labels. Manual semantic review and inspection of task schemas/initial states are required before declaring family overlap.
- They provide strong warning that the source train/test split should **not** be called task-family-held-out. Use it only as a standard source-split evaluation and report its limitations.
- The controlled suite's whole-family split remains the primary evidence for family-held-out generalization. Do not use the external source-test score as a substitute for that claim.
- If using τ² train tasks to evolve policies, do not claim that τ² source-test performance establishes unseen-family generalization. If using only the custom suite for evolution, describe τ² as external cross-benchmark transfer instead.
