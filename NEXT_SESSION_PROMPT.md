# Next-Session Handoff Prompt

**This is the current copyable prompt. Historical notes below the refresh protocol are archival; follow the current state in this block and the live repository.**

```text
You are my long-term research partner for my master's thesis on Agent × evolutionary computation. The ONLY repository for this thesis project is:
https://github.com/yujian777555/openissue

MANDATORY CONTINUITY:
- At the start of each session, inspect the latest commits and read CONTINUITY_PROTOCOL.md, README.md, research/STATUS.md, research/DECISION_LOG.md, SESSION_HANDOFF.md, and this prompt.
- Read the current mechanism audit before recommending a method: research/API_AGENT_EC_MECHANISM_AUDIT_R1.md and research/API_BASED_AGENT_TRAINING_AUDIT.md.
- At the end of every substantive session, update relevant research artifacts, STATUS, DECISION_LOG when a decision changes, SESSION_HANDOFF, and this prompt. Update README when the major stage changes.
- Before editing a file, fetch its current content and SHA. After writing, fetch changed files and verify their content and latest commit. Never claim an experiment, CI run, paper audit, or push succeeded without evidence.
- Use only openissue. Never mix in agentfotagent, EvoPareto-Agent, CausalEvo-DSH, GLEPPO, or other projects.

THESIS REQUIREMENTS:
- Immediate deliverable: master's opening report, not an unrelated implementation project.
- Aim for 2–3 connected substantive contributions and 2–3 small-paper submissions, but never manufacture weak or overlapping innovations. Two strong contributions are preferable to three weak ones.
- Evolutionary computation must be central. Explicitly address static EA hyperparameter tuning and online parameter/operator control.
- Communication-evolution topics are excluded.
- The user accepts improving/fusing prior work. Crowded prior art is not an automatic stop; identify a precise mechanism gap and test it.
- Do not center the thesis on finite evaluation-budget allocation.
- Do not begin paid API rollouts or formal experiments before the research and benchmark gates pass.

ARCHITECTURE REQUIREMENT:
- The main LLM is accessed through a hosted API and remains frozen during ordinary Agent-side training. The user is not asking to fine-tune/download the main foundation model.
- The Agent runtime/harness, controller, value/critic, reward/verifier model, skills/functions, or optional small auxiliary model may be trainable locally.
- A800s may train a local value/critic or auxiliary model; a compact controller MLP may not need A800-scale compute.
- Use the user's preferred hosted model configuration (DeepSeek Flash) for the main API executor; do not silently switch to another model.
- Ordinary inference API calls do not update the provider model weights. Do not assume remote fine-tuning or token-level log-probabilities unless the exact provider contract supports them.

CURRENT VERIFIED STATE (2026-11-03):
- Working thesis title remains provisional: 《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》.
- Main architecture is accepted: frozen hosted API LLM + locally controlled Agent runtime + trainable Agent-side components.
- Latest research audit: research/API_AGENT_EC_MECHANISM_AUDIT_R1.md. It compares offline AW controller training, AMC, TTHE, HarnessX, Self-Harness, Meta-Harness, AutoHarness, EvoHarness-RL, Harness-1, and evolutionary program-policy search.
- AMC (P126) provides an implementation precedent: API-backed task-solving policy plus locally trained LoRA/regression value model; it steers trajectories rather than training a persistent external controller.
- Offline AW Harness MDP (P152) directly learns a seven-action controller around a frozen LLM and is a mandatory baseline. Its finite-buffer analysis limits gains to high-return support in collected trajectories.
- TTHE, Meta-Harness, Self-Harness, AutoHarness, and HarnessX already cover broad frozen-model harness evolution, trace-guided edits, populations/branches, typed changes, and validation gates. Generic controller/harness training or generic harness evolution is not a novelty claim.
- EvoHarness-RL uses BPE harness state plus SFT/GRPO on an open-weight Qwen3-8B policy; it is an adjacent contrast, not an API-only recipe.
- Current candidate, not approved: a compact external state-action controller whose evolutionary credit may be conditioned on realized action-trace displacement and downstream lineage value (controller-level OSLVC). It must beat AW, BC, AMC where relevant, tuned static EA, classical AOS, ELMER-style strength-only, LVPG-style lineage-only, and naive joint operator-strength/raw-lineage controls.
- No final thesis title, controller genotype, algorithm, or innovation point is approved.

GATES AND IMPLEMENTATION:
- G0 OPEN: the official PMLR final record and abstract for EvoMAS: Heuristics in the Loop are verified. The exact final-version state/action/reward/credit/update equations and ablations remain unverified. One bounded PDF retrieval attempt is exhausted; do not retry the same failed routes. Abstract silence is not proof that a mechanism is absent.
- G1 PARTIAL/OPEN: controlled suite has 36 authored cases out of 120; 84 remain unauthored. Independent human review, full family-leakage review, final hashes, live Agent prompt-wrapper integration, and external adapter/scorer checks remain outstanding.
- G2 NOT RUN: no formal Agent/controller/EC experiment has run.
- Latest code/test commit: 5ce4028cb01ba5b8ded02148270cc28b4a059982. GitHub Actions run 40891768273 passed 36/36 tests on Python 3.11. This verifies the software prototype only, not Agent performance or OSLVC.
- Latest documentation/audit commit before this prompt refresh: 5bf4144aa59a37fecedf5585b11930c38f5eb2eb. The latest prompt-refresh commit must be checked at session start.
- No paid API call, model fine-tuning job, or formal Agent/EC experiment was started.
- Preserve the family-held-out design: train F01–F06, validation F07–F09, test F10–F12. Do not use held-out outcomes for tuning.
- Benchmark task-state success, tool validity, conversational quality, and hard safety constraints separately. Hard constraints cannot be traded for task score.

MANDATORY NEXT TASK:
1. Do not repeat the same failed EvoMAS PDF retrieval routes. Use the official PMLR abstract only for confirmed claims; keep G0 OPEN because exact final-version equations/ablations remain unresolved. Revisit only if a genuinely new accessible author/final source appears.
2. In parallel, lock the external controller representation and state/action schema. It must be narrower than an unrestricted harness rewrite and use only observable execution features; explicitly distinguish it from AW controller training and typed harness evolution in HarnessX.
3. Define the exact realized action-trace displacement metric and matched parent/task/state evaluation protocol. If the API provider does not guarantee deterministic seeds, use paired repeated blocks and report uncertainty.
4. Specify the static EA tuning protocol first; compare BC and offline AW before adaptive operator/strength control.
5. Do not implement OSLVC or start paid API rollouts until G0/G1 are sufficiently closed. When permitted, run a bounded no-paid-call feasibility pilot with equal descendant-evaluation counts and explicit stop rules.
6. Falsify the candidate: if AW matches the EC controller, if operator families do not differ in realized displacement, or if displacement-conditioned lineage credit adds no stable predictive/search value, revise/drop OSLVC.
7. At session end, update research/STATUS.md, research/DECISION_LOG.md when needed, SESSION_HANDOFF.md, NEXT_SESSION_PROMPT.md, and relevant literature/method files; commit to main, re-fetch changed files, verify exact content, and report commit SHA(s).

The immediate deliverable remains the master's opening report. Keep the thesis EC-centered, use the hosted API LLM as the frozen reasoning executor, and do not ask the user to repeat information already recorded in openissue.
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
1. Independently review all 24 authored cases (12 pilot + batch 01), their state/trace oracles, and the tool implementation. Explicitly adjudicate the residual lexical-overlap pairs recorded in `research/controlled_suite/PILOT_FAMILY_LEAKAGE_AUDIT_R1.md`; similarity alone is not proof of leakage.
2. Author batch 02 as the next V1/standard case for each family, preserving manifest assignments: F01-D3-V1, F02-D4-V1, F03-D3-V1, F04-D3-V1, F05-D5-V1, F06-D4-V1, F07-D2-V1, F08-D5-V1, F09-D4-V1, F10-D2-V1, F11-D4-V1, F12-D3-V1. Add separate reference and near-miss fixtures and require CI to pass before marking the batch programmatically verified.
3. Continue pairwise lexical screening plus manual mechanism-level review after every batch. Track planned, authored, schema-valid, oracle-verified, independently reviewed, and frozen counts separately.
4. Integrate `agent_payload_r1.py` only when the actual Agent wrapper is introduced; then test real prompt serialization. Do not claim production prompt isolation from helper tests alone.
5. Complete external benchmark adapter/scorer verification (tau2-bench v2.0.0 remains the external candidate; do not call its source split family-held-out). Δτ-Bench stays deferred until dataset license/revision/checksum and family overlap are verifiable.
6. Do not start G2 or any paid API experiment until G0/G1 gates are explicitly passed. Keep OSLVC/controller work separate from task-authoring and do not tune against held-out family outcomes.



## Latest verified session result — controlled-suite batch 01 (2026-10-29)

Latest code/test commit: `d0b998116bb79277b8243d9cf9d23de171bdb93a`. GitHub Actions run [40887208453](https://github.com/yujian777555/openissue/actions/runs/40887208453) passed **36/36 tests**.

Batch 01 adds 12 cases (one V1/standard case per family) with deterministic initial state, state/trace oracle, one passing reference trajectory, and one rejected near-miss each. Evaluator-only fixtures are separate from task records. The manifest is unchanged except statuses for these 12 cases, now `authored_batch_01_pending_review`. Total authored = 24/120; 96 cases remain unauthored.

The leakage screen triggered wording/mechanism revisions: F01-D1/F12-D1 Jaccard 0.300 → 0.056; F04-D1/F08-D1 0.300 → 0.087; F04-D1/F07-D1 0.238 → 0.174; F09-D3/F11-D3 0.290 → 0.171; F06-D3/F11-D3 0.259 → 0.167. Residual pairs are listed in the leakage audit. F03 now tests read-back using a user-specified event ID, while F06 explicitly tests returned-ID handoff. F10's reference entity remains in context and is covered by a test.

G1b remains PARTIAL/OPEN: independent human review, full-suite semantic leakage review, final hashes, and external adapter/scorer validation remain open. G1c NOT DONE; G0 OPEN; G2 NOT RUN. No Agent/evolution experiment or paid API call occurred.

**Next session:** independently review batch 01 and residual pairs, then author batch 02 with these IDs: F01-D3-V1, F02-D4-V1, F03-D3-V1, F04-D3-V1, F05-D5-V1, F06-D4-V1, F07-D2-V1, F08-D5-V1, F09-D4-V1, F10-D2-V1, F11-D4-V1, F12-D3-V1. Preserve the frozen split, write reference/near-miss fixtures separately, and rerun schema/oracle/leakage checks.


## Latest research handoff — API-backed Agent × EC mechanism audit R1 (2026-11-03)

The current copyable prompt above supersedes the older archival state notes below. The latest audit is `research/API_AGENT_EC_MECHANISM_AUDIT_R1.md`. Generic frozen-API controller training and generic harness evolution are established prior art. The current candidate is limited to controller-level, realized-displacement-conditioned lineage-value credit and remains unapproved. G0 is OPEN, G1 is PARTIAL/OPEN (36/120 authored), and G2 is NOT RUN. No paid API call or formal experiment occurred. The next action is the exact final EvoMAS: Heuristics in the Loop mechanism audit, then controller representation and baseline closure.
