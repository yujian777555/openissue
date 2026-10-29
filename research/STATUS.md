# Current Project Status

**Last updated:** 2026-10-29  
**Stage:** 3 — thesis-level proposal framing and candidate-method validation  
**Overall status:** OPEN; topic not selected  
**Source of truth:** this repository

## Objective

Prepare a defensible graduate thesis proposal on evolutionary computation applied to AI agents, aiming for 2–3 connected innovation points and 2–3 small-paper submissions.

## Confirmed requirements

- The immediate milestone is the thesis proposal/opening report.
- The thesis should be built around 2–3 substantive, connected contributions.
- Each contribution should have a plausible path to an independently publishable paper.
- The research should use evolutionary computation as a central method.
- Related work may be borrowed and improved; novelty does not require being completely unrelated to prior work.
- Existing work must be examined carefully before accepting or rejecting an idea.
- This project must be resumable across new ChatGPT conversations using repository records.
- Do not import candidate directions or conclusions from unrelated projects or previous conversations.

- The user explicitly excludes communication-evolution topics from the thesis candidate pool; do not reopen that lane unless the user asks.

## Not yet decided

- Exact research question and title.
- Whether the central object is a single-agent component, a multi-agent system, an evolutionary search mechanism, or another agent capability.
- Whether RSI is in scope for the final proposal.
- Candidate evolutionary algorithm(s), representation, base model, benchmarks, and evaluation metrics.
- Which papers or codebases will be the primary baselines.
- Final 2–3 innovation points and their mapping to papers.

## Research completed so far

- Added research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md with a staged experiment plan: benchmark sanity, policy DSL, static EA, static HPO, then adaptive parameter/operator control. It defines parameter layers, initial pilot ranges, baselines, metrics, ablations, and stop criteria.
- Audited ToolMaze (arXiv 2026 + official repository) as a potential controlled evaluation substrate: task DAG complexity C1–C4, explicit/implicit × transient/permanent faults, deterministic injection, valid-path enumeration, and TSR/PRR/RC metrics. It remains a benchmark, not an EA contribution. The source-pinned audit now records that current code intentionally changed RC to hit-conditioned at commit `f8620d8`, while paper/README still describe all-run RC; report both definitions and exposure rate if adopted.
- Deep-read key sections of EVOTOOL's paper: its ablations show that targeted module selection, trajectory plus explicit feedback, and diversity-aware selection all matter; its prior-art overlap with generic failure-aware tool-policy evolution is therefore high.
- Read the method and limitations of Code World Models for Parameter Control and LLaMEA-HPO. CWM controls mutation strength in a classical (1+1)-RLS_k optimizer and depends on problem descriptions/structured transition statistics in harder settings; LLaMEA-HPO separates LLM algorithm-structure search from SMAC tuning of generated-heuristic parameters. Neither establishes that online EA parameter control helps an LLM Agent policy EA.
- Registered ToolMaze, hierarchical QD recovery, the 2025 adaptive-operator-selection survey, APB, EvA, τ²-bench, and BFCL V4 as P45–P51 in the related-work matrix. APB-guided refinement is a non-EA baseline; EvA's abstraction/rollback controller is adjacent prior art, not automatically a population-based EA. APB is not yet a license-cleared fallback: the inspected code tree and HF card lack explicit license metadata, and its HF viewer fails schema casting. The current τ²-bench repository declares MIT and BFCL code/data declare MIT/Apache-2.0 respectively; these are auxiliary external evaluations, not direct replacements for controlled fault injection.
- ToolMaze adoption remains blocked: Hugging Face exposes one split named `train` rather than a documented optimization train/validation/test protocol, its viewer currently fails nested-schema inference, and neither the code tree nor dataset card exposes an explicit license. The new `research/TOOLMAZE_BENCHMARK_AUDIT.md` specifies split-leakage prevention, dual RC reporting, and the license gate.
- Audited recent primary sources for Agent-World, SEAL, SENTINEL, COvolve, RLAnything, and the 2026 co-evolution survey. Generic agent–environment co-evolution and failure-driven task generation are too crowded to claim as novel. Added P52–P57 and `research/COEVOLUTION_CANDIDATE_AUDIT.md`; typed recovery-program EA plus valid fault-program search remains a speculative narrow hypothesis.
- Audited Promptbreeder, Gödel Agent, Darwin Gödel Machine, HyperAgents, RQGM, SIA, Meta-Harness, MetaBench-Harness, and MoMHa. Generic meta-evolution, evaluator co-evolution, and harness/benchmark-generation search are also crowded. Added P58–P65 and `research/META_EVOLUTION_CANDIDATE_AUDIT.md`; only a narrow transferable search-controller question remains speculative.
- Broadened the candidate search to transactional tool-agent reliability and added P66–P71. A second-pass audit added P72–P79 (Cordon, Agentic Transaction, Verified Tool Calls, LIMBO, Sentry, Bench2Robust, AIR, IdempotencyBench) and found that broad transaction-aware recovery-controller evolution is too crowded to claim as novel. Atomix is the clearest licensed runnable runtime baseline; ResiliBench and Vera reuse rights remain unresolved, and several newer papers have no confirmed official code/data release.
- Added P80–P84 (Causal Agent Replay, Counterfactual Planning, JTPRO, ContDa, Gecko) and `research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md`. Candidate F—counterfactual-evidence-guided evolutionary credit assignment—did not pass its expanded novelty gate because causal repair and linkage-learning EA already cover core ingredients.
- Directly audited the official `amazon-science/EvoMAS` implementation. Confirmed that invalid mutation output returns the original parent, invalid crossover returns the better parent, crossover chooses the top two observed rewards, and operation traces omit parent-pair IDs. The selection index comments “win rate” but actually sorts by cumulative `total_wins`, then average accuracy. This is a concrete audit observation; the magnitude/impact of fallback on the paper's reported executability metric has not been independently recomputed.
- Added `research/EVOMAS_CODE_AUDIT_AND_PARENT_SELECTION_CANDIDATE.md` and `research/CANDIDATE_G_G0_REASSESSMENT.md`. The additional 2026 GPDPS⁽ᵒ⁾ paper directly combines diverse partner selection, brood recombination, surrogate offspring-performance estimation, and offspring selection. Together with DPS+BR, PAIR/LMEA, MECo/MTHS, and EoH-S, this means Candidate G's current formulation did not pass Gate G0 and should not be implemented as written. The EvoMAS fallback behavior is confirmed in code, but its effect on the paper's published executability metric remains unverified. `openissue` currently contains no lineage-linked run logs for the proposed offline analysis.
- Completed a second-pass mechanism audit of the communication-evolution lane. CLSR already evolves reusable symbolic protocols and evaluates cross-model/cross-domain transfer; GlossoGen directly tests newcomer-agent transmission and monitorability; CPE covers rollout-driven communication-policy evolution; GTD, MOC, and ProtocolBench cover topology generation, message consolidation, and protocol routing. Candidate H0 did not pass as formulated; see research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md. The current CLSR and CPE code URLs returned 404 in direct retrieval, and MOC/GTD reuse terms remain unverified.


