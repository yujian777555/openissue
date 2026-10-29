# Benchmark and Baseline Decision R2 — Agent × Evolutionary Computation

**Date:** 2026-10-27  
**Status:** Provisional research decision; benchmark and thesis topic are not finally approved.  
**Scope:** `yujian777555/openissue` only. No experiment or paid API call was started in this audit.

## 1. What this audit establishes

The immediate task is the master's thesis opening report. We need a reproducible setting that can test a specific EC mechanism, not just a benchmark where an Agent happens to run.

The current hypothesis is still OSLVC-R1: test whether the continuation value of an Agent-policy variation operator can be predicted more accurately when conditioned on the **realized behavior displacement** of the offspring, rather than assigning raw immediate or lineage reward to an operator–strength pair. This is not yet a novelty claim.

## 2. Direct baseline: EvoTool

Primary sources:

- Paper: https://aclanthology.org/2026.acl-long.2016/
- Official implementation: https://github.com/SYang2000/ACL_2026_EvoTool
- Implementation contract: https://github.com/SYang2000/ACL_2026_EvoTool/blob/main/SPEC.md
- Evolution loop: https://github.com/SYang2000/ACL_2026_EvoTool/blob/main/src/evolve/loop.py
- Selection: https://github.com/SYang2000/ACL_2026_EvoTool/blob/main/src/evolve/select.py

### Verified implementation facts

- The policy genotype contains four evolvable modules: Planner, Selector, Caller, and Synthesizer.
- The standard mutator changes exactly one selected module, using an execution episode and feedback as guidance.
- A child is admitted when it beats its parent on the current mini-batch; population selection then uses validation-set instance-wise wins to retain complementary policies and weight parent sampling.
- The default deployment artifact is one selected policy, not an ensemble.
- The repository declares an MIT license.

### Consequence for the thesis

EvoTool is a strong direct baseline and a useful implementation reference. We cannot claim modular policy evolution, blame-guided targeted mutation, or diversity-aware selection as new. The proposed method must improve a clearly specified EC control mechanism beyond EvoTool and strong tuned baselines.

### Demo split is not suitable as the final test protocol

The current `scripts/data/build_taubench.py` source list orders upstream tasks as `tasks_test.py`, then `tasks_train.py`, then `tasks_dev.py`, while its introductory docstring describes a different order. The demo builder then selects the first valid tasks in source order, and the demo runner partitions the resulting pool. Consequently, the bundled 150-instance demo must not be treated as an untouched official test set. Use it only for smoke tests. Rebuild from pinned upstream source splits and audit overlap before producing paper results.

The BFCL converter similarly builds a selected subset rather than preserving an untouched official leaderboard split. An independent September 2026 review of BFCL v4 reported defects affecting 24 of 50 sampled tasks. This does not invalidate the entire benchmark, but it is a reason not to rely on BFCL v4 alone without auditing the exact subset.

## 3. Updated real-task benchmark candidate: official τ²/τ³-bench repository

Primary source: https://github.com/sierra-research/tau2-bench

### Verified facts from the official repository

- The repository declares an MIT license.
- The current release line is `v2.0.0`, released in October 2026.
- The release provides frozen benchmark manifests and updated tasks across airline, retail, and telecom domains.
- The README explicitly warns that v2.0 results are not directly comparable with 1.x because task content, prompts, and grading behavior changed. All methods in our study must use one pinned version.
- The source tree contains explicit task split files. In the current tree, the airline split contains 30 train / 20 test tasks; retail contains 74 / 40; telecom contains 74 / 40. The separate `text-v1` leaderboard manifest freezes 50 tasks per domain, so we must not assume that the manifest and source `train/test` lists are interchangeable.

### Provisional recommendation

Use a pinned τ²/τ³-bench release as the **realistic Agent validation environment**, subject to a split-overlap audit and a feasibility check for the selected Agent-policy representation. For evolutionary optimization, use only a declared training partition; split validation data from training groups; keep the test groups locked. Do not label a custom split as an official leaderboard score.

The test split must be grouped by task family, not merely randomly split by task ID. Candidate grouping signals include task-template/purpose, tool/action signatures, shared scenario factors, and generated-variant IDs. Before adopting any split, compare its task IDs against the frozen benchmark manifest and document all overlaps.

