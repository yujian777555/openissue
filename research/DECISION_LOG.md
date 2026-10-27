# Research Decision Log

Record consequential project decisions here so future sessions do not reopen settled questions without new evidence. A decision can be provisional and later revised; record the evidence that triggers a change.

## D-000 — Use this repository as the durable project record

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** This repository is the source of truth for the thesis proposal workflow, literature corpus, candidate directions, innovation mapping, and session handoffs.
- **Rationale:** The project will span multiple conversations and research stages; state must survive context loss.
- **Evidence:** User explicitly requested that long-term continuity be maintained in this repository.
- **Revisit when:** Repository access or workflow changes.

## D-001 — Do not preselect a topic before the literature review

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** Do not treat any agent-evolution subtopic as the answer before systematic comparison of recent work and feasible experiments.
- **Rationale:** The user rejected the current premature idea and asked for independent, evidence-based discovery.
- **Implication:** Search broadly, compare close prior work, then rank candidate research questions.
- **Revisit when:** The first literature corpus and comparison matrix are complete.

## D-002 — Aim for 2–3 connected contributions and papers

- **Date:** 2026-10-23
- **Status:** Target
- **Decision:** Plan the thesis around 2–3 substantive contributions, with a target of developing 2–3 small papers for submission.
- **Rationale:** This is the user's stated thesis and publication objective.
- **Caveat:** Do not manufacture weak contributions just to reach three; report honestly if evidence supports a different feasible structure.
- **Revisit when:** The candidate contribution map is evaluated against novelty, feasibility, and timeline.

## D-003 — RSI is an open question, not a foregone conclusion

- **Date:** 2026-10-23
- **Status:** Accepted as review policy
- **Decision:** Neither automatically exclude nor automatically select RSI / recursive self-improvement.
- **Rationale:** Its suitability depends on current prior art, objective evaluation, reproducibility, cost, and whether a specific tractable problem exists.
- **Revisit when:** Relevant recent papers and evaluation methods have been reviewed.

## D-004 — Broad EA + agent directions require narrow differentiation

- **Date:** 2026-10-23
- **Status:** Provisional evidence-based warning
- **Decision:** Do not use generic prompt evolution, modular agent search, multi-agent generation, workflow evolution, whole-agent configuration tuning, memory evolution, or cost-aware optimization as a thesis innovation claim without a precise mechanism-level distinction.
- **Evidence:** First-pass review of EvoPrompt, AgentSquare, EvoAgent, AFlow, EvoAgentX, GEPA, ARTEMIS, HFlow, and MemEvolve. See research/RELATED_WORK_MATRIX.md and research/INITIAL_RESEARCH_MEMO.md.
- **Caveat:** This is not a rejection of those areas. A specific, meaningful improvement may still be possible after deeper comparison.
- **Revisit when:** Close-work audits and broader EA literature review are complete.

## D-005 — Do not make finite evaluation budget the central thesis problem

- **Date:** 2026-10-23
- **Status:** Accepted as current scope guidance
- **Decision:** Do not center the thesis on fitness estimation, evaluation-budget allocation, or survivor selection merely because Agent evaluation is noisy and expensive. Evaluation cost may remain a secondary constraint or metric when relevant.
- **Rationale:** The user judges the finite-budget problem insufficiently compelling as the main research contribution. The thesis should target a meaningful Agent capability/behavior limitation and use evolutionary computation to improve it.
- **Implication:** Continue literature review by extracting substantive failure modes and improvement opportunities from recent EA + Agent work, rather than defaulting to evaluation efficiency.
- **Revisit when:** A concrete agent capability problem is supported by literature and shows a clear, feasible evolutionary-method contribution.


## D-006 — 2026 literature requires capability-level and mechanism-level triage

- **Date:** 2026-10-23
- **Status:** Accepted as research procedure
- **Decision:** Do not select a thesis topic from broad labels such as tool-use evolution, memory/skill evolution, planning evolution, multi-agent evolution, or generalization. The second-pass literature shows substantial recent overlap in all these areas.
- **Evidence:** Second-pass sources registered in research/RELATED_WORK_MATRIX.md and synthesized in research/CAPABILITY_GAP_REVIEW.md, including EVOTOOL, EvoMAS, EvA, GEA, CORAL, CoEvoSkills, Mem²Evolve, HarnessEvolve, OpenAgent, ScaleEnv, APB, EvoPlan, and SkillComposer.
- **Current audit candidate:** State-contingent recovery from unseen tool/environment failures, explicitly provisional and subject to rejection if too close to EVOTOOL, EvA, HarnessEvolve, APB, or quality-diversity planning.
- **Revisit when:** Full-text and code-level comparisons identify a concrete unaddressed failure mode and a distinct evolutionary mechanism.


