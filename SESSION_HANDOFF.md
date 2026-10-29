# Session Handoff — Read This at the Start of Every New Chat

Copy the prompt below into a new ChatGPT conversation. The repository is the source of truth; do not assume the new conversation has access to prior chat history.

---

**Parameter tuning/control is mandatory:** explicitly separate Agent genotype, static EA hyperparameters, online control, variation-model settings, and task/evaluation settings. Use static HPO as a strong baseline before testing adaptive control. Do not reject a research line solely because it is crowded; use prior work as a basis for method improvement and fusion.

## Thesis-level correction (2026-10-27)

The user clarified that this is the **first step toward the master's thesis opening report**, not a request to implement one paper. Read `research/THESIS_PROPOSAL_FRAMEWORK.md` and `research/THESIS_PAPER_MAP.md` before continuing. OSLVC is a candidate core method only. Work toward one coherent umbrella problem with two core contributions and a possible third only if a distinct mechanism is found. Do not claim three innovations by splitting one method into components. Explicit EA parameter tuning/control is mandatory; communication evolution is excluded; this repository alone is the source of truth.

## Reusable continuation prompt

You are my research partner for a graduate thesis on **evolutionary computation applied to AI agents**. The repository is:

https://github.com/yujian777555/openissue

The immediate priority is the thesis proposal/opening report. The target is a coherent thesis with 2–3 substantive innovation points, aiming for 2–3 independently publishable small papers.

### Mandatory first steps

1. Read README.md, research/PROJECT_CHARTER.md, research/STATUS.md, research/LITERATURE_REVIEW.md, research/RELATED_WORK_MATRIX.md, research/CAPABILITY_GAP_REVIEW.md, research/EC_ROLE_AND_PARAMETER_CONTROL.md, research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md, research/TOOLMAZE_BENCHMARK_AUDIT.md, research/COEVOLUTION_CANDIDATE_AUDIT.md, research/META_EVOLUTION_CANDIDATE_AUDIT.md, research/TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md, research/COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md, research/EVOMAS_CODE_AUDIT_AND_PARENT_SELECTION_CANDIDATE.md, research/CANDIDATE_G_G0_REASSESSMENT.md, research/COMMUNICATION_EVOLUTION_LANE_SCREEN.md, research/COMMUNICATION_EVOLUTION_CANDIDATE_H_REASSESSMENT.md, research/AGENT_SKILL_GENERALIZATION_LANE_SCREEN.md, research/AGENT_SKILL_LANE_REASSESSMENT.md, research/FAITHFUL_SELF_EVOLVERS_CODE_AUDIT.md, research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md, research/AMC_CODE_AUDIT.md, research/INITIAL_RESEARCH_MEMO.md, research/THESIS_PAPER_MAP.md, and research/DECISION_LOG.md.
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

- Last substantive research commit reviewed: 9ae4440184369a8db56402b483c6d7a5f7429edf.

### Next concrete action

1. Read `research/EC_PARAMETER_CONTROL_FUSION_AUDIT.md`, the primary-source audit of ELMER and LVPG plus the verified scope of EvoMAS: Heuristics in the Loop.
2. Current candidate: **OSLVC (Operator-Specific Lineage-Value Control)**. Test whether calibration of realized behavior scale per operator, joint operator–scale selection, and downstream lineage credit improve Agent task success and held-out task-family generalization. This is not yet a novelty claim.
3. Fully audit EvoMAS: Heuristics in the Loop: full PDF, exact controller state/action/credit/update equations, and official code availability. If its method covers OSLVC, refine the mechanism rather than abandoning the whole direction.
4. Verify code/licensing/reproduction status for ELMER and LVPG. Audit EVOTOOL and official EvoMAS generation as candidate baselines.
5. Choose a reproducible Agent benchmark and structured representation after leakage/license checks. Define behavior displacement on training-only action/tool traces, then validate separate calibrations per operator.
6. Compare tuned static EA, classical AOS, self-adaptation, ELMER-style strength-only, LVPG-style lineage-only, EvoMAS strategy selection, and OSLVC. Main outcomes are task success and held-out task-family generalization; cost is secondary.
7. Do not start paid API experiments until method and benchmark gates pass. Use overlap to strengthen the method, not as an automatic reason to stop.

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


## Latest method-level research update (2026-10-27)

Read `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md` before continuing. The original OSLVC fusion (behavior scale + adaptive operator choice + lineage credit) is not enough as a novelty statement because ELMER, LVPG, classical AOS, and EvoMAS: Heuristics in the Loop cover substantial parts. The revised candidate tests whether operator continuation value should be conditioned on **realized behavior displacement**, estimated with matched parent/task/state comparisons. Required baselines now include AOS with diversity/parent-distance reward and a naive joint operator–strength controller with raw lineage return. The exact EvoMAS HIL credit/state mechanism and official code remain unverified; G0 is open. Do not implement yet; next close the full-paper/code/benchmark feasibility audit and prepare the opening-report gap matrix. Communication evolution remains excluded.


## Latest audit handoff (2026-10-27)

