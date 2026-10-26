# Faithful Self-Evolvers — Code Audit (First Pass)

**Audit date:** 2026-10-26  
**Status:** Code observations recorded; no claim that the paper's primary behavioral results are invalid.  
**Repository inspected:** https://github.com/Dreamcatcher0622/Faithfulness  
**Project boundary:** This audit is part of yujian777555/openissue only; the external repository was read, not modified.

## 1. What was inspected

The public repository README identifies itself as the official code for the ICML 2026 paper *Large Language Model Agents Are Not Always Faithful Self-Evolvers*. It describes four representative self-evolving frameworks, 13 LLM backbones, nine environments, interventions on raw and condensed experience, and an information-gain analysis. The GitHub tree is retrievable, including:
- ExpeL intervention logic in ExpeL/agent/expel.py;
- ReasoningBank prompt modification and runtime paths;
- cdt/src/stats_frscore.py and cdt/src/stats_igscore.py plotting/analysis helpers.

A root LICENSE file was not found by direct path retrieval. Treat the code as inspectable but not license-cleared for reuse.

## 2. Confirmed implementation observations

### 2.1 ExpeL's “irrelevant” and “filler” conditions are stochastic partial replacements

In ExpeL/agent/expel.py:
- the empty condition returns an empty insights list;
- the corrupted condition modifies each insight using randomized word substitutions, optional insertion of an error marker, and optional word deletion;
- the irrelevant condition replaces each insight with an unrelated template with probability 0.8 and preserves the original insight with probability 0.2;
- the filler-token condition follows the same 0.8 replacement / 0.2 preservation pattern.

This is not automatically a defect: partial corruption can be a deliberate intervention. But the interpretation must be precise. The irrelevant/filler conditions are **stochastic partial perturbations**, not clean “all semantic information removed” conditions. The empty condition is the clean ablation. Comparisons should account for intervention strength and run-to-run randomness.

The helper functions use Python's random module. The repository has seed-setting code in some utilities, but this audit did not establish that every ExpeL intervention call receives a fixed, recorded seed. This remains a reproducibility check, not a confirmed failure.

### 2.2 ReasoningBank's raw-experience intervention branch is commented out, consistent with its stated scope

In ReasoningBank/agents/legacy/agent.py, the raw few-shot modification branch is commented out. The repository README labels ReasoningBank as a “Condensed-Only” setting, so this is consistent with the intended experiment scope rather than evidence of a missing required condition. Do not compare this branch as if it tested raw and condensed experience symmetrically.

### 2.3 A secondary FR-score plotting helper appears order-dependent

In cdt/src/stats_frscore.py, draw() initializes a cumulative scores vector, adds the current sample's layer-wise attention contributions, and then divides the **entire accumulated vector** by 8 inside the per-sample loop. Since the cumulative vector is not reset for each sample, earlier samples are repeatedly rescaled as later samples are processed. This makes the plotted aggregate order-dependent and different from the straightforward “sum each sample's contribution, normalize once” computation.

This is a code-level concern about a secondary FR-score analysis/plot, not proof that the paper's primary task-success or behavioral-faithfulness results are invalid. Before drawing a scientific conclusion from that figure, compare the implementation with the paper's exact FR-score equation and regenerate the figure from saved per-sample artifacts.

### 2.4 A secondary IG-score averaging helper has a likely denominator off-by-one

In cdt/src/stats_igscore.py, draw_all_average() increments total before checking whether num exceeds end and breaks. With the default inclusive end threshold, the excluded row can be counted in total even though it is not accumulated into y_data. This likely biases the plotted average downward slightly. Again, this is a plotting/aggregation issue, not a verdict on the paper's main behavioral findings.

## 3. What this means for the proposed research lane

The paper provides a useful intervention design and an accessible code path for studying whether agents depend on their stored experience. It does **not** itself supply an evolutionary algorithm for choosing experience representations or skill boundaries.

The following claims are not justified from this first pass:
- that the primary faithfulness results are invalid;
- that all interventions are unreproducible;
- that a new faithfulness score would be novel;
- that a memory-evolution algorithm is automatically warranted by the observed failures.

A future method would need to show an EC-specific mechanism that improves both held-out task behavior and faithful use of experience, while beating task-specific skill generation (GSO), hybrid episodic–procedural memory (H-EPM), AgentEvo, and classical GP/EC baselines. A weighted sum of the two metrics is not sufficient.

## 4. Follow-up checks

1. Read the full GSO paper and supplement; determine whether any official implementation or released benchmark exists.
2. Inspect H-EPM and AgentEvo method details and code availability.
3. Compare the FR-score implementation with the paper's equation and saved results before using that figure as evidence.
4. Verify license terms for Faithfulness and DIVE before any code/data reuse.
5. Do not start API experiments or implementation until the novelty and benchmark gates pass.
