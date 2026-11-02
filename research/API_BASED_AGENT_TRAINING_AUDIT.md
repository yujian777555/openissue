# API-Based LLM Inference and Trainable Agent Components — Literature Audit

**Date:** 2026-11-02  
**Project:** `yujian777555/openissue` only  
**Status:** Initial primary-source audit; architecture constraint clarified; no thesis topic or innovation claim approved.  
**Purpose:** Determine how to train an Agent while its main LLM is accessed through a hosted API, and identify where A800 compute can be used without assuming access to the provider's model weights.

## 1. Correct interpretation of the intended system

The intended architecture is:

- **Main LLM:** a hosted model accessed through its inference API. The Agent sends prompts/messages to the provider and receives model outputs. The model is treated as frozen unless a separate, explicit provider fine-tuning service is available and approved.
- **Agent runtime / harness:** the locally controlled loop that constructs context, decides which stage to run, invokes tools, checks results, revises, and terminates.
- **Trainable Agent-side components:** controller policies, tool/function definitions, skills, workflow modules, retrieval policies, value/critic models, or reward/verifier models. These can be stored and trained independently of the hosted LLM.
- **Evolutionary-computation layer:** searches or adapts the representation, structure, parameters, operators, and selection of the trainable Agent-side components.
- **A800 resources:** train the local controller/value/reward models or optional local auxiliary model; they do not automatically provide access to update the hosted API model's weights.

This is different from the phrase “the Agent calls external APIs as tools.” The point here is that **the LLM itself is called through an API as the Agent's reasoning engine**.

A normal inference request to a hosted model endpoint is not a weight update. To update the provider model itself requires a separate fine-tuning/RL training interface explicitly offered by that provider. The public DeepSeek API guide currently documents an OpenAI-compatible Chat Completions inference endpoint and the model name `deepseek-flash`; the guide is not evidence that ordinary chat requests train or update the model. The thesis design should therefore not depend on remote base-model fine-tuning.

## 2. Taxonomy of training methods for API-backed Agents

### 2.1 Train the model weights

SFT, DPO, PPO/GRPO, and related methods update the LLM policy weights. They are applicable when either:
1. the model is open-weight and can be trained locally; or
2. the provider exposes a separate fine-tuning/RL API for the exact model and account.

This is not the default assumption for a black-box hosted API model. API inference alone does not expose gradients or optimizer access.

### 2.2 Train Agent artifacts while keeping the LLM frozen

The optimized object can be outside the LLM:
- executable functions and tool definitions;
- skill files and procedural instructions;
- prompts, workflow graphs, and harness configurations;
- memory/retrieval policies and tool-selection rules.

This is directly relevant to a hosted API model because the target LLM can remain unchanged while the Agent wrapper learns.

### 2.3 Train a separate Agent controller

A small controller observes the Agent's current execution state and selects structural actions, such as observe, retrieve, call-tool, verify, revise, or submit. The hosted LLM still generates the substantive reasoning/content when invoked; the controller learns how the overall Agent should execute.

The controller can be:
- a small MLP or policy network;
- a compact open-weight model trained locally (for example, with LoRA);
- a constrained decision program or state machine.

This is the clearest way to use A800 compute without requiring the hosted model's weights.

### 2.4 Learn a value function and steer black-box trajectories

A value model can be trained on Agent trajectories and used to rank, prune, or resample candidate continuations from a frozen API model. This is not the same as fine-tuning the API model: it improves selection/search around its outputs.

### 2.5 Hybrid Agent training

A practical hybrid is:
1. call the hosted LLM API to execute Agent rollouts;
2. log the observable states, model requests/responses, tool events, and final task outcomes;
3. train a local controller/value model from the collected traces;
4. use evolutionary computation to improve the controller's representation, parameters, or decision structure;
5. deploy the frozen API LLM with the updated Agent-side component.

The model API remains the reasoning service; the learned component changes the Agent's behavior.

## 3. Closest primary-source works

### P150 — AgentOptimizer: functions as learnable weights (ICML 2024)

Shaokun Zhang, Jieyu Zhang, Jiale Liu, Linxin Song, Chi Wang, Ranjay Krishna, and Qingyun Wu. **Offline Training of Language Model Agents with Functions as Learnable Weights.** Proceedings of ICML 2024, PMLR 235, 60315–60335.  
Paper: https://proceedings.mlr.press/v235/zhang24cd.html  
arXiv: https://arxiv.org/abs/2402.11359

**Verified mechanism:** the method explicitly trains Agent functions without modifying LLM weights. It treats functions as learnable Agent parameters; an LLM proposes function updates; rollback and early-stop control the update loop. The paper evaluates GPT-4+-based and ReAct agents.