Read these first:
1. research/EVOMAS_HIL_METHOD_AUDIT_R1.md — official EvoMAS abstract-level mechanisms verified, exact reward/state/credit equations and final code/license not yet verified. G0 OPEN.
2. research/PROPOSAL_GAP_MATRIX_R1.md — proposal-ready closest-work matrix, falsifiable RQs, baseline ladder, parameter-tuning sequence, and benchmark split/rights risks.
3. research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md — current provisional mechanism candidate.

Key new finding: EvoTool is a strong MIT-licensed direct baseline with local offline evaluation, but its τ-bench demo builder chooses canonical test tasks before train/dev and then the runner randomly splits the selected pool. Do not use that demo split for final official test claims. The original τ-bench tasks are marked outdated; updated τ³-bench requires adapter work. BFCL is a possible controlled offline benchmark, but data terms and a family-held-out split remain open.

Do not implement the controller yet. Next: obtain a readable final EvoMAS PDF, audit exact strategy-selection/reward/lineage equations; verify selected data terms; lock family-held-out splits; then run a no-paid-call local smoke test. Current gate state: G0 OPEN, G1 PARTIAL/OPEN, G2 NOT RUN.


## New literature finding — two EvoMAS papers (2026-10-27)

Do not conflate:
- Wei et al., *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*, ICML 2026: seven-strategy portfolio, adaptive selection, role-level evolution, curriculum, reflective Cyber Creator. Exact reward/state equations remain unverified.
- Hu et al., *EvoMAS: Evolutionary Generation of Multi-Agent Systems*, ICML 2026: full HTML and official code audited; execution-feedback-conditioned mutation/crossover, task-relevance/performance-history selection, parent-relative reward acceptance, structured MAS configuration search, and cross-query experience memory. Official code is CC BY-NC 4.0.

Read research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md and research/PROPOSAL_GAP_MATRIX_R1.md. Generic feedback-guided mutation/crossover, memory, and adaptive operator portfolios are not new. The current candidate remains conditional lineage-value credit based on realized behavioral displacement. Do not implement until the remaining Wei HIL mechanism audit, benchmark data/split gate, and local baseline smoke gate are resolved.


## Latest action — EvoMAS HIL PDF access attempt (2026-10-27)

The official PMLR page verifies the ICML 2026 publication and abstract, but the linked PDF could not be parsed by the web reader and the direct download failed. The earlier anonymous OpenReview PDF now triggers a verification challenge. Therefore the full method audit is **still blocked**, not completed. G0 remains OPEN; do not claim the paper lacks displacement-conditioned lineage credit. Next step is to obtain a readable final PDF or verified author source, then compare the exact state/action/reward and ablations against OSLVC-R1, ELMER, LVPG, CWM, and classical AOS.




## Latest continuity update — 2026-10-29

**Read first:** `research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md`, `research/STATUS.md`, `research/DECISION_LOG.md`, `research/THESIS_PROPOSAL_FRAMEWORK.md`, `research/THESIS_PAPER_MAP.md`, `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`, and `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`.

### Current user goal
The user is preparing the **master's thesis opening report**, not asking to implement one paper immediately. The thesis should have 2–3 connected substantive contributions and aim for 2–3 small-paper submissions; evolutionary computation must be central and explicit EA parameter tuning/control must be considered. Communication evolution is excluded. Use this repository only; do not mix other project repositories.

### Current feasibility view
The last conversational estimates were: thesis completion 75–85%; OSLVC as the final effective algorithm 35–50%; 2–3 independent defensible innovation points 50–65%; 2–3 small-paper submissions 40–60%. These are subjective judgment ranges, not calibrated probabilities or experimental findings. Do not present them as measured results.

### Candidate method
OSLVC-R1 remains a **hypothesis**, not an approved innovation. Its narrow test is whether operator continuation value conditional on realized behavior displacement adds value beyond immediate reward, raw lineage return, displacement-only prediction, and a naive joint operator–strength controller. ELMER, LVPG, EvoMAS: Heuristics in the Loop, classical AOS, and EvoTool cover substantial adjacent mechanisms; the final EvoMAS HIL method audit is incomplete.

### Gate state
- **G0 OPEN:** verify the final EvoMAS HIL state/action/reward/credit/update mechanism from readable final paper/author source and compare closest methods.
- **G1 PARTIAL/OPEN:** lock benchmark version, license, task-family splits, task IDs, and scorer checks. Tool-Veritas is a local execution substrate, not a ready-made complete benchmark. τ²/τ³-bench is external validation only after exact task/split/scorer audit. Do not use the full frozen `text-v1` manifest as held-out after evolution on source-train tasks.
- **G2 NOT RUN:** no local mechanism pilot has run. No formal OSLVC experiment or paid API call has been performed.

### Next action
1. Finish the final-paper prior-art audit (G0).
2. Freeze a controlled task-family split and audited external validation subset (G1).
3. Only if G0/G1 are sufficiently closed, run a small no-paid-call pilot testing (a) operator/strength displacement heterogeneity and (b) whether conditional operator credit adds predictive value under matched parents/tasks/states and equal descendant-evaluation counts.
4. If the conditional residual is negligible or unstable, revise/drop OSLVC instead of defending it by name.
5. Draft the proposal's linked sections: related work → concrete gap → research questions → contents/candidate innovations → technical route → experiment feasibility → risks/alternatives.