## D-007 — Separate agent-policy evolution from EA parameter control

- **Date:** 2026-10-23
- **Status:** Accepted as research procedure
- **Decision:** Every candidate method must explicitly separate (A) the Agent phenotype/policy being evolved, (B) the evolutionary algorithm's own parameters and online control rules, and (C) task/environment/evaluation settings. Generic numerical tuning of population size, mutation rate, crossover rate, or retry count is not sufficient as the sole contribution.
- **Evidence:** EVOTOOL official code exposes mechanism-level axes (blame/random/fixed/all/none mutation target; diversity/greedy/top-k/static selection; trajectory/feedback guidance). LLaMEA-HPO separates structural algorithm evolution from SMAC-based HPO. Code World Models for Parameter Control (2026), the LLM mutation-control line, and classical EC parameter-control literature directly study adaptive parameter settings. See research/EC_ROLE_AND_PARAMETER_CONTROL.md and P38–P44 in research/RELATED_WORK_MATRIX.md.
- **Implication:** Any proposed EC innovation must state its genotype, representation, variation operators, selection/replacement, fitness, parameter-control policy, and the ablations needed to show the EC mechanism itself causes the capability gain.
- **Revisit when:** Mechanism-level audits identify a concrete capability limitation and a distinct EC contribution supported by primary-source evidence.


## D-008 — Validate the evolutionary contribution in stages

- **Date:** 2026-10-23
- **Status:** Accepted as research procedure; topic remains provisional
- **Decision:** For the recovery-policy candidate, first validate the benchmark and policy representation, then test a static EA, then test static HPO, and only if the EA adds capability test adaptive parameter/operator control.
- **Rationale:** Adaptive operator selection, self-adaptation, and mutation-strength control are mature research areas. Starting with a complex adaptive controller before showing that evolution helps would confound policy representation, evolutionary search, and parameter-control effects.
- **Evaluation candidate:** ToolMaze, because it offers deterministic perturbation injection, a task-DAG complexity axis, explicit/implicit and transient/permanent fault types, enumerated recovery paths, and TSR/PRR/recovery-cost metrics.
- **Closest-work warnings:** EVOTOOL already has blame-aware targeted mutation and diversity-aware selection; HarnessEvolve has reference-trajectory alignment, error clustering, quality/performance gates; hierarchical QD has diverse repertoire-based recovery; classical AOS/self-adaptation prior art is extensive.
- **Required comparisons:** fixed rule baseline, direct reflection/replanning, random mutation, greedy one-child search, static EA, statically tuned EA, classical AOS, self-adaptation, and an EVOTOOL-style baseline if reproducible.
- **Revisit when:** ToolMaze baseline reproduction and the first static-EA pilot produce verified evidence.


## D-009 — Benchmark metric and license verification is a hard gate

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** ToolMaze remains a candidate benchmark, not an approved experimental substrate, until its metrics and data/code usage terms are verified.
- **Evidence:** The paper defines mode-level RC with an exposure indicator, and the README says no-hit runs contribute zero. The inspected current public `evaluation/core/metrics.py` computes RC over hit runs only, excluding no-hit cases from the denominator. For an illustrative three-run case (no-hit = 0, hit-fail = 1, hit-success = 0.2), the paper/README definition gives 0.4 while the current hit-conditioned implementation gives 0.6. The inspected GitHub tree had no visible root LICENSE file and the Hugging Face dataset card did not expose a clear license field.
- **Implication:** Create a synthetic metric fixture, determine which version produced published results, report both variants if unresolved, and confirm code/data terms before redistribution. Do not compare methods using the current RC implementation without disclosing this discrepancy.
- **Revisit when:** The metric discrepancy and licensing are verified against an authoritative release or author clarification.