Because a user-simulated interaction can add variance, fix the agent and user-simulator model/version, decoding settings, environment version, and seeds. Repeat evaluations where necessary; use paired comparisons. Local inference is preferred for the first feasibility work, so the core method is not dependent on paid API availability.

## 4. Recommended two-level evaluation design

### A. Controlled mechanism test

Create a small, independently authored deterministic tool-task environment with explicit tool schemas, state transitions, and exact success oracles. This is not a replacement for a real benchmark; it isolates the mechanism and avoids unclear third-party data rights.

Use a fixed probe set and compare parent/offspring tool-call traces after canonicalization. A candidate behavior-distance metric can combine normalized tool-call sequence edit distance, tool-name disagreement, and argument-field/value changes. Keep task success, executability, and displacement as separate variables. Do not use raw prompt-token edit distance as the behavior metric.

### B. Realistic validation

Port or adapt the policy/evaluator to the pinned τ²/τ³-bench release and report the exact release, task split, model, seeds, and evaluator. The EvoTool demo is not the official split. BFCL v4 can be an additional audited robustness check, not the sole source of evidence.

ToolMaze remains blocked as a primary benchmark until its code/data rights and split design are resolved.

## 5. Falsification-first experiment protocol

### Gate 1 — Is operator-specific scale calibration necessary?

Use three clearly specified variation operators, for example:

1. local rule/constraint edit within one module;
2. whole-module rewrite (EvoTool-like targeted mutation);
3. coordinated edit of a linked module pair, with interface validation.

For each operator, test low/medium/high requested strengths on matched parents and probe tasks, with randomized assignment where feasible. Record realized displacement, validity, immediate task reward, and failure mode separately.

**Reject operator-specific calibration** if the operators do not show material differences in realized displacement/validity, or if the differences do not alter downstream search decisions.

### Gate 2 — Does displacement-conditioned credit add information?

Compare:
- immediate-reward credit;
- raw lineage-return credit;
- displacement-only prediction;
- operator + displacement prediction;
- scale-conditioned lineage-value credit.

For lineage outcomes, equalize the number of descendant evaluations allocated to each sampled action. Report best-so-far improvement and best-so-far AUC over a fixed evaluation horizon. Do not use a raw maximum over unequal-sized branches as the only outcome: it is vulnerable to unequal search opportunities and optimistic selection bias.

The conditional operator term is a **predictive residual**, not automatically a causal effect. Any operator-specific interpretation requires matched/randomized comparisons and overlap in realized displacement; do not describe conditioning on displacement alone as causal identification.

### Gate 3 — Does the method improve Agent performance?

Minimum baseline ladder:

1. no evolution;
2. static EA with its parameters tuned on train/validation tasks;
3. EvoTool;
4. classical adaptive operator selection using immediate reward;
5. adaptive operator selection with diversity/parent-distance credit;
6. behavior-scale-only control (ELMER-style comparison);
7. lineage-only scale control (LVPG-style comparison);
8. naive joint operator–scale control with immediate reward;
9. naive joint operator–scale control with raw lineage return;
10. OSLVC-R1.

Match policy representation, base model, tasks, evaluation calls, seeds, stopping rule, and tuning data wherever possible. Tune static EA settings first (e.g., population size, offspring count, mutation probability, selection pressure, and fixed operator mixture), then freeze the selected configuration before testing online control.

Primary metrics: task success and held-out task-family success. Mechanism diagnostics: offspring validity, realized displacement, conditional-value prediction/ranking, diversity, and lineage best-so-far AUC. Cost is secondary.

## 6. Current decisions and unresolved gates

- **EvoTool:** accepted as a direct baseline/reference implementation; its demo split is not accepted as final evaluation.
- **τ²/τ³-bench:** strongest current realistic benchmark candidate, but exact split/manifest overlap and adapter feasibility remain to be verified.
- **BFCL v4:** secondary only after auditing the selected examples.
- **ToolMaze:** not adopted until rights/split issues are resolved.
- **OSLVC-R1:** remains a hypothesis, not an approved innovation.
- **EvoMAS: Heuristics in the Loop:** final ICML PDF's detailed method audit remains open because the PDF could not be retrieved as readable text in this session. The earlier indexed manuscript is useful evidence about an earlier version, not a substitute for the final version.

No full experiment and no paid API call was performed. The next useful work is to close the τ²/τ³ task-split overlap audit and obtain a readable final EvoMAS HIL method section. Only then should a local, no-paid-call feasibility pilot be authorized.


