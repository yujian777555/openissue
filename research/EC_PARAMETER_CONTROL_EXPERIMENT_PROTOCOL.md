# Experimental Protocol: Evolutionary Policy Search and Parameter Control for Agent Recovery

**Date:** 2026-10-23  
**Status:** Proposed protocol for a feasibility pilot; not an approved thesis method or novelty claim.  
**Research constraint:** Evolutionary computation must be tested as a causal mechanism for improved Agent capability, not used as a decorative optimizer or justified only by lower evaluation cost.

## 1. Why this is the next useful experiment

Three strands of prior work now define the comparison space:

1. **EVOTOOL (ACL 2026)** already combines modular tool-use policies, trajectory-grounded module blame, feedback-guided targeted mutation, and diversity-aware selection. Its ablations directly compare static, random, single-module, monolithic, greedy, top-k, and diversity-aware variants.
2. **ToolMaze (arXiv, June 2026)** provides a controlled testbed for recovery after tool perturbations. Its axes are task-graph complexity C1–C4 and perturbation type P1–P4: explicit/transient, explicit/permanent, implicit/transient, and implicit/permanent. It provides task success rate (TSR), perturbation recovery rate (PRR), and recovery cost (RC), and injects deterministic faults at predefined tool nodes.
3. **Parameter-control prior art** already includes static HPO, adaptive operator selection (AOS), self-adaptation, and the 2026 Code World Models (CWM) preprint. Therefore “adjust mutation probability when progress stalls” is a baseline, not a novelty claim.

A potential experiment is to test whether a constrained, interpretable recovery-policy genotype plus a principled evolutionary search/control mechanism improves recovery on held-out fault/topology combinations. This remains provisional: a result may show that a simpler rule-based policy or existing EVOTOOL mechanism is sufficient, in which case the EA-centered candidate should be rejected or revised.

Primary sources:
- EVOTOOL: https://aclanthology.org/2026.acl-long.2016/
- ToolMaze paper: https://arxiv.org/abs/2606.05806
- ToolMaze code: https://github.com/Zhudongsheng75/ToolMaze
- LLaMEA-HPO: https://doi.org/10.1145/3731567
- CWM parameter control: https://arxiv.org/abs/2602.22260
- AOS survey: https://www.computer.org/csdl/journal/ai/2025/08/10904096/24CDFPmIqdi
- Hierarchical Trial and Error / QD recovery: https://doi.org/10.1145/3596912

## 2. Three parameter levels — do not conflate them

| Level | Examples | How to handle it |
|---|---|---|
| **Agent policy genes** | Retry limit, rule conditions, anomaly thresholds, selected recovery action, priority order, backtrack depth | Evolve as part of the candidate policy genotype; do not silently count these as EA hyperparameters. |
| **EA meta-parameters** | Population size, offspring count, mutation/crossover probabilities, operator mixture, parent/survivor selection, replacement strategy | Tune on training/validation only using a documented HPO method or pilot design; then freeze for test. |
| **Online controller parameters** | AOS credit assignment, exploration rate, probability-matching pressure, UCB/Thompson parameters, stagnation window, feedback schedule | Compare static, deterministic, adaptive, and self-adaptive controllers. If tuned, use nested training/validation, never the final test set. |
| **Evaluation/environment settings** | Task topology, tool family, perturbation class, fault location, task split | Define the scientific test. Do not tune against the held-out test distribution. Use these variables for stratified analysis and OOD evaluation. |

A nominal LLM instruction such as “make a small mutation” is not a calibrated mutation-strength parameter. For every offspring, log the actual changed rules/fields, whether its structure changed, whether behavior changed on a fixed probe set, and whether the policy remains valid.

## 3. Candidate policy representation to test

For a first feasibility pilot, use a restricted, typed domain-specific language (DSL) rather than arbitrary executable code or unrestricted natural-language prompts. The goal is to make variation measurable, candidates inspectable, and invalid policies rejectable.

### Candidate rule schema

Each rule contains:
- **Condition:** observable tool/runtime evidence, such as explicit error code, timeout, repeated failure, schema-valid but inconsistent output, postcondition violation, number of failed attempts, or existence of alternative paths.
- **Action:** retry once, verify output, switch to a compatible tool/path, backtrack to the last consistent state, replan remaining dependencies, or stop/ask for clarification when the task is infeasible.
- **Parameters:** retry limit, anomaly threshold if supported by a verifier, maximum backtrack depth, and rule priority.
- **Guardrails:** preconditions for side-effecting actions, no infinite retries, no use of hidden benchmark labels at runtime, and explicit termination.

