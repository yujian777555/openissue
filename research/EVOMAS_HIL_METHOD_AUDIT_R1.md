# EvoMAS: Heuristics in the Loop — Method Audit R1

**Audit date:** 2026-10-27  
**Audit status:** PARTIAL — official publication record verified; full-paper equations and final-version implementation not independently verified in this session.  
**Decision:** Gate G0 remains OPEN. Do not claim a precise novelty gap against EvoMAS until the method sections are checked directly.

## 1. Sources and confidence hierarchy

1. **Primary publication record:** ICML 2026 / Proceedings of Machine Learning Research, volume 306, pages 133736–133763: https://proceedings.mlr.press/v306/wei26m.html
2. **Official PDF link exposed by PMLR:** https://raw.githubusercontent.com/mlresearch/v306/main/assets/wei26m/wei26m.pdf
3. **Earlier anonymous code link referenced by a secondary index:** https://anonymous.4open.science/r/EvoMAS-DEF4 — this is associated with an earlier OpenReview version, not verified as the final ICML code artifact; access and license could not be independently verified here.
4. Secondary paper-index summaries are discovery aids only. They are not used to certify exact equations or implementation details.

The official PMLR record is accessible and confirms the title, authors, venue, pages, and abstract. The PDF endpoint was exposed by the official page but its full text could not be extracted in this session. Accordingly, this is not a completed full-text audit.

## 2. Mechanisms verified from the official publication record

The official abstract confirms the following:

- **Adaptive evolutionary strategy portfolio:** seven strategies, comprising six biologically inspired operators (three exploration and three exploitation) plus a domain-specific custom operator.
- **Adaptive strategy selection:** the system dynamically selects from the portfolio.
- **Role-level evolution:** agent specialization and collaboration patterns are evolved.
- **Curriculum-guided evolution:** workflows are advanced from simpler to more complex tasks, with cross-stage stability.
- **Cyber Creator meta-controller:** formulates and reflectively updates evolutionary rules and strategies.
- The paper reports evaluation across multiple domains and cost efficiency.

These points are sufficient to rule out a broad claim that “using an adaptive operator portfolio for Agent evolution” or “adding an LLM meta-controller that reflects on evolutionary rules” is new.

## 3. What remains unverified and must not be guessed

| Mechanism question | Evidence status | Why it matters for OSLVC-R1 |
|---|---|---|
| Exact operator names, preconditions, and implementation | Not verified from full paper/code | Need to know whether its operators already encode requested mutation strength or behavior displacement |
| Strategy-selection state features | Not verified | Could overlap with a state-conditioned controller |
| Reward / credit assignment equation | Not verified | Critical: could already condition operator value on offspring or lineage outcomes |
| Cyber Creator update rule and memory horizon | Not verified | Must distinguish reflection over heuristic rules from the proposed scale-conditioned credit estimator |
| Whether lineage or descendant outcomes are used explicitly | Not verified | If equivalent downstream credit already exists, the candidate must be revised |
| Whether realized behavioral displacement is measured and conditioned on | Not verified | This is the narrowest candidate difference under consideration |
| Final ICML artifact's public code and license | Not verified | The older anonymous repository reference does not prove a final, reproducible code release |
| Dataset split, seed, and evaluation protocol | Not verified from the full paper | Needed for fair reproduction and overlap analysis |

Do not infer that a mechanism is absent simply because the abstract does not mention it.

## 4. Implications for the thesis candidate

The prior-art constraints are now clear:

- **Not a novelty claim:** adaptive operator selection, seven-strategy portfolios, role-level evolution, curriculum, reflective meta-control, or generic evolutionary-agent workflow search.
- **Already covered by adjacent work:** behavior-grounded mutation strength (ELMER), state-/horizon-dependent radius selection and lineage return (LVPG), and classical adaptive operator selection (AOS).
- **Remaining hypothesis to test:** whether an operator's downstream continuation value should be conditioned on the *realized behavior displacement* it produces, using matched parent/task/state comparisons, rather than assigning raw immediate or lineage reward to an operator–strength pair.

This distinction is provisional. The full paper's exact reward and strategy-selection equations must be inspected before the hypothesis can be treated as a credible gap.

## 5. Required next audit steps

1. Obtain a locally readable copy of the final ICML PDF or a verified author-provided source.
2. Extract the exact algorithm, equations, ablation tables, appendix, task split, seeds, and evaluator details.
3. Verify whether the final paper links code; if only an earlier anonymous code link exists, record that distinction and inspect its license before reuse.
4. Compare its strategy-selection state/action/reward with ELMER, LVPG, CWM, classical AOS, and OSLVC-R1 line by line.
5. Update the decision only after the direct comparison. If equivalent displacement-conditioned lineage credit exists, revise OSLVC-R1 rather than rename it.

## 6. Primary citation

Wei, Y., Huang, Z., Xu, R., Wang, H., & Xing, W. W. (2026). *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*. Proceedings of the 43rd International Conference on Machine Learning, Proceedings of Machine Learning Research, 306, 133736–133763. https://proceedings.mlr.press/v306/wei26m.html


## 7. Retrieval attempt log (2026-10-27, follow-up)

- Opened the official PMLR final record and followed its official PDF link (`raw.githubusercontent.com/mlresearch/v306/main/assets/wei26m/wei26m.pdf`). The web reader rejected the PDF as `application/octet-stream`; the direct container download also failed.
- Queried the older OpenReview PDF URL for the anonymous submission. The endpoint now redirects to an OpenReview verification challenge, so it was not independently readable.
- Search indexing returned the earlier manuscript abstract, but this does not substitute for the final paper's method section, equations, appendix, or ablations.
- **Updated conclusion:** G0 is still OPEN. This is an access/retrieval blocker, not evidence that the paper lacks the proposed mechanism. Do not infer absence of scale-conditioned lineage credit.
- Next acceptable routes: obtain the PDF from a user-provided local copy, an author-provided mirror/source, or a browser session with legitimate access; then inspect the algorithm, equations, and ablations. Do not use the older anonymous code artifact as if it were verified final-version code.



## Retrieval re-check and next action (2026-10-29)

- Rechecked the official PMLR final record: https://proceedings.mlr.press/v306/wei26m.html. It confirms the ICML 2026 final publication and exposes the official PDF URL: https://raw.githubusercontent.com/mlresearch/v306/main/assets/wei26m/wei26m.pdf.
- The web reader still rejects the PDF as `application/octet-stream`; the linked OpenReview page redirects to a browser-verification challenge. These are retrieval limitations, not evidence about the final paper's method.
- The accessible earlier anonymous manuscript is not a substitute for the final ICML/PMLR version. Any use of it must be explicitly labelled **preprint-only / final-version unverified**; do not use it to conclude that the final version lacks an equivalent mechanism.
- **G0 remains OPEN.** Immediate action: make a bounded attempt to obtain the final PDF or a verified author-hosted copy. If it remains inaccessible, perform a clearly labelled provisional equation/algorithm audit of the accessible manuscript while keeping the final-version gap explicit, and advance G1 (task-family split/scorer protocol) in parallel rather than stalling all proposal work.
- No experiment, code reproduction, or paid API call was started in this retrieval check.
