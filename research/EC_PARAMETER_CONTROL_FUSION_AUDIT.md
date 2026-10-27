# Mechanism-Level Audit: ELMER, LVPG, and Adaptive Agent Evolution

**Date:** 2026-10-27  
**Status:** Primary-source mechanism audit completed for ELMER and The Time Value of Evolution/LVPG; EvoMAS: Heuristics in the Loop is verified from its ICML/PMLR record and abstract but its full method/code audit remains open.  
**Purpose:** Turn the literature into a concrete, falsifiable method-improvement hypothesis. This is not a novelty certification or final thesis-topic approval.

## 1. Executive result

The initial idea “combine adaptive operators + mutation strength + lineage credit” is too vague. Each ingredient already exists:

- **ELMER** learns a semantic mutation operator conditioned on low/medium/high *realized behavioral displacement*. It does not merely ask an LLM to obey a strength word: it trains on executable transitions and common-parent preference pairs. Its outer search samples strength uniformly; the paper explicitly identifies adaptive mutation scheduling as future work.
- **LVPG / The Time Value of Evolution** learns state- and remaining-horizon-dependent choice among Refine/Interpolate/Explore and credits actions using downstream best-so-far improvement over a lineage. It keeps the underlying ELM and its three calibrated radii frozen.
- **EvoMAS: Heuristics in the Loop** already uses seven evolutionary strategies, adaptive strategy selection, role-level evolution, curriculum, and a reflective meta-controller. A generic “learn which operator to choose” claim is therefore not defensible.
- **EvoMAS: Evolutionary Generation of Multi-Agent Systems** already uses feedback-conditioned mutation/crossover on structured MAS configurations, execution traces, and experience memory. Generic feedback-guided configuration evolution is not defensible either.

**Revised hypothesis to test:** in LLM-Agent evolution, the same nominal mutation-strength request can produce different realized behavioral displacement under different variation operators. Therefore, calibrate mutation scale *conditional on operator family*, then learn a controller over the joint action `(operator, requested behavioral scale)` using the estimated continuation value of its descendant lineage—not just the immediate child's score. Test whether this interaction improves Agent capability and held-out task-family generalization over the strongest fixed-HPO, adaptive-operator, strength-only, and lineage-only baselines.

This is a plausible mechanism gap, not yet a verified novelty claim. It is narrower and more testable than the original fusion slogan.

## 2. Primary-source evidence

### 2.1 ELMER — behaviorally calibrated semantic mutation

Primary source: Siper, Khalifa & Togelius, *ELMER: Evolutionary Language Model that Explores and Refines*, arXiv:2608.10196 (10 August 2026).  
https://arxiv.org/abs/2608.10196

Method facts verified from the paper:

1. It mutates natural-language descriptions of trading policies and compiles them into typed GPTL programs for deterministic execution.
2. Behavioral displacement is computed from parent/child action-sequence disagreement on the same historical windows; this is deliberately distinct from token/AST edit size.
3. The training set contains 45,639 examples across conditional mutation, compilation, and translation. Strength labels are equal-frequency behavioral-distance bins. Common-parent offset-DPO uses 14,735 training preference pairs.
4. Across 36 matched runs per system, mean run-level Spearman correlation between requested strength and realized displacement is 0.824 for oDPO, 0.310 for behavior-grounded SFT, and 0.018 for prompt-only labels.
5. The requested strength changes edit composition. Parameter changes account for 86.4% of low-strength edits, versus 35.5% at medium and 0.46% at high; high strength reallocates probability toward indicator substitutions, comparator swaps, and structural rewrites.
6. The authors report broad medium/high distributions and high-strength saturation, so the interface provides ordered regimes rather than exact numeric control.
7. The outer-loop study uses multiple evolutionary algorithms, but the authors explicitly identify variation across outer loops and uniform strength sampling as motivation for future adaptive mutation scheduling.

Interpretation:

- **Established:** execution-grounded behavior-scale calibration is a real contribution; prompt-only “small/large mutation” instructions are not an adequate baseline.
- **Not established:** online selection of strength based on the current evolutionary state; a shared calibration across heterogeneous operator families; long-horizon credit for an operator–scale pair in a stochastic Agent environment; cross-task transfer of such a controller.
- **Do not claim:** “behavioral mutation strength,” “low/medium/high semantic mutation,” or “LLM-controlled mutation size” as new.
- **Transfer caveat:** ELMER studies executable trading programs with fixed historical trajectories and a deterministic evaluator. An LLM Agent's action/tool trajectories may be stochastic and task-dependent; the displacement measurement must be redesigned and validated rather than copied blindly.

### 2.2 LVPG — lineage-value control of mutation intensity

Primary source: Siper, Khalifa & Togelius, *The Time Value of Evolution*, arXiv:2608.13297 (13 August 2026).  
https://arxiv.org/abs/2608.13297

