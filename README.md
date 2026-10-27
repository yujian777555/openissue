# Evolutionary Computation for Agents — Thesis Research Workspace

This repository is the durable source of truth for a graduate thesis project on **using evolutionary computation to improve AI agents**.

The goal is not to commit prematurely to a fashionable topic. The project will systematically review recent work, reproduce and critique promising baselines where feasible, identify evidence-backed limitations, and develop **2–3 connected thesis contributions**, with the aim of producing **2–3 independently publishable small papers**.

## Start here

1. Read [Project Charter](research/PROJECT_CHARTER.md) for scope and research principles.
2. Read [Current Status](research/STATUS.md) for the current stage and next actions.
3. Read [Literature Review](research/LITERATURE_REVIEW.md) for the review protocol and paper registry.
4. Read [Related-Work Matrix](research/RELATED_WORK_MATRIX.md) for the current paper comparison and overlap warnings.
5. Read [Capability-Gap Review](research/CAPABILITY_GAP_REVIEW.md) for second-pass 2026 literature and provisional candidate triage.
6. Read [EC Parameter-Control Experiment Protocol](research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md) for the staged policy-search, parameter-tuning, and adaptive-control experiment plan.
7. Read [ToolMaze Benchmark Audit](research/TOOLMAZE_BENCHMARK_AUDIT.md) before adopting ToolMaze or running recovery-policy experiments.
8. Read [Co-Evolution Candidate Audit](research/COEVOLUTION_CANDIDATE_AUDIT.md) before treating policy–environment co-evolution as a novelty claim.
9. Read [Meta-Evolution Candidate Audit](research/META_EVOLUTION_CANDIDATE_AUDIT.md) before treating self-improving search mechanisms as a novelty claim.
10. Read [EvoMAS Code Audit and Parent-Selection Candidate](research/EVOMAS_CODE_AUDIT_AND_PARENT_SELECTION_CANDIDATE.md) and [Candidate G G0 Reassessment](research/CANDIDATE_G_G0_REASSESSMENT.md) before revisiting Candidate G.
11. Read [Transactional Agent Robustness Candidate Audit](research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md) before promoting transaction-aware recovery-controller evolution.
12. Read [Counterfactual Evolution Candidate Audit](research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md) before promoting counterfactual-evidence-guided evolutionary search.
13. Read [EC Role and Parameter Control](research/EC_ROLE_AND_PARAMETER_CONTROL.md) for the distinction between Agent-policy evolution, EA parameter control, and ordinary hyperparameter tuning.
14. Read [Initial Research Memo](research/INITIAL_RESEARCH_MEMO.md) for first-pass findings and open questions.
15. Read [Thesis–Paper Map](research/THESIS_PAPER_MAP.md) for how candidate contributions may map to papers.
16. Read [Decision Log](research/DECISION_LOG.md) before revisiting previously assessed ideas.
17. Use [Session Handoff](SESSION_HANDOFF.md) when starting a new ChatGPT conversation.
18. Read [Communication Evolution Lane Screen](research/COMMUNICATION_EVOLUTION_LANE_SCREEN.md) before promoting any communication-protocol or topology idea.

## Non-negotiable research principles

- Treat the literature and experiments as evidence; do not treat any initial idea as proven.
- Do not import unrelated ideas or assumptions from other projects or previous conversations. Use this repository as the project context.
- Do not reject a direction merely because prior work exists. Identify the closest work, its limitations, and whether a meaningful, testable improvement remains.
- Do not call an idea novel until the closest related work has been checked.
- Distinguish verified facts, author claims, our interpretations, and open hypotheses.
- Prefer papers with inspectable methods, reproducible experiments, public code or datasets, and measurable outcomes.
- Keep evolutionary computation central to the research contribution, rather than merely using an EA as an interchangeable optimizer.
- Each proposed contribution must have a clear research question, closest baselines, falsifiable hypothesis, evaluation protocol, and failure criteria.
- Never fabricate citations, paper details, benchmark results, reproduction status, or repository changes.
- Update the status and decision log whenever a consequential decision is made.

## Intended deliverables

- A defensible thesis proposal and research plan.
- A literature map covering evolutionary algorithms, LLM-based agents, agent optimization/self-improvement, and relevant evaluation methodology.
- A thesis architecture with 2–3 connected contributions.
- For each contribution: a paper plan, baseline comparison, experiment plan, risks, and publication-readiness criteria.
- A durable trail of decisions, sources, experiment results, and handoffs.

## Current state

The first and second-pass literature maps are recorded, including a provisional capability-gap review. **No thesis topic, algorithm, benchmark, or innovation point has been approved yet.** The next task is a mechanism-level audit of the closest methods, not premature topic selection.

18. Use [Communication Evolution Lane Screen](research/COMMUNICATION_EVOLUTION_LANE_SCREEN.md) before promoting any communication-protocol or topology idea.
19. Read [Candidate H0 Reassessment](research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md) before reopening communication evolution; the current transfer/monitorability formulation did not pass its novelty gate.

19. Read [Candidate H0 Reassessment](research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md) before reopening communication evolution; the current transfer/monitorability formulation did not pass its novelty gate.
20. Read [Agent Skill/Workflow Generalization Lane Screen](research/AGENT_SKILL_GENERALIZATION_LANE_SCREEN.md) for the next exploratory lane; it is not an approved candidate.

20. Read [Agent Skill/Workflow Generalization Lane Screen](research/AGENT_SKILL_GENERALIZATION_LANE_SCREEN.md) for the next exploratory lane; it is not an approved candidate.
21. Read [Faithful Self-Evolvers Code Audit](research/FAITHFUL_SELF_EVOLVERS_CODE_AUDIT.md) for the source-code findings and limitations before using this work as a baseline.


## Latest research updates (2026-10-27)

- [Skill/generalization lane reassessment](research/AGENT_SKILL_LANE_REASSESSMENT.md): broad formulation downgraded after checking SkillComposer, Rep2Skill, MetaMem, Live-Evo, SelSkill, and Skill Following.
- [AMC direct code audit](research/AMC_CODE_AUDIT.md): records a potential particle/client aliasing issue in the current public main snapshot; verify before reproducing, and do not infer paper-result invalidity from code inspection alone.
- [Black-box agent test-time search lane](research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md): an exploratory candidate for state-validated trajectory recombination; no method or thesis innovation is approved.
- User constraint: communication evolution is excluded from the thesis candidate pool unless the user explicitly reopens it.

- [Trajectory-search second-pass audit](research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md): Candidate I0 did not pass as stated after SE-Agent, ToolTree, TTHE, TBETS, and classical plan-optimization overlap was added.