**Implication:** “keep the hosted LLM frozen and train the Agent wrapper/functions” is established prior art. A new thesis cannot claim this general idea as novel. The exact function representation, update policy, evolutionary role, and held-out generalization mechanism must differ and be experimentally justified.

### P151 — Agent Lightning (2025 paper; current v1.0 framework)

Xufang Luo et al. **Agent Lightning: Train ANY AI Agents with Reinforcement Learning.** arXiv:2508.03680, 2025.  
Paper: https://arxiv.org/abs/2508.03680  
Official repository: https://github.com/microsoft/agent-lightning  
Current architecture documentation: https://github.com/microsoft/agent-lightning/blob/main/docs/05-basics.md

**Verified mechanism:** it separates Agent execution from the training service, records rollouts and model-call events, and converts trajectories into training transitions. The paper's LightningRL includes hierarchical credit assignment. The current v1.0 architecture uses an API Gateway, rollout controller, and customized trainer; the trainer runs on the GPU side and updates a policy.

**Important boundary:** an OpenAI-compatible proxy is an interface and tracing mechanism, not proof that an arbitrary remote proprietary model can be gradient-updated. The training backend needs suitable policy-training signals. The project's serving documentation discusses token IDs/log-probabilities and notes that ordinary hosted APIs may not expose the exact token-level information required for faithful policy-gradient training. Therefore Agent Lightning is a strong architecture reference, but direct training of a closed API model must not be assumed.

### P126 — Agentic Monte Carlo (ICML 2026; cross-reference to the main matrix)

Dae Yon Hwang et al. **Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents.** Proceedings of ICML 2026, PMLR 306, 49179–49208.  
Paper: https://proceedings.mlr.press/v306/hwang26i.html  
Official code: https://github.com/layer6ai-labs/Agentic-Monte-Carlo

**Verified mechanism:** targets black-box Agents whose model parameters cannot be optimized. It learns a value function and uses Sequential Monte Carlo to steer trajectory sampling while keeping the black-box LLM fixed.

**Implication:** value-guided search around a frozen API model is already a strong, peer-reviewed baseline. A new method must not claim “train a value model to improve a black-box Agent” as novel by itself. The exact relation between the value model, evolutionary search, and the Agent's structural policy must be differentiated.

### P152 — Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning (2026 preprint)

Haiwen Yi and Xinyuan Song. **Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning.** arXiv:2607.05458, 2026.  
Paper: https://arxiv.org/abs/2607.05458

**Verified mechanism:** keeps the LLM executor and its prompts frozen, and trains a small state-conditioned controller over seven structural actions: observe, retrieve, call-tool, draft, check, revise, and submit. It uses offline rollouts and advantage-weighted regression (AW). The reported controller is a one-hidden-layer 64-unit MLP. It separates terminal task quality from a post-hoc process diagnostic (Harness Maturity Score), and explicitly analyzes the finite-buffer limitation: offline learning can reweight good behavior already represented in the buffer but cannot reliably invent missing high-return trajectories.

**Implication:** this is a direct and very recent baseline for the proposed API-LLM + trainable Agent controller architecture. A thesis contribution cannot simply be “train a small controller around a frozen LLM.” It must demonstrate a specific evolutionary mechanism that improves on AW, behavior cloning, fixed/forced-check rules, and other controller baselines.

### P153 — SkillOpt: Agent skills as trainable parameters (2026)

Microsoft Research. **SkillOpt: Agent skills as trainable parameters.** Microsoft Research article, 2026-06-30; linked paper title: *SkillOpt: Executive Strategy for Self-Evolving Agent Skills*.  
Research article: https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/

**Verified mechanism from the research article:** a frozen target model executes tasks with a skill file; a separate optimizer model analyzes trajectories and proposes bounded add/delete/replace edits. A textual learning-rate budget limits edit size; a held-out validation gate accepts only improvements; rejected edits are retained as negative feedback; slow/meta updates consolidate longer-horizon lessons.

**Implication:** generic skill-file training, bounded edits, validation gating, and rejected-edit memory are already covered. Skill optimization is a required baseline if the thesis evolves instructions or reusable skills.

### P154 — SMITH: joint tool creation and use (NeurIPS 2026 poster)

Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, and Hung-yi Lee. **Joint Optimization of Tool Creation and Use for Large Language Model Agents (SMITH).** Accepted to NeurIPS 2026 (Poster).  
Project/paper/code: https://tool-use-smith.github.io/  
arXiv: https://arxiv.org/abs/2608.24571

