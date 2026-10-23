# Literature Review: Protocol and Registry

## Purpose

Determine the current state of research at the intersection of evolutionary computation and AI agents, and find evidence-backed opportunities for a thesis with 2–3 connected contributions.

## Search window

Prioritize work published or publicly released in **2024–2026**, while retaining older foundational papers when they are direct baselines or necessary to understand the field. Record the version/date of each source because preprints and conference versions may differ.

## Search lanes

1. Evolutionary optimization of LLM agents and agent systems.
2. Evolution of prompts, instructions, workflows, tool-use policies, skills, memory, and agent architectures.
3. Evolutionary algorithms for multi-agent cooperation, role assignment, communication, and coordination.
4. Evolution of code-writing or research agents and constrained agent improvement / RSI.
5. Evolutionary operators, population management, fitness estimation, credit assignment, diversity, and search efficiency for agent optimization.
6. Evaluation reliability: benchmark leakage, reward hacking, judge bias, cost-aware evaluation, generalization, and reproducibility.
7. Surveys and benchmark papers that reveal the field's taxonomy and unresolved challenges.

These lanes guide retrieval; they are not a commitment to any particular topic.

## Source quality and verification

Prioritize official conference proceedings, journal pages, arXiv records, author project pages, and original GitHub repositories. Use secondary summaries only for discovery, not as the sole basis for technical claims.

For every candidate core paper:
- verify title, authors, date, venue/status, and canonical URL;
- read the abstract and method, then the full paper and supplement where available;
- distinguish reported results from our interpretation;
- inspect official code, issues, and evaluation scripts when available;
- check follow-up work and papers that may have independently proposed similar mechanisms.

Do not infer publication acceptance from an arXiv page. Do not infer a limitation solely from a missing experiment. Do not claim code reproduces results until this has been checked.

## Search log

| Date | Source / query family | Purpose | Outcome / follow-up |
|---|---|---|---|
| 2026-10-23 | Pending first systematic search | Establish recent-paper corpus and taxonomy | Not started |

## Paper registry

No papers have been fully screened and registered yet.

Use this schema for each paper:

| Field | What to record |
|---|---|
| ID | Stable local identifier, e.g. P001 |
| Citation | Authors, exact title, venue/status, year |
| Canonical source | DOI / proceedings / arXiv URL |
| Code/data | Official repository and benchmark URLs |
| Research question | What problem is addressed? |
| Evolved object | What exactly is encoded and changed? |
| Evolution method | Representation, initialization, variation, selection, replacement, budget |
| Agent/task | Model, tools, environment, task family |
| Fitness/evaluation | Objective, judge, splits, metrics |
| Baselines | Strongest and closest comparisons |
| Results | Verified quantitative results with source/table/figure references |
| Limitations | Author-stated vs independently supported limitations |
| Reproducibility | Code, configs, datasets, cost, missing details |
| Overlap risk | Closest work and what it already establishes |
| Borrowable ideas | Mechanisms worth adapting |
| Potential extension | Testable extension, explicitly marked as a hypothesis |
| Relevance | High / medium / low, with reason |
| Status | Discovery / screened / full-text reviewed / code inspected / reproduced |

## Comparison dimensions

For cross-paper comparison, record:
- evolutionary search space and genotype/phenotype mapping;
- how candidates are generated and modified;
- whether variation operators are fixed, learned, or adapted;
- fitness noise, evaluation cost, and how these are controlled;
- population diversity and selection pressure;
- single-task performance vs held-out generalization;
- whether the optimized object transfers across tasks/models;
- external verification and safeguards against reward hacking;
- computational cost and reproducibility;
- evidence that evolutionary search is essential compared with simpler alternatives.

## Research-gap standard

A proposed gap must be supported by at least one of:
- an explicit limitation or future-work statement in a relevant paper;
- a concrete failure pattern in reported experiments;
- a mechanism-level weakness demonstrated by analysis or controlled tests;
- a meaningful setting not covered by close prior work, with a clear reason it matters.

A gap is not validated until the closest prior work and competing explanations are checked. Any proposed innovation should include a falsifiable hypothesis and an experiment that could show it does **not** help.