## D-010 — ToolMaze metric version drift is intentional in code but documentation is stale

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** Do not describe the RC difference as an accidental code bug. Pin the code version and report both definitions if ToolMaze is used.
- **Evidence:** Current official code HEAD `f8620d841b67a72ac921caee9df87af6ab9befbb` (2026-10-20) explicitly says it changed RC from all-sample to exposure-conditioned; no-hit runs are `rc=None` and excluded from the denominator. The paper's Eq. (4) and README still say no-hit runs contribute zero. For per-run penalties [0, 1, 0.2], all-run RC is 0.4 and hit-conditioned RC is 0.6; exposure rate is 2/3.
- **Additional blockers:** The HF dataset page exposes one split named `train`, not a documented train/validation/test split; its viewer fails nested-schema inference; no root code LICENSE or explicit dataset-card license was found in inspected sources.
- **Implication:** ToolMaze is on hold as the primary benchmark. If later adopted, pin source/data revisions, validate raw JSON schema, group all perturbation variants by base task/template, report both RC definitions plus exposure rate, and confirm code/data terms before redistribution. APB is a possible external benchmark, but its own license and data interface must be audited.
- **Revisit when:** License terms are confirmed and the dataset/schema is validated, or a clearly licensed alternative benchmark is selected.


## D-011 — APB is a useful baseline concept, not a license-cleared benchmark

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** Keep APB in the prior-work and potential external-evaluation matrix, but do not treat it as a ready replacement for ToolMaze.
- **Evidence:** The APB paper (arXiv v3, 2026-10-05) describes 4,209 cases across 22 domains, broken-tool/unsolvable settings, and APB-guided refinement evaluated on ToolSandbox and τ²-bench. The inspected APB code repository has no root LICENSE; the Hugging Face dataset card declares no explicit license and its viewer currently fails schema/column casting. The six dataset files are task categories, not a declared policy-search train/validation/test protocol.
- **Implication:** Treat APB-guided refinement as a strong non-EA baseline conceptually, but audit code/data rights, raw JSONL loading, and leakage before use. If neither APB nor ToolMaze has suitable terms, build an independent controlled task generator or select a benchmark with clear use terms.
- **Revisit when:** Dataset/code license and reproducibility checks are complete.


## D-012 — Separate the controlled evolution environment from external evaluation

- **Date:** 2026-10-23
- **Status:** Accepted as a planning rule; benchmark choice remains open
- **Decision:** Do not force ToolMaze or APB to serve as both the evolution/training environment and the final test set. Prefer a clearly licensed controlled environment for policy search; use frozen public benchmarks only as held-out external checks.
- **Evidence:** ToolMaze and APB have unresolved code/data license metadata and current Hugging Face viewer/schema friction. τ²-bench's repository declares MIT and BFCL V4 code/dataset declare MIT/Apache-2.0 respectively, but neither supplies ToolMaze's exact controlled fault matrix. τ²-bench's public leaderboard trajectory files have a separate license question.
- **Implication:** If permissions for ToolMaze/APB cannot be confirmed, build a small independent DAG/fault generator for training/development and reserve τ²-bench/BFCL categories for frozen external evaluation. The generator is infrastructure, not a claimed innovation. Pin benchmark versions and avoid evolving directly on final public test tasks.
- **Revisit when:** Code/data terms are confirmed and the target recovery capability plus baselines are finalized.


## D-013 — Audit policy–curriculum co-evolution in parallel, without approving it

- **Date:** 2026-10-23
- **Status:** Accepted as a research procedure
- **Decision:** Do not force state-contingent recovery-policy evolution to become the thesis topic. Audit a second candidate in parallel: co-evolution of an agent recovery policy and a valid failure/task curriculum.
- **Rationale:** The policy-only candidate has direct overlap with EVOTOOL, EvA, HarnessEvolve, APB-guided refinement, and QD recovery, while its most direct benchmark candidates have unresolved data/code terms. A procedural environment generator could remove third-party task-data dependence and make evolutionary computation central in both policy and curriculum search.
- **Prior-art warning:** Adversarial environment design and automatic curricula have substantial history, including POET, PAIRED, and ACCEL. “Co-evolution” alone is not novel. The audit must test whether LLM tool-failure semantics and held-out compositional fault generalization reveal a specific gap.
- **Required comparisons:** fixed curriculum, random curriculum, policy-only EA, curriculum-only search, policy–curriculum co-evolution, and a strong non-EA recovery/reflection baseline. Validate task solvability independently to prevent generator reward hacking.
- **Implication:** Paper 1 (static EA over policy genotype) is a gate; Paper 2 (co-evolution) proceeds only if Paper 1 shows evolutionary capability gains; Paper 3 (external transfer) is optional and must establish an independent claim. Do not fill the thesis–paper map yet.
- **Revisit when:** The policy-only and co-evolution prior-art audits identify a mechanism-level difference with a feasible evaluation design.


