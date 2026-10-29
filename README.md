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


## Latest parameter-control direction (2026-10-27)

- [Joint operator–mutation-scale control candidate](research/EC_PARAMETER_CONTROL_FUSION_CANDIDATE.md): active exploratory plan for tuning the EA explicitly and improving/fusing ELMER, LVPG, adaptive operator selection, and EvoMAS strategy control. This is a hypothesis, not an approved novelty claim.
- [EC role and parameter control](research/EC_ROLE_AND_PARAMETER_CONTROL.md): separates Agent phenotype, static EA hyperparameters, online control, and evaluation settings.
- Research rule: prior-art overlap is not an automatic reason to abandon a direction; use it to define the exact mechanism improvement, baselines, and falsifiable tests.


## Thesis proposal framework (2026-10-27)

- [硕士毕业论文开题框架（候选版）](research/THESIS_PROPOSAL_FRAMEWORK.md): thesis-level umbrella problem, provisional title, connected research contents, parameter-tuning plan, experiment design, and opening-report outline.
- [Thesis–Paper Contribution Map](research/THESIS_PAPER_MAP.md): maps candidate Paper A/B and optional Paper C; no innovation claim is pre-approved.
- Project framing: the immediate deliverable is the thesis opening report, not a standalone OSLVC paper. OSLVC remains a candidate core method; two strong connected contributions are preferable to three weak or duplicated claims.


## Latest method-level candidate refinement (2026-10-27)

- [OSLVC-R1: Scale-Conditioned Lineage-Value Credit](research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md): revised, falsifiable candidate that tests whether operator credit should be conditioned on realized Agent behavior displacement when estimating lineage continuation value. This is a hypothesis, not an approved novelty claim.
- The next step is to finish the published EvoMAS: Heuristics in the Loop method audit and benchmark/license feasibility check. No implementation or paid experiment has started.


## Research update — source and benchmark feasibility audit (2026-10-27)

- [EvoMAS method audit R1](research/EVOMAS_HIL_METHOD_AUDIT_R1.md): official ICML/PMLR abstract verified; exact reward equations, final implementation, and displacement/lineage mechanism remain unverified because the full PDF could not be extracted in this session. Gate G0 remains OPEN.
- [Proposal-ready gap matrix R1](research/PROPOSAL_GAP_MATRIX_R1.md): closest-work matrix, falsifiable research questions, baseline ladder, parameter-tuning protocol, and benchmark/split risks.
- **Important benchmark caution:** the EvoTool reference code is MIT-licensed and offers offline execution, but its τ-bench demo builder selects canonical test tasks before train/dev and the runner then randomly partitions the demo subset. Do not treat that subset as an untouched official test set. The original τ-bench repository itself warns that its tasks are outdated.
- No experiment or paid API call has been started. The next gate is readable full-text EvoMAS audit plus a verified family-held-out benchmark split.


## Research update — disambiguate the two EvoMAS papers (2026-10-27)

Two distinct ICML 2026 papers share the name EvoMAS. Wei et al.'s *Heuristics in the Loop* covers seven strategies, adaptive selection, role evolution, curriculum, and Cyber Creator. Hu et al.'s *Evolutionary Generation of Multi-Agent Systems* covers structured MAS configuration evolution, execution-trace-conditioned single-component mutation, topology-inheriting crossover, reward-based pool updates, and cross-query experience memory.

New audit: research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md. Generic feedback-conditioned mutation/crossover, configuration evolution, and experience memory are not standalone innovation claims. The narrowed candidate remains realized-displacement-conditioned lineage-value credit.


## Latest benchmark and baseline audit (2026-10-27)

- [Benchmark and Baseline Decision R2](research/BENCHMARK_AND_BASELINE_DECISION_R2.md): source-level EvoTool audit, demo-split leakage risk, τ²/τ³-bench version/split considerations, BFCL quality caveat, and the falsification-first experiment protocol.
- Current decision: EvoTool is a direct baseline, not a novelty claim; τ²/τ³-bench is the leading realistic validation candidate pending split-overlap and adapter checks; OSLVC-R1 remains unapproved.




## Thesis feasibility and continuity update (2026-10-29)

- [Feasibility and Next Research Gate](research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md): current thesis-level feasibility assessment, subjective confidence ranges, OSLVC novelty boundaries, G0/G1/G2 status, benchmark guardrails, and next steps.
- Current stage: thesis opening report; no final topic, algorithm, or innovation point has been approved.
- OSLVC-R1 remains a falsifiable hypothesis. G0 (final EvoMAS HIL method audit) is OPEN; G1 (benchmark/split/scorer) is PARTIAL/OPEN; G2 (local mechanism pilot) has NOT RUN.
- The numerical feasibility ranges are subjective planning judgments, not calibrated probabilities or experimental results. No paid API experiment is authorized.
- Long-session continuation: read the feasibility note, `research/STATUS.md`, `research/DECISION_LOG.md`, and `SESSION_HANDOFF.md` first.




