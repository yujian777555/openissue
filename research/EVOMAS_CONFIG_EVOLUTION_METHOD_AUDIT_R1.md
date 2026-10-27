# EvoMAS: Evolutionary Generation of Multi-Agent Systems — Method Audit R1

**Audit date:** 2026-10-27. **Status:** Primary full text and official code inspected. Distinct from Wei et al.'s *EvoMAS: Heuristics in the Loop*.  
**Paper:** Hu et al., ICML 2026, arXiv:2602.06511v4. https://arxiv.org/html/2602.06511  
**Official code:** https://github.com/amazon-science/EvoMAS  
**Code license:** CC BY-NC 4.0; non-commercial use only, with attribution.

## 1. Two separate ICML 2026 papers share the name EvoMAS

- **Wei et al., “EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows”** — PMLR 306:133736–133763. The official abstract confirms seven evolutionary strategies, adaptive selection, role-level evolution, curriculum, and the Cyber Creator reflective meta-controller. Exact reward/state equations remain unverified in this pass.
- **Hu et al., “EvoMAS: Evolutionary Generation of Multi-Agent Systems”** — PMLR 306:45989–46021, arXiv:2602.06511v4. This has a readable full HTML paper and official code. Do not merge these papers or citations.

## 2. Exact method of Hu et al.

The optimization object is a structured MAS configuration: communication DAG, agent backbone models, prompts, tool sets, and input/output agent design. Four operations are defined:

1. **Select:** retrieve configurations by task relevance, metadata, historical performance, and complementary capability/diversity.
2. **Mutate:** execution traces guide diagnosis of the primary bottleneck; each mutation changes exactly one component type, such as prompts, model assignments, tools, or communication topology.
3. **Crossover:** use two parents and their traces. The offspring inherits the entire communication topology from one parent, then recombines agent-level prompts/models/tools from both parents.
4. **Consolidate:** summarize mutation/crossover operations and results into experience memory.

For each task, the method selects k candidates, executes them, performs up to n evolution steps, evaluates offspring, and returns the highest-reward configuration. This is per-query evolution plus cross-query learning, not a classical EA with a fixed operator-probability vector.

Reward: R(q,C) = Metrics(q,C) − β · Cost(C). Metrics is an LLM-as-judge scalar for correctness, completeness, and reasoning quality; Cost combines token usage and latency. The paper includes β sensitivity and reports gains from explicit task metrics when available.

After each query, the best configuration is added to the pool. Memory stores the query, best configuration, and a summary of useful evolutionary patterns. At each evolutionary step, up to three similar prior experiences are retrieved by task-description similarity. The official code's pool update checks whether the new reward exceeds the maximum parent reward by a threshold.

## 3. Prior art already covered

Hu et al. already covers execution-trace-conditioned mutation, one-component-type mutations, structured crossover, task-relevance/performance-history parent selection, reward-based pool updates, trace consolidation, cross-query memory, and task-conditioned reuse. None is a standalone novelty claim.

| Candidate mechanism | Evidence in Hu et al. | Consequence |
|---|---|---|
| Feedback-conditioned mutation | Explicit | Not new |
| Prompt/model/tool/topology configuration evolution | Explicit | Not new for MAS configuration search |
| Structured crossover | Explicit | Not new |
| Task-conditioned selection and parent-relative acceptance | Explicit | Not new |
| Cross-query experience memory | Explicit and ablated | Not new |
| Mutation strength calibrated to realized behavior displacement | Not identified in reviewed method/code | Possible distinction; compare with ELMER/LVPG |
| Operator continuation value conditioned on realized displacement | Not identified in reviewed method/code | Candidate gap, not certified; compare with Wei HIL and classical AOS |
| Classical EA parameter control (mutation rate/operator probabilities/population size) | Not the main method; β is a reward trade-off parameter, not adaptive EA operator control | Supports focusing on EC parameter/credit control rather than adding configuration-evolution components |

“Not identified in the reviewed method/code” is deliberately narrower than claiming no analogous concept exists anywhere. The candidate distinction is explicit conditioning of lineage continuation value on realized behavior displacement under matched parent/task/state comparisons.

## 4. Feasibility and license

- Evaluated on BBEH, WorkBench, SWE-Bench-Lite, and SWE-Bench-Verified using large models including Claude and Qwen3-235B/Qwen3-Coder-480B. A full reproduction is not a low-cost first smoke test.
- Benchmark data are not shipped in the repository; setup downloads datasets and uses external model providers and/or large local models.
- Official code is CC BY-NC 4.0, not MIT/Apache. Preserve attribution and non-commercial terms; do not assume unrestricted commercial reuse or relicensing.
- Treat this as a strong conceptual/method baseline. A direct comparison must align optimization objects or compare the relevant operator/credit component.

## 5. Research decision

The Agent+EC space is crowded: Wei et al. cover adaptive strategy portfolios and reflective meta-control; Hu et al. cover feedback-conditioned mutation/crossover and cross-query memory; EvoTool covers blame attribution, targeted mutation, and diversity-aware selection. The current candidate remains **scale-conditioned lineage-value credit**: test whether operator continuation value should be conditioned on realized behavior displacement under matched parent/task/state comparisons. This remains a hypothesis, not a novelty verdict.

## References

- Hu, Y. et al. (2026). *EvoMAS: Evolutionary Generation of Multi-Agent Systems*. ICML 2026, PMLR 306:45989–46021. https://proceedings.mlr.press/v306/hu26bg.html
- Official code: https://github.com/amazon-science/EvoMAS
- Wei, Y. et al. (2026). *EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows*. ICML 2026, PMLR 306:133736–133763. https://proceedings.mlr.press/v306/wei26m.html
