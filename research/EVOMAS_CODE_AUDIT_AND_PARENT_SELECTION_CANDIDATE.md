# Direct Code Audit: EvoMAS and a Candidate Improvement to Evolutionary Parent Selection

**Audit date:** 2026-10-26  
**Repository inspected:** [amazon-science/EvoMAS](https://github.com/amazon-science/EvoMAS), branch main  
**Thesis workspace:** [yujian777555/openissue](https://github.com/yujian777555/openissue) only. No files or conclusions were written to any other user project.  
**Status:** A concrete improvement candidate is now defined, but its novelty gate remains OPEN. No experiment or thesis topic is approved.

## 1. Why audit EvoMAS?

EvoMAS is an ICML 2026 paper with a public implementation. It is a useful strong baseline because it evolves structured multi-agent configurations using LLM-guided selection, mutation, crossover, execution feedback, and experience memory. The goal here is not to claim that EvoMAS is weak overall, but to find a precise mechanism whose improvement can be tested.

Primary paper: [PMLR / ICML 2026](https://proceedings.mlr.press/v306/hu26bg.html)  
Official code: [amazon-science/EvoMAS](https://github.com/amazon-science/EvoMAS)  
Repository license: CC BY-NC 4.0 (per official README/license); check license terms before redistributing or commercial use.

## 2. Directly confirmed code-level observations

### Observation A — invalid generated offspring can be silently replaced by a parent

- In src/meta_model/metamodel.py, generation validation failure returns the original configuration (lines 407–418): [source](https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/metamodel.py#L404-L418).
- In crossover, invalid offspring returns whichever parent has the higher observed accuracy (lines 594–608): [source](https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/metamodel.py#L594-L608).
- This is a sensible robustness fallback for the running system, but it means **execution of the returned configuration is not the same measurement as validity of the attempted offspring**. If execution-rate metrics count the fallback as a successful generated system without separately reporting fallback incidence, the metric cannot distinguish a valid offspring from a failed generation followed by parent reuse.
- The official paper's exact execution-rate calculation and fallback denominator must be checked against the full paper/evaluation code before claiming the reported number is inflated. This audit has not independently reproduced that metric.

**Research opportunity:** distinguish proposal validity, repair/fallback rate, executable-child rate, and final system task success. Consider a typed configuration genotype and schema-preserving variation operators, but compare against ordinary repair/retry and do not treat type safety alone as a novel algorithm.

### Observation B — crossover chooses the two highest-reward configurations in the current trace

In main.py, when crossover is selected, the implementation sorts all_rewards and chooses the top two configurations (lines 676–690): [source](https://github.com/amazon-science/EvoMAS/blob/main/main.py#L672-L693). The default mutation probability is 0.8, so crossover is a fixed minority action in the default configuration (see main.py constants).

This is a fitness-first pairing rule. It does not use an explicit estimate of whether a given pair tends to produce useful offspring on a particular task family. The LLM crossover prompt can reason about parents, but the algorithm does not record a persistent parent-pair offspring-yield statistic.

The per-step trace records action type, step, accuracy, reward, and a generic change label, but not parent IDs or parent-pair identity (main.py, lines 720–729): [source](https://github.com/amazon-science/EvoMAS/blob/main/main.py#L720-L729). Consequently, this trace cannot directly estimate which parent pairs repeatedly generate useful children.

**Research opportunity:** retain lineage and estimate task-conditioned offspring yield rather than assuming that the two individually strongest configurations are the best pair to recombine.

### Observation C — the selection index ranks by cumulative wins and average accuracy

MASIndex.get_selection_context sorts configurations by total_wins, then avg_accuracy, and presents at most 20 entries (lines 175–213): [source](https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/mas_index.py#L175-L213). It also exposes recent solved-task snippets.

Cumulative wins are not a rate and can favor older or more frequently evaluated configurations when exposure differs. The LLM still sees task descriptions and history, so this is a potential ranking bias, not proof that actual selection is wrong in every run. A controlled audit should compare win count, win rate, task-conditioned success, and uncertainty-aware ranking.

### Observation D — experience records lack explicit parent lineage

The ActionExperience schema stores query, action type, config changes, old/new accuracy, success, and an LLM-authored analysis, but no parent IDs, child ID, task-family ID, or repeated-trial uncertainty (lines 15–32): [source](https://github.com/amazon-science/EvoMAS/blob/main/src/meta_model/experience.py#L15-L32).

The evolution loop records each operation's type and outcome but not parent-pair identity. This prevents the current memory from directly learning task-conditioned pair compatibility from observed offspring outcomes. The natural-language explanation can be useful, but it is not a substitute for lineage-linked quantitative evidence.

## 3. Candidate G — task-conditioned evolvability-aware parent-pair selection

**Working question:** For LLM-generated multi-agent configurations, can selection based on observed offspring yield and complementary task-family performance outperform selecting the individually strongest parents, while preserving configuration validity and generalization?

This is an extension candidate, not a novelty claim.

### Proposed mechanism (to falsify)

1. **Lineage-aware evaluation record.** Store immutable parent IDs, offspring ID, operator type, task-family descriptors, task IDs, repeated outcome metrics, and whether the returned configuration was a genuine offspring, repaired offspring, or fallback parent.
2. **Task-conditioned utility.** Estimate each configuration's performance on task families with uncertainty, instead of using cumulative win count as the main ranking signal.
3. **Pairwise offspring-yield model.** For a candidate pair (i,j), predict the distribution of child quality from prior observed crossover outcomes for similar task families. The model must account for sparse pairs and avoid overfitting to one query.
4. **Complementarity-aware mating.** Select parents by predicted child improvement and useful specialization complementarity, with an explicit exploration term for uncertain pairs. Do not use raw structural dissimilarity as a proxy for complementarity.
5. **Validity-aware variation accounting.** Enforce schema/semantic constraints where possible; count failed proposals and fallback separately. Never credit a parent fallback as a valid offspring.
6. **Generalization test.** Train the selection rule on some task families and evaluate on held-out task families and task combinations. Freeze the test families before tuning.

A minimal formal target is:
Q(i,j|t) = E[R(child(i,j)) - max(R_i,R_j) | t,H],
where t is the task family and H is the observed lineage history. This expected improvement is uncertain; selection should use a calibrated posterior or confidence-aware estimate rather than a point estimate alone.

### Why this might be an EA contribution

The target is the evolutionary mating/parent-selection mechanism—not prompt engineering alone. The hypothesis is that parent fitness and parent reproductive value differ: a strong individual need not be a useful recombination partner, and pair utility may depend on task family.

This is only valuable if observed pair-level offspring outcomes add predictive information beyond:
- the individual fitness of each parent;
- simple structural diversity;
- task similarity;
- standard uncertainty-aware selection;
- generic LLM-based pair ranking.

## 4. Closest-work audit and novelty risks

| Work | Overlap | Required distinction |
|---|---|---|
| [EvoMAS (Hu et al., ICML 2026)](https://proceedings.mlr.press/v306/hu26bg.html) | Exact target setting: evolutionary generation of MAS configurations, LLM selection/mutation/crossover, execution feedback, experience memory. | The proposed method must show a specific selection-mechanism improvement, not just more metadata or an extra scoring term. |
| [EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows (Wei et al., ICML 2026)](https://proceedings.mlr.press/v306/wei26m.html) | Uses a diverse repertoire of evolutionary strategies, adaptive strategy selection, role-level evolution, and curriculum-guided workflows. | Direct baseline for adaptive evolutionary strategy/operator choice; do not claim adaptive operator selection itself as new. |
| [EvoAgent (NAACL 2025)](https://aclanthology.org/2025.naacl-long.315/) | Evolves agents using crossover/mutation and selection. | Compare against the exact published implementation/protocol where feasible. |
| [MECo: Multi-Task Evolution for Zero-Shot Cross-Problem Generalization using LLMs](https://arxiv.org/abs/2610.03316) | Task-conditioned populations, cross-task transfer gap, recombination, and complementary coverage selection for heuristics. | Generic task-conditioned transfer or coverage-based archive selection is already covered in automated heuristic design. |
| [MTHS: Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs](https://proceedings.mlr.press/v306/liu26ge.html) | Two-level evolution of task-agnostic metaheuristics and task-specific programs with cross-task knowledge transfer. | A general shared/task-specific evolution split alone is not new. |
| [MES-RET: Breaking Multi-Task Curse](https://proceedings.mlr.press/v306/li26dc.html) | Negative-transfer control and reward-weighted knowledge transfer for many-task evolutionary optimization. | Compare against robust transfer gating; task similarity alone is insufficient. |
| [PAIR: LLM-Guided Parent Selection in Evolutionary Algorithms](https://arxiv.org/abs/2503.03239) | Uses LLM reasoning about fitness, diversity, and crossover compatibility to select mating pairs. | Pair compatibility and LLM-guided mating are already studied. The candidate must add empirically learned, task-conditioned offspring-yield evidence, not simply ask an LLM to rank pairs. |
| [On the Dynamics of Mating Preferences in Genetic Programming](https://link.springer.com/article/10.1007/s12293-025-00466-2) | Studies mating restrictions/preferences as a diversity and premature-convergence control. | Standard mating-selection methods must be included as baselines. |
| [What Makes an LLM a Good Optimizer? (Findings of ACL 2026)](https://aclanthology.org/2026.findings-acl.1252/) | Finds that successful LLM-guided evolutionary search tends to make localized refinements; novelty alone does not predict final quality. | Use trajectory diagnostics and test whether offspring-yield selection improves search quality, not only configuration novelty. |
| [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](https://arxiv.org/abs/2608.20274) | Finds that skill transfer can be negative; subtask-level and text-form skills transfer better on average in its evaluated setting, and joint specificity/abstractness predicts utility. | Motivation for transfer diagnostics, not evidence that the proposed EA is novel. |

## 5. Minimum experiment to decide whether the candidate survives

### Gate G0 — algorithmic distinctness

Write a formal definition of offspring-yield utility and show it differs from PAIR's LLM-based compatibility judgment, standard mating selection, task-conditioned fitness, and MECo/MES-RET transfer scoring. If the only difference is an extra historical feature or another weighted sum, reject.

### Gate G1 — measurement integrity

For every proposal, log raw offspring validity, repair/fallback status, execution success, task success, and parent IDs. Verify that invalid offspring cannot silently inflate offspring-executability. Use deterministic schema checks before any model calls.

### Gate G2 — selection value

Compare:
- EvoMAS's original LLM parent selection and fitness-first crossover;
- random parent pairing;
- top-fitness pairing;
- diversity-aware pairing;
- PAIR-style LLM compatibility selection;
- uncertainty-aware task-conditioned fitness selection;
- proposed lineage-based offspring-yield selection.

Use identical parent pools, variation prompts, model, evaluation task IDs, and number of candidate evaluations.

### Gate G3 — transfer and robustness

Train on a set of task families; test on held-out families and combinations. Report mean success, variance across seeds, child-validity rate, fallback rate, average child improvement over parents, and per-family regressions. Do not tune on the held-out set.

### Stop criteria

Reject Candidate G if:
- the pair-yield model cannot predict held-out offspring improvement beyond parent fitness and structural diversity;
- PAIR or ordinary uncertainty-aware selection matches it;
- gains disappear under fixed evaluation tasks and matched calls;
- gains occur only on seen task families;
- apparent executability gains come from fallback-to-parent behavior rather than valid offspring.

## 6. Decision

**Candidate G is worth a focused prior-art and code-reproduction audit, not yet a thesis topic.** It is a concrete improvement path on an existing strong paper, and the official code exposes measurable issues in how offspring validity and parent-pair lineage are represented. The strongest novelty risk is that evolvability-aware mating and task-conditioned parent selection may be considered incremental extensions of PAIR, multi-task evolutionary optimization, and adaptive strategy selection.

The next step is to verify the EvoMAS paper's exact execution-rate denominator and fallback reporting, inspect its published ablations, then implement only a small offline analysis of existing logs or synthetic lineage data to test whether pair-level offspring yield is predictable. No full LLM experiment should start until G0 passes.
