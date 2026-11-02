# API-Backed Agent × Evolutionary Computation — Mechanism-Level Prior-Art Audit R1

**Date:** 2026-11-03  
**Repository:** `yujian777555/openissue` only  
**Status:** Research audit; the research question is narrowed, but no novelty claim, final algorithm, or experiment authorization is approved.  
**User requirement:** The main LLM is called through a hosted API. The thesis must train/improve the Agent-side system while keeping the foundation model fixed during ordinary inference/training.

## 1. Executive conclusion

The architecture is technically feasible, but the broad research claim is already crowded.

1. A hosted API LLM can remain the Agent's reasoning executor while separate Agent-side components are trained locally. The most concrete implementation reference is **Agentic Monte Carlo (AMC)**: its official code exposes an OpenAI-compatible `APIModel` for the task-solving LLM, while its value function is trained locally with a LoRA adapter and regression head.
2. A lightweight state-conditioned controller around a frozen LLM is already studied directly by **Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning**. It defines a finite-horizon Harness MDP, seven structural actions, terminal task-rubric reward, and offline advantage-weighted regression (AW).
3. General evolution of executable harnesses is also directly covered by **TTHE**, **Meta-Harness**, **Self-Harness**, **AutoHarness**, and **HarnessX**. Generic claims such as “evolve the Agent harness,” “use populations to improve a frozen API Agent,” “use execution traces to guide edits,” or “train an Agent controller” are not sufficient innovations.
4. **EvoHarness-RL** is an important adjacent work but uses supervised harness fine-tuning and cost-aware GRPO on a trainable Qwen3-8B model; it does not establish that an arbitrary closed API model can be weight-trained.
5. The only candidate gap worth continuing from the current openissue line is narrower: **evolutionary optimization of an explicit, compact Agent-side execution controller, with operator credit conditioned on the behavior displacement actually realized in matched Agent traces and on downstream lineage value**. This is a refined OSLVC hypothesis, not a certified novelty result.

The research object is therefore not the hosted LLM's weights and not an unrestricted rewrite of the entire harness. It is a constrained external controller that determines how a frozen API LLM is orchestrated.

## 2. Architecture boundary

### 2.1 Fixed and trainable parts

| Layer | Status | Role |
|---|---|---|
| Main LLM (for example, DeepSeek Flash through its hosted API) | Frozen during ordinary training | Produces the substantive reasoning, text, and tool-call proposals |
| Agent runtime / harness | Locally controlled | Builds observable state, routes model calls, executes tools, verifies postconditions, and records traces |
| External Agent controller | Trainable / evolvable | Selects structural execution actions such as observe, retrieve, call-tool, check, revise, or submit |
| Local value/critic model | Trainable on A800 if useful | Estimates continuation value of partial Agent trajectories; does not update the hosted LLM |
| Evaluator and tool environment | Fixed during an experiment | Supplies task-state outcomes, trace constraints, and hard safety checks |
| Evolutionary optimizer | Main candidate EC method | Searches the external controller and adapts variation/operator/strength control |

A normal hosted inference call does not update provider model weights. Remote foundation-model fine-tuning would require a separate, explicitly documented provider training product; this thesis design does not assume such an interface.

### 2.2 Feasible implementation precedent: AMC

The official AMC repository confirms a directly relevant split:

- `smc/policy.py` implements `APIModel` using the OpenAI Python client with an API key, base URL, and model name. This is the task-solving policy and can be an API-backed model.
- The value-function training path is local: `smc/train_lora_regression.py` loads a Hugging Face base model, attaches LoRA, adds a regression head, and trains it on trajectory-derived return-to-go targets.
- `smc/traj_train_convert.py` converts collected trajectories into per-state training examples.
- `smc/bootstrap_filter.py` uses incremental weights based on reward since the previous resampling point plus the change in estimated value, then resamples particles (fixed schedule or effective-sample-size trigger).