## D-014 — Generic policy–environment co-evolution is not a novelty claim

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** Downgrade Candidate B. Do not present “co-evolve a tool agent and failure curriculum” or “generate tasks from failures” as the thesis innovation.
- **Evidence:** Primary-source audit in `research/COEVOLUTION_CANDIDATE_AUDIT.md`. COvolve (GECCO 2026) co-evolves LLM-generated executable policies and environments in a zero-sum game; Agent-World synthesizes tool/database environments and tasks and uses multi-environment RL with capability-gap-driven expansion; SEAL adapts a tool-use learning interface and policy updates from verifier-grounded failure diagnoses; SENTINEL generates executable tasks from failure patterns and trains with RL; RLAnything jointly adapts environment, policy, and reward. The 2026 co-evolution survey explicitly maps this landscape.
- **Implication:** A narrower hypothesis may be tested: EA over typed executable recovery programs coupled to a constrained grammar of valid tool-fault transformations, targeting held-out combinations of fault semantics and task-DAG topology. This is not yet a novelty claim; domain shift alone is insufficient. Compare against EVOTOOL, reflection/replanning, policy-only EA, failure-driven task generation, and adversarial co-evolution.
- **Alternative:** Add meta-evolution of the search mechanism to the literature audit because the survey describes it as an early area, while checking PromptBreeder, Gödel Agent, HyperAgents, RQGM, and classical adaptive operator selection.
- **Revisit when:** The mechanism-level audit establishes a difference and a matched-budget experiment can falsify it.


## D-015 — Generic meta-evolution is not a novelty claim

- **Date:** 2026-10-23
- **Status:** Accepted
- **Decision:** Downgrade Candidate D in its broad form. Do not claim novelty for a self-improving optimizer, an evolving mutation prompt, an editable meta-agent, or a co-evolved evaluator.
- **Evidence:** Primary-source audit in `research/META_EVOLUTION_CANDIDATE_AUDIT.md`. Promptbreeder evolves task and mutation prompts; Gödel Agent, Darwin Gödel Machine, and HyperAgents study recursive self-modification and evolution of improvement routines; RQGM co-evolves agents and evaluators; SIA selects between harness and weight updates; Meta-Harness searches harness code; MetaBench-Harness evolves benchmark-generation workflows; MoMHa studies multi-objective harness optimization. Classical adaptive operator selection is mature prior art.
- **Implication:** Only a narrow transferable search-controller hypothesis remains: learn to choose among typed policy-edit/structural operators using out-of-sample operator-impact evidence, and prove transfer to held-out tasks against classical AOS and the closest self-modification systems. This is not yet a validated gap.
- **Next action:** Broaden the candidate search to other underexplored intersections before selecting any thesis topic.
- **Revisit when:** A mechanism-level distinction and feasible falsification plan are established.


## D-016 — Test transaction-aware recovery control before choosing a thesis topic

- **Date:** 2026-10-23
- **Status:** Accepted as a candidate-screening procedure; topic remains unapproved
- **Decision:** Add Candidate E: evolutionary synthesis of a bounded recovery controller around stateful transactional tools, under immutable safety contracts. Compare it with the policy-only recovery and transferable search-controller candidates before selecting the thesis topic.
- **Rationale:** Recent primary sources establish a concrete, consequential problem: stochastic tool failures and flawed instructions (ResiliBench), partial/irreversible tool effects and transaction settlement (Atomix), state-race guard precision, and safety/functionality Pareto trade-offs in evolutionary harness search (Harmony Harness). This gives observable state invariants and deterministic evaluation signals.
- **Closest-work warnings:** Atomix already provides a transaction-aware runtime; semantic state-race guards and Vera-style executable safety verification are direct baselines; Harmony Harness and MoMHa already evolve harnesses over functionality/safety/cost. The contribution cannot be “EA optimizes safety and success” or a new benchmark alone.
- **Required gate:** Show that an evolved bounded controller improves the safe-completion/false-abort frontier over Atomix + fixed rules, conservative abort, semantic-predicate guards, reflection/replanning, and a reproducible harness-evolution baseline under matched budgets. Hard safety invariants must remain outside the evolved genome.
- **Revisit when:** Code/data rights are verified and the first matched-budget pilot demonstrates or falsifies an EA-specific benefit.