Method facts verified from the paper:

1. The controller's action space is three calibrated radii: Refine, Interpolate, Explore.
2. State includes the current natural-language and executable program, execution feedback, best-so-far fitness, and remaining search horizon.
3. A frozen ELM produces and compiles mutations. Separate actor/critic LoRA adapters learn which radius to choose and estimate lineage continuation value.
4. The path reward telescopes to downstream best-so-far improvement. A child may be a temporary regression and still receive positive credit if a later descendant exceeds the previous path best.
5. The critic is bootstrapped using deterministic depth-five mutation trees. The target is an optimistic maximum over evaluated descendants, not an unbiased expectation over stochastic futures.
6. In 90 paired runs, PPO-Path improves validation best-so-far AUC over PPO-Immediate by 0.394 Sharpe units and raises mean sealed-test Sharpe from 0.862 to 1.321. These are results on three futures markets and one policy language, not evidence of general Agent transfer.
7. The authors explicitly state that the ELM content distribution and three radii are fixed, preventing online improvement of edits and leaving a coarse, domain-specific action space. The critic is useful but imperfectly calibrated; the study also does not establish live financial profitability.

Interpretation:

- **Established:** lineage-level credit and state/horizon-dependent mutation-radius selection are prior art. Delayed reward, actor–critic control, and adaptive mutation intensity are not new in isolation.
- **Not established:** selecting among *different operator families* and calibrating a distinct behavior scale for each operator; whether this joint action matters in Agent evolution; transfer to held-out task families.
- **Do not claim:** “credit descendants rather than immediate children” or “adapt mutation intensity using search state” as new.
- **Transfer caveat:** LVPG uses a single frozen mutator, a small discrete action space, and optimistic tree maxima. A stochastic Agent setting needs an explicit comparison against that controller and should not assume the critic's max-descendant target is calibrated.

### 2.3 EvoMAS: Heuristics in the Loop

Primary source: Wei et al., *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*, ICML 2026, PMLR 306.  
https://proceedings.mlr.press/v306/wei26m.html

Verified from the official proceedings record and abstract:

- A repertoire of seven evolutionary strategies, including exploration and exploitation operators.
- Adaptive strategy selection.
- Role-level evolution and curriculum-guided progression from simpler to more complex tasks.
- A Cyber Creator meta-controller that formulates and reflectively updates evolutionary rules and strategies.

Additional mechanism evidence from an accessible earlier manuscript appendix (OpenReview PDF indexed by search; not yet reconciled line-by-line with the final PMLR version):

