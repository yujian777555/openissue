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
- Current method candidate: OSLVC-R1, scale-conditioned lineage-value credit. It remains a falsifiable hypothesis, not a confirmed novelty claim.
- Prior art already covers substantial ingredients: ELMER (behavior-grounded mutation scale), LVPG / The Time Value of Evolution (adaptive radius and lineage value), classical adaptive operator selection/self-adaptation, EvoTool (blame-aware targeted mutation and diversity-aware selection), and EvoMAS methods. Do not claim these ingredients alone as novel.
- G0 = OPEN: the final ICML/PMLR method of EvoMAS: Heuristics in the Loop has not been fully verified at state/action/reward/credit/update-equation level. Retrieval failure or abstract-level silence is not evidence of absence.
- G1a = design specified; G1b = PARTIAL/OPEN; G1c = NOT DONE; G1 overall = PARTIAL/OPEN. The local suite has five isolated mock domains, 22 deterministic tools, and 12 revised pilot cases. The 120-case manifest is planned, but 108 cases remain unauthored. Independent human review, family-template leakage audit, final hashes, and external adapter/scorer validation remain outstanding.
- Latest executor implementation commit: `14ac8634607094b720e3c96ad1bd9a786a9386f5`; latest test commit: `67f831cd605d0e8f70f9e53ec5db85c430c86e04`. GitHub Actions run `40878796822` passed **31/31 tests**. Read `research/controlled_suite/EXECUTOR_ORACLE_AUDIT_R2.md` for findings.
- R2 fixes: explicit budget-attempt/event accounting; strict integer budget validation; per-tool idempotency keys; type-safe oracle operators; ordered tool/status/argument trace constraints; dynamic-ID-independent booking/transfer/email oracles; side-effect guards; F10 prior-turn context; and explicit F07 state-only scoring limitation.
- G2 = NOT RUN: no local OSLVC mechanism pilot, formal Agent/evolution experiment, or paid API call has been performed.
- Benchmark guardrails: EvoTool is a direct baseline, but its bundled tau-bench demo split is smoke-test-only. Tool-Veritas is a local execution substrate, not a sufficient ready-made thesis benchmark. Tau2/tau3 is external validation only after exact task/split/scorer audit. Do not call the full frozen text-v1 manifest held-out after evolution on source-train tasks. Report goal-state completion separately from tool validity and conversational quality.
- Static EA tuning must precede adaptive-control claims. Required comparisons include tuned static EA, EvoTool or a faithful component-level baseline, classical AOS (including diversity/parent-distance credit), ELMER-style scale-only control, LVPG-style lineage-only control, and naive joint operator-strength control with raw lineage return.
- Subjective planning estimates recorded in the repository (not calibrated probabilities or empirical results): thesis completion 75–85%; OSLVC becoming the final effective method 35–50%; 2–3 independent defensible innovations 50–65%; 2–3 small-paper submissions 40–60%. Do not present these as measured facts.

MANDATORY FIRST TASK:
1. Read the latest `CONTINUITY_PROTOCOL.md`, `research/STATUS.md`, `research/DECISION_LOG.md`, `SESSION_HANDOFF.md`, this prompt, `research/controlled_suite/EXECUTOR_ORACLE_AUDIT_R2.md`, `research/controlled_suite/task_case_schema_r1.json`, `research/controlled_suite/pilot_cases_r1.jsonl`, and `research/controlled_suite/family_manifest_r1.json`.
2. Inspect recent commits and confirm the latest CI result before continuing.
3. Audit cross-family template leakage among the 12 pilot cases and compare task goals, state initialization, oracle invariants, trace constraints, and reference trajectories for accidental near-duplicates or overly revealing templates.
4. Define the future Agent-prompt allowlist and add an integration test proving that `initial_state`, `oracle`, split/family metadata, trace constraints, provenance, and reference actions are not serialized into the Agent prompt. The prompt builder does not exist yet, so do not claim this gate is passed.
5. After the leakage/prompt-boundary review, author the remaining 108 original cases while preserving the fixed whole-family split: train F01–F06, validation F07–F09, test F10–F12. Validate all cases against the schema and deterministic oracle, then freeze hashes.
6. Make at most one bounded attempt to obtain a readable final EvoMAS: Heuristics in the Loop paper or verified author copy. If blocked, keep G0 OPEN and proceed with G1; do not spend unlimited time retrying the same inaccessible route.
7. Do not start the controller, formal OSLVC experiment, or paid API experiment until G0/G1 are sufficiently closed. If the gates pass, run only a small no-paid-call local pilot with matched parent/task/state probes and equal descendant-evaluation counts. Revise/drop OSLVC if displacement-conditioned credit adds no stable predictive or search value.
8. At the end of substantive work, update the relevant research note, `research/STATUS.md`, `research/DECISION_LOG.md` if needed, `SESSION_HANDOFF.md`, and this prompt. Commit to `main`, re-fetch changed files, verify the commit and CI, and report exact paths/SHA.

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