## D-017 — Broad transaction-aware recovery evolution fails the novelty gate

- **Date:** 2026-10-26
- **Status:** Accepted
- **Decision:** Downgrade Candidate E from a potential thesis topic to a comparison setting. Do not claim “evolutionary transaction-aware recovery controller” as novel in its broad form.
- **Evidence:** Second-pass primary-source review in `research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md` and P66–P79 of the related-work matrix. Atomix, Cordon, Agentic Transaction, AIR, LIMBO, Verified Tool Calls, Bench2Robust, Sentry, ResiliBench, and Harmony Harness cover transactional execution, non-atomic failures, recovery, controlled recoverability, incident response, and/or evolutionary harness optimization.
- **Code/data gate:** Atomix has Apache-2.0 code, a runtime, baseline implementations, tests, and local experiment configs. ResiliBench's linked repository exposes supplementary JSON artifacts without a top-level license or full runner; Vera's inspected root has no top-level software license; the Harmony Harness repository found is third-party, not author-linked official code. LIMBO, Bench2Robust, Cordon, Agentic Transaction, and Verified Tool Calls have no confirmed official runnable release in the inspected paper pages.
- **Implication:** A new controller representation, safety metric, or benchmark alone is not enough. Any future work in this domain must be justified by a distinct EC mechanism and compared with strong existing methods.
- **Revisit when:** A method-level novelty claim survives a direct comparison and the evaluation substrate has clear rights and executable contracts.

## D-018 — Counterfactual-evidence-guided evolutionary search is the next hypothesis, not an approved topic

- **Date:** 2026-10-26
- **Status:** Provisional
- **Decision:** Investigate whether measured interventional outcome deltas can improve evolutionary credit assignment, mutation-target selection, or operator adaptation for agent policies.
- **Evidence:** Candidate audit in `research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md`; related works P80–P84 include Causal Agent Replay, Counterfactual Planning, JTPRO, ContDa, and Gecko. The key direct overlaps are EVOTOOL, CAR, Counterfactual Planning, and mature adaptive operator selection.
- **Potential contribution:** A precise interventional estimator/update rule that predicts which edits or operators causally improve held-out policy performance, beyond trajectory-only blame, simple paired fitness differences, and classical AOS.
- **Required Gate F0:** Write the estimand and algorithm, compare mechanism-by-mechanism with EVOTOOL, Causal Agent Replay, Counterfactual Planning, AOS/self-adaptation, and test whether the credit signal predicts out-of-sample gains.
- **Stop condition:** The method is only a combination of known components, requires hidden fault labels, or loses to EVOTOOL/AOS under matched calls and held-out fault × topology generalization.
- **Revisit when:** Gate F0 establishes a defensible mechanism-level distinction. No implementation or thesis topic is approved yet.


## D-019 — Counterfactual interaction-guided evolution is not yet distinct

- **Date:** 2026-10-26
- **Status:** Accepted as a negative prior-art finding; candidate remains unapproved
- **Decision:** Do not implement Candidate F in its current form.
- **Evidence:** Updated audit in `research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md` and P85–P90 in `research/RELATED_WORK_MATRIX.md`. CausalFlow generates counterfactual repairs from interventional attribution; Graph-Constrained Joint Replay / Minimal Repair Family Recovery evaluates singleton and pair repairs over dependency graphs; Causal Agent Replay estimates interventional and Shapley effects; Counterfactual Planning uses counterfactual rewards; GAwLL and a 2026 *Evolutionary Computation* paper already learn variable-importance/interaction graphs to guide variation.
- **Implication:** “Counterfactual effects + interaction graph + EA” is not a sufficient method novelty claim. A surviving proposal would need a formal agent-policy-specific estimator/update rule that adds information beyond empirical linkage learning and causal repair/attribution, with held-out transfer evidence.
- **Next action:** Broaden the candidate search again; do not force a thesis topic around the current recovery/counterfactual family.
- **Revisit when:** A distinct mechanism is specified and passes direct comparison with the closest prior art.