- Added research/EC_ROLE_AND_PARAMETER_CONTROL.md to separate Agent-policy evolution, evolutionary-algorithm parameter control, and task/environment/evaluation settings.
- Inspected the official EVOTOOL repository (configs, SPEC.md, blame, mutation, selection, and evolution loop). Its central mechanism axes are blame/random/fixed/all/none mutation targets and diversity/greedy/top-k/static selection, with explicit trajectory/feedback ablations—not simply a numerical mutation-rate sweep.
- Added LLaMEA-HPO, Code World Models for Parameter Control, LLM mutation-control work, classical parameter-control references, and evolutionary recovery-controller work to the related-work matrix.
- Key methodological conclusion: structural/behavioural evolution and numerical hyperparameter tuning must be separated. Parameter control is mature EC prior art; no new method or thesis topic has been approved.

- Second-pass search expanded the related-work matrix from 15 to 37 core or adjacent papers/works, including 2026 work on tool-policy evolution, multi-agent evolution, skills, memory, planning, open-world shifts, and continual adaptation.
- Added research/CAPABILITY_GAP_REVIEW.md with field-crowding evidence, a provisional candidate comparison, and an explicit falsification plan.
- Found direct overlap for failure attribution (EVOTOOL/EvoMAS/HarnessEvolve), group/open-ended evolution (GEA/CORAL/EvE), skill and memory evolution (CoEvoSkills/Mem²Evolve/SkillComposer/ReMe/MCMA/MemEvolve), and planning (EvoPlan/APB/EvA/QD planning).
- No candidate is approved. State-contingent recovery remains a candidate to falsify; generic policy–curriculum co-evolution has been downgraded after direct overlap was found with COvolve, Agent-World, SEAL, SENTINEL, and RLAnything.

