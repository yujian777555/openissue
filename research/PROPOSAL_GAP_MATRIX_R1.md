# Proposal-Ready Gap Matrix R1 — Agent × Evolutionary Computation

**Date:** 2026-10-27  
**Status:** Working matrix for opening-report preparation; not a novelty certification.  
**Project boundary:** yujian777555/openissue. Do not mix this line with EvoPareto-Agent or other repositories.

## 1. Research problem

For structured Agent policies evolved through a gradient-free search, requested mutation intensity does not guarantee the same realized behavioral change across operators. The candidate question is whether estimating operator value conditional on realized behavioral displacement improves evolutionary control over strong static and adaptive baselines.

This is a method-improvement thesis candidate, not pure MetaBBO. The optimization object is an executable Agent policy; evolutionary computation controls how its policy is varied, evaluated, and retained.

## 2. Closest-work matrix

| Closest work / family | What is already established | Candidate distinction to test | Required baseline / ablation | Current status |
|---|---|---|---|---|
| EvoMAS: Heuristics in the Loop (ICML 2026) | Seven-strategy evolutionary portfolio, adaptive strategy selection, role-level evolution, curriculum, reflective meta-controller; exact reward equations not yet verified | No claim around adaptive portfolios or reflective evolutionary meta-control. Test only the narrower displacement-conditioned continuation-credit hypothesis after full-text audit | Reproduce or method-level compare exact selection reward and strategy state from final paper | G0 OPEN: official abstract verified, full-paper method details unavailable in this pass |
| ELMER (2026) | Behavior-grounded semantic mutation at low/medium/high displacement levels; behavior-space distance; current outer loop samples strengths uniformly | Operator-specific realized-displacement response calibration and its downstream value beyond ELMER | ELMER-style strength control; strength-only vs operator-specific calibration | Candidate A; not independently novel until downstream gain shown |
| The Time Value of Evolution / LVPG (2026) | State-/horizon-dependent selection among calibrated mutation radii; critic uses lineage/path outcomes | Estimate operator continuation value conditional on realized displacement and validity, with matched parent/task/state support | LVPG-style lineage/radius control; raw lineage credit | Direct baseline; substantial overlap |
| Classical AOS / self-adaptation | Online operator choice, state-based control, fitness-improvement rewards, and diversity/parent-distance credit are established | No generic RL/UCB/AOS claim; isolate whether displacement-conditioned lineage credit changes operator ranking | Probability matching/adaptive pursuit or UCB; diversity/parent-distance reward; self-adaptation | Required |
| CWM: Code World Models for Parameter Control | Learned optimizer dynamics used for online mutation-strength control | Test Agent-specific realized-behavior conditional credit, not merely learned scale scheduling | CWM if code/reproduction and setting permit; otherwise documented conceptual comparison | Required related-work check |
| LLaMEA-HPO | Separates LLM structural heuristic evolution from numerical hyperparameter optimization | Static HPO is a strong baseline; do not claim the separation of structure and numeric tuning as new | Random search or SMAC over static EA settings, then freeze | Required |
| EvoTool (ACL 2026) | Four-module tool-use policy; trajectory-grounded blame attribution; targeted mutation; diversity-aware survivor selection; parent sampling by win frequency; local/offline reference implementation | Add a distinct EC control mechanism without claiming targeted mutation or diversity selection as new | EvoTool full method; random/fixed/all-module mutation; greedy/top-k/static selection | Strong direct baseline; MIT code available |
| Agent trajectory search / MCTS / SMC | Trajectory search and branching control are established | Current thesis candidate is evolutionary policy mutation control, not generic trajectory search | Include only if the experimental object changes toward test-time trajectory search | Not the current lane |

## 3. Candidate research questions and falsification criteria

### RQ1 — Operator response heterogeneity

**Question:** At the same requested strength, do different variation operators induce measurably different distributions of realized behavior displacement and executable-child rate?

- Measurement: fixed probe tasks, parent/child trace distance, validity, and fitness change recorded separately.
- Control: same parent, task, model, seed, and requested strength wherever feasible.
- Falsification: if response distributions are indistinguishable or do not alter downstream operator decisions, drop operator-specific calibration.

### RQ2 — Scale-conditioned lineage-value credit

**Question:** Does conditioning continuation-value estimates on realized displacement improve ranking/selection of useful operator-strength actions over immediate reward, raw lineage return, and diversity-aware AOS?

- Measurement: predeclared horizon-H branch outcome; conditional prediction error and ranking metrics; task success.
- Control: randomized or matched operator/strength probes with sufficient overlap in realized displacement.
- Falsification: if the method does not beat the naive joint operator-strength controller with raw lineage return and strong AOS, remove the residual-credit decomposition.

### RQ3 — Search improvement and generalization

**Question:** Under matched evaluation budgets, does the controller improve task success on held-out task families rather than only random held-out instances from the same task pool?

- Primary metric: task success on held-out task families.
- Secondary metrics: executable offspring rate, realized displacement, branch-value prediction, diversity/coverage, and compute.
- Falsification: if gains disappear under family-held-out splits or after static EA hyperparameters are tuned, do not claim a general method improvement.

## 4. Experiment design: avoid split leakage

### 4.1 Baseline and benchmark audit

