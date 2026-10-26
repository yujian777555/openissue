# Evolutionary Computation's Role and Parameter Control for Agent Improvement

**Status note (2026-10-26):** This document records the earlier recovery-policy/parameter-control research line. That line is not the active candidate: broad recovery directions were downgraded after prior-art and benchmark audits. Do not execute the ToolMaze/recovery experiment plan unless the current `research/STATUS.md` explicitly reopens it; see `research/CAPABILITY_GAP_REVIEW.md` and `research/TOOLMAZE_BENCHMARK_AUDIT.md`.

**Date:** 2026-10-23  
**Status:** Methodological research note; no final thesis topic or algorithm approved  
**Purpose:** Make evolutionary computation a substantive research method, not a generic wrapper for LLM prompt tweaking or a few numerical hyperparameters.

## 1. Central distinction: three different parameter/search spaces

A research design must not mix these levels.

### Level A — Agent phenotype (what the EA evolves)

These are candidate behaviours or policy structures, not merely optimizer knobs:

- recovery policy: when to retry, replan, switch strategy, repair a call, use a fallback, or stop when a task is infeasible;
- preconditions and state/error signatures that activate a recovery behaviour;
- ordering/composition of actions or sub-policies;
- decomposition of agent functions into modules and their interfaces;
- potentially executable policy code, if a constrained representation is justified.

A candidate can be encoded as structured instructions, a rule/state machine, a small program, or a modular policy. The representation must make invalid or unsafe candidates rejectable and allow behaviour-level differences to be measured. The best representation is an open research question.

### Level B — Evolutionary-algorithm control parameters (how the EA searches)

Examples include population size, parent/offspring counts, mutation probability or strength, operator choice, crossover rate, selection pressure, replacement policy, diversity control, and stopping conditions.

For LLM-based semantic mutation, the classical bit-flip mutation rate is not directly meaningful. Mutation strength must be operationalized—for example, number of modules changed, allowed edit scope, semantic distance, or whether a candidate is locally refined versus structurally redesigned. A prompt saying “make a small change” is not a calibrated mutation operator unless the actual edit size and behaviour change are measured.

### Level C — Task/environment and evaluation settings (what is tested)

Examples include failure distributions, tool availability, environmental perturbations, task horizon, training/validation/test split, and test-case sampling. These are not ordinary optimizer parameters. They define the scientific problem and must not be tuned against the held-out test set. Environment variation may be part of the research object, but then its generation and difficulty must be controlled explicitly.

**Research implication:** The thesis must state which level is the main genotype and which levels are controlled variables. Tuning Level B alone is not sufficient evidence of a new Agent capability.

## 2. What the closest work establishes

### EVOTOOL (ACL 2026): mechanism-level EA for tool-use policies

Primary paper: https://aclanthology.org/2026.acl-long.2016/  
Official code: https://github.com/SYang2000/ACL_2026_EvoTool

The paper evolves four prompt-defined modules—Planner, Selector, Caller, Synthesizer. Its loop diagnoses a low-reward trajectory, asks an LLM to attribute the failure to a module, mutates that module, accepts the child if it beats its parent on the mini-batch, and applies validation-set population selection.

The official implementation was inspected:
- `evolve.mutation_target`: `blame`, `random`, `fixed:<module>`, `all`, or `none`;
- `evolve.selection`: `diversity`, `greedy`, `topk`, or `static`;
- `use_trajectory` and `use_feedback` toggle mutation guidance;
- default budget is 3 epochs over 90 training instances in batches of 3, yielding 90 generations; the code keeps separate selection and test splits;
- default selection preserves policies that win at least one validation instance and samples parents in proportion to their win frequency;
- the mutation target and selection strategy have direct ablations.

This is a strong baseline and a warning: failure attribution, module-targeted semantic mutation, and diversity-aware population selection are already directly combined. Merely adding “failure-aware mutation” or “diverse recovery strategies” would overlap substantially.

### LLaMEA and LLaMEA-HPO: separate structure from numeric tuning

