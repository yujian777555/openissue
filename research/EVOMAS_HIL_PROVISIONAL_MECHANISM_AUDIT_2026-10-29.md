# EvoMAS: Heuristics in the Loop — Provisional Mechanism-Level Audit

**Date:** 2026-10-29  
**Project:** `yujian777555/openissue` only  
**Status:** **PROVISIONAL PREPRINT AUDIT — NOT A FINAL-VERSION AUDIT; G0 REMAINS OPEN**  
**Purpose:** Decide which broad claims are already covered and whether the narrower OSLVC hypothesis is worth testing for a master's thesis opening report.

## 1. Evidence boundary and source hierarchy

### Final published version (verified metadata and abstract only)

Wei, Y., Huang, Z., Xu, R., Wang, H., & Xing, W. W. (2026). *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*. Proceedings of the 43rd International Conference on Machine Learning, PMLR 306, 133736–133763. Official record: https://proceedings.mlr.press/v306/wei26m.html

The official PMLR record confirms the final ICML 2026 publication and states that the method uses seven evolutionary strategies (six biologically inspired exploration/exploitation operators plus a custom domain operator), adaptive strategy selection, role-level evolution, curriculum-guided evolution, and the Cyber Creator meta-controller for reflective updates to evolutionary rules and strategies. The record exposes the PDF at https://raw.githubusercontent.com/mlresearch/v306/main/assets/wei26m/wei26m.pdf, but this research session's web reader rejected the PDF as `application/octet-stream`, the container download attempt failed, and the linked OpenReview page redirected to a browser-verification challenge. The PMLR record does not list a software link in its related-material section.

**Therefore, final-version equations, implementation details, and ablations remain unverified.** Do not present any details below as proven facts about the final camera-ready version.

### Earlier anonymous manuscript (read through search-indexed text; provisional only)

Accessible indexed manuscript: https://openreview.net/pdf?id=0rJUulYnow  
The indexed result identifies it as an earlier anonymous ICLR 2026 submission. Direct OpenReview retrieval currently redirects to a verification challenge. It is useful for generating a prior-art hypothesis, but it cannot substitute for the accepted ICML version.

## 2. Mechanism reconstruction from the earlier manuscript

The following points are explicitly marked **preprint-only**.

| Mechanism | What the indexed manuscript describes | Consequence for this thesis |
|---|---|---|
| Evolution state | s_t = (P_t, R_t, A_t): workflow population, rule set, and current exploration/exploitation strategy set/distribution; historical log H_t records candidates, fitness, and applied strategies | Evolution state and historical strategy feedback are already covered broadly |
| Variation operators | Three exploration strategies (Diversity Expansion, Conceptual Recombination, Cross-domain Hybridization); three exploitation strategies (Fine Optimization, Best Practice Synthesis, Role Specialization); a custom strategy is created from evolutionary feedback | A multi-operator portfolio and an additional custom operator are not novel claims |
| Structural diversity | The preprint describes Diversity Expansion as maximizing graph edit distance / introducing structural perturbations | Structural distance is already considered, but it is not automatically the same as the realized behavior change in executed tool traces |
| Candidate selection | An LLM ranks parent and offspring candidates using execution performance, workflow structure, and compliance with the current rule set, rather than relying only on scalar fitness | LLM-guided multi-criteria selection is already covered |
| Strategy credit/update | Every K generations, a historical log is reviewed; the Cyber Creator updates rules and the strategy distribution. The indexed text gives A[t+1](a) ∝ A[t](a) × exp(η × Reward(a)), where Reward(a) is described as the estimated contribution of strategy (a) to recent fitness improvements | Adaptive operator/strategy choice and history-based credit are already covered at a broad level |
| Meta-rule update | The preprint describes pruning obsolete/poor rules and inducing rules from successful structural patterns | Reflective meta-control and evolution of the search rules are already covered |
| Curriculum | Tasks are divided into increasing difficulty levels, with cumulative performance used to protect earlier competence | Curriculum-guided evolution and cross-stage retention are not novel claims |
| Role evolution | Agent roles and collaboration structures are modified as part of the evolving workflow | Role specialization is not a novel claim |
| Ablations (preprint only) | Indexed text reports degradation when exploration, Cyber Creator, curriculum, or the evolution resource library is removed; the preprint reports a 9.38-point MBPP and 12.23-point MATH decline after removing exploration strategies, and an 18% cost increase without Cyber Creator | These results reinforce that broad components have already been tested; values must not be attributed to the final version until verified |

Sources for the indexed preprint excerpts include:
- Section 4.1–4.2 and equation (9): https://openreview.net/pdf?id=0rJUulYnow
- Algorithm 1 and appendix C.1: https://openreview.net/pdf?id=0rJUulYnow
- Operator definitions and Cyber Creator appendix: https://openreview.net/pdf?id=0rJUulYnow
- Preprint ablation excerpt: https://openreview.net/pdf?id=0rJUulYnow

## 3. What this rules out as a thesis innovation

Do **not** claim any of the following as the core innovation:

1. “Adaptive evolutionary operator selection.”
2. “A portfolio of exploration and exploitation operators.”
3. “An LLM meta-controller that reflects on past generations.”
4. “Historical performance-based strategy weights.”
5. “Evolution of agent roles or workflow topology.”
6. “Curriculum-guided workflow evolution.”
7. “Graph edit distance as a diversity signal.”
8. “Combining multiple evolutionary mechanisms” without a specific, measured interaction that existing methods do not already handle.

