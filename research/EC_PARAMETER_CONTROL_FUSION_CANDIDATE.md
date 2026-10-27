# Candidate Research Plan: Joint Operator–Mutation-Scale Control for Agent Evolution

**Date:** 2026-10-27  
**Status:** Active exploratory candidate; not yet an approved thesis topic or innovation claim.  
**Project:** `yujian777555/openissue` only.  
**User requirement:** Evolutionary computation must be a substantive method. Parameter tuning/control must be studied explicitly. Existing papers are starting points for improvement and fusion, not automatic reasons to abandon a direction. Communication evolution is excluded.

## 1. Research question

For LLM-Agent evolutionary search, can we improve task performance and held-out task generalization by jointly controlling **which evolutionary operator to apply** and **how far its realized behavior should move**, with credit assigned to the descendants that an edit enables rather than only to the immediate child?

This is deliberately a *research question*, not a novelty claim. The candidate builds from complementary limitations in recent papers:

- **ELMER** learns to condition semantic mutation on low/medium/high behavioral displacement and uses common-parent offset-DPO to calibrate the mutation model. Its outer evolutionary loop still samples strengths uniformly; its discussion explicitly motivates adaptive mutation scheduling as future work. Paper: https://arxiv.org/abs/2608.10196.
- **The Time Value of Evolution (TVE/LVPG)** learns a state- and remaining-horizon-dependent mutation-radius policy using lineage-level returns. However, the mutation model and three calibrated radii are frozen, and the experiments use one policy language in trading-policy search. Paper: https://arxiv.org/abs/2608.13297.
- **EvoMAS: Heuristics in the Loop** introduces a diverse repertoire of seven strategies, adaptive strategy selection, curriculum, and a reflective meta-controller. This blocks any generic claim that an adaptive operator portfolio is new. Paper: https://proceedings.mlr.press/v306/wei26m.html.
- **EvoMAS: Evolutionary Generation of Multi-Agent Systems** evolves structured MAS configurations with feedback-conditioned mutation and crossover. Its official implementation is inspectable at https://github.com/amazon-science/EvoMAS; the root declares CC BY-NC 4.0, so code reuse is non-commercial and requires attribution.
- **Code World Models for Parameter Control** learns a model of optimizer dynamics to choose mutation strength online in classical combinatorial optimization. Paper: https://arxiv.org/abs/2602.22260.
- **LLaMEA-HPO** separates structural algorithm evolution from numerical hyperparameter optimization; official code: https://github.com/XAI-liacs/LLaMEA.
- **Classical adaptive operator selection (AOS) and self-adaptation** are mandatory baselines, not optional related work.

## 2. Proposed fusion hypothesis

The promising mechanism to test is a **joint operator–strength controller with lineage-aware credit**. It is not enough to bolt a controller onto an EA or to change a few numeric values.

### Search action

For a candidate Agent configuration/policy at generation (t), choose an action
[
a_t=(o_t,z_t),
]
where (o_t) is a typed variation family (e.g. local semantic refinement, module/role edit, structural configuration edit, or compatible recombination) and (z_t) is a requested semantic/behavioral displacement level for operators that support it.

The action space should start small and be justified by the chosen baseline's actual operators. Do not add every possible operator at once.

### Observable search state

Potential state features, all computed from training-time observations only:

- parent fitness/rank and recent improvement;
- stagnation and recent regression/recovery;
- current population/behavior-archive diversity;
- operator and strength history;
- realized parent–child behavioral displacement on a fixed probe set;
- candidate validity and execution success;
- task descriptors available without gold labels;
- remaining generations.

Do not expose held-out labels or evaluator internals to the controller.

### Credit assignment

Compare immediate-child reward with a **lineage return**: whether the child, its children, or a later descendant produces best-so-far improvement over a declared horizon. Credit must be attached to the selected ((operator, strength)) action and conditioned on the search state. A weak child is not automatically useful; it receives positive delayed credit only when a descendant provides evidence of productive continuation.

This extends the *question* beyond ELMER's behavior calibration and LVPG's mutation-radius control, but it is not yet established as distinct from all adaptive-operator and lineage-credit literature. That comparison remains a gate.

### Why Agent evolution is nontrivial

In an LLM Agent, requested mutation strength may not correspond to actual behavioral displacement. A small prompt/configuration diff can change tool-use decisions substantially, while a large diff may have little effect. Unlike deterministic trading-program replay, tool environments and LLM outputs may be stochastic. Behavioral distance therefore needs paired task instances/seeds and a reproducible trace representation (e.g. normalized action/tool-call/decision traces), with stochastic uncertainty recorded rather than hidden.

## 3. Parameter-control plan: what exactly must be tuned

Keep these levels separate.

| Level | Parameters/examples | Required treatment |
|---|---|---|
| Agent phenotype | role/tool/workflow/policy structure, instructions, conditions, actions | Define the genotype and legal edits. These are the object being evolved, not EA hyperparameters. |
| Static EA configuration | population size, offspring count, mutation/crossover rates, selection pressure, replacement, operator mixture, strength distribution | Tune on train/validation only. Compare random search or SMAC with a documented search space; freeze the selected setting before test. |
| Dynamic EA control | operator choice, mutation strength, crossover activation, exploration pressure, restart/diversity injection | Compare fixed settings, deterministic schedule, classical AOS, self-adaptation, and the proposed state-/lineage-conditioned controller. |
| Variation-model control | requested semantic strength, output constraints, model sampling settings | Measure realized behavior change and validity; do not assume a prompt label controls the actual mutation. |
| Task/evaluation settings | task family, split, environment seed, verifier, benchmark difficulty | Freeze as experimental design. Never optimize against held-out test outcomes. |