Paper: https://arxiv.org/abs/2405.20132  
HPO paper: https://arxiv.org/abs/2410.16309  
Official code: https://github.com/XAI-liacs/LLaMEA

LLaMEA evolves algorithm implementations through generation, execution-based fitness, mutation, and selection. LLaMEA-HPO integrates SMAC so the LLM can search algorithm structure while a dedicated HPO procedure tunes the numeric parameters of each generated heuristic. This establishes a useful methodological rule: **algorithmic/behavioural structure search and numeric hyperparameter tuning should be separated and compared**, not conflated.

### Adaptive parameter control is a mature EC research area

Foundational classification:
- Eiben, Hinterding & Michalewicz (1999), *Parameter Control in Evolutionary Algorithms*: https://doi.org/10.1109/4235.771166
- Aleti & Moser, *A Systematic Literature Review of Adaptive Parameter Control Methods for Evolutionary Algorithms*: https://research.monash.edu/en/publications/a-systematic-literature-review-of-adaptive-parameter-control-methods-for-evolutionary-algorithms/

The classical distinction is between selecting settings before a run (parameter tuning) and changing them during search (parameter control). Common control families include deterministic schedules, feedback/adaptive rules, and self-adaptation where strategy parameters are encoded in individuals and evolve alongside solutions. Any proposal about changing mutation rate, population size, or operator probability must be compared with this prior art.

### Code World Models for Parameter Control (2026)

Paper: https://arxiv.org/abs/2602.22260

This work synthesizes an executable model of optimizer dynamics from trajectories, then uses it to choose mutation strength online. It reports promising results on OneMax, LeadingOnes, Jump_k, and NK landscapes. The work is about controlling a classical optimizer's mutation strength—not an LLM Agent recovery policy—but it directly warns against claiming novelty for “use an LLM to adapt EA parameters” without a more precise distinction. Its results also rely on problem descriptions and/or empirical transition statistics in some settings, so transfer to stochastic tool-use agents remains unproven.

### LLM mutation control (2025)

Paper: https://doi.org/10.1007/978-3-031-90065-5_27 (verify exact chapter metadata before formal citation)  
Discovery/abstract: https://www.alphaxiv.org/abs/2412.03250

This line uses dynamically adjusted mutation prompts and heavy-tailed edit-strength ideas in LLM-driven algorithm evolution. It reinforces that LLM semantic mutation magnitude and control are already being studied. Formal publication metadata and the precise method should be checked from the publisher before citing it in the proposal.

### Classical recovery after unexpected failures

Bongard et al., *Automated Robot Function Recovery after Unanticipated Failure or Environmental Change* (2004): https://meclab.w3.uvm.edu/papers/2004_CEH_Bongard.pdf

This work shows that evolutionary recovery after unanticipated physical damage predates LLM agents. A tool-agent recovery thesis must therefore explain what the discrete, language-mediated, long-horizon, tool/environment setting adds scientifically; “evolutionary recovery from unexpected failures” is not a new general concept.

## 3. What role should EC play in an Agent recovery study?

EC should be justified by the structure of the search problem, not by preference for a fashionable optimizer.

A plausible rationale to test is that recovery behaviour is a mixed, discrete, non-differentiable space: policies contain conditions, tool/action choices, stopping rules, and sequences of operations; success is measured by executing the agent in an environment; and candidate behaviours may be complementary across failure classes. Population-based search can propose and retain several structurally different candidates rather than relying on one gradient path or one reflective rewrite.

That rationale is only a hypothesis. It must be tested against simpler alternatives.

