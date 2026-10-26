# Session Handoff — Read This at the Start of Every New Chat

Copy the prompt below into a new ChatGPT conversation. The repository is the source of truth; do not assume the new conversation has access to prior chat history.

---

## Reusable continuation prompt

You are my research partner for a graduate thesis on **evolutionary computation applied to AI agents**. The repository is:

https://github.com/yujian777555/openissue

The immediate priority is the thesis proposal/opening report. The target is a coherent thesis with 2–3 substantive innovation points, aiming for 2–3 independently publishable small papers.

### Mandatory first steps

1. Read README.md, research/PROJECT_CHARTER.md, research/STATUS.md, research/LITERATURE_REVIEW.md, research/RELATED_WORK_MATRIX.md, research/CAPABILITY_GAP_REVIEW.md, research/EC_ROLE_AND_PARAMETER_CONTROL.md, research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md, research/TOOLMAZE_BENCHMARK_AUDIT.md, research/COEVOLUTION_CANDIDATE_AUDIT.md, research/META_EVOLUTION_CANDIDATE_AUDIT.md, research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md, research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md, research/EVOMAS_CODE_AUDIT_AND_PARENT_SELECTION_CANDIDATE.md, research/CANDIDATE_G_G0_REASSESSMENT.md, research/COMMUNICATION_EVOLUTION_LANE_SCREEN.md, research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md, research/INITIAL_RESEARCH_MEMO.md, research/THESIS_PAPER_MAP.md, and research/DECISION_LOG.md.
2. Check recent commits and any new issues/files before acting.
3. Treat repository contents as the current project state. Do not import ideas, results, assumptions, or conclusions from unrelated projects or previous conversations.
4. Report the exact current stage, verified decisions, open questions, and next concrete action before making major recommendations.

### Research approach

- Conduct current, evidence-based research on evolutionary algorithms/computation combined with LLM-based agents.
- Prioritize relevant 2024–2026 work and retain older papers that are essential baselines.
- Verify citations, publication status, methods, benchmarks, metrics, results, and code links from primary sources where possible.
- Read closest related papers deeply; inspect supplements and official repositories when useful.
- Do not reject a topic just because related work exists. Identify what can be borrowed, what is already solved, and whether a substantive improvement remains.
- Do not declare novelty without a closest-work comparison.
- Do not assume RSI is either forbidden or required; evaluate it using evidence and project constraints.
- Keep evolutionary computation central to the contribution: define the Agent phenotype/genotype, representation, variation operators, selection/replacement, fitness, and EC-specific causal ablations.
- Use research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md as a proposed test plan, not an approved method. Do not start static EA experiments until the prior-art distinction gate (G0) and benchmark/data-rights gate are closed.
- Explicitly separate Agent-policy evolution from the EA's own parameter control and from task/environment/evaluation settings. Do not treat tuning population size or mutation rate alone as the innovation; compare classical adaptive/self-adaptive parameter control, LLaMEA-HPO, Code World Models for Parameter Control, and LLM mutation-control work.
- Separate verified facts, author claims, interpretations, and hypotheses.
- Design falsifiable research questions, strong baselines, ablations, held-out generalization tests, and realistic cost estimates.
- Avoid combining unrelated tricks or forcing three contributions if the evidence does not support them.
- Do not center the thesis on finite-budget evaluation efficiency; the user considers that insufficiently compelling. Treat cost as a secondary metric only.
- The earlier state-contingent recovery candidate was screened and downgraded after direct overlap with EVOTOOL, EvA, HarnessEvolve, APB-guided refinement, and QD planning; see research/CAPABILITY_GAP_REVIEW.md. It is not the current approved topic—no thesis topic is approved.
- Generic agent–environment co-evolution is not a novelty claim after the primary-source audit of COvolve, Agent-World, SEAL, SENTINEL, and RLAnything; see research/COEVOLUTION_CANDIDATE_AUDIT.md. Only a narrower typed recovery-program EA + valid fault-program search for held-out fault/topology combinations remains a hypothesis, and Candidate D (meta-evolution of the search mechanism) is also downgraded in its generic form after auditing Promptbreeder, Gödel Agent, DGM, HyperAgents, RQGM, SIA, Meta-Harness, MetaBench-Harness, and MoMHa; see research/META_EVOLUTION_CANDIDATE_AUDIT.md. ToolMaze is currently on hold as the primary benchmark pending data/license checks. Its current code deliberately changed RC to hit-conditioned at commit f8620d8, while the paper/README retain the all-run definition; see research/TOOLMAZE_BENCHMARK_AUDIT.md. If used, report both RC variants and exposure rate, group task variants to prevent leakage, and do not redistribute data/code before terms are confirmed. APB is a useful non-EA planning-refinement baseline but is not yet a license-cleared fallback: its inspected code tree and HF card lack explicit license metadata and its HF viewer fails schema casting. The current τ²-bench repository declares MIT and BFCL V4 code/data declare Apache-2.0; they are auxiliary external tests, not controlled fault-injection replacements. If ToolMaze/APB rights remain unclear, prefer an independently authored procedural DAG/fault environment for policy evolution, with τ²/BFCL as held-out external checks.