**Verified mechanism:** a single trainable policy jointly learns to create tools (Python function plus JSON schema) and later invoke them. Build and use rollouts are mixed; schema/format, execution, and judge rewards are kept separate; DAPO updates the same policy. The reported primary backbone is Qwen3-4B-Instruct fine-tuned with LoRA, with additional open-weight backbones.

**Implication:** this is relevant to using A800s to train an open-weight auxiliary or Agent model. It is not a direct black-box API-only method because the policy weights are trained. It provides a strong local-training comparison if the thesis includes a trainable local Agent-side model.

### P155 — A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain (2026 preprint)

Debjyoti Paul. **A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain.** arXiv:2607.25415, 2026.  
Paper: https://arxiv.org/abs/2607.25415

**Reported method:** a fixed, human-legible harness action space is controlled online by a contextual bandit and REINFORCE. The target LLM remains frozen; the paper reports evaluation with a local Ollama model and AWS Bedrock.

**Implication:** even provider-agnostic policy learning over a frozen-model harness is being explored. Include this as an adjacent preprint, not as an established peer-reviewed result.

## 4. What this means for the A800s

The A800s can be used meaningfully without training the hosted API model itself:

| Trainable component | What is trained | How it participates in the Agent |
|---|---|---|
| Harness/controller | A small MLP or compact policy model | Selects when to observe, retrieve, call a tool, verify, revise, or stop |
| Value/critic model | Expected success or continuation value from a state/partial trajectory | Ranks or steers candidate actions/trajectories from the frozen API model |
| Reward/verifier model | A model that predicts rubric outcomes or detects specific failure modes | Supplies an auxiliary signal; must be calibrated against deterministic/external oracles |
| Skill/function optimizer | External skill files, function implementations, schemas, or workflow modules | Changes the Agent's capabilities without changing the hosted LLM weights |
| Optional local auxiliary LLM | LoRA/SFT/RL weights of a small open model | Performs a bounded Agent-side task such as action classification, tool routing, or critique |

The main API LLM remains the reasoning engine. A locally trained sidecar is an Agent component, not a replacement claim that the provider's model has been fine-tuned.

## 5. A candidate thesis architecture to test — not yet approved

A provisional architecture is:

`Hosted API LLM (frozen) ightarrow Agent runtime/harness leftrightarrow Trainable local controller/value model ightarrow tools/environment`

The Agent runtime exposes a compact, auditable state to the trainable controller. The controller selects a structural action or strategy; the hosted LLM is invoked when natural-language reasoning or content generation is required. The environment and independent evaluator return task-state outcomes and process traces.

A possible EC-centered method family is to evolve a constrained controller representation or policy program, while training a small local value/controller model from API-generated rollouts. However, **this is only a candidate direction**. It is not yet a novelty claim: offline RL harness control, AgentOptimizer, SkillOpt, AMC, and harness evolution already cover important pieces.

### Research questions to falsify

- **RQ-API-1:** Can a structured, evolvable Agent-side controller improve task success and robust execution while the main LLM remains a fixed hosted API model?
- **RQ-API-2:** Does an EC-trained or EC-refined controller outperform a strong learned controller (AW/offline RL), behavior cloning, static HPO, and simple rule-based harnesses under matched API calls and task exposure?
- **RQ-API-3:** Can the learned controller transfer to held-out task families or another API model without retraining, and is any transfer benefit caused by the EC mechanism rather than a better prompt/skill file?

### Evolutionary-computation requirements

Any surviving proposal must specify:
- genotype/phenotype: controller program, state-action policy, modular harness, or another explicit object;
- variation: typed mutation/crossover or a justified neuroevolution operator;
- fitness: externally verifiable task-state success, with process/safety metrics reported separately;
- selection/replacement and diversity maintenance;
- static EA hyperparameter tuning before online control claims;
- online parameter/operator control and how its state/credit are defined;
- comparison with AW/offline RL, BC, static HPO, classical AOS/self-adaptation, AgentOptimizer, SkillOpt, and AMC where applicable.

Do not claim novelty from merely replacing AW with a genetic algorithm, evolving prompts, or adding a controller. The EC component must explain a measurable improvement that simpler learning or optimization methods do not reproduce.

## 6. API and training-interface constraints

1. DeepSeek's public API documentation confirms an OpenAI-compatible inference endpoint and shows `deepseek-flash` as a supported model name: https://api-docs.deepseek.com/ . This confirms API-based inference compatibility, not a model-weight training API.
2. Keep API credentials outside source code, logs, prompts, and Git history.
3. Record provider/model/version, request parameters, token usage, latency, tool calls, and task outcomes. Do not log secrets or private payloads.
4. Do not assume that a provider's API returns token IDs, behavior log-probabilities, or supports fine-tuning. Check the exact provider/model contract.
5. If a future experiment needs token-level policy gradients, use a trainable local model served through an OpenAI-compatible endpoint, or a provider training product that explicitly supports the required signals.
6. Match API call counts and model versions across baselines; report cost as a secondary metric rather than the thesis's central objective.