Only observable information may drive runtime decisions. The optimizer may stratify training results by the benchmark's fault labels, but the candidate policy must not receive hidden labels such as “this is P4” unless the deployed agent could infer that fact from actual observations.

### Variation operators

Use operators with explicit semantics:
1. change one condition or predicate;
2. substitute one recovery action;
3. change a numeric/discrete rule parameter;
4. add or delete a rule;
5. split or merge rules;
6. reorder rule priority;
7. recombine compatible rule subsets from two parents;
8. optionally ask an LLM to propose a structured edit, then parse and validate it against the DSL.

This allows mutation magnitude to be measured as number/type of changed fields or rules, rather than inferred from prose. The first pilot should begin with deterministic structured operators; add LLM-semantic mutation only after the base EA works.

## 4. Research questions and falsifiable hypotheses

### RQ1 — Does evolution add capability?

Does evolution of recovery policies improve fault recovery and recovery efficiency on ToolMaze compared with fixed rules and direct LLM reflection/replanning under matched interaction budgets?

- **H1 (hypothesis):** EA search discovers combinations of conditional recovery rules that improve held-out recovery without degrading clean-task success.
- **Falsifier:** gains disappear against a carefully tuned fixed rule set or direct reflection baseline; or gains occur only on optimization tasks, not held-out topologies/faults.

### RQ2 — Which evolutionary mechanisms matter?

Do structured variation and population selection outperform random edits, one-rule-at-a-time greedy search, and prompt-level mutation under the same task instances and evaluation budget?

- **H2 (hypothesis):** semantically typed rule operators create more valid and behaviorally distinct candidates than unstructured edits.
- **Falsifier:** structured operators do not improve capability, or gains are explained by more LLM calls / rollouts.

### RQ3 — Does adaptive parameter control help beyond static tuning?

Does selecting mutation operators online from search feedback and failure-context signals improve held-out recovery compared with the best frozen operator mixture and classical AOS baselines?

- **H3 (hypothesis):** context-conditioned operator selection can allocate variation differently across error/topology regimes and improve generalization.
- **Falsifier:** a fixed mixture selected by SMAC/random search matches or beats the adaptive controller, or adaptive gains do not transfer to held-out fault/topology combinations.

No hypothesis above is accepted as true in advance. The method should be abandoned or narrowed if the tests falsify them.

## 5. Proposed parameter map and pilot ranges

These ranges are initial engineering hypotheses, not tuned settings or reported optima. The pilot should first verify that each candidate is valid and that metrics respond to controlled changes.

| Parameter | Type / initial candidates | Why it matters | Pilot treatment |
|---|---|---|---|
| Population size N | {4, 8, 16} | Controls policy diversity and evaluations per generation | Small sensitivity sweep |
| Offspring per generation λ | {2, 4, 8} | Controls exploration rate | Sweep jointly with N only if budget permits |
| Rule mutation scope | {one field, one rule, 2 rules, structural edit} | Operationalizes mutation strength | Record realized edit and behavior delta |
| Operator mixture | categorical mixture over condition/action/add-delete/split-merge/reorder/crossover | Determines what changes are explored | Random mixture baseline; then static HPO |
| Crossover probability | {0, 0.2, 0.5} | Tests whether recombination helps rule sets | Disable if policy schema/semantics are not compatible |
| Parent selection | tournament (k=2 or 3), greedy, top-k | Sets selection pressure | Standard baseline comparison |
| Survivor selection | greedy, elitist, NSGA-II, behavior-archive/QD | Trades best score, objectives, and behavioral coverage | Compare only after policy evaluation is stable |
| Stagnation window | {3, 5, 8} generations without meaningful improvement | Candidate signal for online control | Tune on validation; not a standalone innovation |
| AOS controller | static mixture, probability matching/adaptive pursuit, UCB or Thompson sampling | Adapts operator probability based on observed rewards | Compare after static HPO |
| Agent-level retry limit | {0, 1, 2, 3} | Can change behavior but may create loops | Evolve as a policy gene; track excess calls |
| Agent-level backtrack depth | {0, 1, 2, 3} | Controls recovery search depth | Evolve as a policy gene; track success and cost |
| Agent-level rule threshold | bounded discrete/continuous value, if a reliable verifier exists | Trades anomaly detection precision/recall | Evolve or HPO depending on genotype design, not both without a declared reason |

