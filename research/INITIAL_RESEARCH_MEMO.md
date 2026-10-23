# Initial Research Memo: What the First Literature Pass Changes

**Date:** 2026-10-23  
**Stage:** Preliminary literature mapping  
**Status:** Direction not selected; no novelty claim is approved.

## 1. What we now know

The initial search surfaced several strong papers that directly overlap with the most obvious ideas for “EA + Agent”:

- AgentSquare already searches modular agent designs and combines module evolution, recombination, and a cheap in-context performance predictor.
- EvoAgent already uses evolutionary operators to generate multi-agent systems.
- AFlow already searches code-represented agent workflows using MCTS and execution feedback.
- HFlow extends workflow evolution to structure, prompts, and model backbones, with human-preference guidance, cost-aware utility, and hierarchical experience memory.
- GEPA already combines execution-trajectory reflection, prompt evolution, and Pareto-front lessons.
- ARTEMIS jointly optimizes mixed-type agent configurations with semantically aware genetic operators and black-box execution feedback.
- MemEvolve already meta-evolves memory architecture and experience, and reports cross-task, cross-model, and cross-framework transfer.
- EvoAgentX provides a common platform that integrates existing agent/workflow optimizers.
- AgentGym and AgentEvolver are important adjacent self-evolving agent systems, but should be distinguished from classic population-based EA methods.

The field is therefore more mature and more crowded than a simple “EA optimizes topology / prompts / memory” framing suggests.

## 2. What we should not do

Do not make any of the following the main contribution without a much narrower mechanism-level argument:

- “We use a genetic algorithm to optimize multi-agent topology.”
- “We evolve agent prompts.”
- “We automatically search agent workflows.”
- “We jointly optimize prompts and tool configurations.”
- “We use evolutionary computation to optimize memory parameters.”
- “We optimize accuracy and cost as multiple objectives.”
- “We use execution traces to reflect on failures and mutate prompts.”

These are useful design spaces and baseline ideas, but existing work directly covers them in different combinations.

## 3. Evidence that may support a narrower question

The first pass reveals a recurring practical tension: candidate-agent evaluation is expensive and stochastic, and gains may be task-dependent.

- AgentSquare uses a performance predictor to screen candidate designs and reports very low predictor cost relative to full evaluation. Therefore, a proposal about “cheap evaluation” must go beyond adding a surrogate.
- ARTEMIS reports that optimization may overfit to evaluation setups, that some improvements are not statistically significant, and that its expensive optimization can require substantial wall-clock time. Its authors identify optimization-potential prediction and cross-domain transfer as future directions.
- HFlow maintains cumulative performance/preference/cost metrics, uses a human-agent feedback mechanism, and acknowledges that calibrated LLM feedback may not represent the diversity of real user preferences.
- AFlow studies performance/cost trade-offs and notes that workflows optimized under different execution models do not always transfer equally.
- MemEvolve has already reported meaningful memory-system transfer across tasks, backbones, and agent frameworks, so a generic transfer-memory idea would overlap heavily.

The initial thought of **reliable evolutionary selection under uncertain and expensive agent evaluation** is not accepted as the thesis core. The user considers the finite-budget framing insufficiently compelling. Treat it only as a possible supporting mechanism/constraint if a stronger Agent capability problem requires it.

The next research pass should identify substantive failure modes in agent behavior and capabilities, then ask whether an evolutionary method can meaningfully improve them. Potential search lanes include planning, tool use, long-horizon reliability, adaptation/generalization, multi-agent coordination, credit assignment, and other areas supported by the literature. These are discovery lanes, not preselected ideas. Failure-conditioned operator choice and cross-task transfer remain possible mechanisms, but must be assessed as part of a more compelling problem and compared with GEPA/ARTEMIS/HFlow/MemEvolve and relevant traditional EC literature.

## 4. Thesis structure remains an objective, not a forced template

The target remains 2–3 connected innovation points and 2–3 small-paper submissions. Do not force three weak papers. A possible sequence would require each paper to answer a distinct question while sharing a common experimental substrate, but the actual decomposition must wait until the core problem is validated.

For every candidate contribution, require:
1. A specific failure or limitation supported by prior-work evidence.
2. A mechanism that differs from the closest work.
3. A falsifiable hypothesis.
4. A strong baseline and ablations.
5. A held-out generalization test.
6. A fixed-budget or cost-aware comparison where relevant, but only as a supporting evaluation dimension—not automatically the central research problem.
7. A feasible implementation and reproduction plan.

## 5. Immediate next action

Deeply audit the six closest papers listed in research/RELATED_WORK_MATRIX.md. Record their exact representations, variation operators, selection criteria, fitness definitions, data splits, costs, and limitations. Then search the broader evolutionary-optimization literature for existing solutions to the most promising bottleneck.

Only after that should we rank candidate umbrella problems and draft the proposal's 2–3 innovation points.