- Initialized project charter, literature protocol, thesis–paper map, decision log, and session handoff.
- Performed a first-pass search across recent agent/EA papers and surveys.
- Registered a preliminary matrix of 15 papers or closely related works in research/RELATED_WORK_MATRIX.md.
- Wrote research/INITIAL_RESEARCH_MEMO.md to capture what is already crowded and which candidate questions require deeper auditing.
- Confirmed that broad claims about prompt evolution, multi-agent generation, modular agent search, workflow evolution, whole-agent configuration tuning, memory evolution, and cost-aware optimization have substantial prior art.

- Initial-screened a second potential lane around skill/workflow generalization and faithful experience use. GSO reports substantial train-to-test skill regression; Faithful Self-Evolvers finds that condensed experience is often ignored/misused; H-EPM, AgentEvo, DIVE, and CATArena already cover adjacent memory, workflow, task-diversity, and evolutionary-capability questions. See research/AGENT_SKILL_GENERALIZATION_LANE_SCREEN.md. This is only a lane to audit, not an accepted candidate.

- Completed a first-pass source-code audit of Faithful Self-Evolvers: ExpeL's irrelevant/filler interventions are stochastic partial replacements; ReasoningBank is explicitly condensed-only; secondary FR/IG plotting helpers contain possible aggregation issues requiring comparison with the paper equations. These observations are not evidence that the paper's primary behavioral results are invalid. See research/FAITHFUL_SELF_EVOLVERS_CODE_AUDIT.md; code/data reuse is blocked pending license clarification.

- Reassessed the skill/workflow generalization and experience-faithfulness lane after checking SkillComposer, Rep2Skill, MetaMem, Live-Evo, SelSkill, and Skill Following. The broad formulation is too close to direct 2026 prior art and is downgraded; see research/AGENT_SKILL_LANE_REASSESSMENT.md.
- Opened a new exploratory lane for evolutionary test-time search over black-box agent trajectories. AMC (ICML 2026) is a direct baseline, but a current-main code audit found a potential resampling clone/client aliasing defect that must be verified before reproduction. See research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md and research/AMC_CODE_AUDIT.md. This is not an approved candidate; no API or benchmark experiment has started.

- Completed a second-pass prior-art audit for the black-box trajectory-search lane. SE-Agent already recombines prior trajectories, ToolTree searches tool-call trajectories with MCTS, TTHE evolves harnesses at test time, and TBETS/classical plan optimization cover legality-aware plan recombination. Candidate I0 does not pass as formulated; see research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md. Do not implement state-validated crossover as currently described.

- User clarification (2026-10-27): evolutionary-computation parameter tuning/control must be explicitly investigated. Do not reject a direction merely because prior work exists; use those papers as baselines and identify what can be improved or fused. New active exploratory plan: research/EC_PARAMETER_CONTROL_FUSION_CANDIDATE.md, combining a literature-grounded study of ELMER, The Time Value of Evolution/LVPG, adaptive operator selection, and EvoMAS strategy control. No innovation claim is approved yet.
- Added P136–P140 on ELMER, The Time Value of Evolution, EvoMAS: Heuristics in the Loop, AdaptEvolve, and population-based LLM evolution. Initial synthesis: ELMER calibrates semantic mutation strength but samples it uniformly; TVE/LVPG controls mutation radius with lineage returns but freezes the variation model and uses a trading-policy setting; EvoMAS: Heuristics in the Loop already adapts a repertoire of strategies. The promising question is whether a precise joint operator–strength controller with lineage-aware credit adds value for structured Agent evolution and transfers to held-out task families. This is a hypothesis requiring a close-work audit, not a novelty claim.

- Completed a primary-source mechanism audit of ELMER (arXiv:2608.10196) and The Time Value of Evolution/LVPG (arXiv:2608.13297). ELMER calibrates behavior-space mutation strength but its outer loop samples strength uniformly; LVPG learns state/horizon-dependent radius selection with lineage return but freezes its mutator; EvoMAS: Heuristics in the Loop already covers adaptive strategy portfolios and a reflective meta-controller. See research/EC_PARAMETER_CONTROL_FUSION_AUDIT.md.
- Refined the candidate from a vague three-way fusion to **OSLVC (Operator-Specific Lineage-Value Control)**: calibrate realized behavior scale per operator, jointly select operator and scale, and credit the pair by downstream lineage improvement. This remains a hypothesis. It must be compared with static HPO, classical AOS, ELMER-style strength-only control, LVPG-style lineage-only control, and EvoMAS strategy selection; task-family transfer is required.