Potential EA-specific roles to investigate:
1. **Structured behavioural search:** evolve executable or constrained recovery rules, not only free-form prompts.
2. **Variation at explicit semantic units:** operators such as add/remove a condition, change a recovery action, alter a stopping guard, split/merge a rule, or compose two policies. Measure the edits actually produced.
3. **Selection by verified behaviour:** compare candidates across the same deterministic training cases and a held-out validation set; use independent test failure types only for final evaluation.
4. **Population retention:** investigate whether distinct policies solve genuinely different failure classes, rather than assuming diversity is always useful.
5. **Adaptive search control:** test whether operator choice or mutation strength should depend on observed search state. This is a possible mechanism, not an approved innovation; generic adaptive parameter control is established prior art.
6. **Transfer:** test whether the evolved policy generalizes to held-out failure signatures, tool schemas, environments, or task compositions without simply memorizing training instances.

## 4. A defensible parameter-tuning protocol

### Step 1 — Freeze the problem representation and baseline first

Before tuning anything, define:
- the task and failure taxonomy;
- the policy genotype and legal variation operators;
- the execution environment and deterministic fault-injection mechanism;
- the primary capability metric and guardrail metrics;
- disjoint train, validation, and test splits.

Without this, an apparent hyperparameter gain may come from changing the task, representation, evaluation, or model rather than improving the EA.

### Step 2 — Tune static settings before inventing adaptive control

Start from a literature-grounded baseline and conduct a small, explicit sensitivity study. Candidate factors include:
- population size / number of offspring;
- mutation target and mutation scope;
- operator mixture (local edit, condition edit, action substitution, structural redesign, composition);
- parent selection and survivor selection;
- diversity mechanism;
- number of generations;
- batch size and number of training instances per generation.

Use a small pilot sweep or a fractional-factorial design to identify influential factors. If the space is mixed and expensive, compare a dedicated HPO method such as SMAC with random search; use the same training/validation data and total evaluation budget. Do not choose a final setting based on test performance.

### Step 3 — Only then test parameter control

Compare at least:
- **Static:** one setting selected on training/validation and then frozen.
- **Deterministic schedule:** for example, predefined mutation-strength changes over generations.
- **Feedback-adaptive:** change mutation/operator probabilities based on observed search signals such as accepted-child rate, stagnation, policy novelty, or failure-class coverage.
- **Self-adaptive:** encode strategy parameters with each individual and let variation/selection act on them.
- **HPO baseline:** use SMAC or random search to choose a strong fixed setting.

Any proposed adaptive controller must be compared with classical self-adaptation and recent LLM-based parameter control. Do not assume the adaptive variant wins.

### Step 4 — Control the semantic mutation magnitude

For LLM-generated candidates, log:
- which policy components changed;
- textual diff size and, where possible, structured AST/rule diff;
- whether the change is local or structural;
- whether behaviour changes on a fixed probe set;
- child validity, execution success, and acceptance.

This is necessary because a nominal “mutation rate” in the prompt does not guarantee a particular edit magnitude. If semantic edit strength is central to the method, define a measurable operator rather than relying only on natural-language instructions.

### Step 5 — Evaluate capability, not only optimizer convenience

For a recovery candidate, use a multi-part scorecard:
- task completion after a fault;
- recovery success on unseen failure types or signatures;
- normal-case success when no fault occurs;
- unnecessary retries / loops / unsafe or invalid tool calls;
- recovery steps or latency;
- retention of previously solved task families.

A scalar fitness may combine some terms, but report all components separately. Guardrails should prevent a candidate from improving the average by aggressively retrying, abandoning difficult tasks, or degrading normal operation.

### Step 6 — Use causal ablations and fair comparisons

A minimal ablation matrix should isolate:
1. no evolution / static initial policy;
2. random mutation;
3. targeted mutation;
4. ordinary scalar-greedy selection;
5. diversity-aware selection;
6. static versus adaptive mutation/operator control;
7. free-text policy evolution versus structured recovery-policy evolution, if both are in scope;
8. EA versus direct LLM reflection and fixed retry/replan heuristics;
9. EA versus a dedicated HPO baseline for numerical parameters.

Keep backbone model, prompts unrelated to the tested factor, training examples, random seeds, total rollout/API budget, and test protocol matched. Report multiple seeds and uncertainty; freeze the test set until the method is finalized.