## D-020 — Candidate G is a concrete improvement hypothesis, not a novelty claim

- **Date:** 2026-10-26
- **Status:** Provisional; Gate G0 open
- **Decision:** Focus the next research pass on a possible improvement to EvoMAS's parent-pair selection: task-family-conditioned prediction of actual offspring improvement using lineage-linked observations.
- **Code evidence:** Official `amazon-science/EvoMAS` source inspected through GitHub. Invalid mutation returns the original configuration; invalid crossover returns the better parent; crossover selects the two highest observed rewards; per-step operation records omit parent IDs/pair identity; the experience schema lacks lineage, task-family ID, and repeated-trial uncertainty. In `mas_index.py`, a comment says “Sort by win rate” but the actual key is cumulative `total_wins`, followed by `avg_accuracy`.
- **Prior-art warning:** Classical diverse partner selection with brood recombination explicitly uses parent phenotype strengths/weaknesses to estimate crossover benefit; adaptive mating is older EC work; PAIR and LMEA cover LLM-guided parent selection; MECo, MTHS, and EoH-S cover cross-task population interaction/transfer and complementary selection. Thus generic offspring-yield-aware mating is not novel.
- **Possible distinction:** Online, task-conditioned estimation of lineage-linked child improvement for structured MAS configurations, with explicit accounting for invalid proposals/repairs/fallback and transfer to held-out task families. This distinction must be proven against the closest baselines.
- **Next test:** Offline predictive-value analysis first; compare out-of-sample pair-yield prediction against parent fitness, structural diversity, task-conditioned individual fitness, PAIR-style LLM compatibility, and classical diverse-partner selection. Do not start expensive LLM experiments until G0 passes.
- **Stop condition:** If lineage-linked offspring yield adds no predictive value or is matched by PAIR/classical mating under controlled splits, reject Candidate G.
- **Caution:** The code-level fallback issue is verified, but the effect on published executability numbers is not yet recomputed. Do not state that the paper's metric is inflated as a confirmed result.


## D-021 — Candidate G's current formulation fails the prior-art gate

- **Date:** 2026-10-26
- **Status:** Accepted negative prior-art finding; current formulation rejected
- **Decision:** Do not implement Candidate G as currently specified. Its core claim—selecting parent pairs using predicted offspring improvement, optionally conditioned on task family—does not yet provide a defensible mechanism-level distinction.
- **Evidence:** `research/CANDIDATE_G_G0_REASSESSMENT.md` adds GPDPS⁽ᵒ⁾ (2026), which combines diverse partner selection, brood recombination, surrogate offspring-performance estimation, and offspring selection. Existing direct overlaps include DPS+BR (2018), PAIR, LMEA, MECo, MTHS, and EoH-S. The official EvoMAS code also lacks parent-pair IDs in operation traces, and no lineage-linked run logs are present in `openissue`.
- **Evidence boundary:** The code-level parent fallback is verified, but the exact effect on the published executability metric remains unresolved. Do not claim that the metric is inflated.
- **Implication:** Keep EvoMAS as a strong baseline/code-audit target, but broaden the thesis candidate search rather than turning a domain-specific reimplementation of known mating/surrogate mechanisms into an innovation claim.
- **Next action:** Find a different, falsifiable Agent + EC method-improvement opportunity; require primary-source prior-art and data-feasibility gates before implementation.


## D-022 — Communication evolution is a screening lane, not an approved candidate

- **Date:** 2026-10-26
- **Status:** Exploratory; no topic or innovation point approved
- **Decision:** Screen whether evolutionary computation can materially improve communication-protocol transfer and monitorability across unseen or heterogeneous LLM agents, but do not claim novelty for generic protocol evolution, topology optimization, or message consolidation.
- **Evidence:** The new research/COMMUNICATION_EVOLUTION_LANE_SCREEN.md registers P100–P104. CLSR (ICML 2026) already evolves and routes compact symbolic communication protocols; MOC (ICML 2026) optimizes multi-order message aggregation; GTD (ACL 2026) generates task-adaptive communication topologies with proxy-guided multi-objective rewards; GlossoGen provides a controlled language-evolution platform; the emergent-language survey covers zero-shot coordination and channel evolution.
- **Feasibility caveats:** The code URL listed on the CLSR proceedings page currently returns 404 in the checked web view; MOC has a public implementation; GTD's code link is hosted on an anonymous 4open URL; GlossoGen has a public MIT-licensed repository. Runnable-code status, exact benchmark contracts, and reproducibility still require audit.
- **Required gate:** Show a specific capability failure not already addressed by CLSR/GlossoGen and define an evolutionary representation/operator/selection mechanism that adds more than a new scenario or objective weight. Cost/token reduction may remain secondary, not the central thesis problem.
- **Next action:** Audit the closest methods and determine whether a transfer/monitorability gap survives. If not, drop this lane and continue the broader search.