- The population is initialized using RAG retrieval; each generation samples a strategy from a strategy distribution, generates offspring, and applies an LLM-based selection that considers performance, structure, and rule compliance.
- Every (K) generations, the system appends historical records to a log and calls Cyber Creator to update the evolutionary rule set and strategy distribution.
- The curriculum objective averages performance over the current and all previous difficulty stages to reduce forgetting.
- The linked anonymous code mirror (https://anonymous.4open.science/r/EvoMAS-DEF4) was not accessible during this audit, so the implementation is not yet independently reproducible from that link.

Interpretation:

- **Established:** adaptive strategy portfolios, periodic history-conditioned strategy-distribution updates, reflective rule revision, role evolution, and curriculum are direct Agent+EC prior art. A generic operator controller or generic meta-controller is not novel.
- **Not evidenced in the accessible description:** per-operator calibration against realized behavioral displacement and lineage-return credit assigned to a joint ((operator, scale)) action. This is a candidate distinction to verify, not proof that the final paper omits those mechanisms.
- **Do not claim:** dynamic operator portfolios, reflective meta-control, or curriculum alone as new.
- **Next audit:** reconcile the earlier appendix with the final PMLR version and check whether an official code release is accessible. Keep the method gap provisional until this is done.

### 2.4 EvoMAS: Evolutionary Generation of Multi-Agent Systems

Primary source: Hu et al., *EvoMAS: Evolutionary Generation of Multi-Agent Systems*, ICML 2026, PMLR 306.  
https://proceedings.mlr.press/v306/hu26bg.html  
Official implementation: https://github.com/amazon-science/EvoMAS

The paper evolves structured MAS configurations using feedback-conditioned mutation/crossover, execution traces, candidate-pool refinement, and experience memory. The repository declares CC BY-NC 4.0; any reuse must respect the non-commercial condition and attribution.

Interpretation:

- This is a strong Agent+EC baseline for structured configuration evolution.
- It blocks generic claims about feedback-conditioned configuration mutation, crossover, and experience-memory-guided evolution.
- It does not, from the abstract alone, establish operator-specific behavioral-scale calibration or LVPG-style lineage-value control; verify the full method before finalizing this distinction.

## 3. The actual gap worth testing

### Gap A — mutation strength is operator-dependent

ELMER calibrates strength for its semantic mutator. EvoMAS has multiple operators. The realized displacement distribution is likely conditional on both operator and requested strength:

`D \sim P(D\mid s,o,x,\mathcal{T})`

where `s` is requested strength, `o` is the operator family, `x` is the current Agent/configuration, and `\mathcal{T}` is the task probe set.

A “medium” request for local refinement is not automatically comparable to a “medium” request for role replacement or recombination. Sharing one global strength mapping can therefore miscalibrate the actual search step. This is a **testable claim**, not yet an established fact.

### Gap B — operator selection and behavioral scale are usually controlled separately

ELMER makes behavioral scale steerable but does not adaptively select the scale in the outer loop. LVPG selects among three scales but keeps the mutator frozen. EvoMAS adapts among strategies, but the currently verified public abstract does not establish an operator-conditioned common behavior-scale interface.

The relevant action should therefore be a joint choice:

`a_t=(o_t,s_t)`

not “choose an operator, then independently choose a generic scale.” The value of a pair can depend on the current state: a structural edit at high displacement may be useful early or after stagnation, while local refinement at low displacement may be better near a strong solution. These examples are hypotheses to test, not assumed rules.

### Gap C — immediate child reward can mis-rank operator–scale pairs

LVPG establishes the importance of downstream lineage value in its own setting. The new question is whether lineage value should be estimated *for each operator–scale pair* when the action space contains heterogeneous Agent variation operators. A controller must not reward a weak child merely because it is novel; positive delayed credit should require a descendant to improve the declared path-best capability measure or a prespecified held-out-validation proxy.

### Proposed method, provisionally named OSLVC

**Operator-Specific Lineage-Value Control (OSLVC)** is a working label only.

1. **Operator-specific behavior calibration:** For each legal operator, collect parent/child transitions on common training probe tasks. Measure actual changes in structured action/tool traces, rather than text diff alone. Fit or calibrate ordered strength regimes per operator. Track validity and task success separately from displacement.
2. **Joint controller:** Select `(operator, strength)` using the current candidate, population state, recent improvement/stagnation, behavioral archive/novelty, task descriptor available at runtime, and remaining generations.
3. **Lineage-value credit:** Estimate the finite-horizon contribution of the chosen pair from downstream best-so-far improvement. Compare an immediate-reward controller, a lineage controller with a single operator, and the joint controller. Do not use a critic's optimistic maximum as if it were an unbiased expectation.
4. **Transfer:** Train/tune on a subset of task families and test on held-out families or held-out compositions. No held-out test outcomes may enter operator calibration, HPO, controller updates, or stopping decisions.

The possible contribution is the *interaction among operator-specific scale calibration, joint action control, and lineage-level credit in Agent evolution*. It is not the individual ingredients.

## 4. Falsifiable experiments

### RQ1 — Does operator-specific calibration improve control fidelity?

Compare:
- nominal prompt labels only;
- one shared global low/medium/high calibration;
- separate calibration per operator;
- a no-scale operator baseline.

Measure rank correlation between requested and realized displacement, invalid-offspring rate, catastrophic capability regressions, and task success. If per-operator calibration does not improve control fidelity or downstream performance, remove this component.

### RQ2 — Does joint control add capability beyond strong static tuning?

Required conditions:
1. fixed default EA;
2. static HPO (random search or SMAC) selected on training/validation;
3. classical adaptive operator selection;
4. self-adaptive operator/strength parameters;
5. ELMER-style strength-only control;
6. LVPG-style lineage control with one operator;
7. EvoMAS-style strategy selection, after its mechanism is audited;
8. OSLVC joint operator–strength lineage controller.

Freeze the strongest static setting before final test. Match base model, candidate evaluations, training tasks, and stopping rules for primary capability comparisons. Evaluation count/cost is a fairness control and secondary report, not the thesis objective.

### RQ3 — Does it generalize to unseen tasks?

Split by underlying task template, tool family, or task composition, not merely paraphrased user instructions. Report:
- primary: task success rate and held-out task-family success;
- secondary: validity, recovery from temporary regression, clean-task success, behavior coverage, and transfer gap;
- uncertainty: paired runs/seeds and confidence intervals with the run/task as the statistical unit.

### Minimal ablations

- remove operator-specific scale calibration;
- replace joint `(operator, strength)` control with independent heads;
- replace lineage credit with immediate child reward;
- remove task/search-state features;
- replace the learned controller with the best tuned static mixture;
- remove held-out-family adaptation and test whether any gain is only task-specific.

## 5. What would make this direction fail?

1. The full EvoMAS: Heuristics in the Loop method already uses equivalent operator-specific behavioral calibration and lineage-conditioned joint control.
2. A well-tuned fixed mixture or classical AOS matches the proposed controller on held-out Agent success.
3. Per-operator behavior-scale calibration adds no predictive/control value.
4. Lineage credit improves search curves only on the training task family and does not transfer.
5. Behavior displacement cannot be measured reliably enough on Agent traces to distinguish operators, or the required trace representation leaks held-out labels.

If any condition occurs, revise or reject OSLVC as formulated. Do **not** conclude that the entire Agent+EC direction is invalid.

## 6. Next concrete work

1. Retrieve and read the complete ICML 2026 EvoMAS: Heuristics in the Loop PDF; audit its strategy selection and Cyber Creator equations and look for official code.
2. Verify code availability, licenses, and reproduction steps for ELMER/LVPG; paper access is not code access.
3. Select a reproducible Agent task suite and a structured candidate representation only after auditing baseline interfaces and licenses. EVOTOOL and the official EvoMAS implementation are candidate baselines, not yet selected.
4. Freeze a pre-registration for operator/strength calibration, task-family splits, baselines, metrics, and statistical contrasts.
5. Only after these gates, implement the smallest falsification experiment. No paid API experiment is authorized by this document.

## Sources

- ELMER, primary arXiv paper: https://arxiv.org/abs/2608.10196
- The Time Value of Evolution / LVPG, primary arXiv paper: https://arxiv.org/abs/2608.13297
- EvoMAS: Heuristics in the Loop, official PMLR record: https://proceedings.mlr.press/v306/wei26m.html
- EvoMAS: Evolutionary Generation, official PMLR record: https://proceedings.mlr.press/v306/hu26bg.html
- EvoMAS official implementation and license: https://github.com/amazon-science/EvoMAS
- EVOTOOL, ACL 2026: https://aclanthology.org/2026.acl-long.2016/
- AdaptEvolve, ACL 2026 Findings: https://aclanthology.org/2026.findings-acl.2019/


## 7. Second-pass revision — why joint control alone is insufficient (2026-10-27)

A fresh primary-source check confirms that the broad OSLVC fusion is not enough as a novelty statement:
- ELMER directly measures executed parent–child behavior displacement and trains low/medium/high mutation-strength conditioning; its paper explicitly notes uniform outer-loop strength sampling as motivation for future adaptive scheduling.
- LVPG directly learns state-/horizon-conditioned mutation-radius choices and path-level return, while freezing its ELM/radii during controller learning. It also acknowledges optimistic tree-max targets and a single trading-policy language/domain.
- The 2025 AOS survey and existing AOS literature cover state-based operator choice and several credit signals, including fitness improvement and diversity/parent-distance rewards.
- EvoMAS: Heuristics in the Loop is confirmed as an ICML 2026 PMLR paper with seven strategies, adaptive strategy selection, curriculum, role-level evolution, and a reflective meta-controller. The public PMLR page exposed only the abstract in this pass; exact reward/state equations and official code remain unverified, so no detailed gap claim is made against it.

The revised candidate is **scale-conditioned lineage-value credit**: test whether an operator's continuation value can be estimated more reliably by conditioning on the *realized behavior displacement* and comparing matched parent/task/state moves, rather than assigning raw immediate or lineage reward to an operator–strength pair. This is a hypothesis, not a novelty verdict. See `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`.

Required new baseline: classical AOS using diversity/parent-distance reward, plus a naive joint operator–strength controller with raw lineage return. If OSLVC-R1 cannot beat these controls, remove the residualized credit mechanism. The full EvoMAS: Heuristics in the Loop method audit remains open; do not mark Gate G0 closed.


## 8. Direct baseline and benchmark integrity audit (2026-10-27)

EvoTool (ACL 2026) is now confirmed as a strong direct baseline with MIT-licensed official code, local-model support, deterministic offline execution, trajectory-grounded blame attribution, targeted mutation, and diversity-aware selection. These mechanisms must be compared against and are not new contributions by themselves.

A critical benchmark caveat: the EvoTool τ-bench converter selects from canonical test tasks before train/dev and takes the first 150 valid instances; the runner then shuffles/splits that demo subset into train/selection/test. This does not guarantee a clean split against the official test pool. The original τ-bench README warns its tasks are outdated. Use the bundled subset only for smoke testing; for final evidence, create task-template/tool-API-family-held-out partitions from verified source splits and test on an untouched external family. BFCL is a candidate offline controlled benchmark, but data terms and the custom split must be documented.

The official PMLR abstract confirms the broad EvoMAS mechanisms, but the exact credit/state equations and final code still remain unverified. Do not close G0 or make a claim that EvoMAS lacks displacement-conditioned lineage credit. See research/EVOMAS_HIL_METHOD_AUDIT_R1.md and research/PROPOSAL_GAP_MATRIX_R1.md.
