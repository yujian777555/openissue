# OSLVC-R1: Scale-Conditioned Lineage-Value Credit for Agent Policy Evolution

**Date:** 2026-10-27  
**Status:** Revised research hypothesis; not a novelty certification, approved thesis topic, or implemented algorithm.  
**Repository boundary:** `yujian777555/openissue` only.  
**Purpose:** Refine the initial “joint operator + behavioral strength + lineage value” fusion into a more precise, falsifiable evolutionary-computation mechanism for the thesis opening report.

## 1. Why the original fusion statement is not enough

The original OSLVC formulation combined three already established ideas:
- behaviorally calibrated mutation strength (ELMER);
- state-/horizon-dependent mutation-radius selection and long-horizon lineage return (LVPG / *The Time Value of Evolution*);
- a diverse operator portfolio with adaptive strategy selection and a reflective meta-controller (EvoMAS: Heuristics in the Loop).

A plain combination of these ingredients risks being judged as an engineering integration. Classical adaptive operator selection (AOS) is also mature: it includes state-based/stateless selection, multiple credit-assignment schemes, and diversity/parent-distance rewards. Therefore neither “use behavior distance” nor “use RL/UCB to select operators” is enough.

## 2. Primary-source facts and what remains unknown

### ELMER

Primary source: https://arxiv.org/abs/2608.10196

Verified from the paper:
- It measures realized behavioral displacement by comparing parent/child action sequences on common execution inputs.
- It conditions semantic mutation on low/medium/high behavioral displacement, using behavior-grounded supervised fine-tuning and common-parent offset-DPO.
- Its outer loop samples mutation strengths uniformly; the paper explicitly names adaptive mutation scheduling as future work.
- It studies a frozen, task-specific trading-policy representation/evaluator, not a general tool-use Agent policy.

Implication: the thesis cannot claim behavior-space mutation strength or strength conditioning alone as new. The useful opening is whether heterogeneous Agent variation operators can be calibrated and controlled together in a new, measurable way.

### The Time Value of Evolution / LVPG

Primary source: https://arxiv.org/abs/2608.13297

Verified from the paper:
- LVPG chooses among three behaviorally calibrated radii using search-state and remaining-horizon information.
- Its critic is trained on multi-step mutation-tree/path outcomes, and the main comparison contrasts downstream path returns with immediate offspring returns.
- The mutation generator and three radii are frozen during controller learning; the experiments use one policy language and trading-policy search.
- The authors report limitations including optimistic mutation-tree maxima and domain/horizon restrictions.

Implication: adaptive radius control and long-horizon lineage credit are not new in isolation. A credible extension must test heterogeneous Agent operators and must show that the new credit representation adds value beyond a straightforward LVPG-style controller.

### EvoMAS: Heuristics in the Loop

Official ICML 2026 record: https://proceedings.mlr.press/v306/wei26m.html

The published record confirms a seven-strategy portfolio, adaptive strategy selection, role-level evolution, curriculum, and a reflective meta-controller that updates evolutionary heuristics. In this pass, the official page exposes the abstract and citation metadata but did not provide enough machine-readable method detail to verify the exact selection reward, state variables, or credit-assignment equations. An official source repository was not verified. Treat it as a strong conceptual prior-art constraint, but do not claim a detailed mechanism gap until the full published method and code status are checked.

### Classical AOS

- Pei et al., “Adaptive Operator Selection for Meta-Heuristics: A Survey,” *IEEE Transactions on Artificial Intelligence*, 2025, DOI: https://doi.org/10.1109/TAI.2025.3545792
- “Dynamic selection of evolutionary operators based on online learning and fitness landscape analysis,” *Soft Computing*, DOI: https://doi.org/10.1007/s00500-016-2126-x
- “Reinforcement learning for mutation operator selection in automated program repair,” *Automated Software Engineering*, 2025, DOI: https://doi.org/10.1007/s10515-025-00501-z

These works establish that online operator choice, contextual/state-based selection, fitness-improvement credit, ancestor-credit variants, and diversity/parent-distance signals already exist. The new candidate must not be described as a generic RL controller or a distance-aware AOS.

## 3. Revised gap hypothesis: credit is confounded by realized move scale

**Hypothesis, not established fact:** when different Agent variation operators are used, a raw immediate reward or raw lineage return may mix together at least two effects:
1. the effect of how far the child actually changes the Agent's behavior;
2. the effect of which operator generated that change.

An operator may appear better simply because it tends to make larger changes, or worse because it tends to make smaller but more useful changes. A requested “medium” strength is not guaranteed to create the same realized displacement across operators. The practical question is whether this confounding is large enough to alter operator rankings or control decisions in Agent evolution.

This is narrower than “jointly select operator and scale.” The candidate contribution is a **scale-conditioned lineage-value credit** that estimates the future utility of an operator after explicitly modeling the realized behavioral displacement it produces.