## Latest verified research handoff — 2026-10-29 (supersedes prior retrieval-only state)

The latest substantive result is recorded in research/EVOMAS_HIL_PROVISIONAL_MECHANISM_AUDIT_2026-10-29.md. A bounded attempt to retrieve the final ICML/PMLR PDF still failed: the official publication record and abstract are accessible, but the final PDF is not extractable through the current reader and OpenReview redirects to a browser-verification challenge. The search index exposed substantial sections of the earlier anonymous manuscript, which have been audited **provisionally only**. Do not present those details as verified final-version claims.

**Provisional prior-art findings from the earlier manuscript:** EvoMAS already covers a multi-operator portfolio, adaptive strategy selection, history-based strategy credit, LLM-guided multi-criteria candidate selection, reflective rule induction/pruning, structural graph edit distance, role evolution, and curriculum. Do not claim these broad mechanisms as new. The only OSLVC-R1 hypothesis worth testing is whether realized behavior displacement measured from executed Agent/tool traces adds incremental continuation-credit value beyond immediate reward, raw lineage return, structural distance, ELMER/LVPG-style controls, classical AOS, and an EvoMAS-like reflective controller. This remains a falsifiable hypothesis, not a novelty certification.

**Current gates:** G0 OPEN (final ICML equations/ablations unverified); G1 PARTIAL/OPEN (family-held-out split, exact task IDs, license/version manifest, oracle/scorer audit not locked); G2 NOT RUN (no formal experiment, code reproduction, or paid API call).

**MANDATORY NEXT ACTIONS:**
1. Make one bounded attempt to obtain the final ICML PDF or a verified author-hosted copy; if still blocked, do not stall the thesis project or infer absence of a mechanism.
2. Advance G1: lock the controlled local task-family split, exact task IDs, version/license manifest, goal-state oracle, scorer checks, and an audited external validation subset. Use the current benchmark decision file as the starting point.
3. Do not start the formal G2 pilot or paid API calls until G0/G1 are sufficiently closed.
4. Once gates permit, run a small no-paid-call pilot with matched parent/task/state probes and equal descendant-evaluation counts. Drop/revise OSLVC if displacement-conditioned credit adds no stable prediction or search value.
5. At the end of every substantive session, update the relevant audit, research/STATUS.md, research/DECISION_LOG.md when decisions change, SESSION_HANDOFF.md, this prompt, and README if workflow/status changed; commit and re-fetch changed files to verify remote content.

The immediate deliverable remains the master's thesis opening report, not a standalone implementation project. Keep all work in yujian777555/openissue; do not mix unrelated repositories. Communication evolution remains excluded. Prefer two defensible connected contributions over three weak or duplicated claims.



## EvoMAS public-record audit update — 2026-10-29

The official PMLR ICML 2026 abstract explicitly covers a seven-strategy evolutionary portfolio, adaptive strategy selection, role-level evolution, curriculum-guided evolution, and the reflective Cyber Creator meta-controller. Do not claim those broad mechanisms as novel. The official PDF is still not extractable by the current reader; OpenReview redirects to a browser-verification challenge. Exact state/action/reward/credit/update equations and displacement-conditioned lineage value remain unverified, so G0 is still OPEN. Abstract silence is not proof of absence.