## 7. Current conclusion

**Yes: Agent training can be part of the Agent process while the main LLM is used through an API.** The correct training target is not necessarily the foundation model. It can be the Agent's controller, skills/functions, workflow, or value model.

The strongest near-term experimental setup is a frozen API LLM plus a locally trainable Agent-side controller/value model, with evolutionary computation investigated as the central optimization/training method. This is technically feasible with A800 resources, but generic controller learning is already covered by 2026 work. The next research step is a mechanism-level comparison to identify whether EC contributes something beyond existing offline RL, value-guided black-box search, and skill/function optimization.

No experiment, paid API call, or model fine-tuning job was started in this audit.

## References

1. Zhang, S., Zhang, J., Liu, J., Song, L., Wang, C., Krishna, R., & Wu, Q. (2024). Offline Training of Language Model Agents with Functions as Learnable Weights. *Proceedings of ICML 2024*, PMLR 235, 60315–60335. https://proceedings.mlr.press/v235/zhang24cd.html
2. Luo, X., et al. (2025). Agent Lightning: Train ANY AI Agents with Reinforcement Learning. arXiv:2508.03680. https://arxiv.org/abs/2508.03680
3. Hwang, D. Y., et al. (2026). Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents. *Proceedings of ICML 2026*, PMLR 306, 49179–49208. https://proceedings.mlr.press/v306/hwang26i.html
4. Yi, H., & Song, X. (2026). Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning. arXiv:2607.05458. https://arxiv.org/abs/2607.05458
5. Microsoft Research. (2026-06-30). SkillOpt: Agent skills as trainable parameters. https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/
6. Tam, Z. R., Lin, C.-Y., Chen, Y.-N., Sun, S.-H., & Lee, H.-Y. (2026). Joint Optimization of Tool Creation and Use for Large Language Model Agents (SMITH). NeurIPS 2026 Poster. https://tool-use-smith.github.io/
7. Paul, D. (2026). A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain. arXiv:2607.25415. https://arxiv.org/abs/2607.25415
8. DeepSeek API documentation. https://api-docs.deepseek.com/
9. Agent Lightning v1.0 architecture documentation. https://github.com/microsoft/agent-lightning/blob/main/docs/05-basics.md


## 8. Mechanism-level audit update (2026-11-03)

The broad architecture is feasible, but the novelty boundary is narrower than the first pass suggested. See `research/API_AGENT_EC_MECHANISM_AUDIT_R1.md` for the full source-grounded comparison.

Key corrections:
- **AW Harness MDP (P152)** is a direct controller-learning baseline: compact observable state, seven structural actions, terminal task-rubric reward, and offline advantage-weighted regression. Its finite-buffer analysis explicitly limits outcome gains to the high-return support in the collected buffer.
- **AMC (P126)** is the strongest implementation precedent for the API/local-sidecar split: its public code uses an OpenAI-compatible `APIModel` for the task-solving policy and a locally trained LoRA + regression-head value model to guide SMC. It steers trajectories; it does not train the API model or a persistent state-action controller.
- **TTHE (P156)**, **Meta-Harness (P159)**, **Self-Harness (P158)**, **AutoHarness (P160)**, and **HarnessX (P161)** already cover frozen-model harness evolution, trace-guided edits, populations/branches, typed edits, or regression gates. These cannot be claimed as new.
- **EvoHarness-RL (P157)** combines BPE harness state, SFT, and GRPO, but its reported training uses an open-weight Qwen3-8B policy; it is an adjacent contrast rather than a direct closed-API recipe.
- **Code Evolution for Control (P163)** shows that generic LLM-driven evolutionary search over executable state-to-action policies is already explored, albeit in LunarLander rather than LLM tool-use agents.

**Revised research object:** a compact external controller over an explicit Agent state/action interface. Keep the main API LLM, tool schemas, and evaluator fixed. The candidate EC mechanism is OSLVC scoped to that controller: estimate operator continuation value conditional on the *realized action-trace displacement* and matched task/state context. This must be compared with AW, BC, AMC, TTHE/HarnessX-style method-level baselines, static EA, classical AOS, ELMER-style scale-only control, LVPG-style lineage-only control, and naive joint operator-strength control.

**No novelty verdict:** the candidate is not approved until it survives the full EvoMAS: Heuristics in the Loop audit, the controller representation audit, and the G0/G1 gates. No API rollout, model fine-tuning, or formal experiment was started in this session.