Do not run the full Cartesian product. Use a staged design:
1. validate the policy representation and metric implementation;
2. screen a few influential EA settings with a small fractional-factorial or one-factor-at-a-time pilot;
3. tune a static configuration using SMAC or random search on training/validation instances;
4. freeze that configuration and compare parameter-control methods;
5. run confirmatory experiments across independent seeds and held-out splits.

## 6. Parameter-control baselines

At minimum compare these controller families:

1. **Fixed default:** literature-informed, frozen parameters.
2. **Static tuned:** strongest validation-selected configuration from random search or SMAC.
3. **Deterministic schedule:** predefined mutation/operator changes over generations.
4. **Classical adaptive operator selection:** e.g. probability matching or adaptive pursuit with explicit credit assignment; include a bandit-based baseline if implementation is feasible.
5. **Self-adaptive:** encode operator/strength strategy parameters with individuals and allow them to vary and be selected with the policy.
6. **Context-conditioned AOS (candidate):** condition operator selection on observable failure class, task topology/remaining alternatives, accepted-child rate, behavioral novelty, and stagnation. This is only a candidate mechanism; compare against non-contextual AOS and tune all controller hyperparameters on validation.
7. **CWM-style model-based control (later-stage optional baseline):** synthesize/fit an auditable transition model of search state and predict which operator/strength is promising. CWM's published preprint studies mutation strength in classical combinatorial optimization, not LLM-Agent policy evolution. Do not claim direct transfer; first establish that a useful state/action/transition model can be estimated.

The online controller should receive only information available at that point in the run. If the controller uses the hidden ground-truth perturbation label, it is an oracle diagnostic upper bound, not a deployable method.

## 7. Benchmark and split design

Use ToolMaze as a candidate evaluation substrate because it supplies deterministic perturbation injection and explicit task-complexity/fault axes. First verify the current repository, data license, task generator, evaluation scripts, and actual baseline reproducibility.

Recommended split logic:
- **Training:** task templates and tool families used for candidate evolution.
- **Validation:** disjoint task instances for static HPO, parent/survivor selection, and controller tuning.
- **In-distribution test:** unseen instances from represented fault classes and topologies.
- **Compositional/OOD test:** held-out combinations of graph complexity and perturbation type (for example, train on a subset of C/P combinations and evaluate on combinations not used for tuning).
- **Tool/domain transfer:** if the benchmark supports it, hold out tool families or domains rather than only paraphrased queries.

Split by underlying DAG/template and tool-family identity, not merely natural-language query string, to avoid near-duplicate leakage. Never use test scores for selection, HPO, or prompt edits.

## 8. Metrics and fitness

