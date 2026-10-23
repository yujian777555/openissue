# Literature Review: Protocol and Registry

## Purpose

Determine the current state of research at the intersection of evolutionary computation and AI agents, and find evidence-backed opportunities for a thesis with 2–3 connected contributions.

## Search window

Prioritize work published or publicly released in **2024–2026**, while retaining older foundational papers when they are direct baselines or necessary to understand the field. Record the version/date of each source because preprints and conference versions may differ.

## Search lanes

1. Evolutionary optimization of LLM agents and agent systems.
2. Evolution of prompts, instructions, workflows, tool-use policies, skills, memory, and agent architectures.
3. Evolutionary algorithms for multi-agent cooperation, role assignment, communication, and coordination.
4. Evolution of code-writing or research agents and constrained agent improvement / RSI.
5. Evolutionary operators, population management, fitness estimation, credit assignment, diversity, and search efficiency for agent optimization.
6. Evaluation reliability: benchmark leakage, reward hacking, judge bias, cost-aware evaluation, generalization, and reproducibility.
7. Surveys and benchmark papers that reveal the field's taxonomy and unresolved challenges.

These lanes guide retrieval; they are not a commitment to any particular topic.

## Source quality and verification

Prioritize official conference proceedings, journal pages, arXiv records, author project pages, and original GitHub repositories. Use secondary summaries only for discovery, not as the sole basis for technical claims.

For every candidate core paper:
- verify title, authors, date, venue/status, and canonical URL;
- read the abstract and method, then the full paper and supplement where available;
- distinguish reported results from our interpretation;
- inspect official code, issues, and evaluation scripts when available;
- check follow-up work and papers that may have independently proposed similar mechanisms.

Do not infer publication acceptance from an arXiv page. Do not infer a limitation solely from a missing experiment. Do not claim code reproduces results until this has been checked.

## Search log

| Date | Source / query family | Purpose | Outcome / follow-up |
|---|---|---|---|
| 2026-10-23 | ToolMaze benchmark version, metric, dataset-schema, and license audit | Determine whether the benchmark can support evolutionary recovery-policy experiments | Added research/TOOLMAZE_BENCHMARK_AUDIT.md. Current code intentionally uses hit-conditioned RC while paper/README use all-run RC; dataset split/license remain blockers. |
| 2026-10-23 | APB (arXiv v3) and EvA (ACL 2026) primary-source audit | Strengthen non-EA planning/recovery baselines and identify adjacent adaptive-control methods | Registered P48–P49; APB-guided refinement and EvA abstraction/rollback are direct comparisons, not EA contributions. |
| 2026-10-23 | License and evaluation-scope audit: τ²-bench 2.0.0 and BFCL V4 | Find auxiliary benchmarks with clearer code/data terms while preserving a separate controlled training environment | Registered P50–P51. τ²-bench (MIT) and BFCL V4 (Apache-2.0) are auxiliary external tests, not substitutes for controlled failure injection.
| 2026-10-23 | EC parameter-control audit: EVOTOOL official implementation, LLaMEA-HPO, Code World Models for Parameter Control, LLM mutation control, classical parameter-control literature, evolutionary recovery controllers | Separate policy evolution from EA parameter tuning/control and determine necessary baselines | Added research/EC_ROLE_AND_PARAMETER_CONTROL.md; generic parameter tuning is not accepted as a sole contribution. |
| 2026-10-23 | Second-pass primary-source search: recent EA-agent evolution, tool-use policy, skills, memory, planning, open-world generalization, continual learning | Identify direct overlaps and concrete capability failure evidence | Registered 22 additional core/adjacent works in RELATED_WORK_MATRIX.md; all candidate gaps remain provisional. |
| 2026-10-23 | Search: evolutionary algorithms for LLM agents, agent design/workflow search, prompt evolution, multi-agent evolution | Find direct EA + agent methods and current baselines | Found EvoAgent, AgentSquare, AFlow, EvoPrompt, EvoAgentX, ARTEMIS, GEPA, HFlow, MemEvolve and adjacent self-evolving agent work. |
| 2026-10-23 | Search: agent optimization surveys and EC–MAS surveys | Build a field taxonomy and locate overlooked prior art | Found Du et al. (ACM Computing Surveys 2026) and Chen et al. (IEEE/CAA Journal of Automatica Sinica 2025). |
| 2026-10-23 | Primary-source review: ICLR/ACL proceedings and arXiv full text | Inspect mechanisms, evaluation, and stated limitations | Read abstract/method/results portions of several core papers; full close-work audit remains incomplete. |
| 2026-10-23 | Primary-source audit: Agent-World, SEAL, SENTINEL, COvolve, RLAnything, and co-evolution survey | Falsify generic policy–failure-curriculum co-evolution | Registered P52–P57 and added research/COEVOLUTION_CANDIDATE_AUDIT.md; generic co-evolution and failure-driven task generation are too crowded to claim as novel. |
| 2026-10-23 | Primary-source audit: Promptbreeder, Gödel Agent, DGM, HyperAgents, RQGM, SIA, Meta-Harness, MetaBench-Harness, MoMHa | Test whether meta-evolution of the search mechanism is a distinct thesis direction | Registered P58–P65 and added research/META_EVOLUTION_CANDIDATE_AUDIT.md; generic self-improving optimizer, evaluator co-evolution, and harness/benchmark-generation search are already studied. |

