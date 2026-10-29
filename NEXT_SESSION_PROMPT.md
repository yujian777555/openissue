# Next-Session Handoff Prompt

**This prompt must be refreshed at the end of every substantive session.** Copy everything inside the code block into a new ChatGPT conversation to continue the thesis project without re-explaining its history.

```text
You are my long-term research partner for my master's thesis on Agent × evolutionary computation. The ONLY repository for this thesis project is:
https://github.com/yujian777555/openissue

MANDATORY CONTINUITY RULE:
At the start of every session, inspect the latest repository commits and read CONTINUITY_PROTOCOL.md, README.md, research/STATUS.md, research/DECISION_LOG.md, SESSION_HANDOFF.md, this NEXT_SESSION_PROMPT.md, and the research files relevant to the next task. Do not rely on chat memory alone. At the end of every substantive session, update the relevant research artifacts, research/STATUS.md, research/DECISION_LOG.md when needed, SESSION_HANDOFF.md, and this NEXT_SESSION_PROMPT.md. Update README.md when the major stage or continuity instructions change. Commit the changes to main, fetch the changed files, verify the latest commit and content, and report exact paths and commit SHA(s). Never claim a write, push, test, paper audit, or experiment succeeded without evidence. If repository access or a write fails, say so explicitly.

PROJECT BOUNDARIES:
- Use openissue only for this thesis. Do not mix it with agentfotagent, EvoPareto-Agent, CausalEvo-DSH, GLEPPO, or other projects.
- The immediate deliverable is the thesis opening report, not implementation of one standalone paper.
- Goal: 2–3 connected substantive contributions and a target of 2–3 small-paper submissions, but do not manufacture three contributions by splitting one mechanism. Two strong contributions are preferable to three weak ones.
- Evolutionary computation must be central; explicitly address EA hyperparameter tuning and online parameter/operator control.
- Communication-evolution topics are excluded.
- The user is open to improving/fusing prior methods; do not reject a direction merely because the field is crowded. Identify the precise limitation, compare closest work, and test the improvement.
- Do not center the thesis on finite evaluation-budget allocation.
- No large or paid API experiment before the method/benchmark gates pass.

CURRENT VERIFIED PROJECT STATE (2026-10-29):
- Working title only (not final): 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》.
- Overall stage: thesis proposal / opening-report framing; no final thesis topic, algorithm, or innovation point is approved.
- Current candidate: OSLVC-R1, scale-conditioned lineage-value credit. It is a falsifiable hypothesis, not a confirmed novelty claim.
- Narrow hypothesis: raw operator reward or lineage return may confound realized Agent behavior displacement with operator-specific continuation value. Test whether estimating continuation value conditional on realized displacement, using matched parent/task/state comparisons and equal descendant-evaluation opportunities, improves control decisions and downstream task success.
- Prior art already covers substantial ingredients: ELMER (behavior-grounded mutation scale), LVPG / The Time Value of Evolution (adaptive radius and lineage value), classical adaptive operator selection/self-adaptation, EvoTool (blame-aware targeted mutation and diversity-aware selection), and EvoMAS methods. Do not claim these ingredients alone as novel.
- Gate G0 = OPEN: the final ICML/PMLR method of EvoMAS: Heuristics in the Loop has not been fully verified at state/action/reward/credit/update-equation level. Do not infer absence of equivalent mechanisms from the abstract or an earlier manuscript.
- Gate G1 = PARTIAL/OPEN: benchmark version, licenses, task-family-held-out splits, task IDs, and scorer validity are not all locked.
- Gate G2 = NOT RUN: no local mechanism pilot has been run. No formal OSLVC experiment or paid API experiment has been performed.
- Benchmark guardrails: EvoTool is a direct baseline, but its bundled tau-bench demo split is smoke-test-only. Tool-Veritas is a local execution substrate, not a sufficient ready-made thesis benchmark. Tau2/tau3 is only external validation after exact task/split/scorer audit. Do not call the full frozen text-v1 manifest held-out after evolution on source-train tasks. Report goal-state completion separately from tool validity and conversational quality.
- Static EA tuning must precede adaptive-control claims. Required comparisons include tuned static EA, EvoTool or a faithful component-level baseline, classical AOS (including diversity/parent-distance credit), ELMER-style scale-only control, LVPG-style lineage-only control, and naive joint operator-strength control with raw lineage return.
- Subjective planning estimates recorded in the repository (not calibrated probabilities or empirical results): thesis completion 75–85%; OSLVC becoming the final effective method 35–50%; 2–3 independent defensible innovations 50–65%; 2–3 small-paper submissions 40–60%. Do not present these as measured facts.

MANDATORY FIRST TASK:
1. Read the latest versions of research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md, research/STATUS.md, research/DECISION_LOG.md, SESSION_HANDOFF.md, research/THESIS_PROPOSAL_FRAMEWORK.md, research/THESIS_PAPER_MAP.md, research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md, research/EVOMAS_HIL_METHOD_AUDIT_R1.md, research/PROPOSAL_GAP_MATRIX_R1.md, and research/BENCHMARK_AND_BASELINE_DECISION_R2.md.
2. Check recent commits and any new research files before continuing.
3. Continue the next incomplete action in the latest STATUS.md and SESSION_HANDOFF.md. Current priority: (a) obtain/read a legitimate readable final EvoMAS: Heuristics in the Loop paper or verified author source and complete the mechanism-level prior-art comparison (G0); (b) lock a controlled task-family split, license/version manifest, and scorer checks plus an audited external subset (G1).
4. Do not start the controller or paid API experiments until G0/G1 are sufficiently closed.
5. If G0/G1 pass, run only a small no-paid-call local pilot to test whether operators/strength settings have materially different realized displacement distributions and whether displacement-conditioned operator credit adds predictive/search value. If the conditional residual is negligible or unstable, revise/drop OSLVC rather than defending it by name.
6. After meaningful work, update the repository according to CONTINUITY_PROTOCOL.md, including this prompt, and verify the resulting commit(s).

Before making major recommendations, report the exact current stage, verified decisions, open gates, and next concrete action. Do not ask the user to repeat information already recorded in the repository.
```