This is strong evidence that the API-LLM + locally trained sidecar architecture is implementable. It is **not** evidence that AMC trains the API model itself. The public AMC paper frames the method as posterior sampling over trajectories from a fixed black-box policy, guided by a learned value function and Sequential Monte Carlo.

**Code-level reproduction note:** the current public trajectory converter selects the rank-1 trajectory for each task before constructing value-training rows. A reproduction should record this data-selection choice and test whether including lower-ranked trajectories changes value calibration or coverage; do not silently assume the published value model is trained on the complete rollout distribution.

Sources:  
- Hwang et al. (2026), *Agentic Monte Carlo*, ICML 2026, PMLR 306: https://proceedings.mlr.press/v306/hwang26i.html  
- Official code: https://github.com/layer6ai-labs/Agentic-Monte-Carlo  
- Relevant files: `smc/policy.py`, `smc/bootstrap_filter.py`, `smc/traj_train_convert.py`, `smc/train_lora_regression.py`.

## 3. Mechanism-level comparison of closest work

### 3.1 Offline RL harness controller — direct baseline

Yi and Song (2026), *Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning*, arXiv:2607.05458.

**Optimized object:** a lightweight state-conditioned controller around a frozen LLM executor.

**State:** compact observable features covering trajectory progress, draft availability, evidence coverage, tool outputs, verifier feedback, recent failures, remaining budget, last action, and domain-specific structural flags. It does not rely on hidden model activations.

**Action space:** seven structural actions — observe, retrieve, call-tool, draft, check, revise, submit — with invalid actions masked by domain adapters.

**Training:** offline rollouts are assigned terminal task-rubric returns. The controller is trained with advantage-weighted regression, a weighted behavior-cloning objective with exponential advantage weights `exp(A/β)`. The paper deliberately does not directly reward “check” or “revise” action patterns; its Harness Maturity Score is a post-hoc process diagnostic rather than a training reward.

**Important limitation:** the paper formalizes the finite-buffer support constraint. AW can reweight state-action behavior represented in its rollout buffer, but final-outcome gains are bounded by the high-return support already present in that buffer. Better process statistics can improve without a corresponding improvement in final task quality.

**Consequence:** a small learned controller is not a novelty claim. AW, behavior cloning, fixed/forced-check policies, and a matched controller architecture are mandatory baselines. The candidate EC method must show how it explores useful controller behaviors that are not recovered by reweighting the logged buffer, without merely spending more API calls.

Paper: https://arxiv.org/abs/2607.05458

### 3.2 Black-box trajectory steering — AMC

Hwang et al. (2026), *Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents*, ICML 2026.

**Optimized object:** trajectory selection at inference time, not the external controller's parameters.

**Mechanism:** the fixed black-box LLM defines a prior over trajectories. A locally trained value function estimates partial-trajectory continuation value; SMC uses incremental importance weights and resampling to steer particles toward high-value trajectories.

**Strength:** it demonstrates a practical way to combine a hosted API model with a locally trained value model, without needing gradients or log-probabilities from the API model.

**Boundary:** AMC is not a controller-learning algorithm. It changes which sampled trajectory is continued or retained. It is a direct baseline if the proposed method uses a local value model or test-time trajectory search, but it is not a substitute for AW when the object being learned is a persistent state-conditioned execution controller.

Paper: https://proceedings.mlr.press/v306/hwang26i.html  
Code: https://github.com/layer6ai-labs/Agentic-Monte-Carlo

### 3.3 Test-Time Harness Evolution — direct evolutionary prior art

Nie et al. (2026), *TTHE: Test-Time Harness Evolution*, arXiv:2607.08124.

**Optimized object:** arbitrary executable harness code around a fixed LLM.

**Mechanism:** on each unlabeled batch, TTHE executes a population of candidate harnesses, maintains fixed branch lineages, asks LLM-based proposers to edit each branch using execution traces, and uses an agentic judge to commit one final branch. It uses execution-health, round-trip-consistency, and public-test proxies rather than gold labels. The same frozen backbone serves as solver, proposer, and judge.

