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
10. Read [Transactional Agent Robustness Candidate Audit](research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md) before promoting transaction-aware recovery-controller evolution.
11. Read [Counterfactual Evolution Candidate Audit](research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md) before promoting counterfactual-evidence-guided evolutionary search.
12. Read [EC Role and Parameter Control](research/EC_ROLE_AND_PARAMETER_CONTROL.md) for the distinction between Agent-policy evolution, EA parameter control, and ordinary hyperparameter tuning.
13. Read [Initial Research Memo](research/INITIAL_RESEARCH_MEMO.md) for first-pass findings and open questions.
14. Read [Thesis–Paper Map](research/THESIS_PAPER_MAP.md) for how candidate contributions may map to papers.
15. Read [Decision Log](research/DECISION_LOG.md) before revisiting previously assessed ideas.
16. Use [Session Handoff](SESSION_HANDOFF.md) when starting a new ChatGPT conversation.

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