### Tuning sequence

1. **Freeze representation and evaluation.** Before any parameter sweep, define the Agent genotype, legal operators, task split, primary success metric, validity checks, and behavior-distance measurement.
2. **Characterize baseline sensitivity.** Use a small fractional-factorial or staged sweep to identify which static EA parameters materially affect task success and generalization. Do not run the full Cartesian product.
3. **Select a strong fixed configuration.** Compare random search and SMAC (or another justified HPO method) on training/validation tasks; preserve the exact trial log and selection rule.
4. **Only then test online control.** Compare the best fixed setting against deterministic schedules, probability matching/adaptive pursuit, UCB/Thompson-style AOS, self-adaptive parameters, ELMER-style strength-only control, and LVPG-style lineage-value control.
5. **Test the proposed fusion.** Compare operator-only, strength-only, immediate-credit, lineage-credit, and joint operator–strength control. Use ablations to show whether any gain comes from the interaction rather than an extra controller or more evaluations.
6. **Test generalization.** Hold out task families or compositions, not merely paraphrases. Report success, validity, robustness, and generalization gap. Evaluation count/cost is matched as a fairness control and reported secondarily, not as the thesis's main objective.

## 4. Baseline and prior-art matrix

| Method | What it already solves | What a proposed extension must add |
|---|---|---|
| Static EA + SMAC/random search | Strong fixed parameter settings | Show online control beats the strongest tuned fixed setting, not just defaults. |
| Classical AOS / self-adaptation | Online selection of operators or strategy parameters | Show why Agent semantic behavior, measured displacement, and delayed descendant value require a different credit/control signal. |
| ELMER | Behavior-calibrated semantic mutation strength | Do not claim behavioral distance or low/medium/high mutation control as new. Test adaptive selection of strength and operator for Agent tasks. |
| TVE/LVPG | State-/horizon-dependent mutation radius with long-horizon lineage credit | Do not claim delayed lineage reward or adaptive radius alone as new. Test joint operator–strength control in structured Agent evolution and task transfer. |
| EvoMAS: Heuristics in the Loop | Diverse strategy portfolio, adaptive strategy selection, curriculum, reflective meta-controller | Do not claim a dynamic operator repertoire or meta-controller alone as new. Audit its actual credit assignment and test a precise missing mechanism. |
| EvoMAS: Evolutionary Generation | Feedback-conditioned mutation/crossover over structured MAS configurations | Do not claim structured configuration evolution or feedback-guided mutation alone as new. |
| CWM parameter control | Model-based online mutation-strength selection for classical EA | Establish what changes when the state transition is a stochastic, semantic Agent evolution process; compare against a model-based controller if feasible. |
| AdaptEvolve | Confidence-based selection of LLM size for mutation/refinement | This is model routing, not direct EA parameter control; include as adjacent work if multiple mutation models are used. |

## 5. Falsifiable hypotheses

- **H1 — Realized scale:** requested mutation strength predicts behavior displacement on Agent task traces better than raw text/code edit size. If not, the behavior-scale interface is not operationally reliable.
- **H2 — Joint control:** a controller choosing both operator family and behavior scale improves held-out task success/generalization over the strongest static-HPO and separate AOS/strength-only baselines under matched evaluation settings.
- **H3 — Lineage credit:** lineage-level credit improves the controller's ability to retain useful stepping-stone edits without indiscriminately preserving weak children. If it does not beat immediate reward, do not retain the complexity.
- **H4 — Transfer:** the controller transfers to held-out task families or task compositions better than task-specific tuning. If not, narrow the claim to within-family adaptation or reject the transfer claim.

Primary outcomes are task success and held-out generalization. Cost/token count is secondary. Do not select a winner from the best single run; use repeated seeds, paired comparisons, uncertainty intervals, and prespecified primary contrasts.

## 6. Stop and revise conditions

These conditions apply to the *specific formulation*, not to the whole research area:

1. If the closest-work audit finds the same joint action space, lineage credit, and transfer protocol already established, revise the mechanism rather than merely renaming it.
2. If static HPO plus classical AOS matches or beats the proposed controller on held-out tasks, the proposed controller has not shown added value.
3. If gains vanish when evaluation settings and number of evaluated candidates are matched, the method has not demonstrated an EC-specific capability gain.
4. If behavior-distance estimates are too unstable to guide control, redesign the measurement before training a controller.
5. If task-transfer claims fail, report that result honestly; do not replace them with a cost-only claim.
6. Do not abandon a direction merely because its area is crowded. Use overlap to define stronger baselines and the exact improvement required. Abandon only the formulation that is already covered or empirically falsified.

## 7. Immediate next steps

1. Deep-read ELMER and TVE/LVPG methods, appendices, and limitations; record their exact state/action/reward/control design and whether official code is available.
2. Audit EvoMAS: Heuristics in the Loop at method level; locate and verify an official implementation before treating it as reproducible.
3. Extend the literature matrix with the above works and compare them against classical AOS, self-adaptation, CWM, and LLaMEA-HPO.
4. Define a small Agent evolution benchmark and trace-based behavior-distance metric only after confirming task/data licenses and a strong executable baseline.
5. No implementation or paid API experiment until this mechanism-level audit is complete.