**Failure analysis reported by the paper:** search performance is non-monotonic in search budget; the judge sometimes selects an inferior candidate despite a better candidate being present; proxy signals can reward benchmark-incompatible outputs; and candidate coverage can remain incomplete.

**Consequence:** population search, branch lineage, trace-guided edits, and persistent test-time harness improvement are already covered. A proposed method must not claim these generic components as new. It must isolate a different controller representation or a specific credit/variation mechanism and compare against TTHE where a fair reproduction is possible.

Paper: https://arxiv.org/abs/2607.08124

### 3.4 HarnessX — strong overlap with structured evolution and co-training

Chen et al. (2026), *HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry*, arXiv:2606.14249.

**Harness evolution:** harnesses are typed processor pipelines across nine dimensions, including context, memory, tools, execution, evaluation/reward, control/safety, observability, and training bridge. AEGIS uses four LLM-driven stages — Digester, Planner, Evolver, Critic — to convert execution traces into typed edits. A deterministic gate validates manifests, normalization, smoke tests, and non-regression before committing an edit.

**Model co-evolution:** a shared replay buffer supports both harness evolution and cross-harness GRPO. The GRPO path requires token-level behavior log-probabilities and updates a trainable model. The paper explicitly distinguishes non-parametric harness edits from parametric model updates.

**Consequence:** typed harness components, trace-driven multi-stage evolution, deterministic candidate gates, and harness/model co-evolution are already covered. The model-training part is not directly transferable to a closed API model without the necessary trainable policy and token-level training signals. HarnessX is a mandatory closest-work comparison for any structured-controller proposal.

Paper: https://arxiv.org/abs/2606.14249

### 3.5 Other direct and adjacent harness-training/evolution methods

| Work | Optimized object and mechanism | Boundary for this thesis |
|---|---|---|
| AgentOptimizer (Zhang et al., ICML 2024) | Agent functions are treated as learnable parameters; an LLM proposes add/revise/remove operations; rollback and early stop control updates | Function-set optimization without LLM weight updates is established prior art |
| SkillOpt (Yang et al., 2026) | A skill document is trained through rollout reflection, bounded add/delete/replace edits, a textual learning-rate budget, rejected-edit buffer, slow/meta update, and held-out validation gate | Skill-file optimization and validation-gated text edits are not new |
| Self-Harness (Zhang et al., 2026) | Failure traces are clustered; the fixed model proposes diverse minimal harness edits; held-in/held-out regression gates accept only non-degrading improvements | Model-specific failure mining and regression-gated harness edits are established |
| Meta-Harness (Lee et al., 2026) | A proposer accesses all prior candidate code, traces, and scores; generates new harnesses; maintains a candidate population and returns a Pareto frontier | Whole-harness code search with full-history access is established |
| AutoHarness (Lou et al., 2026) | LLM-driven program refinement in a tree; Thompson sampling selects a code hypothesis to refine; environment feedback supplies legality/reward evidence | Code-as-harness, LLM mutation, and tree-based search are established |
| EvoHarness-RL (Ning et al., 2026) | BPE external state (Belief, Progress, Experience); SFT teaches action protocol; cost-aware GRPO trains a Qwen3-8B policy for harness coordination | Strong adjacent work on harness-state policy learning, but it trains an open-weight model rather than a frozen API model |
| Harness-1 (Jiang et al., 2026) | A 20B search agent is RL-trained inside a stateful search harness with external working memory and evidence records | Demonstrates explicit state externalization and RL, but not API-only black-box control |
| Code Evolution for Control (Guo et al., 2026) | LLM-driven population search over interpretable Python control policies using mutation/crossover and episode fitness | Generic evolutionary program-policy synthesis is already explored; its experiments are in LunarLander, not tool-using LLM Agents |

