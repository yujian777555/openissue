# Candidate Audit: Agent–Environment Co-Evolution for Tool-Failure Recovery

**Audit date:** 2026-10-23  
**Status:** Negative novelty result for the generic formulation; narrower counterexample-guided EA candidate remains unvalidated.  
**Scope:** Reassess the provisional idea “co-evolve an LLM-agent recovery policy and the task/failure curriculum” against recent primary sources. This is a research audit, not a proposal approval.

## 1. Executive finding

The generic formulation — *evolve a tool-using agent while also generating tasks/failures that expose its weaknesses* — is **not a defensible novelty claim by itself**.

A new survey explicitly organizes agentic co-evolution into agent–agent, agent–environment, and meta-co-evolution, and names several directly overlapping methods. Primary-source review confirms substantial overlap with:
- **COvolve**: LLM-generated executable policies and environments co-evolve adversarially as a two-player zero-sum game; mixed-strategy Nash equilibrium is used to reduce forgetting.
- **Agent-World**: synthesizes verifiable tool/database environments and tasks, then trains agents with multi-environment RL while using evolving environments to expose capability gaps.
- **SEAL**: uses verifier-grounded failure diagnoses to adapt the tool-use learning interface and guide policy optimization.
- **SENTINEL**: diagnoses failed tool-use trajectories, generates executable tasks that target the failure patterns, and trains the solver with RL.
- **RLAnything**: jointly adapts environment, policy, and reward model.
- **EVOTOOL**: already evolves tool-use policy with trajectory-grounded blame, targeted mutation, and diversity-aware selection.
- **HarnessEvolve**: uses reference-trajectory alignment, failure clustering, and quality/performance gates for reliable harness evolution.
- **POET, PAIRED, ACCEL, and LLM-POET**: establish environment–policy co-evolution and adaptive curriculum as older foundations.

Therefore “we use an EA instead of RL,” “we apply co-evolution to tool faults,” or “we generate tasks from failures” are not enough without a more specific mechanism and a controlled advantage over the closest systems.

## 2. Closest-work matrix