## 4. Candidate mechanism: OSLVC-R1

The name is only a convenient research label.

### 4.1 Representation and behavior measurement

Represent an Agent candidate as a structured, executable single-Agent tool-use policy/workflow. Exclude communication-protocol evolution from the candidate pool.

For a parent policy (x), generated child (x'), and a fixed probe set (E_{mathrm{probe}}), define realized displacement:

[
d(x,x')=rac{1}{|E_{mathrm{probe}}|}sum_{ein E_{mathrm{probe}}}
Digl(	au(x,e),	au(x',e)igr),
]

where (	au) is the tool/action trace and (D) is a preregistered normalized trace-distance function. A possible first version combines action disagreement and tool-call sequence edits, but the exact metric must be fixed before experiments and tested for reliability. Text/token edit distance is a separate baseline, not the behavioral target.

Record validity, task success, immediate fitness change, and behavior displacement as separate fields. Large displacement is not automatically good.

### 4.2 Operator-specific response calibration

For each operator (o), requested strength (z), and observable search state (s), estimate the distribution

[
p(d,vmid s,o,z),
]

where (d) is realized displacement and (v) indicates whether the child is valid/executable. Start with a small operator set and a shared probe suite. Use matched parent/task conditions and randomized operator/strength assignments where feasible so the calibration data have overlap.

The aim is not merely to predict distance. It is to learn which operator/strength combinations reliably realize a desired behavioral scale, and when their validity or displacement distributions differ.

### 4.3 Scale-conditioned lineage-value credit

For a generated child, define a prespecified horizon-(H) lineage outcome:

[
G_H=max_{yinoperatorname{Desc}_{leq H}(x')}F(y)-B_t,
]

where (B_t) is the path-best fitness immediately before the action and (operatorname{Desc}_{leq H}(x')) denotes descendants attributable to that branch within the fixed horizon. For crossover, credit attribution is ambiguous; the initial falsification study should begin with mutation-only operator families or explicitly preregister a two-parent attribution rule rather than silently double-crediting both parents.

Estimate the lineage outcome in two parts:
- a **scale/state baseline** (m(s,d,v,h)), capturing the typical continuation outcome for the realized displacement, validity, current state, and remaining horizon;
- an **operator-conditioned residual** (a(s,o,d,h)), capturing the operator's observed continuation value relative to comparable moves at similar displacement and state.

Conceptually:

[
widehat Q(s,o,z)=
mathbb E_{d,vsim hat p(cdotmid s,o,z)}
left[m(s,d,v,h)+a(s,o,d,h)ight].
]

This decomposition is a predictive/conditional model, not automatically a causal effect. Claims about operator-specific benefit require randomized or matched comparisons with sufficient common support; otherwise the residual may reflect selection bias or unobserved differences.

The controller selects an operator/strength pair using predicted continuation value plus a prespecified uncertainty/exploration term. UCB, Thompson sampling, or policy-gradient selection are implementation choices and are not claimed as innovations themselves.

### 4.4 Why this is more than a simple fusion

The key testable difference is not merely that the action space contains ((o,z)), nor that rewards extend across descendants. It is that **operator credit is estimated conditional on the behavior scale actually realized**, with matched-parent calibration and lineage outcomes. This asks whether the operator's apparent advantage survives after comparing moves of similar behavioral magnitude.

If this conditional decomposition provides no value over a naïve joint ((o,z)) controller, the extra model should be removed. If an existing method already performs equivalent displacement-conditioned lineage credit, this candidate must be revised.

## 5. Required baselines

1. Default static EA.
2. Strong static EA selected by random search or SMAC on train/validation tasks.
3. Classical AOS: probability matching/adaptive pursuit or UCB, with immediate fitness-improvement credit.
4. AOS with a diversity/parent-distance reward.
5. Behavior-scale-only control (ELMER-style calibration/control where reproducible).
6. Lineage-only scale control (LVPG-style credit, adapted fairly to the same task setting).
7. Naïve joint operator–strength control using immediate reward.
8. Naïve joint operator–strength control using raw lineage return.
9. OSLVC-R1: scale-conditioned lineage-value credit.
10. EvoMAS: Heuristics in the Loop as a method-level comparison; use as a direct benchmark baseline only if its implementation, license, search object, and evaluation conditions permit a fair reproduction.

Match base model, task instances, candidate evaluations, seeds, stop rules, and tuning data for the main comparisons. Do not compare a tuned proposed method against untuned baselines.

## 6. Parameter tuning is part of the method plan

Keep the following layers separate:
- **Agent genotype:** policy modules/rules/workflow structure.
- **Static EA parameters:** population size (mu), offspring count (lambda), mutation probability, parent/survivor selection, elitism, and operator mixture.
- **Online control action:** operator family and requested behavior scale.
- **Variation-model settings:** model/version, sampling settings, constraints, and prompt/template version.
- **Evaluation design:** task split, probe set, seeds, verifier, and horizon.

Tune static parameters on training/validation tasks first using a documented random-search/SMAC protocol and a small staged sensitivity design. Freeze the best static configuration before testing online control. Then compare fixed settings, deterministic schedules, classical AOS/self-adaptation, strength-only control, lineage-only control, naïve joint control, and OSLVC-R1. Do not add online adaptation of population size or multiple extra knobs until the central operator–scale credit question is resolved.

## 7. Falsifiable research questions

- **RQ1 — Response heterogeneity:** Do operators produce materially different displacement/validity distributions at the same requested strength? If not, remove operator-specific calibration.
- **RQ2 — Credit deconfounding:** Does scale-conditioned lineage-value prediction improve held-out prediction/ranking of useful operator–strength actions over immediate reward and raw lineage return? Evaluate with matched-parent comparisons and calibration metrics.
- **RQ3 — Optimization gain:** Does OSLVC-R1 improve task success and held-out task-family success over strong static HPO, classical AOS, and the naïve joint controller under matched evaluation conditions?
- **RQ4 — Transfer:** Does any learned control policy transfer to held-out task families? Treat this as a generalization result unless a separate transfer mechanism is proposed and shown distinct from prior work.

Primary metrics: task success and held-out task-family success. Secondary diagnostics: executable offspring rate, realized displacement distribution, conditional lineage-value prediction error/rank correlation, temporary-regression recovery, behavioral coverage, and cost. Cost is not the thesis's central objective.

## 8. Stop/revise conditions

Revise or reject **OSLVC-R1**, not the whole Agent+EC direction, if:
1. operator families do not differ meaningfully in realized displacement;
2. conditional lineage credit does not outperform raw lineage credit or naïve joint control;
3. the method does not beat a strong static-HPO plus classical-AOS baseline;
4. gains disappear under matched task/evaluation/seed conditions;
5. the full EvoMAS: Heuristics in the Loop method or another paper already implements equivalent conditional credit;
6. benchmark/data rights or a reproducible evaluator cannot be established.

## 9. Current decision and next action

The original OSLVC “three ingredients combined” claim is too broad. OSLVC-R1 is a narrower, testable hypothesis focused on displacement-conditioned lineage credit. It remains unapproved and unimplemented.

Next:
1. complete the method-level comparison of EvoMAS: Heuristics in the Loop using the published full paper, not only the abstract;
2. verify code/data licenses and choose one reproducible single-Agent tool-use policy evaluation setting;
3. prepare a proposal-ready gap table mapping each research question to its closest work, baseline, ablation, and failure criterion;
4. only then run a small, non-paid feasibility pilot.

## References

- Siper, Khalifa & Togelius (2026), ELMER: https://arxiv.org/abs/2608.10196
- Siper, Khalifa & Togelius (2026), The Time Value of Evolution: https://arxiv.org/abs/2608.13297
- Wei et al. (2026), EvoMAS: Heuristics in the Loop, ICML/PMLR: https://proceedings.mlr.press/v306/wei26m.html
- Pei et al. (2025), Adaptive Operator Selection for Meta-Heuristics: A Survey: https://doi.org/10.1109/TAI.2025.3545792
- Dynamic selection of evolutionary operators based on online learning and fitness landscape analysis: https://doi.org/10.1007/s00500-016-2126-x
- Reinforcement learning for mutation operator selection in automated program repair: https://doi.org/10.1007/s10515-025-00501-z
- LLaMEA-HPO: https://arxiv.org/abs/2410.16309



## Reassessment after provisional EvoMAS audit (2026-10-29)

The accessible earlier EvoMAS manuscript already covers broad adaptive operator/strategy selection, historical strategy-performance feedback, LLM-based meta-reflection, multi-criteria candidate selection, structural graph-distance diversity, curriculum, and role evolution. These mechanisms cannot be claimed as OSLVC novelty. The final ICML 2026 version has not yet been fully inspected, so this is a provisional boundary, not a final novelty determination.

The only surviving testable distinction is whether **realized behavior displacement measured from executed Agent/tool traces** improves continuation-value credit beyond (i) immediate reward, (ii) raw lineage return, (iii) displacement-only prediction, (iv) graph-structural distance, and (v) existing adaptive operator/strategy control. The earlier manuscript's graph edit distance is a structural measure; it is not automatically equivalent to realized tool-trace behavior. That difference is a hypothesis to test, not proof of novelty.

Required controls include a tuned static EA, immediate-reward AOS, raw lineage return, displacement-only control, naive joint operator-strength control, ELMER-style scale-only control, LVPG-style lineage control, classical AOS, and a method-level EvoMAS-like baseline. Equalize descendant-evaluation counts and use task-family-held-out evaluation. Drop/revise OSLVC if the conditional residual is negligible, unstable, or does not improve held-out search success.

Detailed audit: [EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md](EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md). OSLVC remains a hypothesis, not an approved innovation.