## Mandatory continuity and next-session handoff

**Every substantive research session must update this repository and leave a copyable next-session prompt.** This is a project rule, not an optional reminder.

- [Continuity Protocol](CONTINUITY_PROTOCOL.md): mandatory start-of-session, end-of-session, verification, and repository-update checklist.
- [Next-Session Prompt](NEXT_SESSION_PROMPT.md): copyable handoff prompt; refresh it at the end of every substantive session.
- [Session Handoff](SESSION_HANDOFF.md): detailed current context, decisions, gate states, and next actions.
- [Current Thesis Feasibility and Gates](research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md): thesis feasibility, current method hypothesis, benchmark constraints, and validation gates.

Every session must inspect the latest commits, read the current status and handoff, update the relevant research artifacts plus status/handoff/prompt, commit the changes, fetch the changed files, and verify the resulting commits before reporting success. If no new evidence emerged, preserve an accurate handoff and explicitly say no substantive research result changed. Never fabricate progress or claim an unverified write.



## Current research gate — 2026-10-29

Latest mechanism-level finding: the accessible earlier EvoMAS manuscript already covers broad adaptive strategy selection, history-based strategy credit, reflective meta-control, structural graph-distance diversity, role evolution, and curriculum. OSLVC is therefore narrowed to a falsifiable question about **realized execution-trace behavior displacement** and continuation-credit value; it is not yet an approved innovation. The final ICML version remains incompletely audited.

- [Provisional EvoMAS mechanism audit](research/EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md)
- [Current status and gates](research/STATUS.md)
- [Proposal gap matrix](research/PROPOSAL_GAP_MATRIX_R1.md)
- [Session handoff](SESSION_HANDOFF.md)
- [Next-session prompt](NEXT_SESSION_PROMPT.md)

## G1 benchmark and implementation status

See [G1 Task-Family Split Protocol R1](research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md) for the split design, benchmark caveats, and gate logic.

The first deterministic executor prototype is now present in [research/controlled_suite](research/controlled_suite/README.md):
- 22 in-memory mock tools across five isolated domains.
- 12 independently authored representative task cases, one per family.
- State-invariant and trace-constraint evaluator.
- 16 unit/smoke tests passed in GitHub Actions on Python 3.11.

The manifest still contains 120 planned IDs: 12 pilot cases are authored but not final, and 108 cases remain un-authored. This is not a completed benchmark or Agent experiment. G1 remains PARTIAL/OPEN; G2 has not started. GitHub Actions run `40866638479` passed on Python 3.11 with all 16 tests successful.



## Latest executor/oracle audit (2026-10-29)

The deterministic five-domain executor and 12 pilot cases already exist. The latest focused audit found and patched two evaluator correctness issues: repeated consumer argument propagation was under-checked, and Python boolean/integer equality could create false-positive invariants. See [Executor and Oracle Audit R1](research/controlled_suite/EXECUTOR_ORACLE_AUDIT_R1.md). The final test-patch CI run must be checked before treating the audit as verified. G1 remains PARTIAL/OPEN; the full 120-case suite and independent review are outstanding.


## G1 controlled-suite audit R2 — 2026-10-29

The deterministic controlled-suite prototype is implemented and under validity audit: five isolated mock domains, 22 tools, and 12 revised pilot cases. The planned 120-case manifest is not a completed benchmark; 108 cases remain unauthored.

- [Executor/oracle audit R2](research/controlled_suite/EXECUTOR_ORACLE_AUDIT_R2.md): budget/event accounting, per-tool idempotency, dynamic-ID-independent oracles, ordered call patterns, and side-effect checks.
- [Controlled-suite README](research/controlled_suite/README.md): implementation scope, test instructions, and status boundary.
- Executor implementation commit `14ac8634607094b720e3c96ad1bd9a786a9386f5` passed 29/29 tests; follow-up test commit `67f831cd605d0e8f70f9e53ec5db85c430c86e04` passed 31/31 tests in [CI run 40878796822](https://github.com/yujian777555/openissue/actions/runs/40878796822).

**Gate boundary:** G1 remains PARTIAL/OPEN; independent human review, family-template leakage review, prompt-builder allowlist testing, the remaining 108 cases, final hashes, and external scorer validation remain outstanding. G0 remains OPEN and G2 has not run. No Agent/evolution experiment or paid API call has been performed.
