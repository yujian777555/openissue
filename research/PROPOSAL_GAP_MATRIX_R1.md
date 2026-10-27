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

### Recommended two-level protocol

1. **Feasibility stage:** use the public EvoTool implementation and a small offline benchmark subset to verify the local model, environment, trace capture, deterministic evaluator, and cache. This is a smoke test only, not paper evidence.
2. **Method stage:** construct explicit train/validation/test partitions by task template or tool/API family. Fit the scale/credit model only on train; tune static EA parameters and select checkpoints on validation; freeze everything before test.
3. **External validation:** test transfer on a second benchmark/task family that was not used for mutation calibration. The split and evaluator must be fixed before comparing methods.
4. **Matched budget:** same backbone, generation/evaluation budget, seeds, cache policy, stop rule, and evaluation calls for all methods. Report extra probe cost separately.

### Benchmark audit

| Candidate | Verified feasibility evidence | Risk | Recommendation |
|---|---|---|---|
| EvoTool repository | Official ACL 2026 implementation; MIT code; local OpenAI-compatible model endpoint; deterministic offline executor; demo subsets; one A100-class GPU stated as sufficient for Qwen3-8B | Its demo subset is not equivalent to an untouched official leaderboard test set; split is random within the bundled 150 examples | Best harness for a low-cost feasibility pilot and strong direct baseline |
| BFCL v4 via EvoTool | Upstream Gorilla repository identifies Apache-2.0 license; EvoTool converter selects hard multi-call categories; offline execution is supported | A repository-level code license does not automatically settle every upstream data/annotation term; custom evolution splits must not be reported as official BFCL leaderboard scores | Candidate primary controlled benchmark after task/API-family split and license review |
| Original τ-bench | Upstream repository license is MIT | Its own README says the tasks are outdated; EvoTool's converter iterates canonical test tasks before train/dev and takes the first 150 valid tasks, then the runner randomly partitions those 150 into train/selection/test. This can place official test tasks into evolution data | Do not use this demo builder for final test claims |
| τ³-bench / updated τ-bench line | Official successor repository provides updated/fixed tasks and MIT code license | EvoTool's existing vendored adapter targets the older interface; port and verify the adapter and evaluator | Candidate external validation after adapter audit |
| RestBench / RestGPT | RestGPT code repository is MIT; EvoTool uses an offline executor | The original task set is a test set; data redistribution terms and any API-schema rights need explicit review; random partition is not a family-held-out split | Secondary benchmark only after rights and split review |
| ToolBench | Upstream repository uses Apache-2.0 code license | Processed answer sets are large and derived from external/API-related sources; confirm data-specific terms and source availability before redistributing or using them as a thesis artifact | Not first choice for the initial pilot |

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