Primary sources:  
- AgentOptimizer: https://proceedings.mlr.press/v235/zhang24cd.html  
- SkillOpt: https://arxiv.org/abs/2605.23904  
- Self-Harness: https://arxiv.org/abs/2606.09498  
- Meta-Harness: https://arxiv.org/abs/2603.28052  
- AutoHarness: https://arxiv.org/abs/2603.03329  
- EvoHarness-RL: https://arxiv.org/abs/2608.05446  
- Harness-1: https://arxiv.org/abs/2606.02373  
- Code Evolution for Control: https://arxiv.org/abs/2601.06845

## 4. Novelty boundary: claims that are not acceptable

Do **not** claim any of the following as a standalone contribution:

- using a hosted API LLM while keeping its weights frozen;
- training a controller around a frozen LLM;
- training a local value model to steer black-box Agent trajectories;
- evolving a generic Agent harness, skill, function set, workflow, or executable policy;
- using LLM-generated mutations/crossover, a population, branch lineages, trace feedback, or a validation gate;
- using a multi-objective EA or a learned operator-selection policy without a new mechanism;
- using task-family holdout or cross-model transfer alone as a third innovation.

These are all directly covered or strongly adjacent to the works above and to existing openissue entries for EVOTOOL, EvoMAS, ELMER, LVPG, and classical AOS.

## 5. Narrow candidate to continue — not a novelty verdict

### 5.1 Object of optimization

Keep the main API LLM and the tool environment fixed. Optimize a compact external Agent controller that selects structural execution actions from an auditable state vector.

The controller should be narrower than an unrestricted harness program. The first representation candidate is a typed rule/program policy over externally observable features, rather than the full harness code or the foundation model's weights.

Possible state features:
- task progress and pending subgoals;
- evidence/draft availability;
- tool-call status and structured outputs;
- verifier feedback and recent error category;
- previous structural action;
- remaining task steps / execution horizon;
- hard-constraint and postcondition flags.

Possible actions (adapted from the AW controller paper):
- observe;
- retrieve;
- call-tool;
- draft;
- check;
- revise;
- submit.

The action set and state schema must be frozen before comparing methods.

### 5.2 Candidate EC mechanism

Retain OSLVC only as a falsifiable candidate, now scoped to the external controller:

1. **Typed controller variation:** use explicit controller-level operators, such as condition/guard insertion or deletion, threshold adjustment, state-feature substitution, action replacement, and typed subtree exchange. These are candidate operators, not yet a locked implementation.
2. **Realized behavior displacement:** run parent and offspring controllers on matched probe tasks/states using the same frozen API model and environment protocol. Measure the actual change in structural action traces, not just the number of code edits or textual edit distance.
3. **Scale-conditioned lineage-value credit:** estimate downstream continuation value conditional on the realized trace displacement, operator family, task/state context, and remaining horizon. Separate the expected effect of “how much behavior changed” from the residual value of “which operator caused the change.”
4. **Matched comparisons:** compare candidates under the same task family and initial state. If API stochasticity cannot be controlled by a provider seed, use repeated paired blocks and report uncertainty. The conditional residual is predictive unless randomized/matched evidence supports a causal interpretation.
5. **Evolutionary selection:** select controller variants using exact task-state success and hard feasibility constraints. Do not let task success trade away prohibited side effects or invalid state transitions.

A conceptual decomposition is:

`Q(s,o,d,h)=m(s,d,h)+a(s,o,d,h)`

where `d` is realized behavior displacement, `o` is the variation-operator family, and `h` is remaining horizon. The candidate hypothesis is that `a(s,o,d,h)` gives incremental information about downstream lineage value beyond raw operator reward, raw lineage return, or displacement-only credit. This is not assumed to be causal or novel.

### 5.3 Why evolutionary computation might help — and what must be proven

The proposed argument is not “GA works on black-box functions.” It is:

- The controller phenotype is a typed, discontinuous state-action program; structural changes may not be well represented by a small differentiable policy update.
- API model outputs and tool/environment transitions form a black-box, stochastic evaluation loop; gradients through the hosted LLM are unavailable.
- Population-based variation can explicitly explore alternative controller structures, while matched task/state probes and a local value model can provide more informative credit than raw terminal return.
- The method is worthwhile only if it beats a strong AW-trained MLP controller and strong static/classical EA baselines under matched task exposure and API calls.

