# Thesis Feasibility and Next Research Gate — 2026-10-29

**Repository:** `yujian777555/openissue` only  
**Immediate deliverable:** Master's thesis opening report  
**Stage:** Proposal-stage; no thesis topic, algorithm, or innovation point is finally approved  
**Last known pre-update HEAD:** `f3b65679c409a8ca7ad25e5f8d5adb5720ffe4dd`  
**Experiment status:** No formal Agent experiment or paid API experiment has been run for OSLVC-R1.

## 1. User's objective and scope

The work is the first step toward a coherent master's thesis, not implementation of a single standalone paper. The intended thesis should have 2–3 connected substantive contributions and aim to produce 2–3 small papers, but contributions must not be split artificially just to reach a count. Evolutionary computation must be central. Parameter tuning/control must be explicit. Communication-evolution topics are excluded. The immediate task is to build an evidence-based proposal: related work → concrete limitation → research question → candidate mechanism → strong baselines → falsifiable experiments → feasibility and risk plan.

## 2. Current working framing

**Provisional title:** 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》

**Umbrella question:** How can evolutionary optimization of structured LLM-Agent tool-use policies be made behaviorally controllable and adaptively governed, while improving held-out task-family performance?

This is a working frame only. Do not treat the title, candidate method, or contribution map as final.

## 3. Current core candidate and novelty boundary

**OSLVC-R1 — scale-conditioned lineage-value credit** is the most specific current candidate, not an approved innovation.

The narrow hypothesis is: raw immediate reward or raw lineage return may confound (a) the realized magnitude of a policy's behavioral change with (b) the operator's additional continuation value. Test whether estimating operator continuation value conditional on realized behavior displacement, using matched parent/task/search-state comparisons and equal descendant-evaluation opportunities, improves operator/strength decisions and downstream Agent task success.

The following ingredients are already prior art and cannot be claimed as novel in isolation:
- behavior-grounded mutation-scale calibration (ELMER);
- long-horizon mutation-radius/lineage-value control (LVPG / *The Time Value of Evolution*);
- adaptive strategy portfolios/meta-control (EvoMAS: Heuristics in the Loop);
- modular Agent-policy evolution, trajectory/blame-guided targeted mutation, and diversity-aware selection (EvoTool);
- generic adaptive operator selection and self-adaptive parameter control.

The final ICML/PMLR method of *EvoMAS: Heuristics in the Loop* is still not fully audited at equation/code level. Do not infer absence of equivalent mechanisms from its abstract or from an earlier manuscript. Gate G0 remains OPEN.

## 4. Feasibility assessment (explicitly subjective)

The latest conversational estimate was:
- **Whole-thesis completion feasibility: 75–85%**;
- **OSLVC as the final effective algorithmic contribution: 35–50%**;
- **Ending with 2–3 independent, defensible innovation points: 50–65%**;
- **Achieving the target of 2–3 small-paper submissions: 40–60%**.

These are rough judgment ranges, not calibrated probabilities, statistical forecasts, or claims based on completed experiments. They express that the overall thesis is more feasible than this specific candidate's novelty and empirical success. The estimate must be revised when G0/G1/G2 evidence becomes available. Do not quote the ranges as measured results.

Why the thesis remains feasible even if OSLVC fails: the umbrella problem can remain Agent policy evolution with explicit EC control; the specific credit estimator can be revised or removed if it adds no value. This fallback only works if a genuinely distinct alternative mechanism is established before expensive experiments—not by relabelling existing ideas.

## 5. Current benchmark and evaluator decisions

- **EvoTool (ACL 2026, MIT implementation):** strong direct baseline/reference; targeted mutation and diversity-aware selection are prior art. Its bundled τ-bench demo split is smoke-test-only, not final held-out evidence.
- **Tool-Veritas:** candidate local deterministic execution substrate (Apache-2.0 subproject), not an already sufficient benchmark. The bundled set has 70 examples across 16 domains and no ready-made thesis split. Build and independently verify a larger family-held-out suite; use goal-state invariants as the primary success oracle.
- **τ²/τ³-bench:** candidate external realistic validation only after pinning a single release and auditing exact task/scorer behavior. Do not use the full frozen `text-v1` manifest as held-out evidence after evolution on source-train tasks: the source audit found airline_50 = 30 train / 20 test IDs, retail_50 = 28 / 22, telecom_50 = 27 / 23.
- **Evaluator reliability:** a 2026 audit reports 92 evaluator–human disagreements across 496 tool-calling executions (18.5%), including 11/112 in its τ²-Bench Retail sample. This does not invalidate every benchmark task; it requires auditing the selected tasks and scoring rules.
- **BFCL v4:** secondary robustness check only after auditing the exact subset; not the sole evidence source.
- **ToolMaze:** not the default primary benchmark while its data/license/split gate remains unresolved.