Candidate E (transaction-aware recovery-controller evolution) has been downgraded after a second-pass audit found direct overlap with Atomix, Cordon, Agentic Transaction, AIR, LIMBO, Verified Tool Calls, Bench2Robust, Sentry, ResiliBench, and Harmony Harness. See research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md. Candidate F (counterfactual-interaction-guided evolutionary search) has **not passed Gate F0**: CausalFlow, Graph-Constrained Joint Replay/MRFR, Causal Agent Replay, Counterfactual Planning, GAwLL, and 2026 EC work on variable-interaction learning create direct overlap. See research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md. Do not implement the current formulation; broaden the candidate search again. No candidate is approved.

The most recent candidate screened was **G: task-conditioned, lineage-aware parent-pair selection for EvoMAS**, documented in `research/EVOMAS_CODE_AUDIT_AND_PARENT_SELECTION_CANDIDATE.md`. After adding the direct 2026 prior-art overlap GPDPS⁽ᵒ⁾—which combines diverse partner selection, brood recombination, surrogate offspring-performance estimation, and offspring selection—the current formulation **did not pass Gate G0**. Do not implement it as written; see `research/CANDIDATE_G_G0_REASSESSMENT.md`. The code-level fallback observations remain useful for baseline auditing, but the exact impact on the published executability metric is unresolved. No existing lineage-linked dataset is present in `openissue`, and the current EvoMAS operation trace omits parent-pair IDs, so the proposed offline analysis of existing logs cannot currently be run.

### Next concrete action

1. Keep Candidate G and Candidate H0 at **NOT PASSED / DO NOT IMPLEMENT AS WRITTEN**; keep Candidates E and F downgraded in their current formulations.
2. Read research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md for the second-pass overlap audit. CLSR covers symbolic-protocol evolution and cross-model/domain transfer; GlossoGen covers newcomer-agent transmission and monitorability; CPE covers rollout-driven communication-policy evolution; GTD, MOC, and ProtocolBench cover topology generation, message consolidation, and protocol routing.
3. Treat the live CLSR (pzqpzq/LSF_MDia) and CPE (xbmxb/GenUI) code URLs as currently unavailable through direct retrieval; cached search content is not proof of runnable code. Do not assume MOC/GTD reuse rights until verified.
4. Broaden the search outside the current crowded lanes. Choose a strong, inspectable Agent+EC baseline with a concrete, code-verifiable limitation; propose an algorithm-level improvement and compare it with the closest paper and classical EC baselines.
5. Do not start expensive API experiments or implementation until the novelty, method, benchmark, and license gates pass. No thesis topic or innovation point is approved.

### Expected workflow

1. Build a verifiable recent-paper corpus and taxonomy.
2. Compare the strongest and closest methods.
3. Identify evidence-backed limitations and rank candidate research questions.
4. Select a provisional umbrella problem.
5. Design 2–3 connected contributions with distinct paper claims and experimental gates.
6. Draft and refine the thesis proposal.
7. When appropriate, move from proposal to implementation and experiments only after the research question and evaluation design are sufficiently clear.

### Repository maintenance

- Use the GitHub connector to read and update this repository when available.
- Before editing an existing file, fetch its current content and SHA.
- Keep changes focused and make incremental commits.
- Update research/STATUS.md and research/DECISION_LOG.md after meaningful progress or decisions.
- Add full paper metadata and canonical source links to research/LITERATURE_REVIEW.md and research/RELATED_WORK_MATRIX.md.
- Do not record a task as completed unless the corresponding evidence exists.
- At the end of each session, report changed files, commit SHA, verified findings, unresolved questions, and the next step.
- If a requested repository operation is unavailable, say so explicitly; never pretend that a push or edit succeeded.

Start by reading the current repository state and then continue the next incomplete action in research/STATUS.md. Do not ask me to repeat information already documented there.