- Follow-up audit of EvoMAS: Heuristics in the Loop found additional mechanism details in an accessible earlier manuscript appendix: sample from a strategy distribution; LLM-select candidates using performance/structure/rule compliance; periodically update the strategy distribution and rule set from a historical log every K generations; cumulative curriculum scoring across difficulty stages. The final PMLR version still needs line-by-line reconciliation, and the linked anonymous code mirror was inaccessible. This confirms adaptive strategy portfolios/meta-control are crowded, while operator-specific behavioral-scale calibration plus lineage credit remains only a candidate gap. See research/EC_PARAMETER_CONTROL_FUSION_AUDIT.md.

## Evidence state and caveats

This is a **multi-pass preliminary map**, not a completed systematic review or novelty assessment. Some papers have been read at abstract/method/results level; not every paper, supplement, or codebase has been fully audited. Candidate research questions remain hypotheses. No innovation point is approved.

## Latest scope adjustment (2026-10-23)

The user considers finite-budget evaluation efficiency insufficiently compelling as the central thesis problem. Therefore:
- Do **not** promote evaluation-budget allocation, noisy-fitness estimation, or survivor selection under limited evaluation budget as the default thesis direction.
- Evaluation cost may remain a secondary constraint/metric when relevant, but must not drive topic selection merely because it is measurable.
- Refocus the next search on important agent capability/behavior limitations where evolutionary computation could enable a substantive improvement, while remaining open to borrowing and improving existing methods.
- Do not treat this scope adjustment as a rejection of all work on evaluation reliability; retain it as supporting background only if a stronger problem requires it.

## Next actions (ordered)

1. Read research/EC_PARAMETER_CONTROL_FUSION_AUDIT.md. The concrete open question is operator-specific behavior-scale calibration plus joint operator–scale lineage-value control for Agent evolution; do not treat this as a proven novelty claim.
2. Reconcile the accessible earlier EvoMAS: Heuristics in the Loop appendix with the final ICML/PMLR version; confirm its controller state, strategy-distribution update, credit signal, and code availability. If this overlaps OSLVC, refine the mechanism instead of abandoning the whole line.
3. Verify official code availability, license and reproduction steps for ELMER/LVPG; separately audit the official EvoMAS generation code and EVOTOOL as candidate baselines.
4. Choose an executable Agent task suite and representation only after code/data rights and leakage checks. Define behavior displacement from structured action/tool traces on training probes; validate it separately for each operator.
5. Pre-register a compact static-HPO search space, task-family split, primary capability metric, and comparisons: static HPO, classical AOS, self-adaptation, ELMER-style strength-only, LVPG-style lineage-only, EvoMAS strategy selection, and OSLVC.
6. Main outcomes are task success and held-out task-family generalization. Evaluation counts are matched for fairness; cost is secondary. No paid API experiment until baseline and benchmark gates pass.
7. Prior-art overlap is a reason to sharpen the mechanism and strengthen baselines, not an automatic reason to abandon a research direction.

## Definition of done for the next milestone

The literature-scouting milestone is complete only when there is:
- a cited and verifiable set of relevant papers;
- a taxonomy and comparison matrix;
- deep analyses of the closest prior work;
- a ranked shortlist with explicit uncertainty and reasons;
- a recommended provisional direction with a falsifiable research question;
- no unsupported claims that the direction is novel.

- Latest substantive research commit verified before this update: 3814bb4ed569eaaaf879baeb65191249a9134455. The next update records the user's correction that parameter control must remain an active research axis and that overlap is not an automatic stop condition.

## Update protocol

At the end of every meaningful research session, update this file with what was verified, files and sources added, decisions made and why, unresolved questions, the next concrete action, and the relevant commit SHA when available.


## Thesis-level framing update (2026-10-27)

The user clarified that the current task is preparation for the **master's thesis proposal/opening report**, not the development of one standalone paper. The thesis must provide one coherent umbrella problem and 2–3 connected research contents; OSLVC is only a candidate core method, not the thesis title or three pre-approved innovations.