Full source-level decisions are in `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`.

## 6. Three gates before full implementation

### G0 — Prior-art distinction (OPEN)
Obtain a readable final ICML/PMLR version of *EvoMAS: Heuristics in the Loop* or verified author source; document its state, action, reward/credit, update equations, lineage horizon, baselines, and ablations. Compare against ELMER, LVPG, classical AOS including diversity/parent-distance credit, EvoTool, and static HPO. If an equivalent mechanism already exists, revise the candidate rather than claiming novelty.

### G1 — Benchmark, data, and split validity (PARTIAL/OPEN)
Select one local controlled substrate and one external realistic validation route. Verify licenses, exact version, task IDs, task-family fingerprints, split hashes, and scorer rules. Assign whole near-duplicate task families to train/validation/test. Keep the test split locked. Do not call a custom split an official leaderboard split.

### G2 — Baseline and mechanism feasibility (NOT RUN)
Only after G0/G1 are sufficiently closed, run a no-paid-call local pilot:
1. validate deterministic task execution and goal-state oracle;
2. test whether operators/strength settings produce materially different realized displacement distributions under matched parents/tasks;
3. test whether displacement-conditioned operator credit predicts continuation value beyond immediate reward, raw lineage return, and displacement-only features;
4. check whether that predictive improvement changes search decisions.
If the conditional operator residual is negligible or unstable, remove/revise it. Do not start the full controller or paid API runs merely to protect the current idea.

## 7. Required baseline ladder

At minimum compare:
1. no evolution / base Agent;
2. static EA with train/validation-tuned hyperparameters;
3. EvoTool or a faithful component-level baseline where direct porting is infeasible;
4. classical adaptive operator selection with immediate-reward credit;
5. AOS with diversity/parent-distance credit;
6. behavior-scale-only control (ELMER-style);
7. lineage-only control (LVPG-style);
8. naive joint operator–strength control with raw lineage return;
9. proposed scale-conditioned lineage-value credit.

Match representation, model/version, tasks, seeds, candidate-evaluation count, stopping rule, and tuning data. Tune static EA settings first and freeze them before online-control comparison. Primary metrics are task success and held-out task-family success; behavior-distance calibration, validity, lineage best-so-far AUC, and value-prediction quality are mechanism diagnostics. Cost is secondary.

## 8. Proposal-writing guidance

The proposal may present OSLVC-R1 as a **research hypothesis**, not a proven innovation. State:
- what prior methods already do;
- what precise limitation is hypothesized;
- why the limitation matters for Agent policy evolution;
- the proposed EC mechanism and its mathematical target;
- strong baselines, ablations, task-family holdout, and falsification criteria;
- a fallback decision if the hypothesis fails.

Do not claim that the three research layers automatically equal three innovations. The defensible target is two strong connected contributions; a third remains optional unless an independent mechanism survives prior-art review.

## 9. Next concrete actions

1. Continue the final EvoMAS HIL method audit; keep G0 OPEN until evidence is sufficient.
2. Finish a task-family/split/scorer protocol for Tool-Veritas plus the selected τ²/τ³ external subset.
3. Draft the proposal's linked sections: research status → concrete gap → scientific questions → research contents → candidate innovations → technical route → experiments/feasibility → risks and alternatives.
4. Only then authorize a small local pilot. No paid API experiment before the gates are passed.

## 10. Continuity rules

- Use only `yujian777555/openissue` for this thesis project; do not mix it with `agentfotagent`, `EvoPareto-Agent`, `CausalEvo-DSH`, `GLEPPO`, or other repositories.
- Start each new conversation by reading `research/STATUS.md`, `research/DECISION_LOG.md`, `SESSION_HANDOFF.md`, this file, `research/THESIS_PROPOSAL_FRAMEWORK.md`, and `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`.
- Distinguish source-verified facts, interpretations, hypotheses, and experiment results.
- Record each major decision and gate state. Never claim a paper audit, experiment, push, or test completed without evidence.
