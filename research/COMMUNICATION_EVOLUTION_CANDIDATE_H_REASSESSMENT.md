# Candidate H0 Reassessment: Communication Evolution Under Transfer and Monitorability

**Audit date:** 2026-10-26  
**Decision:** **H0 NOT PASSED for the current formulation — do not implement as written.**  
**Project boundary:** This research record belongs only to [yujian777555/openissue](https://github.com/yujian777555/openissue). No other user project was accessed or modified.

## Executive finding

The screened question was whether evolutionary computation could produce communication protocols that preserve coordination quality after agent/model replacement and on held-out task compositions, while keeping protocol semantics verifiable and communication human-monitorable.

This is a consequential problem, but the current formulation is not yet a defensible algorithmic contribution. A second-pass audit found that the core axes are already covered across several close works:

- **CLSR (ICML 2026)** already evolves reusable symbolic protocols, applies grammar/contract constraints, uses correctness-and-token Pareto selection with elitist inheritance, shares protocols across agents and benchmarks, and evaluates cross-model and cross-domain transfer. Its cross-model experiment also shows a concrete weakness: swapping the LSF generator can reduce tokens while degrading accuracy, particularly when the generator is weaker than the inference model.
- **GlossoGen (2026 preprint)** directly studies transmission to a newly swapped-in agent, including different amounts of visible interaction history. It reports wide variation in transmissibility and languages that can be learned by newcomers but may be difficult for humans to understand. It is a useful controlled substrate, not an EA method.
- **Communication Policy Evolution (CPE, EMNLP 2026)** optimizes communication behavior through rollout-driven prompt patches and train/validation acceptance gates in user–agent and planner–executor settings. It is adjacent rather than a population-based EA, but it closes the generic “evolve communication policy from feedback” claim.
- **GTD (ACL 2026)** covers task-adaptive topology synthesis with proxy-guided multi-objective rewards; **MOC (ICML 2026)** covers multi-hop message aggregation and semantic-topological merging; **ProtocolBench/ProtocolRouter (ICML 2026)** covers protocol selection under task requirements and runtime signals, including robustness under failures.
- The **communication-alignment survey (Findings of EMNLP 2026)** explicitly frames semantic fidelity and convention consistency as communication-quality dimensions. Prior work on human-like emergent language, language transmission, zero-shot coordination, and population turnover further weakens a broad transfer/interpretability novelty claim.

Consequently, “add transfer and human-readability scores to the fitness function” is not enough. Nor is changing the benchmark, adding a Pareto objective, or adding a grammar to a protocol. The current Candidate H formulation does not identify a distinct evolutionary representation, variation operator, selection/replacement rule, or theoretical property that is not a combination of established ideas.

## 1. Mechanism-level comparison

| Work | What is already covered | Consequence for Candidate H |
|---|---|---|
| CLSR, Pei et al., ICML 2026 | LLM-generated symbolic protocol evolution; symbol inventory, grammar, usage/validity constraints; Pareto-style correctness/token selection; elitism; cross-agent adoption and cross-benchmark pooling; cross-model and cross-domain transfer tests | Generic protocol evolution and transfer-aware evaluation are not new. The measured transfer degradation is a real limitation to study, not proof of a novel method. |
| GlossoGen, Stengel-Eskin et al., 2026 preprint | Controlled complex interaction; event-sourced logs; swap/fork interventions; newcomer learns from message/action history without seeing the original postmortem definitions; human monitorability concerns | Agent replacement and language transmission are already directly testable. A new evolutionary optimizer must add more than “evaluate on a swapped agent.” |
| CPE, Ma et al., EMNLP 2026 | Rollout-based communication-policy refinement; LLM-generated policy patches; train gate plus validation gate; User–Agent and Planner–Executor evaluation | Generic feedback-driven communication-policy evolution is crowded, even though CPE is prompt-level optimization rather than a conventional population EA. |
| GTD, Jiang et al., ACL 2026 | Iterative task-adaptive communication-topology generation guided by a proxy predicting multiple rewards | Generic graph/topology search or proxy-guided topology adaptation is not a gap. |
| MOC, Guan et al., ICML 2026 | Multi-order evidence streams and semantic-topological message merging | A new message-consolidation operator alone is insufficient. |
| ProtocolBench/ProtocolRouter, Du et al., ICML 2026 | Success, latency, message/byte overhead, and failure robustness; constraint-aware protocol selection by scenario/module | A routing-only solution is a strong non-EA comparator; a new benchmark or router alone is not the thesis contribution. |
| Communication Alignment survey, Wei et al., Findings of EMNLP 2026 | Semantic fidelity and convention consistency as explicit communication-quality dimensions | “Measure alignment/interpretability rather than task success only” is an evaluation insight, not an algorithmic novelty claim by itself. |
| Boldt & Mortensen, EMNLP 2025; emergent-language transfer literature | Hyperparameter search for human-like emergent language; cross-play/zero-shot coordination and language learnability/transfer | Human-likeness, transferability, and partner generalization need comparison against established measures and methods. |
| Dziewoński et al., CoNLL 2026; Botoko Ekila et al., TACL 2026 | Population turnover/language drift; heteromorphic populations and adaptation to environmental changes | Agent replacement and heterogeneous populations are not unexplored, although the settings are not identical to LLM tool-agent systems. |

## 2. Important evidence and limitations

### CLSR: closest evolutionary baseline

The paper's LSF is a reusable symbolic protocol, not a one-off prompt. It includes a symbol inventory, grammar/output schema, usage and validity constraints, reasoning operations, and an empirical profile. The evolutionary loop selects correct and token-efficient traces, uses them to refine/recombine protocols, and preserves strong protocols by elitist inheritance. The paper reports cross-model generator/inference experiments and cross-domain transfer; it explicitly notes that model mismatch can lower accuracy even when token usage decreases. Its limitations include costly offline evolution and dependence on reasoning exemplars.

Primary sources:
- Paper: https://proceedings.mlr.press/v306/pei26a.html
- Full text: https://arxiv.org/abs/2606.29354
- Code URL stated by the paper: https://github.com/pzqpzq/LSF_MDia

**Code-availability caveat:** direct GitHub/API retrieval of the stated code URL returned 404 during this audit. Search results still expose a cached README snapshot describing a broader “MDia” framework with heterogeneous speaker–listener transfer profiles, but that snapshot is not currently retrievable from the live repository. It is not evidence of runnable code, yet it is a material prior-art warning: do not claim heterogeneous transfer matrices or listener-conditioned routing as novel until the repository/status question is resolved.

### GlossoGen: close evaluation substrate, not the method

The paper's swap experiment first lets an original pair develop a language, then replaces one agent. The newcomer receives varying amounts of recent interaction history (0, 1, 5, or 10 rounds) but not the original postmortem definition; the team then runs further rounds and measures task success. Results show that transmission varies across languages and model pairings. The authors also caution that the study has privileged access to environment state and effectively unbounded newcomer reasoning time, and that the setting is cooperative.

Primary sources:
- Paper: https://arxiv.org/abs/2609.01491
- MIT-licensed platform: https://github.com/agencyenterprise/GlossoGen

The current README describes event-sourced runs, swap/fork interventions, and pluggable metrics. Its current installation text specifies Python 3.14; pin a release and re-check dependencies before any future adoption. GlossoGen could support an independently authored test scenario, but adopting it would not itself provide an EA contribution.

### CPE and other adjacent work

CPE's two-stage train/validation gate accepts a candidate only if it improves on the training batch and then beats the best-so-far policy on validation. This is useful prior art for preventing purely local prompt changes from being accepted, but it optimizes a text/UI communication policy rather than a symbolic protocol population. The paper states its code URL as https://github.com/xbmxb/GenUI; direct repository retrieval also returned 404 during this audit. Do not claim reproducibility from the paper link alone.

Primary sources:
- CPE: https://aclanthology.org/2026.emnlp-main.2038/
- MOC: https://proceedings.mlr.press/v306/guan26i.html
- GTD: https://aclanthology.org/2026.acl-long.1764/
- ProtocolBench: https://proceedings.mlr.press/v306/du26l.html
- Communication Alignment survey: https://aclanthology.org/2026.findings-emnlp.332/

The MOC repository is publicly browsable, but the inspected root does not show a license file; do not assume code reuse is permitted until its terms are verified. GTD's linked implementation is hosted on an anonymous 4open URL, so license and reproducibility remain unverified.

## 3. Gate H0 verdict

**Not passed; do not implement Candidate H as currently stated.**

The current proposal fails for three reasons:

1. **No mechanism-level difference:** transfer-aware selection, human-monitorability objectives, protocol grammars, and task-adaptive routing are individually established. Combining them is not sufficient.
2. **The closest papers already expose the relevant failure:** CLSR documents cross-model mismatch; GlossoGen measures newcomer transmission and opacity; CPE evolves communication policies; the emergent-language literature studies cross-play, learnability, and population turnover.
3. **Reproducibility is incomplete:** the live CLSR/CPE code URLs returned 404, while MOC/GTD code licensing or release conditions are unresolved. GlossoGen is the clearest runnable licensed substrate, but its current scenario is not a ready-made evaluation of the full proposed claim.

This is a negative decision on the current formulation, not a claim that communication is an unimportant research area or that every possible EC method is exhausted.

## 4. What could be salvaged, if new evidence appears?

A future proposal would need to state a formal algorithmic difference beyond an extra fitness term. For example, a protocol genotype could expose typed semantic commitments and evidence provenance, while variation preserves those contracts; selection could then be evaluated on a held-out matrix of speaker–listener pairs and task compositions. But this remains **only a research prompt**, not an approved candidate: typed/grammar-guided synthesis, robustness selection, quality-diversity archives, and compatibility-aware protocol routing each have substantial prior art.

Before reopening this lane, resolve the live CLSR/MDia repository status and audit the closest work on protocol compatibility and evolutionary/quality-diversity selection. If the only remaining contribution is a weighted combination of success, transfer, and monitorability, drop it.

## 5. Next action

Broaden the search outside communication evolution and choose a strong, inspectable Agent+EC baseline with a concrete limitation that can be isolated in code and tested against strong alternatives. For the next candidate, require:
- an exact genotype/phenotype and evolutionary operator/selection distinction;
- a direct closest-work comparison, including classical EC mechanisms;
- a reproducible evaluation substrate with clear code/data rights;
- a falsifiable hypothesis and a stop condition;
- no expensive API or formal experiment before those gates pass.

No thesis title, innovation point, implementation, or API experiment is approved by this audit.