**Next session:**
1. Make one bounded attempt to obtain a readable final/verified author copy.
2. If still blocked, do not spend unlimited time on retrieval: label any older manuscript analysis preprint-only, keep G0 OPEN, and proceed with G1 in parallel.
3. Advance the controlled task-family split, pinned benchmark/version/license manifest, exact task IDs, goal-state oracle, scorer checks, and audited external validation subset.
4. No formal experiment or paid API call before G0/G1 are sufficiently closed.
5. End with repository updates and remote verification under `CONTINUITY_PROTOCOL.md`.

Detailed audit: `research/EVOMAS_HIL_METHOD_AUDIT_R1.md`; decision D-044 in `research/DECISION_LOG.md`.



## Latest G1 protocol update — 2026-10-29

Read `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md` before continuing.

**Primary controlled suite design:** 120 original deterministic tasks across five mock domains and twelve global task families, two variants each. Whole-family split: train F01–F06 = 60 tasks; validation F07–F09 = 30; test F10–F12 = 30. These task artifacts are not authored yet; do not claim the benchmark is complete. Tool-Veritas's bundled 70 cases lack family labels/splits and are not the thesis benchmark; original task content should be authored from scratch.

**Pinned external candidate:** tau2-bench v2.0.0 commit `989d3285ae669e49503324bdb9981bf14fccedeb`; exact source test IDs for airline (20) and retail (40) are in the protocol. This is a custom source-test evaluation, not official `text-v1` leaderboard scoring. Audit DB/state and judge-based reward components separately.

**New candidate to audit, not yet selected:** Delta tau benchmark (arXiv:2610.34238, posted 2026-10-25), 1,588 tasks, 42 domains, six tool ecosystem versions, 1,191 train / 397 test. Code repo says MIT, but separately hosted dataset's exact license/revision/checksum and task-family leakage are unverified. Audit these briefly; do not let it cause scope drift.

**Gate states:** G0 OPEN; G1a design provisionally specified; G1b task artifacts/oracle tests/hash NOT DONE; G1c external adapter/scorer and Delta tau decision NOT DONE; G1 overall PARTIAL/OPEN; G2 NOT RUN. No tasks were generated/executed, no adapter smoke test, and no model/API experiment was run in the latest design round.

**Next concrete action:** (1) inspect Delta tau dataset license/revision/checksum and train/test family-overlap evidence; (2) explicitly select or defer it; (3) implement the original task schema and deterministic oracle tests, then generate the 120-case manifest. Do not start formal OSLVC experiments or paid API calls before gates pass. At session end, update all continuity files and verify remote commits per `CONTINUITY_PROTOCOL.md`.



## Latest τ² task-family leakage warning (2026-10-29)

A heuristic word-level TF-IDF screen over pinned tau2-bench v2.0.0 source tasks found nearest-train cosine ≥0.45 for 4/20 airline test tasks and 17/40 retail test tasks. Examples: retail 94↔93 (1.000), 32↔31 (0.968), 62↔63 (0.963), airline 16↔15 (0.695). These are screening signals, not ground-truth duplicate labels; manual semantic/schema review is needed. Do not describe the τ² source train/test split as family-held-out. The primary family-held-out evidence must come from the custom 120-task suite. See `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`.

Next: (1) boundedly verify Δτ dataset license/revision/checksums and split structure, then explicitly select or defer it; (2) create the original task schema and deterministic oracle unit tests; (3) author/hash the planned family manifest and case suite. G1 remains PARTIAL/OPEN; no task suite or experiment has run.

## Δτ-Bench decision and next G1 action (2026-10-29)

The code repo for Δτ-Bench states MIT, but the executable dataset is hosted separately. Attempts to read its Hugging Face page/metadata/card failed; exact dataset license, revision, checksum, and family overlap remain unverified. Defer it as a selected benchmark; do not repeatedly retry the same URL. Keep it in related work. τ²/τ³-bench v2.0.0 remains the external candidate, but the heuristic similarity screen means its source split is not family-held-out. See `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md` and decisions D-046/D-047.