## 5. What would make EC scientifically central?

A strong paper should be able to answer all of these:
- **Search-space claim:** what difficult policy space is being searched, and why is it not merely a few numeric parameters?
- **Operator claim:** what variation operation is specific to the behavioural representation, and what evidence shows it creates useful candidates?
- **Selection claim:** what behaviours are preserved or removed, and why does this help beyond taking the current best candidate?
- **Control claim:** if parameters adapt during search, what observable state drives the change, and does that control beat static tuning and existing adaptive methods?
- **Causal claim:** do ablations show the gain comes from the proposed evolutionary mechanism rather than extra LLM calls, larger prompts, more rollouts, or a different backbone?
- **Generalization claim:** do improvements hold on unseen failure classes / environments rather than only the optimization instances?

If the only positive result is “GA with tuned hyperparameters beats defaults,” EC is not yet a substantive innovation.

## 6. Candidate hypotheses to test—not accepted contributions

### H1 — Structured recovery-policy evolution
A constrained policy representation and semantically meaningful operators may discover valid recovery strategies that are hard to obtain by prompt-only rewrites. Risk: code/program evolution and EVOTOOL overlap; representation complexity may not pay off.

### H2 — Failure-conditioned operator control
The search controller may choose different variation operators depending on the diagnosed failure and population/search state. Risk: EVOTOOL already uses blame to target a module; generic adaptive operator selection is mature EC prior art. A distinct mechanism must be demonstrated.

### H3 — Self-adaptive search parameters
Each candidate may carry its own mutation/variation settings, with selection favouring settings that work for its policy and environment. Risk: classical self-adaptation is established and may not be useful when candidates are natural-language specifications. Only retain if the parameter encoding has a clear semantics and measurable benefit.

None of H1–H3 is approved. They are testable directions for prior-art comparison and small pilot experiments after the problem is validated.

## 7. Immediate next actions

1. Complete a mechanism-level audit of EVOTOOL, including its actual configuration, mutation/selection ablations, validation selection, and official code.
2. Read LLaMEA-HPO and Code World Models for Parameter Control in full; document what is tuned, what is evolved, and what assumptions their evaluations require.
3. Review the classical parameter-control taxonomy and recent systematic review; add self-adaptive and adaptive-operator-selection literature.
4. Search evolutionary robotics / genetic programming / program synthesis for recovery-controller evolution after unanticipated faults.
5. Only after these audits, decide whether the thesis contribution should be (a) an Agent policy representation and evolution method, (b) a novel parameter/operator controller, or (c) another better-supported EC-centered mechanism.
6. Keep the state-contingent recovery problem provisional. If it overlaps too heavily with EVOTOOL and classic recovery controllers, reject it rather than forcing a novelty claim.


## 8. Mechanism-level audit update: ToolMaze, HarnessEvolve, QD recovery, and parameter tuning

### ToolMaze supplies a controlled evaluation space, not an EA solution

Paper: https://arxiv.org/abs/2606.05806  
Official code: https://github.com/Zhudongsheng75/ToolMaze

ToolMaze crosses task-DAG complexity C1–C4 with four perturbation modes: explicit/transient, explicit/permanent, implicit/transient, and implicit/permanent. It injects deterministic faults at predefined tool nodes and enumerates valid recovery paths. It reports Task Success Rate (TSR), Perturbation Recovery Rate (PRR), and Recovery Cost (RC). The paper reports that implicit semantic failures are especially difficult and that larger models do not close the fault-tolerance gap at the same rate as ordinary task execution.

**Implication:** ToolMaze is a promising candidate for controlled experiments on agent recovery and generalization. It does not itself demonstrate that evolution helps. The benchmark's hidden fault labels must not be exposed to the deployed policy; they may be used to stratify analysis or create an explicitly labelled oracle upper bound.

### HarnessEvolve closes several generic “reliable self-evolution” claims

Paper: https://arxiv.org/abs/2609.00829

