# Agent Skill/Workflow Generalization and Experience Faithfulness — Initial Screen

**Screen date:** 2026-10-26  
**Status:** Exploratory lane only. **No candidate or thesis innovation is approved.**  
**Project boundary:** This screen belongs only to yujian777555/openissue.

## 1. Why screen this lane?

The communication-evolution lane did not pass its current novelty gate. A different, evidence-backed failure pattern is worth screening before selecting another method: an agent may improve on the tasks used to evolve a skill or workflow, yet fail to transfer the improvement to held-out tasks; it may also store a condensed experience but not faithfully use it during execution.

The initial evidence is unusually concrete:

- **Do Self-Evolving Skills Generalize to Held-Out Tasks?** evaluates five self-evolving methods and a one-shot skill across six benchmarks. Among 21 skills that improve on training tasks, only five retain all the improvement on test tasks, thirteen retain part, and three retain none. Its proposed Generalizable Skill Optimization (GSO) keeps a guide for writing skills and generates a new skill per task, outperforming reusable-skill alternatives on the six reported benchmarks.
- **Large Language Model Agents Are Not Always Faithful Self-Evolvers (ICML 2026)** studies experience faithfulness with controlled interventions across four representative frameworks, 13 LLM backbones, and nine environments. Its repository describes a marked asymmetry: agents use raw trajectories more reliably than condensed experience summaries, which may be ignored or misused.
- **Experience-Evolving Multi-Turn Tool-Use Agent with Hybrid Episodic–Procedural Memory (H-EPM, ICML 2026)** already combines a tool graph with context-bearing episodic summaries on recurring tool dependencies.
- **AgentEvo (2026)** already studies cost-aware agentic workflow evolution using adaptive exploration/refinement/crossover and a diverse Pareto archive.
- **DIVE (ICML 2026)** shows that executable, verifiable task diversity is central to out-of-distribution tool-use generalization; it derives tasks from executed tool traces rather than inventing unsupported tasks.
- **CATArena (ICML 2026)** evaluates iterative code-agent improvement separately from static generation proficiency and reports that current agents struggle to combine peer-learning with self-reflection effectively.

This is a better evidence-backed problem to investigate than simply assuming that more evolutionary generations produce more generalizable agents. It is not yet a novelty claim: each of these works covers a substantial part of the space.

## 2. Current closest-work map

| Work | Existing contribution | What it blocks |
|---|---|---|
| GSO, arXiv 2609.39148 | Direct train/test audit of evolving reusable skills; task-specific skill generation with a general guide | “Evolve reusable skills and evaluate held-out generalization” is not new. A new method must beat both reusable and task-specific skill baselines. |
| Faithful Self-Evolvers, ICML 2026 | Causal interventions that test whether agents actually depend on raw or condensed experience; IG-score analysis | “Measure whether memory is used” or “add a faithfulness score” is not new by itself. |
| H-EPM, ICML 2026 | Hybrid episodic/procedural memory and a graph of tool-to-tool dependencies augmented with contextual summaries | A tool graph or hybrid memory format alone is not an innovation. |
| AgentEvo, 2026 | Adaptive multi-stage evolution, performance/cost Pareto archive, cost-aware parent selection for workflows | Generic workflow evolution, cost Pareto search, and adaptive exploration/refinement/crossover are already covered. Cost will not be the thesis's central contribution. |
| DIVE, ICML 2026 | Executable task synthesis grounded in real tool traces; large-scale tool-pool and toolset diversity for OOD generalization | Task diversity and OOD evaluation need a strong baseline; task synthesis alone is not an EC method improvement. |
| CATArena, ICML 2026 | Tournament-based evaluation of iterative code-agent improvement and peer-learning/self-reflection | An evaluation framework alone is not an algorithmic contribution; static ability and improvement ability should not be conflated. |

Primary sources:
- GSO: https://arxiv.org/abs/2609.39148
- Faithful Self-Evolvers: https://proceedings.mlr.press/v306/zhao26aw.html
- Official Faithfulness repository: https://github.com/Dreamcatcher0622/Faithfulness
- H-EPM: https://proceedings.mlr.press/v306/li26bn.html
- AgentEvo: https://link.springer.com/article/10.1007/s40747-026-02325-0
- DIVE: https://proceedings.mlr.press/v306/chen26gj.html
- DIVE official repository: https://github.com/XinGuoZJU/DIVE
- CATArena: https://proceedings.mlr.press/v306/fu26a.html

## 3. A possible question to test — not an accepted candidate

Could evolutionary search learn **where to specialize and where to reuse** in an agent's experience representation, while requiring that any claimed improvement (a) transfers to held-out task variants and (b) is causally used during execution?

A possible genotype might encode a decomposition into:
1. stable procedure or tool-dependency structure;
2. task-conditioned slots/parameters;
3. retrieval or application conditions;
4. provenance and verification conditions.

But this is only a prompt for further literature and code review. It may collapse into an ordinary skill-architecture search, a weighted combination of generalization and faithfulness metrics, or a rediscovery of H-EPM/GSO. Those outcomes would not pass the novelty gate.

## 4. Main risks and stop conditions

1. **GSO is a strong counterargument to reusable-skill evolution.** Its task-specific skills outperform the reusable alternatives in its six reported benchmarks. Any proposed method must explain why a reusable/compositional representation is needed and compare against per-task skill generation.
2. **Faithfulness is already operationalized.** The ICML 2026 work uses controlled interventions on experience content and provides an official experiment repository. A new “experience-use score” alone is not novel.
3. **Memory and workflow evolution are crowded.** H-EPM, MemEvolve, AgentEvo, and existing agent-architecture/workflow search must be included in the closest-work matrix.
4. **The EC mechanism is currently missing.** There is no approved novel representation, variation operator, selection/replacement mechanism, or theorem. A fitness function that merely combines generalization and faithfulness is insufficient.
5. **Rights/reproducibility are not cleared.** The Faithfulness repository is retrievable but no LICENSE file was found at its root. DIVE code is retrievable and its README says code/data/model were released, but no LICENSE file was found at the inspected path. GSO, H-EPM, AgentEvo, and CATArena code availability has not yet been verified. Do not reuse code/data until the relevant terms are confirmed.

**Stop condition:** if the closest-work audit finds that the only difference is a new weighted fitness score, a new skill format, or another memory graph, stop and choose a different lane.

## 5. Next action

Deep-audit the GSO and Faithful Self-Evolvers papers and their actual evaluation code, then compare the proposed skill/experience representation against H-EPM and AgentEvo. Determine whether a concrete evolutionary operator or selection mechanism can address a specific failure that those methods do not already solve. Do not start API experiments or implementation yet.