If a small AW controller matches or exceeds the evolutionary controller, or if simple TTHE/HarnessX-style harness edits explain the gains, the EC claim fails and the method must be revised.

## 6. Falsifiable research questions

- **RQ1 — Variation response:** At the same requested controller-edit strength, do different typed variation operators produce materially different realized action-trace displacement and feasibility distributions? If not, remove operator-specific scale calibration.
- **RQ2 — Credit deconfounding:** Does displacement-conditioned lineage-value credit improve held-out prediction/ranking of useful offspring beyond immediate reward, raw lineage return, displacement-only credit, diversity/parent-distance AOS, and a naive joint operator-strength controller? If not, remove the conditional residual.
- **RQ3 — Optimization gain:** Does the resulting EC controller improve task-state success and held-out task-family success over the strongest static EA and offline AW controller under matched model, task, seed/repeat, API-call, and evaluation conditions? If not, do not claim an EC method improvement.
- **RQ4 — Transfer:** Does the learned controller transfer across held-out task families or API models without retraining? Treat this as a generalization result unless a separate transfer mechanism survives prior-art review.

## 7. Required baseline ladder

| Stage | Baseline / method | Purpose |
|---|---|---|
| B0 | Frozen API LLM + fixed ReAct-style harness | Establish the base Agent capability |
| B1 | Fixed rule-based controller / forced-check and forced-submit controls | Rule-based process control |
| B2 | Behavior-cloned controller | Separate imitation from return-aware learning |
| B3 | Offline AW controller from Yi & Song | Strong direct trainable-controller baseline |
| B4 | AMC: API policy + local value model + SMC | Strong black-box trajectory-steering baseline |
| B5 | TTHE / Self-Harness / Meta-Harness / AutoHarness or component-level faithful baselines | Compare whole-harness evolution where reproduction is fair |
| B6 | Strong static EA over the same controller representation, tuned on train/validation | Establish whether evolution helps before adaptive control |
| B7 | Classical AOS / self-adaptation, including diversity or parent-distance credit | Establish the value of adaptive operator control |
| B8 | Behavior-scale-only controller (ELMER-style) | Isolate displacement calibration |
| B9 | Lineage-only controller (LVPG-style) | Isolate downstream lineage credit |
| B10 | Naive joint operator-strength controller with raw lineage return | Reject simple fusion explanations |
| B11 | Scale-conditioned lineage-value controller (OSLVC candidate) | Test the narrow proposed mechanism |

Some baselines optimize different objects; do not pretend they are directly interchangeable. Use component-level comparisons or clearly label method-level comparisons where a fair end-to-end reproduction is not possible.

## 8. Parameter-tuning and experiment sequence

1. Freeze the API model/version, prompt protocol, tool schemas, controller state/action schema, evaluator, and cache semantics.
2. Establish the API baseline and log task IDs, model/version, generation parameters, requests/responses, tool events, latency, and outcomes without logging credentials.
3. Collect a small, controlled set of rollouts and train the local value/critic model only on training tasks. Validate its calibration and ranking on held-out validation tasks.
4. Tune **static EA parameters first** on train/validation: population size, offspring count, mutation/crossover probabilities, elitism, selection pressure, and fixed operator mixture. Use random search or SMAC with a bounded staged design; freeze the chosen configuration.
5. Compare static EA with BC and AW before adding adaptive operator/strength control.
6. Only if the EC controller adds value, compare AOS, ELMER-style strength-only, LVPG-style lineage-only, naive joint control, and the scale-conditioned lineage-value candidate.
7. Lock the task-family test split before final evaluation. Cost is secondary; match API exposure and candidate evaluations across the primary comparisons.

## 9. Current feasibility and gates