## 7. Follow-up: exact overlap between the frozen text-v1 manifest and source splits

I compared the checked-in `airline_50`, `retail_50`, and `telecom_50` subset IDs with each domain's `split_tasks.json` in the official `sierra-research/tau2-bench` repository.

| Domain | Frozen text-v1 subset size | IDs also in source train | IDs also in source test |
|---|---:|---:|---:|
| Airline | 50 | 30 | 20 |
| Retail | 50 | 28 | 22 |
| Telecom | 50 | 27 | 23 |

All frozen-subset IDs fall into the source train or test lists; the frozen `text-v1` manifest is not an untouched external test set if the evolutionary search trains on the source train partition. The official subset artifacts record `task_split = base`, which explains why they span both partitions.

**Decision:** do not evolve on source train tasks and then report the full `text-v1` frozen-subset score as held-out performance. Use the source test split only for a within-domain held-out result, or create a separately declared group-held-out split and clearly label it as a research split, not an official leaderboard score.

There is a second issue: the default source train/test split is not automatically a task-family split. For example, telecom train and test both contain the same high-level issue families. Airline has only one exact `description.purpose` overlap, but that does not prove that near-duplicate scenario patterns are absent; retail's purpose field is null for many records. Before locking a split, construct family fingerprints from scenario instructions after entity redaction, issue/template metadata where available, and tool/action signatures. Assign whole groups—not individual task IDs—to train, validation, and test.

This is a source-level split audit; it did not execute any agent or call a model.


## 8. Follow-up: evaluator validity audit and a better controlled substrate

