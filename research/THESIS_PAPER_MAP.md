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


## 5. Candidate-method refinement (2026-10-27)

Paper B's candidate is no longer described as merely combining operator choice, mutation scale, and lineage credit. Its testable core is **scale-conditioned lineage-value credit**: estimate operator-specific continuation value conditional on realized behavior displacement under matched parent/task/state comparisons. Paper A remains the possible operator-specific behavior-response calibration study, but it is independently publishable only if it improves downstream search beyond ELMER. Paper C remains optional; held-out task evaluation alone is not an innovation.

Detailed specification and rejection criteria: `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`.


## 6. Benchmark and baseline gate update (2026-10-27, revised after split and evaluator audits)

- EvoTool (ACL 2026, MIT code) is the strongest direct Agent-policy evolution baseline; its bundled τ-bench demo split is not valid final test evidence.
- Tool-Veritas (Apache-2.0 subproject) is a candidate local deterministic execution substrate, not a pre-approved benchmark. It currently contains 70 examples across 16 domains and needs an independently verified family-held-out task set; its author-reported evaluator agreement has not been independently reproduced here.
- The official `sierra-research/tau2-bench` repository remains a realistic external-validation candidate, but Bhat et al. (2026) report evaluator–human disagreement in its Retail sample (11/112). Audit the exact selected tasks and scoring rules; do not treat the official score as unquestionable ground truth.
- Exact source split overlap remains: `airline_50` = 30 train / 20 test IDs; `retail_50` = 28 / 22; `telecom_50` = 27 / 23. The complete frozen `text-v1` manifest cannot be called held-out if evolution used the source-train partition.
- Epoch AI separately reports defects affecting 24/50 sampled BFCL v4 tasks; use BFCL only as an audited secondary check.
- Main success oracle should verify goal-relevant state outcomes; tool-call validity and conversational quality must be separate metrics. See `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`.
## 7. Additional nearest prior art: Hu et al. EvoMAS (2026)

Hu et al.'s *EvoMAS: Evolutionary Generation of Multi-Agent Systems* already combines execution-feedback-conditioned mutation/crossover, task-relevance-based parent selection, reward-based pool updates, and cross-query experience memory. Paper A cannot claim feedback-guided mutation or memory alone, and Paper B must compare its conditional-credit mechanism against this configuration-evolution family. The object differs (MAS configuration vs current single-Agent policy), so a fair direct comparison may require matching the operator/credit component rather than comparing whole systems. Official code is CC BY-NC 4.0; see research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md.




## 8. Feasibility and contribution independence update (2026-10-29)

The thesis-level route remains worth pursuing, but OSLVC-R1 is not yet an approved core contribution. Current subjective planning ranges (not calibrated probabilities or empirical findings): thesis completion 75–85%; OSLVC as final effective method 35–50%; 2–3 independent defensible innovation points 50–65%; 2–3 small-paper submissions 40–60%.

The thesis should target two strong connected contributions first:
- **A (conditional):** operator-specific behavior-scale calibration, only if it improves downstream search beyond ELMER.
- **B (core candidate):** realized-displacement-conditioned lineage-value credit, only if it beats static HPO, classical AOS (including diversity/parent-distance credit), ELMER-style scale-only control, LVPG-style lineage-only control, and a naive joint operator–strength controller.
- **C (optional):** a separate transfer/control mechanism only if a distinct prior-art gap is identified. Held-out evaluation alone is not a third innovation.

G0 remains OPEN, G1 PARTIAL/OPEN, and G2 has NOT RUN. No paid API experiment is authorized. See `research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md`.


## 8. API-backed LLM and Agent-side training architecture (2026-11-02)

The intended deployment model is now a hosted API LLM used as the fixed reasoning executor, with training integrated into the Agent runtime. This is distinct from asking the Agent to call external APIs as tools.

