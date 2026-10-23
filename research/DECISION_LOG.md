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