HarnessEvolve aligns failed runs to reference trajectories, clusters errors, rejects data leakage/prompt bloat, and gates updates against degradation on recent batches plus held-out validation. Therefore reference-trace credit assignment, generic error clustering, anti-shortcut gates, and anti-forgetting acceptance checks are not novel alone. A future method would need to differ at the representation, operator, controller, or a specific recovery capability level.

### Hierarchical QD already studies recovery after unforeseen damage

Paper: https://doi.org/10.1145/3596912

Hierarchical Trial and Error stores diverse lower-level skills and uses experience-guided selection to adapt a robot after physical damage. This predates current LLM agents and rules out broad claims that “a diverse evolutionary repertoire enables recovery from unseen failures.” The new setting would need to demonstrate a specific challenge arising from language-mediated tool use, semantic tool outputs, or long-horizon dependency graphs.

### Parameter-control distinction sharpened

- **LLaMEA-HPO** (ACM DOI: https://doi.org/10.1145/3731567) uses SMAC to tune the numeric parameters of each LLM-generated heuristic, while the LLM evolves algorithmic structure. This is strong prior art for separating structural search from numeric tuning; it does not by itself propose an adaptive controller for an Agent's EA loop.
- **Code World Models for Parameter Control** (2026 arXiv preprint: https://arxiv.org/abs/2602.22260) synthesizes an executable dynamics model and uses one-step planning to select mutation strength for (1+1)-RLS_k. It reports strong results on LeadingOnes, OneMax, Jump_k, and NK landscapes. However, the work uses known problem descriptions and/or structured empirical transition statistics, studies a single mutation-strength control problem rather than an LLM Agent policy population, and lists limits such as dependence on transition statistics for NK and restricted landscape coverage. It is a relevant comparison, not a ready-made Agent method.
- **Adaptive operator selection (AOS)** is a mature family. Its design normally separates operator credit assignment from operator selection; probability matching, adaptive pursuit, and bandit-style controllers are established baselines. “Use recent progress to raise the probability of a successful operator” is not new by itself.
- **EVOTOOL** already tests targeted mutation and selection mechanisms with controlled ablations. The paper's ablations show that mutation targeting, trajectory plus natural-language feedback, and population selection each affect results. A proposal must compare against these components, not just a default prompt search.

### Revised audit conclusion

The recovery candidate discussed here was subsequently downgraded after direct prior-art overlap and benchmark/data-rights blockers. The following question is historical, not an approved implementation target; it may be reopened only after a new novelty and feasibility review:

> Can a measurable, structured representation of recovery rules provide a useful evolutionary search space, and does a specific parameter/operator-control mechanism improve generalization to held-out combinations of tool-fault semantics and task-graph structure beyond static tuning and existing blame-aware prompt evolution?

Do not approve this as a novelty claim yet. It must survive the full comparison with EVOTOOL, HarnessEvolve, ToolMaze, QD recovery, and classical AOS/self-adaptation.


### ToolMaze implementation caveat discovered in the public code

The paper's RC definition averages the per-trajectory recovery penalty over all trajectories with an explicit perturbation indicator, and its README says no-hit runs contribute zero. However, the inspected `evaluation/core/metrics.py` implementation excludes no-hit runs from `compute_rc`'s denominator by filtering for `r["hit"]`. This is a concrete paper/README/code discrepancy that may change the reported RC. Before adopting the benchmark, build a three-case synthetic fixture (no-hit, hit-and-fail, hit-and-success), calculate both formulas, and determine which implementation generated the paper's results. Do not use RC comparisons until this is resolved or both variants are reported. See https://arxiv.org/html/2606.05806v1 and https://github.com/Zhudongsheng75/ToolMaze/blob/main/evaluation/core/metrics.py.

The inspected public GitHub tree did not expose a root LICENSE file and the Hugging Face dataset card did not expose a clear license field in its metadata. Confirm code/data licensing before redistributing modified copies or derived artifacts. This is a reproducibility check, not a legal conclusion.