| Layer | Candidate object | Training / optimization | EC role |
|---|---|---|---|
| Main LLM | Hosted API model, frozen during ordinary training | Inference only; provider fine-tuning is optional and must be verified separately | Not directly evolved unless a supported trainable endpoint is explicitly chosen |
| Agent controller | Compact state-conditioned policy over harness actions | SFT/BC or offline RL on rollout traces; can be trained locally on A800 | Candidate genotype/policy search, parameter evolution, operator/scale control |
| Value/critic | State/partial-trajectory value estimator | Train from task outcome and trajectory data | Guide candidate action or evolutionary lineage selection; AMC is a direct baseline |
| Skills/functions | External skill files, functions, schemas, workflow modules | LLM-assisted edits with held-out validation and rollback | Possible structured evolution, but AgentOptimizer and SkillOpt are direct baselines |
| Optional auxiliary model | Small open-weight model/LoRA for a bounded Agent-side role | Local GPU training and OpenAI-compatible serving | Candidate trainable component, not a replacement for the hosted main LLM |

### Candidate paper chain (not approved)

- **Paper A — Trainable Agent-side controller:** define a compact, auditable harness state/action representation for an API-backed Agent and establish that a learned controller improves over fixed harness rules. This is not yet an innovation claim because offline RL harness control already exists.
- **Paper B — Evolutionary controller learning/control:** test a specific EC method for optimizing the Agent-side controller or its structured policy, and require gains over AW/offline RL, BC, static HPO, classical AOS/self-adaptation, and the closest frozen-model baselines. Replacing AW with a GA without a mechanism-level advantage is insufficient.
- **Paper C — Optional transfer:** test whether the learned evolutionary controller transfers across held-out task families or API providers through a distinct mechanism. Cross-provider evaluation alone is not a third innovation.

The A800s can train a local controller/value model or optional small auxiliary LLM. The main API LLM remains frozen. The paper map will be revised only after the new candidate passes a closest-work audit and the benchmark/API contract gates.


## 9. API-backed external-controller contribution map (2026-11-03)

The optimized object is narrowed from a generic Agent harness to a compact external state-action controller around a frozen hosted API LLM. Full mechanism comparison: `research/API_AGENT_EC_MECHANISM_AUDIT_R1.md`.

| Candidate | Research question | Candidate mechanism | Mandatory closest baselines | Status |
|---|---|---|---|---|
| A — Operator-specific controller behavior-response calibration | Do typed controller variation operators produce different realized action-trace displacement at the same requested strength, and does operator-specific calibration improve downstream controller search? | Matched parent/task/state probes; measure action-trace displacement and feasibility separately; calibrate each operator's strength-to-behavior response | AW controller, static EA, classical AOS, parent-distance/diversity AOS, ELMER-style scale control, TTHE/HarnessX method-level comparison | Conditional; not yet shown independently publishable |
| B — Scale-conditioned lineage-value credit for controller evolution | Does downstream controller lineage value depend on operator identity after conditioning on realized behavior displacement and task/state context? | Estimate `Q(s,o,d,h)=m(s,d,h)+a(s,o,d,h)`; use matched comparisons; use local value model only as auxiliary estimator | Raw lineage return, immediate reward, displacement-only control, naive joint operator-strength control, LVPG-style lineage-only, ELMER-style strength-only, AW, tuned static EA, classical AOS | Core candidate; novelty/effectiveness unverified |
| C — Optional cross-family / cross-model transfer | Can the learned controller or operator preferences transfer to held-out task families or another API model? | Only a distinct transfer mechanism can count as a third contribution | No-transfer, task-specific controller, AW transfer, direct reuse of controller | Optional; held-out testing alone is not an innovation |

**Architecture:** hosted API LLM is frozen; controller and optional value model are local Agent-side components. A800s may train the value/critic or a small auxiliary model. The API model is not fine-tuned.

**Critical acceptance rule:** Paper B is not ready unless it beats a strong offline AW controller and strong static/classical EA baselines on task-state success and held-out task-family success under matched model/API exposure. If not, retain only the empirically supported contributions; do not force three papers.
