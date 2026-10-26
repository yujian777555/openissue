# Candidate Audit: Evolutionary Control of Transactional, Stateful Tool Agents

**Audit date:** 2026-10-23  
**Status:** New candidate to investigate; not a novelty claim and not yet ranked above the existing candidates.  
**Reason for adding it:** The broader search found a concrete reliability problem at the boundary between LLM decisions and stateful tool side effects: partial execution, state races, irreversible actions, and over-conservative guards. This is narrower than generic “agent robustness” and may support a verifiable, independently generated evaluation setting.

## 1. Problem statement

Tool-using agents increasingly execute multi-step workflows that read and mutate external state. A failure can occur after some actions have already changed state; an external update can invalidate an earlier read; a retry can duplicate a side effect; a losing speculative branch can leave residue; and some actions (sending a message, deleting data, publishing, or transferring funds) cannot be cleanly undone.

The research question is whether **evolutionary synthesis of a bounded recovery/control policy** can improve safe task completion under stochastic tool failures and state races, while a separate runtime monitor enforces non-negotiable safety contracts.

This is not a proposal to evolve a safety monitor that can waive constraints. The monitor/verifier remains outside the policy and cannot be edited by the candidate policy. Evolution optimizes choices such as verify state, refresh read, retry only if idempotent, checkpoint, wait for conflicting work, compensate, request confirmation, switch to a safe alternative, or abort/escalate.

## 2. Primary sources and exact overlap

