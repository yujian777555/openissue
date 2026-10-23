# ToolMaze Benchmark Audit

**Audit date:** 2026-10-23  
**Status:** Source-level audit completed; benchmark adoption remains **blocked pending license/data validation**. No benchmark execution or live LLM call was performed.  
**Purpose:** Determine whether ToolMaze can serve as a defensible environment for the provisional state-contingent recovery-policy candidate.

## 1. Sources and pinned versions

- Paper: [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806), submitted 2026-06-04.
- Official code: [Zhudongsheng75/ToolMaze](https://github.com/Zhudongsheng75/ToolMaze).
- Code HEAD inspected: `f8620d841b67a72ac921caee9df87af6ab9befbb`, commit dated 2026-10-20: “Refine RC to exposure-conditioned; tolerate victim retries in C1 permanent abort check (#2)”.
- Dataset: [dongsheng/ToolMaze on Hugging Face](https://huggingface.co/datasets/dongsheng/ToolMaze), 119 MB and 2,804 files per the visible dataset page/history.

All conclusions below refer to those exact sources, not to a locally installed copy.

## 2. Recovery Cost (RC): intentional implementation revision, stale public definitions

This is more precise than calling the difference a code bug.

### Paper and README definition

The paper's Equation (4) defines mode-level RC as an average across all trajectories, multiplied by the perturbation-exposure indicator. Therefore a trajectory that never encounters a perturbation contributes zero. The GitHub README currently states the same all-run definition and says “No-hit runs contribute 0”.

### Current implementation

The current `evaluation/core/metrics.py` deliberately uses a different definition:
- a no-hit run receives `rc=None`;
- `compute_rc` includes only runs with `hit=True`;
- RC is therefore averaged over runs that actually encountered a perturbation.

The 2026-10-20 commit message explicitly says that RC was changed from all-sample to exposure-conditioned because including no-hit runs diluted RC when the fault was rarely triggered. This is evidence of an intentional metric revision, while the paper and README have not been brought into sync. It is not evidence that the current code accidentally implemented its own stated definition incorrectly.

### Small synthetic arithmetic check

Use three trajectories:
- no hit: per-run penalty (0);
- hit and failed to recover: penalty (1);
- hit and recovered with normalized penalty (0.2).

Then:
- **paper/README all-run RC** = ((0+1+0.2)/3=0.4);
- **current hit-conditioned RC** = ((1+0.2)/2=0.6);
- **exposure rate** = (2/3).

This illustrates why a reported RC value is not comparable unless its denominator is specified.

### Recommended reporting rule for our study

If ToolMaze is eventually adopted:
1. Report the current **hit-conditioned RC** and the perturbation-exposure rate separately.
2. Also calculate the paper-compatible **all-run RC** as a sensitivity/reproduction metric.
3. Report TSR and PRR alongside both RC variants; do not interpret RC without the exposure rate.
4. Pin the code commit and label which definition is used in every table.
5. Do not silently patch upstream files. If a local evaluator adapter is necessary, keep the metric implementation in our own experiment code and test both formulas on synthetic cases.

The official published results' exact generating code version is not established by this source audit. Reproducing the paper's numbers and evaluating a new method against the current code are different goals.

## 3. Dataset structure, split leakage, and loader friction

The paper reports 100 tasks per complexity level in its task composition table and defines complexity levels C1–C4 and perturbation modes P0–P4. The Hugging Face page exposes a single split named `train`, not a documented train/validation/test protocol. That name must not be mistaken for a benchmark-author-provided split suitable for policy evolution.

The dataset page's viewer currently fails while casting nested records to a single inferred schema: different records expose different nested output keys (for example, `error` versus `message`). This does not prove the underlying JSON files are corrupt, but it means the HF streaming viewer is not a reliable validation path for the current dataset revision. A raw-file parser and schema audit would be needed.

**Minimum split rules if use is later authorized:**
- Group all P0–P4 variants by their shared base `task_id`; never place perturbation variants of the same base task in both train and test.
- If templates are reused, group by `template_id`/template family as well.
- Stratify by complexity and domain for an in-distribution split.
- Add a separate OOD split holding out at least one structural factor (e.g. task-template family or topology level) and/or tool/domain family.
- Keep the final test split untouched during genotype design, mutation-operator design, parameter tuning, and prompt iteration.
- Validate all raw JSONs against a declared schema before running any agent. Report malformed/ambiguous cases and exclusions.

Because the dataset is small for adaptive policy search, one random split alone would be weak evidence. Prefer repeated grouped splits or cross-validation for development, followed by a pre-registered held-out test.

## 4. License / redistribution gate

The inspected GitHub tree has no root `LICENSE` file. The visible Hugging Face dataset card's metadata does not declare a license either. This is not a legal conclusion about ownership or permitted research use, but there is no explicit permissive license in the inspected locations that we can safely rely on.

Until terms are confirmed:
- do not redistribute the code or dataset;
- do not commit copied task JSONs into our repository;
- do not make ToolMaze the only thesis benchmark;
- seek an explicit license/permission clarification, or use a benchmark with clear terms / build an independent controlled task generator.

The code and data are separate artifacts and may have different rights. Confirm both independently.

## 5. What ToolMaze can and cannot establish

**Useful properties:** deterministic fault injection; explicit/implicit and transient/permanent failure modes; C1–C4 task-DAG complexity; valid-path ground truth; observable tool-call traces; TSR/PRR/RC-style outcomes.

**Limitations for our research:** no official optimization split; relatively small task pool; the public RC formula has version drift; data viewer schema inference currently fails; license metadata is missing; the paper itself acknowledges that controlled DAG topologies are not open-ended web environments.

ToolMaze is an evaluation substrate, not an evolutionary-computation contribution. Even if it becomes usable, a successful result on ToolMaze alone would not prove broad recovery generalization.

## 6. Adjacent prior work that must be in the baseline audit

- **EVOTOOL (ACL 2026):** already evolves modular tool-use prompts with trajectory-grounded blame attribution, targeted mutation, and diversity-aware selection. It is the closest EA-based baseline for failure-focused tool policy evolution.
- **EvA / Evolving Agents (ACL 2026):** uses quasi-symbolic abstractions, a Perceptor/Actor/Controller arrangement, and rollback to adapt under mid-episode distribution shifts. The abstract does not establish that it is a conventional population-based EA; treat it as an adjacent adaptive-controller baseline, not mislabel it as an EA.
- **Agent Planning Benchmark (APB, arXiv v3 revised 2026-10-05):** 4,209 cases across 22 domains, including broken tools and unsolvable tasks; the paper reports APB-guided refinement on ToolSandbox and τ²-bench. It is a useful non-EA refinement baseline conceptually, but **not a license-cleared fallback**: the inspected GitHub tree has no LICENSE file, the HF card declares no explicit license, and the HF viewer fails a schema/column-casting step. The six named task-category files are not a documented train/validation/test split for policy evolution. Audit data rights and raw JSONL loading before considering it.
- **HarnessEvolve:** reference-trajectory alignment, failure clustering, and acceptance gates already cover broad claims about generic failure attribution and reliable self-evolution.
- **Hierarchical quality-diversity recovery:** diverse repertoires and experience-guided selection for unexpected physical damage predate LLM agents. “Diversity enables recovery” is not a sufficient novelty claim.

## 7. Potential auxiliary benchmarks with clearer repository licensing

These are not direct replacements for ToolMaze's controlled fault-injection design, but may provide external validity checks.

- **τ²-bench / τ-bench 2.0.0** — [official repository](https://github.com/sierra-research/tau2-bench). The current repository and `pyproject.toml` declare MIT. Its released benchmark manifests include frozen tasks across airline, retail, telecom and additional settings, and it evaluates stateful tool-agent-user interaction. It does **not** provide ToolMaze's explicit/implicit × transient/permanent fault matrix, so treat it as a secondary transfer/generalization evaluation rather than the primary recovery environment. An open issue asks about the separate license for public leaderboard trajectory files; do not assume external S3 trajectory dumps inherit the repository license.
- **Berkeley Function Calling Leaderboard (BFCL V4)** — [official code](https://github.com/ShishirPatil/gorilla) and [dataset card](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard). The inspected code is Apache-2.0 and the HF dataset card declares Apache-2.0. V4 includes agentic evaluation surfaces such as multi-turn use, web-search/multi-hop behavior, memory, format sensitivity and error-recovery-related evaluation. It is not a controlled dynamic fault-injection environment; use it only as an auxiliary external test of tool-use robustness, with exact version/category pins.
- **Independent procedural training environment** — if ToolMaze/APB rights remain unclear, author a small DAG-based tool environment and deterministic fault injector from scratch, with our own code and task generator. This gives a legitimate training/development split and permits OOD task-template/fault combinations. It is experimental infrastructure, not an innovation claim by itself.

## 8. Gate decision

**Current decision: HOLD ToolMaze as the primary benchmark.** Do not start the proposed baseline run yet. First resolve the code/data terms and validate a raw dataset sample/schema. APB is not yet a cleared fallback either: its inspected code tree and dataset card lack explicit license metadata, and its HF viewer currently fails. In parallel, continue the closest-work comparison and seek a benchmark with explicit use terms or design an independent task generator. If no suitable benchmark has clear use terms, design a small independent controlled environment instead of relying on unclear redistribution rights.

The provisional scientific question remains falsifiable:

> Does evolutionary search over an explicit, typed, state-conditioned recovery-policy representation improve recovery on held-out combinations of tool-failure semantics and task structure beyond fixed rules, direct reflection/replanning, and EVOTOOL-style policy evolution?

This is a question to test, not an approved novelty claim. Parameter/operator control remains a later experiment, only after static EA shows a repeatable capability gain.