## Preliminary registry

The detailed paper list and comparison are maintained in [RELATED_WORK_MATRIX.md](RELATED_WORK_MATRIX.md). It now contains 65 core or closely related works across the first and second search passes. See [CAPABILITY_GAP_REVIEW.md](CAPABILITY_GAP_REVIEW.md) for second-pass synthesis and provisional candidate triage.

### Initial core reading order

1. AgentSquare — modular agent search, recombination, and performance prediction.
2. AFlow — workflow representation, MCTS, execution feedback, cost, and transfer.
3. GEPA — trajectory reflection, prompt evolution, Pareto-based selection, rollout efficiency.
4. ARTEMIS — whole-agent configuration optimization, mixed-type search, statistical evidence, and compute costs.
5. HFlow — preference feedback, hierarchical experience memory, and cost-aware workflow evolution.
6. MemEvolve — memory architecture meta-evolution and cross-task/model/framework transfer.
7. EvoAgent — evolutionary generation of multi-agent systems.
8. EvoPrompt and Promptbreeder — foundational prompt evolution.
9. EvoAgentX and ADAS — workflow optimization platforms and adjacent methods.
10. AgentGym and AgentEvolver — adjacent self-evolving agent-learning paradigms.
11. Du et al. and Chen et al. surveys — broad taxonomy and related-work discovery.

## EC role and parameter-control audit

A staged experiment protocol is now recorded in [EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md](EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md). It proposes validating a recovery benchmark first, then testing static EA over an interpretable recovery-policy representation, and only then testing adaptive parameter/operator control. ToolMaze is currently on hold as the primary benchmark pending metric-version, data-schema, and license checks; see TOOLMAZE_BENCHMARK_AUDIT.md. It includes static HPO, classical AOS, self-adaptation, optional CWM-style control, and explicit stop criteria. A separate audit in [EC_ROLE_AND_PARAMETER_CONTROL.md](EC_ROLE_AND_PARAMETER_CONTROL.md) distinguishes (A) the Agent phenotype being evolved, (B) the evolutionary algorithm's own control parameters, and (C) task/environment/evaluation settings. EVOTOOL's official code shows the importance of mechanism-level ablations (mutation target, selection strategy, trajectory/feedback guidance). LLaMEA-HPO separates algorithm-structure evolution from numeric HPO; Code World Models and classical EC literature show that adaptive parameter control is itself established prior art. Therefore a numerical sweep of mutation rate/population size alone is not an adequate thesis contribution.

## Current interpretation after second pass

The 2026 literature directly covers generic tool-policy evolution, failure attribution, multi-agent configuration evolution, skill/verifier co-evolution, memory/experience evolution, plan-level evolution, quality-diversity planning, open-world generalization, and continual adaptation. The next milestone is mechanism-level comparison and attempted falsification of candidate gaps, not more broad keyword collection. Finite-budget evaluation remains a secondary consideration, not the central thesis problem.

## Comparison dimensions

For cross-paper comparison, record:
- evolutionary search space and genotype/phenotype mapping;
- how candidates are generated and modified;
- whether variation operators are fixed, learned, or adapted;
- fitness noise, evaluation cost, and how these are controlled;
- population diversity and selection pressure;
- single-task performance vs held-out generalization;
- whether the optimized object transfers across tasks/models;
- external verification and safeguards against reward hacking;
- computational cost and reproducibility;
- evidence that evolutionary search is essential compared with simpler alternatives.

## Research-gap standard

A proposed gap must be supported by at least one of:
- an explicit limitation or future-work statement in a relevant paper;
- a concrete failure pattern in reported experiments;
- a mechanism-level weakness demonstrated by analysis or controlled tests;
- a meaningful setting not covered by close prior work, with a clear reason it matters.

A gap is not validated until the closest prior work and competing explanations are checked. Any proposed innovation should include a falsifiable hypothesis and an experiment that could show it does **not** help.