- The main API architecture is accepted as a user requirement. Use the user's preferred hosted API model for the main executor; do not assume remote weight updates.
- A800s can train a local value/critic model or optional small auxiliary model. A compact controller MLP may not need A800-scale compute.
- The controlled suite currently has **36 authored cases out of 120**; 84 remain unauthored. It is a deterministic software/evaluator prototype, not a completed benchmark or an Agent performance result.
- **G0 remains OPEN:** the final ICML version of EvoMAS: Heuristics in the Loop still needs exact state/action/reward/credit/update-equation audit.
- **G1 remains PARTIAL/OPEN:** independent task/oracle review, family leakage review, final hashes, and external adapter/scorer checks remain outstanding.
- **G2 remains NOT RUN:** no formal Agent/controller/EC experiment has been run.
- No paid API call or model fine-tuning job was started in this audit.

## 10. Immediate next action

Do not implement OSLVC yet. The official PMLR final abstract for EvoMAS: Heuristics in the Loop has now been verified, but one bounded attempt to inspect the final PDF failed; exact state/action/reward/credit/update equations and ablations remain unresolved. G0 stays OPEN, and the same failed PDF routes should not be retried unless a genuinely new accessible source appears.

Proceed in parallel with (i) locking the compact controller representation and its observable state/action schema, and (ii) closing G1 task-family, oracle, leakage, hash, and external-scorer gates. Only after G0/G1 are sufficiently closed should a no-paid-call feasibility pilot run, using matched parent/task/state probes and equal descendant-evaluation counts. Preserve the option to reject OSLVC while retaining the broader API-backed Agent × EC thesis direction.

## References

1. Zhang, S., Zhang, J., Liu, J., Song, L., Wang, C., Krishna, R., & Wu, Q. (2024). Offline Training of Language Model Agents with Functions as Learnable Weights. *Proceedings of ICML 2024*, PMLR 235, 60315–60335. https://proceedings.mlr.press/v235/zhang24cd.html
2. Hwang, D. Y., Suri, R., Villecroze, V., Caterini, A. L., Cresswell, J. C., Vouitsis, N., & Ross, B. L. (2026). Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents. *Proceedings of ICML 2026*, PMLR 306, 49179–49208. https://proceedings.mlr.press/v306/hwang26i.html
3. Yi, H., & Song, X. (2026). Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning. arXiv:2607.05458. https://arxiv.org/abs/2607.05458
4. Nie, J., Zhang, Y., Song, J., Cai, Q., Yu, D., Guo, Y., Tian, X., & Han, B. (2026). TTHE: Test-Time Harness Evolution. arXiv:2607.08124. https://arxiv.org/abs/2607.08124
5. Chen, T., et al. (2026). HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry. arXiv:2606.14249. https://arxiv.org/abs/2606.14249
6. Zhang, H., et al. (2026). Self-Harness: Harnesses That Improve Themselves. arXiv:2606.09498. https://arxiv.org/abs/2606.09498
7. Lee, Y., Nair, R., Zhang, Q., Lee, K., Khattab, O., & Finn, C. (2026). Meta-Harness: End-to-End Optimization of Model Harnesses. arXiv:2603.28052. https://arxiv.org/abs/2603.28052
8. Lou, X., Lázaro-Gredilla, M., Dedieu, A., Wendelken, C., Lehrach, W., & Murphy, K. P. (2026). AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness. arXiv:2603.03329. https://arxiv.org/abs/2603.03329
9. Ning, X., et al. (2026). EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents. arXiv:2608.05446. https://arxiv.org/abs/2608.05446
10. Jiang, P., et al. (2026). Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses. arXiv:2606.02373. https://arxiv.org/abs/2606.02373
11. Guo, P., Li, C., Feng, Y., & Zhang, C. (2026). Code Evolution for Control: Synthesizing Policies via LLM-Driven Evolutionary Search. arXiv:2601.06845. https://arxiv.org/abs/2601.06845
12. Yang, Y., et al. (2026). SkillOpt: Executive Strategy for Self-Evolving Agent Skills. arXiv:2605.23904. https://arxiv.org/abs/2605.23904
13. DeepSeek API documentation, Chat Completions: https://api-docs.deepseek.com/api/create-chat-completion/
