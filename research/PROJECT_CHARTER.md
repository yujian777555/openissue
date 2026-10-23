# Project Charter

## 1. Mission

Develop a graduate thesis around **evolutionary computation (EC/EA) for AI agents**, with a coherent research narrative and 2–3 substantive contributions that can each form the basis of a small research paper.

The immediate priority is the **thesis proposal / opening report**. Topic selection must therefore balance novelty, methodological substance, feasibility, measurable evaluation, and the likelihood of completing a credible research project on a graduate timeline.

## 2. Desired research structure

The target is not three unrelated tricks or three loosely connected projects.

Preferred structure:

1. One umbrella problem about a meaningful limitation of current agents.
2. A common experimental setting and a clear definition of the agent, evolutionary search space, and evaluation objective.
3. Two or three connected contributions, each addressing a distinct subproblem and capable of independent evaluation.
4. A final thesis that integrates the contributions into one narrative.

Each small paper should answer a distinct research question. Shared infrastructure is desirable; duplicated claims or experiments presented as separate novelty are not.

## 3. Research scope

Investigate the broad intersection of evolutionary computation and agents, including—but not limited to—evolution of agent policies, workflows, tool-use strategies, prompts, memory/skills, multi-agent coordination, search operators, evaluation/selection mechanisms, and constrained forms of agent improvement.

These are **search categories, not preselected thesis directions**. RSI (recursive self-improvement) is neither automatically accepted nor automatically excluded. Its value and feasibility must be assessed against current prior art, evaluation reliability, cost, reproducibility, and whether a specific tractable problem exists.

## 4. How to assess prior work

For each relevant paper, record:

- Full title, authors, publication venue/status, year, DOI/arXiv URL and code URL when available.
- Problem setting and the exact object being evolved.
- Evolutionary algorithm and representation; initialization, variation, selection, replacement, and stopping criteria.
- Agent architecture, base model, tools, environment, datasets, and evaluation metrics.
- Main results and what the authors actually demonstrate.
- Limitations explicitly acknowledged by the authors.
- Additional limitations supported by experiments, method analysis, or code inspection.
- Closest related papers and how the methods differ.
- What could be borrowed, what would need to change, and what evidence would establish a new contribution.
- Reproducibility, compute/API cost, and implementation risk.

Keep separate labels for **verified fact**, **paper-author claim**, **our interpretation**, and **untested hypothesis**.

## 5. Innovation quality bar

A candidate contribution is not sufficient merely because it combines an EA with an agent, adds another heuristic, uses a new benchmark, or reports a small score increase.

A candidate must state:

- **Problem:** what concrete limitation exists?
- **Mechanism:** what new or materially improved method addresses it?
- **Rationale:** why should this mechanism work?
- **Evidence:** which baseline, ablation, and statistical test can distinguish the explanation from alternatives?
- **Boundary:** when should it help, and when might it fail?
- **Practicality:** can it be implemented and evaluated with available time, models, tools, and compute?
- **Positioning:** how is it different from the closest prior work?

Novelty is provisional until the nearest prior work has been investigated.

## 6. Feasibility and experimental discipline

Prefer external, reproducible task success measures over self-reported improvement. When model-based judging is unavoidable, assess judge bias and use independent checks where possible. Track API calls, tokens, wall-clock time, hardware, seeds, and failures.

Use train/validation/test separation or equivalent held-out evaluation to limit overfitting to a benchmark. Include strong baselines, ablations, multiple seeds where practical, and uncertainty estimates. Report negative results honestly.

## 7. Decision policy

Do not lock the topic before comparative review. Maintain a shortlist of candidate directions and score them against novelty, prior-art risk, methodological depth, feasibility, objective evaluation, reproducibility, relevance to evolutionary computation, and publication potential.

The score supports discussion; it does not replace expert judgment or literature evidence.

## 8. Project context boundary

This repository is the durable project record. Do not silently import candidate ideas, conclusions, experimental results, or assumptions from unrelated projects or previous conversations. If a detail is not documented here or verified from a source, mark it unknown and investigate it.

## 9. Current decision

As of 2026-10-23: project initialized; no candidate topic or innovation point has been approved. Immediate priority: recent-literature retrieval, taxonomy, closest-work comparison, and a ranked candidate shortlist.
