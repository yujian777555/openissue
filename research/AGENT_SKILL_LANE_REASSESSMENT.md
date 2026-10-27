# Reassessment: Agent Skill Generalization and Experience Faithfulness

**Audit date:** 2026-10-27  
**Decision:** This lane does **not** pass as a thesis candidate in its current broad formulation. Keep it as related-work context; do not implement a new method from this framing.  
**Project boundary:** This document belongs only to yujian777555/openissue. Communication evolution is excluded from the thesis candidate pool per the user's explicit instruction.

## 1. Why the first screen is no longer sufficient

The first screen already identified GSO, Faithful Self-Evolvers, H-EPM, AgentEvo, DIVE, and CATArena. A second pass through current 2026 work shows that almost every obvious narrowing is now directly occupied:

- **GSO** studies held-out generalization of evolving skills and learns a metaskill that writes a task-specific skill at test time. It reports the best test score among the compared methods on six benchmarks, while explicitly noting that its experiment does not isolate which part of the whole method causes the gain and that cross-task-family metaskill transfer remains open.
  - Paper: https://arxiv.org/abs/2609.39148
- **SkillComposer (Findings of EMNLP 2026)** decomposes skill evolution into create, improve, and merge operations and reports cross-domain/task-type generalization.
  - Paper: https://aclanthology.org/2026.findings-emnlp.759/
- **Rep2Skill** uses internal representation trajectories to localize deviations from successful execution dynamics and guide targeted textual-skill revisions. This blocks the generic claim that skill edits should be grounded in more fine-grained execution evidence.
  - Paper: https://arxiv.org/abs/2609.39149
- **EvoSkill** already uses failure-driven skill creation/refinement and Pareto selection over held-out validation performance.
  - Paper: https://arxiv.org/abs/2603.02766
- **MetaMem** evolves meta-memory for using fragmented historical knowledge, while **Live-Evo** updates experience weights from online feedback and decays stale or misleading experiences.
  - MetaMem: https://aclanthology.org/2026.findings-acl.270/
  - Live-Evo: https://arxiv.org/abs/2602.02369
- **SelSkill** learns when to invoke or skip a relevant skill at a particular decision point.
  - Paper: https://aclanthology.org/2026.findings-emnlp.222/
- **Skill Following** introduces a matched same-task measure (RAE) to test whether retrieved skills actually help on the tasks where they are invoked. A new experience-faithfulness score alone is therefore not a novelty claim.
  - Paper: https://aclanthology.org/2026.findings-emnlp.244/
- **H-EPM** combines episodic context with procedural tool-transition graphs; **AgentEvo** evolves executable workflows with adaptive multi-stage search; **DIVE** targets task diversity for out-of-distribution tool use.
  - H-EPM: https://proceedings.mlr.press/v306/li26bn.html
  - AgentEvo: https://link.springer.com/article/10.1007/s40747-026-02325-0
  - DIVE: https://proceedings.mlr.press/v306/chen26gj.html

## 2. Mechanism-level conclusion

The following are not sufficient contributions on their own:

1. Adding held-out generalization or experience-faithfulness to a weighted fitness function.
2. Introducing another skill format, memory graph, or create/improve/merge lifecycle.
3. Adding internal-state signals to textual skill editing without a distinct EC mechanism.
4. Adding an invoke/skip decision, online forgetting rule, or same-task skill-use metric.
5. Replacing the baseline with a new benchmark while leaving the algorithm unchanged.

This is not a claim that all skill research is exhausted. It is a decision that the current umbrella is too broad and too close to direct 2026 prior art to be a responsible thesis direction without a sharply different genotype, variation operator, selection/replacement rule, or formal property.

## 3. Reproducibility and rights caveats

- GSO's paper provides a detailed protocol and locked task splits, but no official code repository was found in the targeted search.
- SkillComposer is a published paper, but no official code repository was found in the targeted search.
- Rep2Skill's paper was located; a reproducible official implementation was not verified in this audit.
- The Faithfulness and H-EPM repositories are inspectable, but their roots did not expose a LICENSE file during direct retrieval. Do not reuse their code/data without resolving terms.
- Live-Evo, MetaMem, and SelSkill have public code links, but each benchmark and dependency still needs its own license/reproducibility check before reuse.

## 4. Decision and next step

**Decision: downgrade this lane; do not implement it as a thesis candidate.**

The next exploratory lane is black-box agent test-time search, starting from Agentic Monte Carlo (AMC) as an inspectable ICML 2026 baseline. This is not yet approved either: the exact evolutionary operator must be distinguished from SMC, adaptive SMC, lineage-preserving resampling, and existing tool-policy evolution. See research/BLACK_BOX_AGENT_TEST_TIME_SEARCH_LANE_SCREEN.md and research/AMC_CODE_AUDIT.md.
