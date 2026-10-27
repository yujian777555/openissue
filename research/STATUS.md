# Current Project Status

**Last updated:** 2026-10-27  
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