- Added `research/THESIS_PROPOSAL_FRAMEWORK.md` in Chinese, with a provisional title, umbrella research question, prior-art boundaries, two core candidate contributions plus one optional transfer extension, explicit EA parameter-tuning protocol, experiment plan, opening-report structure, and decision gates.
- Updated `research/THESIS_PAPER_MAP.md` to map candidate paper A (operator-specific behavior-scale calibration), paper B (joint operator–scale adaptive control with lineage value), and optional paper C (transfer mechanism). Paper C must not be counted as an innovation unless it has a distinct mechanism beyond held-out evaluation.
- Current working title: 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》. This is provisional and must not be treated as final until the closest-work audit, benchmark/license gate, and feasibility baseline are complete.
- Confirmed prior-art constraints: EVOTOOL covers modular tool-use policy, blame-aware targeted mutation, and diversity selection; EvoMAS covers structured MAS configuration evolution and feedback-conditioned variation; EvoMAS: Heuristics in the Loop covers adaptive strategy portfolios and reflective meta-control; ELMER covers behavior-grounded mutation scale; LVPG covers state/horizon-dependent scale control and lineage credit. A generic combination is not enough.
- No implementation or paid API experiment authorized yet. Next action is to finish mechanism-level comparison and benchmark/license feasibility, then produce a proposal-ready literature-gap matrix—not to prematurely lock three innovation claims.


## Parameter-control mechanism refinement (2026-10-27)

- A second-pass source check sharpened the candidate: a plain combination of ELMER-style behavior-scale control, LVPG-style lineage return, and AOS-style operator selection is not enough as an innovation claim.
- Added `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`, which reframes the testable mechanism as operator-specific continuation value conditioned on realized behavioral displacement, with matched parent/task/state comparisons.
- Added stronger baselines: classical AOS with diversity/parent-distance reward and a naive joint operator–strength controller with raw lineage return. The new decomposition must beat these baselines or be removed.
- Primary-source verification: ELMER's outer loop samples strength uniformly and explicitly identifies adaptive scheduling as future work; LVPG uses state/horizon-conditioned radius selection and lineage return with frozen ELM/radii; the official PMLR record confirms EvoMAS: Heuristics in the Loop's seven-strategy portfolio and reflective meta-controller. The exact EvoMAS HIL credit/state mechanism and official code remain unverified, so G0 remains OPEN.
- No implementation, API calls, or formal experiment has been started. Next step: finish full-paper/code/benchmark feasibility audit, then prepare the proposal-ready literature-gap table.


## Source and benchmark feasibility audit R1 (2026-10-27)

- **EvoMAS HIL:** verified from the official ICML/PMLR record that the paper uses seven evolutionary strategies, adaptive strategy selection, role-level evolution, curriculum-guided evolution, and a reflective Cyber Creator meta-controller. The exact reward/state/credit equations and final-version code/license could not be independently verified from a readable full paper in this pass. New record: research/EVOMAS_HIL_METHOD_AUDIT_R1.md. **G0 remains OPEN**; do not claim EvoMAS lacks scale-conditioned lineage credit.
- **Strong direct baseline:** EvoTool ACL 2026 official code is MIT licensed, uses a local OpenAI-compatible model endpoint, provides a deterministic offline executor and reference demo subsets, and exposes blame/random/fixed/all mutation targets plus diversity/greedy/top-k/static selection switches. Its core mechanisms (blame-aware mutation and diversity-aware selection) are established prior art and must be baseline, not claimed innovations.
- **Benchmark warning:** the EvoTool τ-bench converter orders canonical test tasks before train/dev and selects the first 150 valid tasks; the runner then random-shuffles those 150 into 90/30/30 train/selection/test. Thus canonical test tasks can enter the evolution pool. The original τ-bench README also warns that task versions are outdated. Do not use this demo split for final official test claims.
- **Benchmark candidate:** BFCL v4 via EvoTool offers an offline path and its upstream Gorilla repository is Apache-2.0 licensed, but data-specific terms and a task/API-family-held-out split still require verification. τ³-bench is the current updated alternative, but the old EvoTool adapter must be ported and validated.
- New proposal artifact: research/PROPOSAL_GAP_MATRIX_R1.md maps closest work, hypotheses, baselines, ablations, stop rules, and benchmark risks.
- **Gate status:** G0 (EvoMAS exact mechanism audit) OPEN; G1 (data rights + family-held-out split) PARTIAL/OPEN; G2 (local baseline execution) NOT RUN. No implementation, formal experiment, or paid API call has started.
- Next: obtain readable final EvoMAS PDF, finish exact method comparison; lock benchmark data/license/split; then run only a local, no-paid-call smoke test before preregistering the falsification experiment.


## Second EvoMAS paper audit (2026-10-27)

