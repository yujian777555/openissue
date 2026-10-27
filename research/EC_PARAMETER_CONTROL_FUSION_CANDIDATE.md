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

## 2. Revised fusion hypothesis after primary-source audit

The first formulation—joint operator selection, mutation strength, and lineage credit—was too broad. The detailed evidence and falsifiable mechanism gap are now recorded in [EC_PARAMETER_CONTROL_FUSION_AUDIT.md](EC_PARAMETER_CONTROL_FUSION_AUDIT.md).

The candidate is provisionally **Operator-Specific Lineage-Value Control (OSLVC)**:

1. Calibrate realized behavioral displacement separately for each operator family; a shared “low/medium/high” label may not mean the same thing for local refinement, structural edits, and recombination.
2. Treat the control action as a joint pair `(operator, behavioral scale)`, rather than two independent choices.
3. Estimate the pair's value from downstream lineage improvement, while directly comparing against immediate-child reward and a strong static-HPO configuration.
4. Test task-family transfer, with the final test split sealed from calibration and controller tuning.

The hypothesis is not that the ingredients are individually novel. ELMER establishes behavior-grounded scale calibration; LVPG establishes state/horizon-dependent scale selection and lineage credit; EvoMAS: Heuristics in the Loop establishes adaptive operator portfolios and reflective meta-control. The unverified question is whether operator-specific behavioral calibration and lineage-value credit interact beneficially in Agent evolution and transfer to unseen task families.

**Current status:** promising enough for the next primary-source audit, not yet approved as a thesis topic. Do not implement until the exact EvoMAS control mechanism, official code/rights, and a reproducible Agent benchmark are checked.

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


## 8. Revision R1 — sharpen the method beyond a generic fusion (2026-10-27)

The initial `(operator, strength) + lineage credit` formulation is not sufficiently distinct by itself. ELMER already calibrates mutation strength against executed behavior; LVPG already learns state-/horizon-dependent radius control and lineage-level returns; classical AOS already covers adaptive operator selection and includes diversity/parent-distance credit variants; EvoMAS: Heuristics in the Loop already has a dynamic operator portfolio and reflective meta-control.

The revised hypothesis is **scale-conditioned lineage-value credit**: estimate an operator's lineage continuation value conditional on the behavior displacement it actually produces, using matched parent/task/state comparisons. This tests whether apparent operator quality is confounded by how far the operator moves behavior. It is not a causal claim without randomized/matched support, and it is not approved as novel until the complete EvoMAS HIL method and additional nearest prior art are checked.

See `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md` for the formal candidate, equations, baselines, parameter tuning plan, and stop conditions. Static HPO must still precede online control. The extra decomposition must beat a naive joint controller with raw lineage return or be removed.