These are directly covered by the official final abstract or the earlier manuscript.

## 4. Narrow candidate gap that remains worth testing (not yet a novelty claim)

The only OSLVC-R1 hypothesis still worth investigating is much narrower:

> **Does the realized behavior displacement of an offspring, measured from its executed Agent/tool-use traces, explain operator–strength continuation value beyond immediate fitness gain, raw lineage return, structural graph distance, and existing adaptive strategy selection?**

The key distinction is **realized execution behavior**, not just requested mutation strength and not just structural graph edit distance.

A workflow-graph edit can be large but behaviorally inert on a given task; conversely, a small prompt or tool-selection change can substantially alter the executed tool trajectory. This is a motivation for a test, not an established empirical fact. It must be checked with matched parent/task/state probes.

The preprint's indexed state and strategy-update equations do not explicitly show a behavior-displacement variable conditioning the operator credit. However, because the final ICML version has not been fully read, this is only a provisional gap statement. The final paper could contain an equivalent mechanism not visible in the abstract or accessible excerpts.

### Candidate estimand

For parent (p), task family (x), search state (z), operator (o), requested strength (s), realized displacement (d), and a predeclared descendant horizon (H), estimate:

[
Q_H(o,s,d\mid p,x,z)
=\mathbb{E}[R_{t:t+H}\mid o,s,d,p,x,z].
]

The research question is whether conditioning on (d) changes the ranking of operator–strength actions and improves held-out search outcomes after matching/equalizing descendant evaluation counts. This is not a license to call the estimator causal: observational conditioning alone cannot establish causality; the pilot must randomize/match operator-strength probes and maintain overlap across displacement ranges.

## 5. Required comparison ladder

The pilot must compare the candidate with strong, explicit alternatives:

1. Tuned static EA (static hyperparameters tuned on training/validation only).
2. Immediate offspring fitness gain as operator credit.
3. Raw descendant/lineage return without displacement conditioning.
4. Displacement-only predictor/control (no operator-specific residual).
5. Joint operator–strength controller using raw return.
6. ELMER-style behavior-scale control.
7. LVPG-style lineage/horizon-value control.
8. Classical adaptive operator selection (AOS), including a diversity-/parent-distance-aware reward where feasible.
9. EvoMAS-like reflective strategy selection as a method-level baseline; final-version implementation/reproduction status must be stated honestly.
10. EvoTool or a faithful component-level baseline for the Agent-policy evolution setting.

All comparisons must use equalized evaluation budgets, paired tasks/seeds where applicable, a frozen scorer, and task-family-held-out testing. Do not compare only against default static parameters.

## 6. Falsification and decision rule

Keep OSLVC only if all of the following hold:

- **Signal:** matched probes show reproducible operator/strength differences in realized behavior displacement or executability.
- **Incremental credit:** displacement-conditioned continuation-value estimates improve held-out prediction/ranking beyond raw lineage return and displacement-only control.
- **Search value:** the controller improves held-out task-family success or best-so-far performance against the strongest tuned baseline at the same evaluation budget.
- **Robustness:** gains survive seeds, model/task-family shifts, and removal of any single operator.
- **Attribution:** ablations show that the conditional-credit component, not merely more operators, extra evaluations, or LLM reflection, causes the gain.

Drop or redesign OSLVC if the residual signal is negligible, unstable, unavailable in a realistic online setting, or fails to improve search outcomes. Do not rescue a failed result by renaming the method.

## 7. Current gate decision

- **G0 (final-version prior-art audit): OPEN.** The official final publication record and abstract are verified; final method equations/ablations are not.
- **G1 (benchmark/split/scorer): PARTIAL/OPEN.** The existing decision remains a controlled local deterministic tool-task suite with family-held-out splits plus an audited external subset; task IDs, license/version manifest, and scorer checks still need locking.
- **G2 (local mechanism pilot): NOT RUN.** No formal experiment, code reproduction, or paid API call was started in this audit.

### Next actions

1. Make no more than a bounded further attempt to obtain the final PDF or verified author-hosted version. If still blocked, ask the user for a local PDF only if needed, and continue the proposal work with explicit provisional labels.
2. In parallel, freeze the controlled task-family split, exact task IDs, version/license manifest, goal-state oracle, and scorer audit.
3. Only after the method and benchmark gates are sufficiently closed, run a small no-paid-call pilot with matched parent/task/state probes and equal descendant-evaluation counts.
4. Update the proposal gap matrix based on this evidence; do not yet approve OSLVC as an innovation or the thesis title as final.

## 8. Bibliographic records

Wei, Y., Huang, Z., Xu, R., Wang, H., & Xing, W. W. (2026). *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*. Proceedings of the 43rd International Conference on Machine Learning, PMLR 306, 133736–133763. https://proceedings.mlr.press/v306/wei26m.html

Wei, Y., Huang, Z., Xu, R., Wang, H., & Xing, W. W. (2026, earlier anonymous submission). *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*. OpenReview manuscript for ICLR 2026, ID 0rJUulYnow. https://openreview.net/pdf?id=0rJUulYnow. **Preprint-only source used provisionally; do not cite as the final ICML method without version verification.**