**Next concrete action:** implement the original task schema and machine-readable 12-family manifest, add deterministic state-transition/oracle tests, then generate original task cases. G1 remains PARTIAL/OPEN; no tasks have been authored or run and no model/API experiment occurred.

## Latest state: deterministic suite prototype exists (2026-10-29)

Continue only in `yujian777555/openissue`. Read `CONTINUITY_PROTOCOL.md`, `research/STATUS.md`, `research/DECISION_LOG.md`, `SESSION_HANDOFF.md`, and `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md` first.

### Implemented
- `research/controlled_suite/world_r1.py`: 22 in-memory tools in five isolated domains, argument validation, atomic state transitions, idempotency replay/conflict protection, structured event trace, state oracle, trace constraints.
- `research/controlled_suite/pilot_cases_r1.jsonl`: 12 independently authored representative cases (one per family; 6 train / 3 validation / 3 test).
- `research/controlled_suite/test_world_r1.py`: 14 local unit/smoke tests passed.
- `research/controlled_suite/task_case_schema_r1.json`: now includes trace-constraint schema.
- `research/controlled_suite/family_manifest_r1.json`: 120 unique planned IDs, 12 marked `pilot_case_authored_not_final`, 108 remain `planned_not_authored`.
- `research/controlled_suite/README.md` and `.github/workflows/controlled-suite-smoke.yml`.

### Do not overclaim
The 16/16 result is a software smoke test, not an Agent capability result or evidence for OSLVC. All tools are synthetic/in-memory. No real API or paid call occurred. Latest GitHub Actions run `40866638479` on commit `8e4d8f721ba4a8232e7090d6d9493b3d6c7d5f3f` passed; the job log confirms 16 tests ran and `OK` on Python 3.11. G1 remains PARTIAL/OPEN; G2 NOT RUN.

### Next tasks, in order
1. Independently review the 12 pilot cases, expected state invariants, trace constraints, and the tool implementation for correctness.
2. Add adversarial tests for atomicity, idempotency key conflicts/replay, invalid tool schemas, and trace-evaluator edge cases.
3. Author the remaining 108 task cases without changing family-to-split assignment; test every case against the schema and deterministic oracle.
4. Conduct family-template leakage review, pin final data hashes, and only then close G1b.
5. Complete external benchmark adapter/scorer verification (tau2-bench v2.0.0 remains the external candidate; do not call its source split family-held-out). Δτ-Bench stays deferred until dataset license/revision/checksum and family overlap are verifiable.
6. Do not start G2 or any paid API experiment until the gates are explicitly passed.



## Latest verified session result — per-case adversarial validation (2026-10-29)

Latest test commit: `67f831cd605d0e8f70f9e53ec5db85c430c86e04`. GitHub Actions run [40878796822](https://github.com/yujian777555/openissue/actions/runs/40878796822) passed **31/31 tests**.

The R2 executor/oracle audit corrected budget/event accounting, per-tool idempotency scope, JSON-safe oracle operators, generated-ID-independent booking/transfer/email scoring, exact ordered call patterns, and unrequested side-effect checks. A new aggregate test rejects one plausible near-miss for each pilot case F01–F12; another test verifies the 120-ID manifest, split counts 60/30/30, and pilot assignment consistency.

This is programmatic discriminability evidence, not exhaustive soundness or independent human review. G1 remains PARTIAL/OPEN: 12 revised pilot cases exist and 108 remain unauthored; family-template leakage, actual prompt-builder allowlisting, final hashes, and external adapter/scorer audit remain open. The actual Agent prompt builder does not yet exist, so metadata non-leakage is not verified. G0 remains OPEN; G2 remains NOT RUN. No model/evolution experiment or paid API call occurred.

**Next session:** audit family-template leakage, define and test the prompt-builder allowlist, then author the remaining 108 cases without changing the whole-family split. Keep all work in `yujian777555/openissue`.
