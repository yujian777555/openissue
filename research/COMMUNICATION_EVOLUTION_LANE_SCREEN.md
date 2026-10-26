# Communication Evolution Lane — Initial Prior-Art Screen

**Date:** 2026-10-26  
**Status:** exploratory screening lane only; **not an approved thesis topic or innovation claim**.  
**Project boundary:** All research records and project-state changes are maintained in yujian777555/openissue only.

## 1. Why this lane is being screened

Communication is an observable part of multi-agent behavior: the content, structure, and protocol of messages can determine whether agents share evidence, coordinate roles, and generalize when the partner or task changes. This could support an evolutionary-computation contribution if a concrete failure mode and a distinct evolutionary mechanism can be identified.

However, generic communication-protocol evolution and topology optimization are already directly studied. The goal of this memo is to map the immediate overlap and specify a narrow follow-up gate—not to promote “evolve agent communication” as a novel idea.

## 2. Direct prior art found in the initial screen

### P100 — When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning (CLSR)

- Authors: Zhengqi Pei, Qingming Huang, Shuhui Wang.
- Venue: ICML 2026, PMLR 306:97643–97678.
- Primary source: https://proceedings.mlr.press/v306/pei26a.html
- Method: multiple LLM agents invent, evolve, and share compact Language Symbolism Frameworks (LSFs), with symbols, usage rules, and message-passing contracts. A latent-free router selects or composes protocols per query; the reported objective trades task correctness against token cost.
- Code availability: the software URL listed by the PMLR page, https://github.com/pzqpzq/LSF_MDia, currently returns 404 in the web check performed for this screen. Treat runnable-code availability as unverified, not as proof that no code exists elsewhere.
- Overlap consequence: generic evolutionary invention and sharing of compact multi-agent communication protocols is already directly covered.

### P101 — MOC: Multi-Order Communication in LLM-based Multi-Agent Systems

- Authors: Yao Guan, Lin Wang, Zhihui Lu, Ziyi Wang, Wenzhu Yan, Qiang Duan.
- Venue: ICML 2026, PMLR 306:37603–37619.
- Paper: https://proceedings.mlr.press/v306/guan26i.html
- Official code: https://github.com/yao-guan/MOC
- Method: constructs multi-order evidence streams for multi-hop communication and uses Semantic-Topological Merging to preserve semantic fidelity while reducing redundant messages.
- Overlap consequence: multi-hop evidence aggregation and semantic/topological message consolidation are established mechanisms; a new evolutionary message-merging heuristic alone would be insufficient.

### P102 — Dynamic Generation of Multi LLM Agents Communication Topologies with Graph Diffusion Models (GTD)

- Authors: Eric Hanchen Jiang et al.
- Venue: ACL 2026, Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics, pp. 38042–38060.
- Paper: https://aclanthology.org/2026.acl-long.1764/
- Code link listed by the ACL Anthology: https://anonymous.4open.science/r/diffusion_agent-953C
- Method: iterative guided graph diffusion builds task-adaptive communication topologies; a lightweight proxy predicts multi-objective rewards such as accuracy, utility, and cost.
- Overlap consequence: generic topology search, task-adaptive communication graphs, and proxy-guided multi-objective topology construction are already directly studied.

### P103 — GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions

- Authors: Elias Stengel-Eskin, Newton Sander, Carlos Bonetti, Sasha Boguraev, James Bowler, Hale Sirin, Simon Kirby.
- Status: arXiv preprint submitted 2026-09-01.
- Paper: https://arxiv.org/abs/2609.01491
- Official platform: https://github.com/agencyenterprise/GlossoGen
- License shown by the repository: MIT.
- Method/environment: controlled multi-agent simulations with event-sourced logs, environment state, swap/fork interventions, and post-hoc metrics. The paper reports that communication pressure, a postmortem stage, and model strength affect language emergence; emergent protocols may become difficult for humans to understand, and weaker agents may learn a language after it has emerged.
- Overlap consequence: the platform is useful for studying communication evolution and transfer, but it is an experimental substrate rather than an evolutionary algorithm contribution by itself.

### P104 — Emergent Language: A Survey and Taxonomy

- Authors: Jannik Peters et al.
- Venue: Autonomous Agents and Multi-Agent Systems, 2025.
- Paper: https://link.springer.com/article/10.1007/s10458-025-09691-y
- Relevance: surveys emergent communication and highlights transfer/zero-shot coordination, language properties, communication-channel design, and evolution of communication channels as active research themes.
- Overlap consequence: protocol evolution and cross-population communication must be compared with the broader emergent-language literature, not only LLM-agent workflow papers.

## 3. Initial conclusion

The following broad claims are **not** defensible as new contributions on their own:

- evolving a compact communication protocol among LLM agents;
- optimizing a multi-agent communication topology;
- merging or compressing multi-hop messages;
- allowing agents to invent shorthand under communication pressure;
- using task correctness plus a cost term to select communication strategies.

The token/cost axis can be a secondary metric, but it should not become the thesis's central problem merely because it is measurable.

## 4. Narrow follow-up question to test—not a candidate approval

One possible capability-level question is:

> Can an evolutionary method produce communication protocols that preserve coordination quality when agent identities/models are replaced and task compositions are held out, while keeping protocol semantics verifiable and messages human-monitorable?

This question is only worth pursuing if the closest-work audit finds a specific unaddressed failure. “Generalize to unseen agents” and “keep language interpretable” are not automatically novel; they are already adjacent to zero-shot coordination, protocol transmission, CLSR, and GlossoGen.

The next audit must determine:
1. Which exact protocol/genotype CLSR evolves and whether its method can be reproduced from an authoritative implementation.
2. Whether CLSR already evaluates heterogeneous agent replacement, unseen partner models, and held-out task compositions.
3. Whether MOC and GTD solve the same failure through message aggregation or topology adaptation.
4. Whether GlossoGen provides a valid, licensed, repeatable test environment for the proposed failure mode, and what its current scenarios can and cannot measure.
5. Which evolutionary-computation mechanism would be materially different from the existing protocol-evolution method—not merely another objective weight or prompt.
6. Whether an external task-success oracle can measure coordination independently of the communication protocol's own self-report.

## 5. Stop criteria

Do not promote this lane to Candidate H if:
- CLSR already addresses the proposed transfer/robustness failure;
- the only difference is using a different scenario or model family;
- the contribution reduces to adding human-readability or transfer as another weighted objective;
- no distinct evolutionary representation/operator/selection mechanism is specified;
- the benchmark cannot separate genuine coordination from shared-model prior knowledge or leakage;
- the only measurable gain is token reduction without a meaningful capability or robustness improvement.

**Current decision:** continue a focused prior-art and feasibility audit of this lane as one option in the broader search. No implementation, benchmark adoption, thesis title, or innovation point is approved.