## D-023 — Communication evolution does not pass the current novelty gate

- **Date:** 2026-10-26
- **Status:** Accepted negative finding for the current formulation
- **Decision:** Do not implement Candidate H as currently stated: evolving communication protocols for transfer to unseen/heterogeneous agents while adding monitorability constraints.
- **Evidence:** research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md and the expanded communication lane audit. CLSR (ICML 2026) evolves reusable symbolic protocols and tests cross-model/cross-domain transfer; GlossoGen directly studies newcomer-agent transmission and human monitorability; CPE (EMNLP 2026) evolves communication policies from rollout feedback; GTD, MOC, and ProtocolBench cover topology generation, message aggregation, and constraint-aware protocol routing. Emergent-language work also covers human-like language, cross-play/zero-shot coordination, learnability, and population turnover.
- **Rationale:** A weighted combination of task success, transfer, and interpretability is not a distinct evolutionary mechanism. The current formulation does not define a new genotype, variation operator, selection/replacement rule, or formal property that survives closest-work comparison.
- **Evidence boundary:** Direct retrieval of the stated CLSR and CPE code URLs returned 404 in this audit. A cached search snapshot appears to describe a broader MDia extension, but the live repository was not retrievable; treat it as an unresolved prior-art warning, not verified runnable code. MOC/GTD code reuse terms also remain unresolved.
- **Implication:** Keep communication evolution as background or a future evaluation setting, not an approved thesis direction. Broaden the candidate search to a different strong, inspectable Agent+EC baseline and require a concrete mechanism-level improvement before implementation.
- **Revisit when:** New primary-source evidence reveals a specific unaddressed failure and a distinct evolutionary mechanism—not merely a new benchmark or objective weight.


## D-024 — Next screening lane: skill/workflow generalization and experience faithfulness

- **Date:** 2026-10-26
- **Status:** Exploratory; not a candidate acceptance
- **Decision:** After the communication-evolution formulation failed its novelty gate, screen whether evolutionary computation can improve held-out generalization and faithful use of agent experience/skills.
- **Evidence:** GSO (arXiv 2609.39148) reports that most skills improving on training tasks do not retain all gains on held-out tasks; Faithful Self-Evolvers (ICML 2026) measures causal dependence on raw and condensed experience and finds condensed experience can be ignored/misused; H-EPM, AgentEvo, DIVE, and CATArena cover adjacent memory, workflow evolution, task diversity, and iterative improvement.
- **Guardrail:** This is a research lane, not an approved thesis topic or innovation point. A new fitness term, memory graph, skill format, or task-specific-skill policy alone is not enough.
- **Next gate:** Deep-read GSO and Faithful Self-Evolvers, inspect official evaluation code, compare with H-EPM and AgentEvo, and define a concrete EC genotype/operator/selection mechanism. Stop if the proposal reduces to weighted generalization/faithfulness objectives or duplicates existing methods.


## D-025 — First-pass Faithful Self-Evolvers code audit

- **Date:** 2026-10-26
- **Status:** Code observations accepted; no candidate accepted
- **Decision:** Retain the experience-faithfulness lane for deeper literature audit, but do not implement an EA method yet.
- **Observed:** ExpeL's irrelevant/filler interventions are stochastic partial replacements (80% replace, 20% preserve); ReasoningBank is explicitly a condensed-only setting; cdt/src/stats_frscore.py appears to rescale a cumulative vector inside its sample loop, and cdt/src/stats_igscore.py may count one excluded row in the denominator.
- **Scope caution:** These observations concern intervention strength and secondary plotting/aggregation. They do not by themselves invalidate the paper's primary behavioral results. Compare the helpers with the paper equations and saved per-sample artifacts before making stronger claims.
- **Rights:** The public repository is retrievable, but a root LICENSE file was not found; no code/data reuse is approved.
- **Next:** Deep-read GSO and compare its task-specific skill generation with H-EPM and AgentEvo. Reject any proposal that merely adds faithfulness/generalization terms to fitness.