- **Disambiguation:** two separate ICML 2026 papers use the name EvoMAS. The Wei et al. HIL paper is covered by research/EVOMAS_HIL_METHOD_AUDIT_R1.md; exact reward/state equations remain unverified. The Hu et al. configuration-evolution paper has a readable full text and official code; audit: research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md.
- **Hu et al. findings:** structured MAS configuration search; execution-trace-conditioned mutation of exactly one component type per step; crossover inherits one parent's topology and recombines agent attributes; task-relevance/performance-history parent selection; reward = task metrics minus token/latency cost; parent-relative pool updates; experience-trace consolidation and retrieval of up to three similar prior experiences.
- **Novelty consequence:** feedback-conditioned mutation, crossover, configuration evolution, task-conditioned selection, and cross-task experience memory are already covered. Do not claim these alone as innovations. The possible narrow distinction remains operator continuation value conditioned on realized behavior displacement, subject to ELMER/LVPG/AOS and the Wei HIL audit.
- **License/compute:** Hu et al.'s official code is CC BY-NC 4.0, not MIT/Apache. Full reproduction with the paper's large models is not the first smoke-test target.
- **Gate status:** G0 remains OPEN for Wei et al.'s exact HIL mechanism; Hu et al. full-text/code audit is complete for the main operators, reward, pool, and memory mechanisms. G1 PARTIAL/OPEN; G2 NOT RUN.


## EvoMAS HIL full-text retrieval follow-up (2026-10-27)

- Attempted the final ICML PDF linked from the official PMLR page; the web reader rejected its binary content type and direct container download failed.
- Attempted the earlier anonymous OpenReview PDF; it redirects to an access-verification challenge. Indexed abstract text is not a substitute for the final method/equations.
- **G0 remains OPEN for a specific, documented access reason.** This is not evidence that the method lacks scale-conditioned lineage credit. No novelty decision should be made from absence in the abstract.
- Next: obtain a readable final PDF or author-provided source through an accessible legitimate route, then audit state/action/reward, operator definitions, lineage horizon, ablations, split, and seeds.


## Benchmark and baseline audit R2 (2026-10-27)

- Added `research/BENCHMARK_AND_BASELINE_DECISION_R2.md` with source-verified EvoTool baseline mechanics, the demo-split contamination risk, the current τ²/τ³-bench candidate, and a falsification-first experiment protocol.
- EvoTool is accepted as a strong direct baseline/reference implementation (MIT), but its bundled τ-bench demo split is not accepted as final test evidence because its builder selects from the upstream test split before train/dev.
- The current official `sierra-research/tau2-bench` release line is the leading realistic benchmark candidate. Pin one version; verify overlap between the source train/test lists and the frozen `text-v1` manifest before choosing the final split.
- BFCL v4 is secondary only unless the exact selected task subset is audited; an independent review reported defects in 24/50 sampled tasks.
- No benchmark, thesis topic, or innovation point is approved. OSLVC-R1 remains a falsifiable hypothesis. No full experiment or paid API call was performed.


## τ²-bench split-overlap finding (2026-10-27)

- Compared the official frozen `text-v1` subsets with source `train/test` task IDs: airline_50 = 30 train + 20 test; retail_50 = 28 train + 22 test; telecom_50 = 27 train + 23 test.
- Therefore the full `text-v1` frozen subset is **not** an untouched test set if policy evolution uses the source train partition. Do not report its full score as held-out generalization.
- The source train/test lists also do not by themselves guarantee task-family separation. Group near-duplicate tasks using redacted scenario instructions, issue/template metadata, and tool/action signatures before freezing train/validation/test.
- Details and protocol: `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`. No model experiment was run.


## Evaluator-validity audit and Tool-Veritas substrate (2026-10-27)

- New source audit: Bhat et al., `Benchmarking the Benchmarks` (arXiv:2607.02577), reports 92 evaluator–human disagreements across 496 tool-calling benchmark executions (18.5%); its τ²-Bench Retail sample was 11/112 (9.8%). Epoch AI separately reported defects affecting 24/50 sampled BFCL v4 tasks.
- This does not invalidate every public benchmark item, but it means we must inspect the exact selected tasks and evaluator rules rather than treat official scores as ground truth.
- Tool-Veritas is a potentially useful Apache-2.0 local execution substrate: deterministic state gates, multi-turn traces, and 70 bundled cases across 16 domains. Its bundled cases are not a ready-made train/validation/test split, and its reported human agreement has not been independently reproduced here.
- Revised plan: use Tool-Veritas as a controlled execution substrate with an independently verified, family-held-out task set; use pinned τ²/τ³-bench only for audited external validation. Keep BFCL v4 secondary. Details: `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`.