| Work | What evolves / adapts | Direct overlap | What remains potentially distinct (not yet proven) |
|---|---|---|---|
| [COvolve, GECCO 2026](https://arxiv.org/abs/2603.28386) | LLM-generated executable Python policies and environments; adversarial two-player zero-sum co-evolution; mixed-strategy Nash equilibrium. Tested in urban driving, symbolic mazes, and geometric navigation. | Very high for generic adversarial policy–environment co-evolution and environment-generated robustness. | A constrained, typed grammar of tool-fault transformations and explicit held-out combinations of fault semantics × task topology could be a different problem definition, but domain change alone is not a novelty claim. |
| [Agent-World](https://arxiv.org/abs/2604.18292) | Scalable executable tool/database environment and task synthesis; multi-environment RL; continuous task expansion driven by capability gaps. The paper reports 1,978 environments, 19,822 tools, and evaluation on 23 benchmarks. | Very high for evolving tool agents through dynamically synthesized environments and tasks. | Black-box evolutionary search over the agent harness without weight updates, with counterexample search rather than RL and strict fault-composition generalization, could distinguish the method if experiments establish a real benefit. |
| [SEAL](https://arxiv.org/abs/2605.24426) | Verifier-grounded turn-level failure diagnosis drives both training-interface adaptation (tool affordances, constraints, recovery feedback) and policy-gradient optimization. Keeps task semantics, rewards, and verifier fixed. | Very high for failure-conditioned tool-agent/environment co-adaptation. | SEAL adapts the learning interface and trains model parameters; a typed recovery-controller EA would optimize a different object. This difference matters only if the controller gives robust capability gains at matched budgets. |
| [SENTINEL](https://arxiv.org/abs/2606.12908) | Controller diagnoses failed rollouts; proposer generates executable tasks targeting observed weaknesses; solver receives RL updates on the generated tasks. Evaluated on τ²-Bench Retail. | Very high for failure-driven task generation and targeted tool-agent improvement. | The key possible difference is search over an explicit executable recovery policy with no RL fine-tuning, plus adversarial compositional fault evaluation. Task generation alone is not novel. |
| [RLAnything](https://arxiv.org/abs/2602.02488) | Jointly forges environment, policy, and reward model in a dynamic RL loop. | High for broad multi-component self-improvement. | A constrained EA-specific genotype/variation/selection method may differ, but must outperform strong RL/co-evolution baselines or demonstrate a relevant low-resource/black-box regime. |
| [EVOTOOL, ACL 2026](https://aclanthology.org/2026.acl-long.2016/) | Evolves modular Planner/Selector/Caller/Synthesizer prompts; trajectory-grounded blame, targeted mutation, diversity-aware population selection. | Very high for evolutionary tool-use policy optimization and failure-targeted edits. | A typed runtime recovery program over observable failure symptoms and a held-out semantic-fault composition protocol is a candidate distinction. A state machine or different benchmark alone is insufficient. |
| [HarnessEvolve](https://arxiv.org/abs/2609.00829) | Aligns failed trajectories to reference trajectories, clusters errors, and gates harness updates against shortcuts and forgetting. | High for failure attribution and reliable harness evolution. | Need a different evolutionary search mechanism or demonstrably stronger transfer/generalization, not just another failure taxonomy. |
| [POET](https://arxiv.org/abs/1901.01753), [PAIRED](https://arxiv.org/abs/2012.02096), [ACCEL](https://arxiv.org/abs/2203.01302), [LLM-POET](https://arxiv.org/abs/2406.04663) | Evolve or adapt environments/curricula alongside the solver, including LLM-driven environment mutation. | Establishes that environment–policy co-evolution and evolutionary curricula are mature ideas. | LLM tool semantics may motivate a new representation/evaluation setting, but cannot be the sole novelty argument. |

## 3. Implications for candidate ranking

### Candidate A — state-contingent recovery-policy evolution

**Status: keep only as a candidate to falsify.**

The strongest possible research object is not a free-text prompt or a generic tool policy. It is a *typed, executable recovery controller* that maps only runtime-observable signals (error type, schema mismatch, stale-state evidence, tool availability, dependency-graph progress, retry history) to bounded recovery actions (retry, repair arguments, switch a valid path, replan, rollback, or abort). It must never access hidden fault labels.

However, EVOTOOL and HarnessEvolve make generic failure diagnosis and targeted policy evolution crowded. The candidate survives only if:
1. the explicit controller representation yields a measurable capability advantage over prompts and hand-written rules;
2. the advantage transfers to held-out combinations of fault semantics and task topology;
3. the gains persist against EVOTOOL-style mutation and direct reflection/replanning under matched model calls and rollout budgets; and
4. normal-case task success and tool-call cost do not regress materially.

### Candidate B — co-evolution of policy and failure curriculum

**Status: downgrade; do not treat as a thesis innovation in its current generic form.**

COvolve, Agent-World, SEAL, SENTINEL, and RLAnything substantially cover the broad idea. A viable version would need a concrete algorithmic difference, such as a constrained adversarial *fault-program* search over a formal tool-task grammar, not arbitrary executable environments, coupled to policy evolution using counterexample and transfer evidence. Even that is only a hypothesis: it must be compared with COvolve-like adversarial co-evolution, failure-driven task generation, and strong non-adaptive curricula.

### Candidate C — compositional generalization of recovery programs

**Status: fallback, not approved.**

Could evaluate whether recovery primitives compose on unseen combinations of tools, task-DAG topology, and fault semantics. This is potentially measurable but overlaps with modular policy search and skill composition. It needs a distinct representation or operator and must beat training on more examples or ordinary recombination.

### Candidate D — meta-evolution of the evolutionary mechanism

**Status: add to literature audit, not yet rank above A.**

The co-evolution survey characterizes meta-co-evolution (where the system adapts what/when/how/where to evolve and how to evaluate) as early, with few methods satisfying its strict definition. This is a potential research opening, but adjacent work already includes PromptBreeder, Gödel Agent, HyperAgents, and RQGM. The next audit must determine whether a narrow, testable meta-controller for choosing policy-edit operators from *measured* operator outcomes is actually distinct from adaptive operator selection, LLM mutation control, and existing agent self-modification. “Let the agent improve its own optimizer” is not enough.

## 4. A narrower experimentable hypothesis (working hypothesis only)

> Under a fixed base LLM and a fixed inference/rollout budget, does evolutionary synthesis of typed recovery programs, coupled to search over valid fault transformations on tool-task DAGs, improve recovery on held-out fault-semantics × topology combinations more than policy-only EA, direct reflection/replanning, EVOTOOL-style targeted mutation, and a fixed/random fault curriculum?

This formulation differs from broad co-evolution by making the unit of environment search a **valid, typed fault transformation** over a controlled task graph, and the primary target a **compositional generalization gap**, rather than unrestricted open-ended environment creation. Whether that is novel remains unknown until the exact mechanisms of COvolve, Agent-World, SEAL, and SENTINEL are compared in detail.

### Proposed formal objects

- **Task genome:** a valid dependency DAG, tool schema, initial state, goal predicate, and known valid paths.
- **Fault-program genome:** a typed transformation (e.g. transient failure, permanent unavailability, schema drift, stale state, silent semantic corruption) applied at a specified dependency point. Validity/solvability checks are external to the generator's own fitness.
- **Policy genome:** a bounded rule/state-machine program using observable runtime evidence only.
- **Policy fitness:** success on a paired mix of normal and faulted cases, recovery cost, unsafe continuation after corruption, and held-out composition score.
- **Adversary fitness:** find valid counterexamples that distinguish current policies from archive policies, while avoiding trivial unsolvable cases and duplicates.
- **Archive descriptor:** fault semantics × graph topology × observability × recovery-path structure; use this to prevent one narrow exploit from dominating the population.
- **Leakage protection:** the solver receives no hidden fault label, oracle path, or generator fitness. Oracle labels are used only by an isolated evaluator.

This is not yet an algorithm specification. In particular, the adversary objective, archive mechanism, and fitness aggregation need to be defined and ablated before implementation.

## 5. Minimum falsification plan

| Gate | Required comparison | Stop condition |
|---|---|---|
| G0 — Prior-art distinction | Mechanism-by-mechanism audit of COvolve, Agent-World, SEAL, SENTINEL, EVOTOOL, HarnessEvolve; inspect official code where available. | No defensible mechanism-level difference. |
| G1 — Valid environment | Hand-written task/fault cases; independent validator; schema/property tests; hidden-label leakage tests. | Generator produces invalid, trivial, or label-leaking tasks. |
| G2 — Policy search has value | Fixed rules, direct reflection/replanning, random valid mutation, greedy one-child search, static population EA, EVOTOOL-style baseline. | Static EA has no repeatable held-out gain at matched calls/rollouts. |
| G3 — Curriculum/co-evolution adds value | Fixed curriculum, random curriculum, policy-only EA, environment-only search, policy–fault co-evolution, and where feasible a COvolve-style baseline. | Co-evolution gains disappear after budget matching, validity checks, or archive cross-play. |
| G4 — Compositional transfer | Hold out fault × topology combinations and tool-schema families; test on a separate external benchmark without optimizing on its test cases. | Only in-distribution performance improves or normal-case performance regresses. |
| G5 — Robust statistics | Multiple seeds; paired task IDs; confidence intervals; report success, recovery cost, exposure, calls, tokens, and cost. | Gains are not robust or depend on one seed/task family. |

## 6. Research decision

**Do not promote generic policy–curriculum co-evolution.** Keep the policy-only candidate and the narrower typed counterexample-guided variant under falsification, and add meta-evolution of the search mechanism to the literature audit. No implementation or official experiment should begin until Gate G0 produces a clear mechanism-level difference and the benchmark/data-rights gate is closed.

The immediate next action is a paper-and-code audit of the most direct methods, followed by a candidate-ranking update. The thesis–paper map remains intentionally unpopulated.