## D-026 — Exclude communication evolution from the thesis candidate pool

- **Date:** 2026-10-27
- **Status:** Accepted user constraint
- **Decision:** Do not propose or continue communication-protocol evolution, communication interpretability, or newcomer-agent communication transfer as a thesis direction unless the user explicitly reopens it.
- **Rationale:** The user stated: “通信方向我不想做”.
- **Implication:** Keep the existing communication papers only as relevant-work records where needed; do not spend further candidate-selection effort on that lane.

## D-027 — Downgrade the broad skill/generalization/experience-faithfulness lane

- **Date:** 2026-10-27
- **Status:** Accepted negative finding for the current formulation
- **Decision:** Do not implement the current broad lane as a thesis candidate.
- **Evidence:** GSO, SkillComposer, Rep2Skill, EvoSkill, MetaMem, Live-Evo, SelSkill, Skill Following, H-EPM, and AgentEvo collectively cover held-out skill generalization, task-specific skill generation, create/improve/merge, representation-guided revision, meta-memory evolution, online forgetting, skill invocation, actual-use evaluation, hybrid episodic/procedural memory, and workflow evolution. See research/AGENT_SKILL_LANE_REASSESSMENT.md and P113–P124 in research/RELATED_WORK_MATRIX.md; newer entries P119–P124 add direct overlap.
- **Rationale:** A new weighted generalization/faithfulness score, skill format, memory graph, or invoke/skip controller is not a distinct EC mechanism.
- **Implication:** Keep this lane as related work and broaden to a different algorithmic problem.

## D-028 — Open an exploratory lane for black-box agent trajectory search

- **Date:** 2026-10-27
- **Status:** Exploratory only; Gate I0 not passed
- **Decision:** Screen whether state-validated evolutionary recombination of per-instance tool-action trajectories can improve test-time black-box agent search.
- **Closest baseline:** Agentic Monte Carlo (ICML 2026), which uses a learned value function and SMC to steer a frozen black-box agent over trajectories. Adjacent work includes ASMC, LP-SMC, EVOTOOL, DUPO, and T-MAP.
- **Potential mechanism:** Recombine trajectory suffixes only at equivalent observable states within the same task instance, then replay/validate offspring. This is not approved as novel; classical plan-space GA/GP and evolutionary planning must be checked.
- **Baseline-integrity warning:** Current public AMC main appears to reuse the same mutable client object in AgentGymAgent.clone(); because SMC resamples with replacement, sibling clones may share one environment ID. See research/AMC_CODE_AUDIT.md. Reproduce this in a minimal local test before relying on AMC.
- **Stop condition:** If state-compatible plan crossover is already established or fails to beat mutation-only EA and the strongest feasible non-EA search under matched conditions, abandon the lane.
- **Guardrail:** No API experiment, formal benchmark run, or implementation is approved before the novelty, baseline-integrity, and benchmark/license gates pass.


## D-029 — Candidate I0 does not pass the trajectory-search novelty gate as formulated

- **Date:** 2026-10-27
- **Status:** Accepted negative finding for current formulation
- **Decision:** Do not implement state-validated evolutionary crossover over black-box agent trajectories as currently described.
- **Evidence:** SE-Agent (NeurIPS 2025) directly performs trajectory revision, recombination, and refinement; its public crossover implementation synthesizes a strategy from two trajectory summaries. ToolTree (ICLR 2026) searches tool-call trajectories using MCTS and dual feedback. TTHE evolves executable harnesses at test time. TBETS and the IJCAI 2024 plan-optimization survey establish adjacent prior art for evolutionary action-sequence search and legality checking during recombination. See P131–P135 and research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md.
- **Rationale:** State-validated action-sequence crossover differs from SE-Agent's strategy-level synthesis, but legality-aware plan recombination is established in evolutionary planning. That difference is not yet enough to support a thesis claim.
- **Implication:** Keep AMC code audit as a reproducibility note, not as a reason to pursue the lane. Broaden candidate search instead of forcing this mechanism.
- **Reopen only if:** A distinct operator or formal search property is identified that cannot be reduced to existing trajectory recombination plus known plan-validity checks, and it has a credible comparison against mutation-only EA and strong non-EA planning baselines.