| Candidate | Source-level finding | Decision |
|---|---|---|
| EvoTool (ACL 2026) | Official implementation is MIT and provides a modular four-part policy, targeted mutation, diversity-aware selection, and offline execution. | Strong direct baseline and smoke-test harness; do not claim its mechanisms as new. |
| EvoTool bundled τ-bench demo | Its builder's actual source order is test → train → dev, then it takes the first valid tasks; the runner later partitions that pool. The docstring and code order also disagree. | Smoke tests only. Do not treat the bundled 90/30/30 split as an untouched official test. |
| Official τ²/τ³-bench, current candidate v2.0.0 | MIT repository; frozen benchmark manifests; explicit source train/test lists. v2.0 differs from 1.x and must be pinned. | Leading realistic validation candidate, pending task-family and manifest-overlap audit. |
| Frozen `text-v1` manifest | Direct ID comparison: airline_50 = 30 source-train + 20 source-test IDs; retail_50 = 28 + 22; telecom_50 = 27 + 23. The subset artifacts are drawn from the `base` frame. | The full `text-v1` score is not held out if evolution used the source-train tasks. Report only locked test groups or a clearly labelled research split. |
| BFCL v4 | An independent 2026 review reported defects affecting 24 of 50 sampled tasks. | Secondary robustness check only after auditing the exact selected examples; do not use as the only evidence source. |
| Tool-Veritas | Apache-2.0 local tool sandbox with deterministic gates and traces; bundled `all.jsonl` has 70 cases across 16 domains, no ready-made thesis split. Its reported human agreement is author-reported and not independently reproduced here. | Use as an execution substrate and independently verify a larger family-held-out task set; do not treat the bundled 70 cases as a complete benchmark. |
| Evaluator-validity audit | Bhat et al. report 92 evaluator-human disagreements across 496 executions (18.5%), including 11/112 for τ²-Bench Retail; Epoch AI separately reports 24/50 sampled BFCL v4 tasks with defects. | Audit selected tasks and scorer behavior. Report task-state success separately from tool-call validity and conversational quality. |
| ToolMaze | Current public code/data rights and official split remain unresolved. | Not a primary benchmark until the rights gate is closed. |

### 4.2 Recommended two-level protocol

1. **Mechanism isolation:** build an independently authored deterministic tool-task suite with exact state transitions and an exact success oracle. Use it to compare operator/strength response distributions under matched parents and fixed probe tasks.
2. **Realistic validation:** port/adapt the selected policy representation to a pinned τ²/τ³-bench release. Do not use the complete frozen `text-v1` manifest as held-out evidence after training on source-train IDs.
3. **Task-family holdout:** derive family fingerprints from redacted scenario instructions, issue/template metadata, and tool/action signatures. Assign whole groups to train/validation/test; do not randomly split near-duplicate task variants.
4. **External check:** optionally use a manually audited BFCL v4 subset, with exact version and task IDs recorded.
5. **Fairness:** match policy representation, model/version, decoding settings, evaluator, seed set, candidate-evaluation count, and stop rules. Report custom research splits as custom splits, not official leaderboard scores.

The exact overlap computation and source links are recorded in `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`.
## 5. Proposed baseline ladder

1. Static starting Agent / no evolution.
2. Tuned static EA: random search or SMAC over population size, offspring count, mutation probability, selection pressure, and fixed operator mixture; tune on train/validation only.
3. EvoTool full method (blame-targeted mutation + diversity-aware selection).
4. Classical AOS with immediate fitness-improvement credit.
5. Classical AOS with diversity/parent-distance credit.
6. ELMER-style behavior-strength control.
7. LVPG-style state/horizon and raw lineage-value control.
8. Naive joint operator-strength control with immediate reward.
9. Naive joint operator-strength control with raw lineage return.
10. OSLVC-R1 scale-conditioned lineage-value credit.

Use the same policy representation, model, tasks, seed set, stop rules, and evaluation budget wherever technically possible. Document deviations instead of pretending all methods are identical.

## 6. Parameter-tuning protocol

- Stage 0: lock the Agent policy representation, task loader, evaluator, trace schema, and cache semantics.
- Stage 1: tune static EA parameters with random search or SMAC on training/validation tasks. Use a small staged design; do not sweep every knob.
- Stage 2: freeze static parameters and compare online control variants.
- Stage 3: test task-family generalization once on a locked test set.
- Avoid adding adaptive population size, multi-objective objectives, new memory banks, or a second meta-controller until the central credit hypothesis survives falsification.

## 7. Opening-report claim boundaries

Allowed now:
- “Existing work establishes adaptive strategy portfolios, behavior-grounded mutation scale, lineage return, and diversity-aware operator/population control.”
- “This research will test whether conditioning lineage-value credit on realized Agent behavior displacement improves evolutionary decisions.”

Not allowed yet:
- “OSLVC-R1 is novel.”
- “The method outperforms state of the art.”
- “EvoMAS does not use lineage or scale-conditioned credit.”
- “The custom split is the official BFCL/τ-bench score.”
- “Three independent innovations have already been established.”

## 8. Immediate next decisions

1. Obtain the final EvoMAS paper PDF in readable form and close the exact reward/state/operator audit.
2. Confirm the precise benchmark and data licenses for the selected subset, including attribution requirements.
3. Fix family-held-out split and metric protocol before any model-based evolution.
4. Run a no-paid-call smoke test using a local model and offline executor.
5. Only after these gates, preregister the small falsification experiment.


## 9. Added nearest work — Hu et al. EvoMAS (2026)

The full-text audit of *EvoMAS: Evolutionary Generation of Multi-Agent Systems* (Hu et al., ICML 2026; https://arxiv.org/html/2602.06511) confirms a structured MAS configuration space, execution-trace-conditioned mutation of one component type per step, topology-inheriting crossover, task-relevance/performance-history-based parent selection, reward combining task metrics and token/latency cost, reward-based pool updates, and cross-query experience memory.

Do not claim generic feedback-conditioned mutation/crossover, experience memory, or reward-based parent acceptance as novel. The official code uses CC BY-NC 4.0, so preserve attribution and non-commercial terms. Detailed audit: research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md.