Report the benchmark's core metrics separately:
- Task Success Rate (TSR);
- Perturbation Recovery Rate (PRR);
- Recovery Cost (RC; lower is better under ToolMaze's definition);
- clean / non-perturbed success rate;
- unnecessary retries, invalid tool calls, loops, and graceful termination on infeasible tasks;
- generalization gap from in-distribution test to compositional/OOD test.

Do not optimize only aggregate TSR. A candidate can appear better by retrying excessively, abandoning hard tasks, or degrading non-perturbed cases. A possible initial fitness is a constrained objective: maximize PRR subject to a minimum clean-task TSR and a maximum recovery-cost/loop rate; compare it with multiobjective optimization (e.g. NSGA-II) as a baseline. Report the full metric vector regardless of the scalar used internally.

## 9. Minimal ablation matrix

| Ablation | Question answered |
|---|---|
| No evolution / fixed policy | Is any search needed? |
| Random structured mutation | Is the EA doing more than sampling edits? |
| Greedy one-child mutation | Does population-based search add value? |
| Static tuned EA vs default EA | Are gains only from hyperparameter tuning? |
| Structured DSL vs free-text prompt mutation | Does the representation help? |
| Fixed operator mixture vs adaptive operator selection | Does online parameter control add value beyond tuning? |
| Context-conditioned AOS vs non-contextual AOS | Does fault/topology context improve operator choice? |
| Scalar fitness vs constrained/multiobjective selection | Are gains due to unsafe metric trade-offs? |
| Remove behavior archive / diversity selection | Is coverage of distinct recovery behaviors useful? |
| Remove one operator family at a time | Which variation mechanisms cause gains? |
| No-fault test | Does recovery specialization damage normal capability? |
| Held-out C/P combinations and tool families | Is the policy generalizing rather than memorizing? |
| Direct LLM reflection/replanning and EVOTOOL-style baseline | Is evolutionary search better than strong nearby methods? |

Match backbone model, task instances, seeds, rollouts, and API/compute budgets as closely as possible. Report both wall-clock/token/API costs and capability metrics, but do not make cost reduction the central scientific claim.

## 10. Feasibility pilot and stop gates

### Pilot A — benchmark and baseline sanity
- Install ToolMaze in an isolated environment; inspect license, dependencies, and perturbation injection.
- Run a small number of unperturbed and perturbed tasks for at least one API model and one local/open model if available.
- Verify TSR, PRR, RC calculations manually on sampled traces.
- Confirm no real external side effects are possible in the sandbox.

### Pilot B — policy DSL
- Implement a hand-written baseline with explicit retry/reroute/verify/abort rules.
- Verify the DSL parser, static checks, deterministic operator behavior, and loop guards.
- Measure whether each operator produces valid and behaviorally distinct children.

### Pilot C — static EA
- Start with small N and λ, structured mutation only, and a fixed training split.
- Compare fixed policy, random mutation, greedy one-child search, and population EA.
- Do not add an adaptive controller until static evolution shows a repeatable capability gain.

### Pilot D — parameter tuning/control
- Use the same training/validation cases and a fixed evaluation budget to tune a static configuration.
- Compare frozen best settings with deterministic schedule, classical AOS, and self-adaptation.
- Add context-conditioned AOS only if its control signal is operationally measurable and its baseline comparison is fair.

### Stop / revise criteria
Reject or redesign this line if:
- the fixed rule baseline performs as well as the EA;
- the EA gain disappears under matched rollout/API budgets;
- gains are limited to training-like fault/task templates;
- the method cannot improve implicit semantic failures without access to hidden labels;
- dynamic parameter control does not beat a static tuned setting;
- behavior changes cannot be attributed to a specific evolutionary component;
- a close-work audit finds that the exact genotype/operator/controller mechanism is already covered.

## 11. Current conclusion

The next practical step is not to announce a new algorithm. It is to validate ToolMaze as an evaluation substrate, reproduce baseline recovery behavior, and test whether an interpretable recovery-policy genotype gives the EA a meaningful search space. Only after a static EA demonstrates capability gains should we invest in parameter control. If static tuning explains the gains, use the simpler method and do not claim adaptive EC as the contribution.


## 12. ToolMaze implementation audit — must resolve before using reported metrics

**Important discrepancy found by inspecting the public repository** (current main branch checked 2026-10-23):

- The paper defines mode-level Recovery Cost as an average over all trajectories with an explicit perturbation indicator, so no-hit trajectories contribute zero to the mode-level average: https://arxiv.org/html/2606.05806v1
- The repository README likewise states “No-hit runs contribute 0”: https://github.com/Zhudongsheng75/ToolMaze/blob/main/README.md
- However, `evaluation/core/metrics.py` implements `compute_rc` by collecting only runs with `r["hit"]` and non-null `r["rc"]`. This excludes no-hit trajectories from the denominator instead of assigning them zero. Unless the authors intentionally changed the metric without updating the paper/README, this can produce different RC values and must be resolved before using RC to compare methods.

**Required check/fix:**
1. Create a tiny synthetic fixture with one no-hit run, one hit-and-fail run (RC=1), and one hit-and-success run (known RC).
2. Compute RC using (a) the paper/README all-run formula and (b) the current code's hit-conditioned formula; assert both outputs and document which definition is used.
3. Verify whether the paper's reported values were computed with the current implementation or a prior version. If unclear, report both definitions as a sensitivity analysis rather than silently choosing one.
4. Do not modify upstream code invisibly. If a local patch is needed, record it in the experiment repository and cite the exact upstream commit/version.

**Licensing / reproducibility caveat:** The inspected ToolMaze GitHub tree did not expose a root LICENSE file, and the Hugging Face dataset card did not expose a clear license field in the inspected metadata. This is not a legal conclusion, but code/data licensing must be confirmed before redistributing modified copies or publishing derived artifacts. Record the exact commit and dataset revision used.

This does not disqualify ToolMaze as a benchmark. It changes the gate: benchmark version, metric implementation, task split, and license must be checked before the first baseline is considered reproducible.

