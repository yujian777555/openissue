# Thesis–Paper Contribution Map

**Updated:** 2026-10-27  
**Status:** Proposal-stage candidate map; not approved as final thesis topic or innovation claims.

## 1. Working thesis framing

**Provisional title:** 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》

**Umbrella problem:** How to make evolutionary optimization of structured LLM-Agent tool-use policies behaviorally controllable, adaptively governed, and effective on held-out task families.

**Core evolutionary-computation role:** representation/genotype design, variation operators, static EA hyperparameter optimization, online operator/scale control, lineage credit assignment, selection and held-out generalization evaluation.

**Current core hypothesis:** per-operator behavioral-scale calibration, joint operator–scale control, and lineage-value credit may improve Agent task success and cross-task generalization. This remains a hypothesis, not a novelty verdict.

## 2. Candidate contribution map

| Dimension | Paper A — Behavior-scale calibration (candidate) | Paper B — Adaptive joint control (core candidate) | Paper C — Transfer/generalization (optional) |
|---|---|---|---|
| Research question | Do heterogeneous Agent variation operators map the same requested strength to different realized behavior changes, and does operator-specific calibration improve search? | Does selecting operator and scale jointly, with lineage-value credit, beat strong static HPO and single-mechanism controllers? | Can a learned controller transfer to held-out task families through a distinct mechanism rather than merely being evaluated on them? |
| Prior-art anchor | ELMER | ELMER, LVPG, classical AOS/self-adaptation, EvoMAS: Heuristics in the Loop | MECo/MTHS and task-conditioned evolutionary transfer |
| Candidate mechanism | Measure parent/child tool/action trace displacement on shared probes; calibrate strength by operator; separately track validity and task success | State-conditioned action (a=(operator, scale)); use immediate and downstream lineage signals; compare with fixed HPO, AOS, ELMER-style scale-only and LVPG-style lineage-only controllers | Only after a separate mechanism-level gap audit; possible task-conditioned initialization/transfer of control preferences |
| Primary metric | Task success after evolution and calibration fidelity; distance correlation alone is insufficient | Held-out task success and improvement over strong static/AOS baselines | Held-out task-family success and transfer gap |
| Essential ablations | Shared vs per-operator calibration; no scale control; nominal text labels vs realized traces | Joint vs independent heads; immediate vs lineage credit; no state features; strongest fixed configuration | No transfer vs task-specific training vs transferred controller |
| Independence gate | Must improve downstream search quality, not just predict distance | Must show added value beyond A and all direct control baselines | Must have a distinct transfer mechanism; held-out testing alone is not a third innovation |
| Status | Candidate, uncertain independent-paper value | Main method candidate, not yet approved | Optional; do not force |

## 3. Contribution dependencies

- Paper A provides a calibrated behavioral action space for Paper B if its benefit is supported.
- Paper B is the core algorithmic contribution and must stand against strong static HPO, classical AOS, ELMER-style strength-only control, LVPG-style lineage-only control, and the closest Agent-evolution baseline.
- Paper C is not yet an innovation point. If no distinct transfer method survives the prior-art review, transfer becomes a generalization experiment within Paper B and the thesis targets two strong contributions instead of three weak ones.

## 4. Current closest-work constraints

- EVOTOOL already covers modular tool-use policy, trajectory-grounded blame, targeted mutation, and diversity-aware selection.
- EvoMAS: Evolutionary Generation already covers structured MAS configuration evolution, feedback-conditioned mutation/crossover, and experience memory.
- EvoMAS: Heuristics in the Loop already covers adaptive strategy portfolios and reflective meta-control.
- ELMER already covers behavior-grounded mutation-scale calibration.
- LVPG already covers state/horizon-dependent mutation intensity and lineage-level return.
- LLaMEA-HPO establishes that static hyperparameter tuning should be separated from structural search.
- Classical AOS and self-adaptation are mandatory baselines.

Therefore no generic claim such as “evolutionary Agent optimization,” “adaptive operator selection,” “behavioral mutation strength,” “lineage reward,” or “cross-task transfer” is sufficient on its own.

## 5. Paper readiness gate

A candidate paper is ready only when:
1. closest-work mechanism comparison is source-verified;
2. benchmark/code/data rights and reproduction are confirmed;
3. static EA hyperparameters are tuned on train/validation and then frozen;
4. direct strong baselines and predeclared ablations are completed;
5. task success/generalization gains are reproducible across seeds;
6. the paper's claim is distinct from the other thesis contributions.
