# Candidate G G0 Reassessment: Parent-Pair Selection for EvoMAS

**Audit date:** 2026-10-26  
**Decision:** **G0 NOT PASSED for the current formulation — do not implement as written.**  
**Project boundary:** This review is recorded only in [yujian777555/openissue](https://github.com/yujian777555/openissue). It does not use or modify any other user project.

## Executive finding

Candidate G proposed task-family-conditioned, lineage-aware prediction of offspring improvement for structured multi-agent-system (MAS) configurations. The key quantity was the expected child improvement over the better parent, estimated from historical parent-pair outcomes.

A second-pass prior-art check found a closer 2026 method that combines diverse partner selection, brood recombination, surrogate estimation of offspring performance, and offspring selection. Combined with classical diverse partner selection, PAIR/LMEA, and recent cross-task evolutionary search, this means the current formulation does not yet offer a defensible algorithmic distinction. Applying an offspring-yield predictor to EvoMAS configurations is a potentially useful experiment, but **the application context alone is not a sufficient novelty claim**.

This is a negative result for the current formulation, not a claim that all research on evolutionary MAS configuration search is exhausted. Do not start expensive LLM experiments for Candidate G unless a materially different mechanism is specified and passes a fresh prior-art gate.

## 1. New direct prior art

### P99 — Genetic Programming with Advanced Diverse Partner Selection for Dynamic Scheduling (2026)

- Authors: Meng Xu, Yi Mei, Fangfang Zhang, Yew Soon Ong, Mengjie Zhang.
- Venue: *Expert Systems with Applications*, volume 322, article 132158 (published 2026-08-01).
- Primary source: https://www.sciencedirect.com/science/article/pii/S0957417426010717
- DOI: https://doi.org/10.1016/j.eswa.2026.132158
- Reported mechanism: advanced diverse partner selection, brood recombination, a surrogate model to estimate candidate offspring performance, and offspring selection.
- Relevance: this is a direct combination of parent-pair selection and offspring-quality estimation. It substantially narrows the room for claiming that “learn which parent pairs produce better offspring” is itself new.

### Previously registered closest work

- **Diverse Partner Selection with Brood Recombination (2018):** https://doi.org/10.1016/j.asoc.2018.03.035 — uses parent phenotype strengths and weaknesses to estimate crossover benefit and allows beneficial pairs to produce more offspring.
- **PAIR (2025 preprint):** https://arxiv.org/abs/2503.03239 — prompts an LLM to select mates using fitness, diversity, and crossover compatibility.
- **LMEA (2023 preprint):** https://arxiv.org/abs/2310.19046 — uses an LLM to select parents and perform crossover/mutation.
- **MECo (2026 preprint):** https://arxiv.org/abs/2610.03316 — task-conditioned populations, transfer-gap-guided interactions, and complementary cross-task selection.
- **MTHS (ICML 2026):** https://proceedings.mlr.press/v306/liu26ge.html — two-level evolution of task-agnostic metaheuristics and task-specific programs with cross-task transfer.
- **EoH-S (AAAI 2026):** https://ojs.aaai.org/index.php/AAAI/article/view/41038 — complementary population management and memetic search.
- **EvoMAS (ICML 2026):** https://proceedings.mlr.press/v306/hu26bg.html and official implementation https://github.com/amazon-science/EvoMAS.

## 2. Gate G0 assessment

| Proposed ingredient | Existing coverage | Assessment |
|---|---|---|
| Select parent pairs based on expected child improvement | Diverse Partner Selection + Brood Recombination; advanced DPS methods | Not new by itself |
| Predict offspring quality using a learned/surrogate model | GPDPS⁽ᵒ⁾ (2026) explicitly estimates candidate offspring performance and selects offspring | Direct overlap |
| Ask an LLM to judge pair compatibility | PAIR and LMEA | Direct overlap |
| Condition evolution/selection on task differences | MECo and MTHS; related complementary-set selection in EoH-S | Direct overlap at the general mechanism level |
| Apply the above to structured MAS configurations with explicit lineage and fallback labels | Relevant domain-specific gap in EvoMAS's trace design, but not yet a distinct algorithm | Insufficient by itself |

Candidate G's proposed estimator,
\[
Q(i,j\mid t,H)=\mathbb{E}[R(\mathrm{child}(i,j))-\max(R_i,R_j)\mid t,H],
\]
is a reasonable research quantity. Defining and estimating this quantity, however, does not by itself distinguish the method from offspring-benefit mating and surrogate-assisted offspring selection. Adding task-family labels, uncertainty, or lineage metadata would be an implementation/data-model extension unless accompanied by a nontrivial algorithmic contribution and evidence that it adds value beyond the closest methods.

**Gate result:** the current Candidate G formulation does not pass G0. Re-label it **PIVOT / DO NOT IMPLEMENT AS WRITTEN**. Reopen only if a formal method is identified that is not reducible to surrogate-assisted offspring prediction, classical mating selection, PAIR-style compatibility ranking, or generic task-conditioned transfer.

## 3. Data feasibility and identifiability

The current `openissue` repository contains research documents but no EvoMAS run logs, lineage tables, or offspring-outcome dataset. The official EvoMAS README also states that task data are not shipped with the repository and must be prepared separately; its output artifacts are generated by running the benchmark scripts. There is therefore no existing dataset on which to perform the proposed offline predictive-value analysis.

The inspected EvoMAS source has two relevant properties:

1. Its crossover branch selects the two configurations with the highest current rewards.
2. Its per-step `evolution_operations` record stores action type, step, accuracy, reward, improvement, a generic change label, and accuracy change, but not parent IDs or parent-pair identity.

As a result, the currently available traces cannot support pair-level outcome reconstruction. Even after adding lineage logging, observations from a top-two-only policy would be selection-biased and provide little coverage of alternative pairs. Any future empirical test would need a controlled parent pool, recorded parent-pair assignments, fixed task IDs, and a deliberate pair-assignment design. Synthetic data may test code and estimators, but cannot establish that the mechanism improves real LLM-generated MAS configurations.

This is an identifiability and evidence problem, not a proposal to make finite-budget evaluation efficiency the thesis's central contribution.

## 4. Executability/fallback issue: retain the caveat, not an unsupported claim

The official code audit verified that invalid mutation output falls back to the original configuration and invalid crossover output falls back to the better parent. The public ICML paper page claims improved executability, but the exact published execution-rate denominator and the incidence of fallback were **not independently recomputed in this review**. A secondary review also flags this as a potential measurement confound; that is a lead for further verification, not primary-source proof.

Therefore:
- It is fair to report the code-level fallback behavior.
- It is fair to require separate counts for attempted-child validity, repair/fallback, successful execution, and task success in future evaluations.
- It is **not** currently justified to state that the published executability rate is inflated or that the paper's task-performance result is invalid.
- A metric-accounting correction alone would be a reproducibility finding, not the thesis's main algorithmic innovation.

Primary code entry points:
- https://github.com/amazon-science/EvoMAS/blob/main/main.py
- https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/metamodel.py
- https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/mas_index.py
- https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/experience.py

## 5. Consequence for the thesis search

1. Keep the EvoMAS code audit as a verified baseline audit and negative research finding.
2. Do not spend LLM calls or implement the current Candidate G predictor.
3. Resume mechanism-level candidate search across strong 2024–2026 Agent + evolutionary-computation papers. The next candidate must target an observable agent capability/behavior limitation and identify a specific evolutionary representation, variation, selection, or replacement mechanism that improves it.
4. Require a closest-work matrix, data/benchmark feasibility check, and explicit stop criteria before implementing a new candidate.
5. Do not choose a thesis title or force three contributions until at least one core direction survives these gates.

## Sources and evidence boundaries

- Primary paper and code links are listed above.
- The 2018 DPS + BR abstract is available at https://www.sciencedirect.com/science/article/pii/S1568494618301571.
- PAIR and LMEA are preprints; their existence establishes overlap but should not be described as peer-reviewed publications without a separate venue check.
- The GPDPS⁽ᵒ⁾ article is a 2026 journal publication and is the most direct newly found overlap in this pass.
- The precise effect of EvoMAS fallback behavior on reported executability remains unresolved.