Do not start large or paid experiments before the gates pass. Prefer two strong contributions over three weak/duplicated ones. Record only evidence-backed completion.




## Mandatory continuity rule — added 2026-10-29

Before doing research in a new conversation, read `CONTINUITY_PROTOCOL.md` and `NEXT_SESSION_PROMPT.md`, then verify the latest commits and read `research/STATUS.md`, `research/DECISION_LOG.md`, and the current research notes.

**At the end of every substantive session, the repository must be updated.** Update the relevant research artifact(s), status, decision log when a decision changes, this `SESSION_HANDOFF.md`, and `NEXT_SESSION_PROMPT.md`. Refresh the README link if the stage or workflow changes. Commit to the intended branch, fetch changed files, and verify the final commit and contents before telling the user the update succeeded. If no substantive research changed, keep the handoff accurate and say so; never fabricate an update, experiment, or test.

The reusable prompt in `NEXT_SESSION_PROMPT.md` is the copy/paste entry point for a new chat and must always reflect the latest confirmed stage, gate states, scope constraints, and next unfinished action. Do not require the user to remind you of this rule.



## Immediate next-session action — re-confirmed 2026-10-29

The latest check reconfirmed that the official PMLR final record for *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows* is public, but the linked final PDF is not extractable through the current reader and the linked OpenReview page is blocked by a browser-verification challenge. This is an access limitation, not evidence that the paper lacks a mechanism.

**Next session must:**
1. Make a bounded attempt to obtain the final PDF or a verified author-hosted copy.
2. If still blocked, conduct a clearly labelled **provisional preprint-only** audit of the accessible earlier manuscript (state/action/reward/credit/update equations/ablation), and keep G0 OPEN until final-version equivalence is verified.
3. Advance G1 in parallel: specify the controlled local task-family split, version/license manifest, exact task IDs, and scorer/oracle audit for an external validation subset.
4. Do not start G2 experiments or paid API calls before the method and benchmark gates are sufficiently closed.

Current gates remain G0 OPEN, G1 PARTIAL/OPEN, G2 NOT RUN. No formal experiment or paid API call was run in this session.



## Latest research result — 2026-10-29 (supersedes the prior retrieval-only handoff)

A provisional mechanism audit has now been completed from search-indexed sections of the earlier anonymous EvoMAS manuscript. This is a real literature-review result, but **not** a final-version audit. See research/EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md.

**What changed:** EvoMAS already covers adaptive strategy selection, historical strategy-performance credit, LLM-guided selection, reflective rule updates, graph edit distance for structural diversity, role evolution, and curriculum in the accessible earlier manuscript. Those broad mechanisms must not be claimed as novel. The narrower candidate remains whether *realized execution-trace behavior displacement* improves operator/strength continuation credit beyond raw lineage reward, immediate reward, structural distance, ELMER/LVPG, and classical AOS. The final ICML version could still contain an equivalent mechanism; G0 therefore remains OPEN.

**Current gates:** G0 OPEN; G1 PARTIAL/OPEN; G2 NOT RUN. No experiments, code reproduction, or paid API calls were started.

**Next session:**
1. Make one bounded attempt to obtain the final ICML PDF or a verified author copy; if still blocked, do not stall the thesis project.
2. Advance G1: freeze the controlled task-family split, exact task IDs, version/license manifest, goal-state oracle, scorer checks, and audited external validation subset.
3. Once G0/G1 are sufficiently closed, run only a small no-paid-call local pilot with matched parent/task/state probes and equal descendant-evaluation counts.
4. Reject or redesign OSLVC if displacement-conditioned credit does not add stable predictive and search value.
5. Keep the opening-report structure as the deliverable; do not turn this into a standalone implementation project prematurely.



## Latest substantive research note — 2026-10-29

The official PMLR abstract for *EvoMAS: Heuristics in the Loop* has now been rechecked. It explicitly covers a seven-strategy evolutionary portfolio, adaptive strategy selection, role-level evolution, curriculum-guided evolution, and a reflective Cyber Creator meta-controller. Therefore, do not claim these broad mechanisms as novel. The official PDF remains unextractable by the current reader, and OpenReview redirects to browser verification; exact reward/credit/update equations and displacement-conditioned lineage value remain unverified.

**Next action:** make one bounded attempt to obtain a readable final/author copy. If blocked, stop spending unlimited time on retrieval and proceed with G1 in parallel: define the controlled task-family split, pinned benchmark/version/license manifest, exact task IDs, goal-state oracle, scorer checks, and external validation subset. Keep G0 OPEN until final-version method equivalence is checked. G2 remains NOT RUN; no formal experiment or paid API call was started.

Details: `research/EVOMAS_HIL_METHOD_AUDIT_R1.md`; decision boundary: D-044 in `research/DECISION_LOG.md`.