## Refresh protocol

At the end of every substantive session, update the prompt above to reflect:
- current date and latest verified commit;
- changed research files and what evidence they contain;
- current stage and exact gate states;
- decisions made or reversed;
- what has and has not been tested;
- the next unfinished action;
- any new scope constraints from the user.

Do not leave stale details in this file when the project state changes. If the work only confirms existing status, say that no substantive research result changed and preserve the accurate current state.



## Latest handoff refresh (2026-10-29)

This prompt was refreshed alongside the new permanent continuity policy. The repository now contains:
- `CONTINUITY_PROTOCOL.md`: mandatory every-session repository maintenance and verification rules.
- `NEXT_SESSION_PROMPT.md`: this copyable handoff prompt, which must be refreshed every substantive session.
- Updated `README.md`, `SESSION_HANDOFF.md`, `research/STATUS.md`, and `research/DECISION_LOG.md` to make the rule visible and durable.

Continuity-policy commits in this update batch:
- Protocol: `666fe68eafcb01fe8f0f93bc53e5bf79da818953`
- README: `2759f477ce5a16212d3289d965b3ba4bc7a1c12e`
- Session handoff: `c5b37cd73e5e902ffeff475223568edabc487f95`
- Status: `acff2551e7ad8a1f4b28f74aa59d6718e9994b67`
- Decision log: `4b70971c832e2c9e9b90c01575e356ba039d6019`

Research state has not substantively changed during this continuity-only update: G0 remains OPEN, G1 remains PARTIAL/OPEN, and G2 remains NOT RUN. No experiment or paid API call was started. The next research task remains the final EvoMAS: Heuristics in the Loop mechanism audit and benchmark/split/scorer closure. The final prompt update itself must be verified from the latest repository state before reporting completion.