## Thesis feasibility and next validation gates (2026-10-29)

- Added `research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md` as the current continuation anchor for thesis feasibility, OSLVC-R1 boundaries, benchmark decisions, gate states, and next actions.
- The immediate deliverable remains the master's thesis opening report—not implementation of a standalone paper. Working title remains provisional: 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》.
- Latest conversational feasibility estimates (explicitly subjective, not calibrated probabilities or experimental results): whole-thesis completion 75–85%; OSLVC as the final effective algorithmic contribution 35–50%; 2–3 independent defensible innovation points 50–65%; 2–3 small-paper submissions 40–60%. Revise these only when G0/G1/G2 evidence arrives; do not present them as measured facts.
- OSLVC-R1 remains a hypothesis, not an approved innovation. The narrow question is whether operator continuation value conditional on realized behavior displacement adds value beyond immediate reward, raw lineage return, displacement-only prediction, and naive joint operator–strength control.
- **G0 OPEN:** final EvoMAS: Heuristics in the Loop state/action/reward/credit mechanism not fully verified. **G1 PARTIAL/OPEN:** benchmark/split/scorer protocol still needs locking. **G2 NOT RUN:** no local mechanism pilot has run.
- Next: finish the closest-paper method audit; finalize a family-held-out controlled suite and audited external subset; then, and only then, run a small no-paid-call mechanism pilot. No paid API experiment is authorized.
- Keep this project separate from all other repositories; communication evolution remains excluded. Two strong contributions are preferable to three duplicated ones.




## Repository continuity protocol (2026-10-29)

- Permanent rule added in root `CONTINUITY_PROTOCOL.md`: every substantive session must inspect latest commits, read status/decision/handoff, update the relevant research files, refresh `SESSION_HANDOFF.md` and `NEXT_SESSION_PROMPT.md`, commit, and verify the resulting remote content.
- Copyable next-session prompt: `NEXT_SESSION_PROMPT.md`; detailed handoff: `SESSION_HANDOFF.md`.
- This rule applies to research, literature review, planning, negative results, and experiments. If no new evidence emerges, preserve a correct handoff and explicitly state that no substantive research result changed; do not fabricate activity.
- This repository remains the sole source of truth for the thesis project. Do not mix unrelated repositories.



## Immediate next action re-confirmed (2026-10-29)

- Rechecked the official PMLR final record for EvoMAS: Heuristics in the Loop; the final publication page is available, but the PDF is still not extractable by the current reader and the linked OpenReview page triggers a browser-verification challenge.
- **G0 remains OPEN.** Next: make a bounded attempt to obtain the final PDF/verified author copy. If access remains blocked, audit the accessible earlier manuscript only as a provisional preprint (clearly label all claims unverified against the final version) and continue G1 in parallel. Do not infer absence of an equivalent mechanism from missing access.
- **G1 remains PARTIAL/OPEN; G2 remains NOT RUN.** No formal experiment or paid API call was started.
- No substantive research conclusion changed in this check; the purpose was to verify the current blocker and make the next action explicit.



## Provisional EvoMAS mechanism audit — 2026-10-29

- A bounded attempt to read the final ICML/PMLR PDF still failed: the official record/abstract are accessible, but the PDF is rejected as binary by the current reader; OpenReview redirects to a browser-verification challenge.
- The search index exposed substantial sections of the earlier anonymous manuscript. A **provisional preprint-only mechanism audit** is now recorded in research/EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md.
- Preprint-level findings: EvoMAS already covers a multi-operator portfolio, adaptive strategy selection, historical performance-based strategy credit, LLM-guided multi-criteria selection, reflective rule updates, graph edit distance for structural diversity, role evolution, and curriculum. These are not standalone novelty claims.
- Narrow candidate to test: whether *realized execution-trace behavior displacement* adds incremental value to operator/strength continuation-credit estimation beyond immediate reward, raw lineage return, structural graph distance, and existing adaptive controls. This is a hypothesis only; final-version equivalence is unverified.
- **G0 OPEN:** final ICML method equations/ablations not yet verified. **G1 PARTIAL/OPEN:** task-family split, version/license manifest, task IDs, and scorer/oracle checks still need locking. **G2 NOT RUN:** no experiment, code reproduction, or paid API call.
- Next: advance G1 in parallel with one bounded attempt to obtain the final paper; freeze the controlled task-family split/scorer protocol before any formal pilot. Do not promote OSLVC to an approved innovation.