| Work | What it establishes | Implication |
|---|---|---|
| [ResiliBench, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/file/93427bc08aef8f9d6d5366d70284f571-Paper-Conference.pdf) | A benchmark with 5,040 tasks from 30 APIs, probabilistic tool errors, workflow dependencies, and controlled perturbations to instruction quality; includes MDP-derived workflows and recovery/replanning evaluation. | Stochastic tool reliability and workflow adaptation are already benchmarked. A new benchmark alone is not enough. Its exact data/code license and raw-loader details still need checking before reuse. |
| [Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows](https://arxiv.org/abs/2602.14849) | A runtime layer records reads/effects, seals transactions, uses per-resource frontiers before commit, suppresses unreleased effects on abort, and compensates externalized reversible effects where possible. | Transactional tool settlement and safe abort/commit are direct prior art. Our candidate must not rediscover transaction management. The possible contribution is an evolutionary *decision policy around* the transaction layer, evaluated against Atomix plus simple controllers. |
| [Stale Does Not Mean Unsafe: Guard Precision for Tool-Using LLM Agents under Infrastructure State Races](https://arxiv.org/abs/2609.29522) | A deterministic simulator injects five non-atomic failure mechanisms across 16 tasks in four domains; compares global-epoch, read-set-version, and semantic commit-predicate guards. Coarse freshness guards prevent unsafe commits but can reject many benign races. | State-race recovery and semantic safety predicates have concrete recent prior art. A policy must improve the safe-completion/false-abort trade-off, not merely block all changed state. |
| [Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses](https://arxiv.org/abs/2610.15150) | Uses decomposition-based evolutionary search (MOEA/D), Pareto-front maintenance, and factorized general-purpose vs environment-specific harness components; evaluates functionality/security trade-offs. | Direct overlap for multi-objective evolutionary harness optimization. Do not claim “EA balances success and safety” or “factorized harness evolution” as novel. Distinction would have to lie in transaction-aware action semantics, contract-preserving controller representation, and fault/race-composition generalization. |
| [MoMHa](https://arxiv.org/abs/2609.30967) | Optimizes harnesses jointly over accuracy, behavioral safety, and token cost. | Generic accuracy/safety/cost multi-objective harness optimization is already studied. |
| [Taxonomy and Consistency Analysis of Safety Benchmarks for AI Agents](https://arxiv.org/abs/2605.16282) | Identifies tool misuse, destructive side effects, incorrect parameters, and irreversible actions without confirmation as distinct agent-safety failure categories. | Supports the importance of the setting, not novelty of a solution. A contribution must be an algorithm or demonstrated capability improvement. |
| [Vera: Safety Testing LLM Agents at Scale](https://arxiv.org/abs/2607.01793) | Generates executable safety cases with deterministic verification predicates and evaluates agents in isolated sandboxes using environment/tool-call evidence rather than self-reports. | Strong adjacent baseline for scenario generation and evidence-grounded evaluation. Do not rely on LLM self-judgment as the sole safety verifier. |

## 3. Candidate formulation

### Search object

A **typed transactional recovery controller**, not a free-form prompt. Its state features can include:
- last observed tool status and typed error;
- read-set/version or semantic-predicate validation result;
- whether an action is idempotent, reversible, compensatable, or irreversible;
- which effects are tentative, sealed, committed, or aborted;
- whether parallel/conflicting work may still arrive;
- task-DAG progress and remaining valid paths;
- retry count, budget, and whether human confirmation is required.

Its action set is bounded: verify, refresh, retry if safe/idempotent, repair arguments, wait, checkpoint, compensate, replan, request confirmation, or abort. The representation must prohibit direct access to hidden race/fault labels.

### Environment and fitness

Use an independently authored procedural environment if benchmark rights are unclear. The task/fault generator should include:
- stochastic transient failures and permanent tool unavailability;
- schema/argument failures;
- partial side effects and duplicate-call hazards;
- read/write races and stale-but-benign state changes;
- conflicting speculative branches;
- reversible vs irreversible effects;
- incomplete instructions and dependency-DAG variants.

The evaluator must independently verify the final external state and all hard invariants. Fitness should be **constrained**, not a single weighted sum that can trade away safety:
1. reject any policy that violates a hard invariant in the validation suite;
2. among policies passing the safety gate, optimize task success, false-abort rate, recovery latency/cost, and unnecessary confirmation rate;
3. report unsafe-attempt rate separately even when the runtime monitor blocks the attempt.

The final test must hold out combinations of race type × side-effect reversibility × task topology, not merely new random seeds from the same combinations.

## 4. Why evolutionary computation might be useful — and how this can fail

**Possible EC role:** search a discrete, compositional controller space where interactions among guards, retry conditions, compensations, and dependency structure make greedy single-edit tuning unreliable. A population/archive could preserve distinct safe strategies for different risk/latency regimes.

**This is not yet demonstrated.** A deterministic transactional runtime plus a few hand-written policies may solve the task better and more safely. Harmony Harness already applies evolutionary multi-objective optimization to functionality/security trade-offs. The candidate only survives if a specific controller representation or variation/selection mechanism produces a repeatable gain beyond those baselines.

## 5. Minimum baseline and falsification plan

| Gate | Baselines / test | Stop condition |
|---|---|---|
| T0 — Contract validity | Independent state oracle, property-based transaction tests, fault-injection tests, hidden-label leakage tests. | The runtime monitor or evaluator can be bypassed, or scenarios are invalid/ambiguous. |
| T1 — Safe controller value | Fixed retry/replan rules; conservative abort; semantic-predicate guard; Atomix + fixed policy; reflection/replanning. | Simple runtime enforcement and rules already achieve the same safe-completion/false-abort frontier. |
| T2 — EC value | Random valid controller; greedy one-child edit; static EA; Harmony-Harness-style multi-objective evolution where reproducible; matched model calls and rollouts. | EA gains disappear under matched budgets or only reflect extra evaluations. |
| T3 — Generalization | Hold out race × topology × reversibility combinations; test unseen tool schemas and task templates. | Gains are in-distribution only or safety degrades on held-out combinations. |
| T4 — Operational trade-offs | Report task success, invariant violations/unsafe attempts, false aborts, duplicate side effects, recovery calls, latency, and token/API cost. | Results hide unsafe attempts behind a runtime guard or scalar score. |

## 6. Candidate status

**Promote to the next candidate-comparison round, not to the thesis shortlist yet.**

This direction is more concretely tied to a consequential agent capability than generic co-evolution, but it still overlaps with Atomix, ResiliBench, state-race guard research, Harmony Harness, MoMHa, and Vera. It passes the *problem importance / measurability* screen provisionally; it has not passed the *distinct evolutionary mechanism* screen.

The next step is to test whether the evolution of controller policies contributes anything beyond a transactional runtime plus simple rules. If not, reject it. Do not claim the environment, safety metric, or multi-objective EA alone as the innovation.


## 8. Second-pass falsification and implementation gate (2026-10-26)

The broader formulation is now **downgraded**. The direct overlap is not limited to Atomix and ResiliBench:
- Cordon and Agentic Transaction study task-scoped semantic/ACID-like transaction boundaries for agent workflows.
- Verified Tool Calls already adds postcondition verification, verify-before-retry, and idempotency keys.
- LIMBO directly evaluates ambiguous write outcomes, late commits, redelivery, and duplicate side effects with a ground-truth effect ledger; it also shows a client-side policy cannot guarantee exactly-once when the tool contract lacks the necessary capability.
- AIR provides incident detection, tool-mediated recovery, and reusable guardrail synthesis.
- Sentry learns failure-conditioned recovery lessons from verified repairs.
- Bench2Robust explicitly controls whether an episode requires retry, fallback, or escalation and studies learned recovery with RL.
- Harmony Harness already uses evolutionary multi-objective optimization over harness functionality/security.

These results leave no basis for claiming novelty for “evolve a transactional recovery controller” alone. A new genome, a new safety metric, or a new combination of an existing runtime and EA is not enough.

### Implementation/rights gate

- **Atomix:** Apache-2.0; inspected source tree includes the Python runtime, fixed protocol baselines (OCC revalidate/retry and TCC confirm), tests, and local experiment configurations. This is the clearest runnable baseline currently available, but its test suite has not been run in this project session.
- **ResiliBench:** the linked repository currently contains supplementary JSON tool/task registries; no top-level license file or license metadata was present, and the inspected root has no full experiment runner. Treat as a paper-specified benchmark and unlicensed/unverified data artifact until the authors clarify terms.
- **Vera:** the official root contains LEGAL.md but no top-level software license file; do not assume permissive reuse.
- **Harmony Harness:** no author-linked official code repository was visible on the inspected arXiv page. A third-party extension is not an official reproduction.
- **LIMBO, Bench2Robust, Cordon, Agentic Transaction, and Verified Tool Calls:** no confirmed official runnable code/data link was found in the inspected paper pages.
- **Sentry:** MIT-licensed source package exists, but reproducing its benchmark setup requires substantial external environments and API configuration; it has not been independently run here.

**Decision:** Keep Candidate E only as a comparison setting for a stronger EC method. Do not use it as the thesis umbrella unless a distinct algorithmic mechanism survives Gate F0 in [COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md](COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md).
