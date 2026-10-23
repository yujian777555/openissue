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