A second independent audit materially changes how benchmark scores should be interpreted. *Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation* (Bhat et al., 2026; https://arxiv.org/abs/2607.02577) reviewed 496 executions across BFCL v4, τ²-Bench, LiveMCPBench, and MCP-Atlas, reporting 92 evaluator–human disagreements (18.5%). Its reported per-benchmark sample included 11/112 disagreements for τ²-Bench Retail (9.8%), 40/200 for BFCL v4 (20%), 29/95 for LiveMCPBench (30.5%), and 12/89 for MCP-Atlas (13.5%). Epoch AI separately found defects affecting 24/50 sampled BFCL v4 tasks. These are audits of sampled tasks, not proof that every item is wrong; they do show that official scores should not be treated as ground truth without inspecting the exact cases and evaluator behavior.

### Tool-Veritas as a reusable execution substrate, not a pre-approved benchmark

- Repository: https://github.com/CoreThink-AI/benchmarking-the-benchmarks
- Tool-Veritas subproject license: Apache-2.0 (https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/main/Tool-Veritas/LICENSE)
- The code provides a local in-memory tool sandbox, multi-turn ReAct harness, deterministic state gates, per-turn traces, and an optional qualitative judge that runs only after deterministic gates pass.
- The checked-in `examples/cases/all.jsonl` contains 70 cases across 16 domains (mostly medium/hard), not a ready-made train/validation/test suite. The README's reported human-agreement result is author-reported; we have not independently reproduced it.
- The gate schema can require specific tools as well as check resulting state. To avoid trajectory lock-in, our own primary success oracle should check goal-relevant state invariants; require a specific tool only when using that tool is itself part of the task objective. Communication quality should be secondary, not allowed to override a failed goal-state check.

### Revised benchmark recommendation

1. Use Tool-Veritas as a **local controlled execution substrate** and independently create/verify a larger task-family set. The 70 bundled cases are seeds/examples, not sufficient by themselves for the thesis's complete split.
2. Use a pinned τ²/τ³-bench release as **external realistic validation**, but manually audit the exact selected tasks and reward checks. Prefer a locked test partition; report both the official evaluator result and an independently adjudicated subset result when feasible.
3. Do not use full `text-v1` as held-out evidence after training on its source-train IDs. Do not rely on BFCL v4 as the only benchmark.
4. Record raw traces and the exact goal-state checks for every evaluated task. Separate tool-call validity, task-state completion, and conversational quality into different metrics.

This supersedes the earlier tentative wording that treated τ²/τ³-bench as a sufficient external validator on its own. It remains a useful candidate, but its exact task/evaluator subset must be audited.




## 10. G1 protocol R1 — family split and pinned source test set (2026-10-29)

The detailed protocol is now in `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`.

- **Primary controlled suite design:** 120 independently authored deterministic tasks, five mock domains × 12 global task families × two variants. Whole families are assigned to train (F01–F06, 60 tasks), validation (F07–F09, 30), and test (F10–F12, 30). Planned family IDs and metric/oracle rules are defined in the protocol. The tasks have **not yet been authored**, so this is a design freeze proposal, not a finished dataset or a G1 PASS.
- Tool-Veritas `all.jsonl` was parsed at source level: 70 cases, 16 domain labels, 20 domain/category combinations, 70 unique normalized goals, no explicit family field or supplied split. Use its Apache-2.0 code as a candidate harness only after adapter smoke test; author original task content from scratch because a separate task-data license was not identified in the files checked.
- **Pinned external candidate:** τ²/τ³-bench `v2.0.0`, commit `989d3285ae669e49503324bdb9981bf14fccedeb`, MIT. Exact source-test IDs are locked provisionally: airline 20 IDs and retail 40 IDs, recorded in the G1 protocol with source task/split blob SHAs. This is a custom source-test evaluation, not the frozen `text-v1` leaderboard manifest; full `text-v1` mixes source train/test IDs.
- Scorer audit: report database/state reward separately from full official reward. Airline test tasks use DB+COMMUNICATE; retail uses DB+NL_ASSERTION for 39 tasks and DB-only for one. Check actual scorer behavior, pin any judge model/version, and cluster related task IDs for uncertainty analysis.
- **New candidate:** Δτ-Bench (arXiv:2610.34238, 2026-10-25) reports 1,588 tasks across 42 domains and six tool-ecosystem versions (1,191 train / 397 test); its code repo states MIT, but dataset license/revision/checksums and task-family leakage still require verification. It is not selected yet; audit boundedly before deciding whether its evolving-tool setting is relevant enough to replace/augment τ².
- **Gate state:** G1a (design) proposed/fixed for review; G1b (original tasks/oracle/tests/hash) NOT DONE; G1c (external adapter/scorer and Δτ decision) NOT DONE. G1 remains PARTIAL/OPEN; G2 NOT RUN; no model/API experiment was run.



## 10. G1 protocol R1 — family split and pinned source test set (2026-10-29)

Detailed protocol: `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`.

- **Primary controlled suite design:** 120 independently authored deterministic tasks, five mock domains × 12 global task families × two variants. Whole families are assigned to train (F01–F06, 60 tasks), validation (F07–F09, 30), and test (F10–F12, 30). Planned IDs and oracle/metric rules are in the protocol. Tasks have **not yet been authored**, so this is a design proposal, not a finished dataset or G1 PASS.
- Tool-Veritas `all.jsonl` was parsed at source level: 70 cases, 16 domain labels, 20 domain/category combinations, 70 unique normalized goals, no explicit family field or supplied split. Use its Apache-2.0 code as a candidate harness only after adapter smoke test; author original task content from scratch because a separate task-data license was not identified.
- **Pinned external candidate:** τ²/τ³-bench `v2.0.0`, commit `989d3285ae669e49503324bdb9981bf14fccedeb`, MIT. Exact source-test IDs (airline 20; retail 40) are in the G1 protocol. This is a custom source-test evaluation, not the frozen `text-v1` leaderboard manifest; the full `text-v1` set mixes source train/test IDs.
- Scorer audit: report database/state reward separately from full official reward. Airline test tasks use DB+COMMUNICATE; retail uses DB+NL_ASSERTION for 39 tasks and DB-only for one. Verify actual scorer behavior, pin any judge model/version, and cluster related task IDs for uncertainty analysis.
- **New candidate:** Δτ-Bench (arXiv:2610.34238, 2026-10-25) reports 1,588 tasks across 42 domains and six tool-ecosystem versions (1,191 train / 397 test); its code repo states MIT, but dataset license/revision/checksums and family leakage still require verification. It is not selected yet; audit boundedly before deciding whether its evolving-tool setting is relevant enough to replace/augment τ².
- **Gate state:** G1a (design) provisionally specified; G1b (original tasks/oracle tests/hash) NOT DONE; G1c (external adapter/scorer and Δτ decision) NOT DONE. G1 remains PARTIAL/OPEN; G2 NOT RUN; no model/API experiment was run.