## EvoMAS HIL public-record audit (2026-10-29)

- Re-opened the official PMLR final record and attempted the official PDF/OpenReview links. The final paper metadata and abstract are readable; the PDF is not extractable by the current reader and OpenReview redirects to browser verification.
- Verified from the official abstract that EvoMAS includes a seven-strategy evolutionary portfolio, adaptive strategy selection, role-level evolution, curriculum-guided evolution, and the reflective Cyber Creator meta-controller.
- Consequence: generic adaptive operator/strategy selection and reflective evolutionary meta-control are already covered and must not be claimed as innovations.
- Exact state/action/reward/credit/update equations, displacement measurement, conditional lineage value, and ablations remain **unverified**. Abstract-level silence does not prove absence.
- G0 remains OPEN; G1 PARTIAL/OPEN; G2 NOT RUN. Next: bounded attempt at a legitimate readable final/author copy; in parallel advance the family-held-out task split and scorer audit. No formal experiment or paid API call was run.
- Detailed evidence and boundaries: `research/EVOMAS_HIL_METHOD_AUDIT_R1.md`.



## G1 progress — task-family protocol R1 (2026-10-29)

- Added `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`: a 120-task original deterministic-suite design, 12 global task families, whole-family split (60 train / 30 validation / 30 test), state oracle, behavior-displacement metric, fairness controls, and exact pinned external task IDs.
- Tool-Veritas's bundled `all.jsonl` was source-parsed: 70 cases, 16 domain labels, 20 domain/category combinations, 70 unique normalized goals, no family field or ready-made split. It is not accepted as the final benchmark. Candidate harness only; author task content from scratch unless data provenance/license is resolved.
- Pinned τ²/τ³-bench v2.0.0 source-test candidate: commit `989d3285ae669e49503324bdb9981bf14fccedeb`; airline test IDs (20) and retail test IDs (40) are recorded in the G1 protocol. This is a custom source-test evaluation, not the `text-v1` leaderboard set. Scorer components must be reported separately.
- Newly found Δτ-Bench (arXiv:2610.34238; 2026-10-25) has 1,588 tasks/42 domains/six ecosystem versions and a state-change evaluator; it is a candidate external benchmark, not selected yet because dataset license/revision/checksum and family-overlap need verification.
- **Gate states:** G0 OPEN; G1a design provisionally specified; G1b original task files/oracle tests/hash NOT DONE; G1c external adapter/scorer and Δτ decision NOT DONE; G1 overall PARTIAL/OPEN; G2 NOT RUN.
- No tasks were authored or executed, no adapter was run, and no model/API experiment occurred in this design round. Next: audit Δτ dataset license/split briefly, choose/defer it; then implement the original case schema and generate the 120-task manifest, starting with deterministic oracle unit tests.



## τ² source-split similarity finding (2026-10-29)

- Ran a heuristic word-level TF-IDF similarity screen on task purpose, user reason-for-call, and task instructions for every source-test task against source-train tasks in pinned tau2-bench v2.0.0.
- At screening threshold cosine ≥0.45, nearest-train similarity was above threshold for 4/20 airline test tasks and 17/40 retail test tasks. Examples include retail test 94 ↔ train 93 (1.000), 32 ↔ 31 (0.968), 62 ↔ 63 (0.963), and airline test 16 ↔ train 15 (0.695).
- This is a heuristic screen, not a validated duplicate detector; manual task/schema review is still needed. It is sufficient to prohibit describing τ² source train/test as task-family-held-out. Use it only as a standard source-split or external-transfer evaluation; family-held-out evidence must come from the original controlled suite.
- Details: `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`. G1 remains PARTIAL/OPEN; no experiment or API call was run.



## Δτ-Bench bounded access decision (2026-10-29)

- The official code repo README/license were inspected and state MIT for code, with the dataset hosted separately. Attempts to read the official Hugging Face dataset page, metadata, and raw card failed through the available reader; this does not prove the dataset lacks a license.
- Dataset license, exact revision, checksum manifest, and task-family overlap are unverified. Δτ-Bench is therefore **deferred as a selected benchmark**, retained as related work, and should not trigger repeated retries of the same URL.
- Next concrete action is now implementation-focused: define the original task schema and machine-readable 12-family manifest, implement deterministic state-transition/oracle tests, then generate the controlled-suite task cases. τ²/τ³-bench v2.0.0 remains the external candidate, but its source split is not family-held-out.
