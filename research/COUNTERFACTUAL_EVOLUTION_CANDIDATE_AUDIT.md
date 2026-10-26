# Candidate Audit: Counterfactual-Evidence-Guided Evolution of Agent Policies

**Audit date:** 2026-10-26  
**Status:** Provisional algorithmic candidate; novelty is unresolved. This is a next-step hypothesis after the broad transactional-recovery formulation failed the novelty screen.  
**Do not implement yet.**

## 1. Why this candidate is being considered

The broad idea “evolve a recovery controller for tool-using agents” is now too crowded: recent work covers transactional runtimes, semantic transactions, verified tool-call wrappers, runtime failure recovery, controlled recoverability, failure-memory learning, and evolutionary tool-policy search.

The remaining possible contribution should therefore be an **evolutionary search mechanism**, not a new application domain or a new benchmark. The candidate is to use controlled counterfactual evidence to estimate which policy edits or variation operators actually change outcomes, then direct evolutionary search using those estimates.

Working question:

> Under fixed base-model weights and matched evaluation conditions, can counterfactual-impact-guided evolutionary search produce more robust agent policies on held-out combinations of tool-fault semantics and task structure than trajectory-judged blame, ordinary adaptive operator selection, and non-evolutionary recovery methods?

This is only a hypothesis. The word “counterfactual” is not itself novel; the question is whether interventional evidence can improve evolutionary credit assignment and transfer.

## 2. Closest prior art and the exact boundary

| Work | What it already does | Implication for this candidate |
|---|---|---|
| [EVOTOOL, ACL 2026](https://aclanthology.org/2026.acl-long.2016/) | Uses an LLM blamer to localize failures to Planner/Selector/Caller/Synthesizer, targeted mutation, and diversity-aware selection. | Direct baseline for blame-guided evolutionary policy search. Replacing its blamer with another judge or renaming the policy modules is not enough. |
| [Causal Agent Replay](https://arxiv.org/abs/2606.08275) | Intervenes on agent trajectory steps, re-executes downstream behavior, estimates causal effects, and uses a Monte-Carlo Shapley estimator for interacting steps. | Direct overlap for counterfactual causal attribution of agent failures. A new contribution must connect verified intervention effects to evolutionary variation/selection and show a benefit beyond CAR-style attribution. |
| [Counterfactual Planning for Generalizable Agents’ Actions, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40184) | Uses causal state representations and a What-If-Not reward to improve action generalization under stochastic feedback. | Direct overlap for counterfactual feedback as a way to improve agent actions. Must compare against causal planning and clarify why evolutionary search is useful. |
| [Where Does Exactly-Once Live? / LIMBO](https://arxiv.org/abs/2609.29095) | Uses a controlled sandbox with a ground-truth ledger, 12 fault modes, and 25,930 episodes; studies ambiguous outcomes, late commits, redelivery, and tool-contract effects. The paper says code/data will be available upon publication. | Strong source for paired, effect-grounded evaluation and impossibility boundaries. Its findings warn that some duplicates cannot be prevented by any client-side policy if the tool contract lacks idempotency support. |
| [Bench2Robust](https://arxiv.org/abs/2608.11977) | Separates retry, switch-to-fallback, and no-viable-path cases; uses Bayesian Tool Memory and RL for recovery behavior. | Strong baseline for scenario-controlled recoverability and learned recovery, not an EC algorithm. |
| [Sentry](https://arxiv.org/abs/2610.02994) · [MIT code](https://github.com/nuglifeleoji/Sentry) | Diagnoses failures at runtime, retrieves matching recovery lessons, verifies recovery, and stores only verified lessons in a playbook. | Strong non-EA runtime recovery baseline. It already addresses conditional exposure of failure knowledge and cross-task transfer. |
| [Verified Tool Calls](https://arxiv.org/abs/2608.02645) | Adds postcondition verification, verify-before-retry, and idempotency keys to a tool wrapper. | Simple deterministic verification/retry baseline must be included; do not assume an LLM controller is necessary. |
| [Atomix](https://github.com/mpi-dsg/atomix) · [Apache-2.0 code](https://github.com/mpi-dsg/atomix/blob/main/LICENSE) | Provides a runnable transactional runtime, experiment configurations, fault-injection workloads, and fixed protocol baselines. | Use as a runtime baseline if compatible, not as the proposed novelty. It already handles many execution-layer guarantees. |
| Classical adaptive operator selection (AOS) and self-adaptation | Select operators using historical rewards, probabilities, pursuit/bandit mechanisms, or encoded control parameters. | The new controller must beat mature AOS, not merely change operator probabilities. A separate literature audit of the exact EC baselines is still required. |

## 3. Proposed algorithmic object

The policy genome should be a bounded, typed program or decision tree, not an unconstrained natural-language prompt. It can encode:
- the observable conditions that trigger verification, safe retry, refresh, fallback, confirmation, compensation, or abort;
- the permitted action after each condition;
- recovery-state transitions and termination conditions;
- operator-editable substructures with explicit type and safety constraints.

The policy never sees hidden fault labels, oracle recovery actions, future outcomes, or fitness annotations. An immutable external monitor enforces hard safety invariants.

### Counterfactual evaluation unit

For each task family, define a controlled *fault twin* pair that shares the same task, initial state, tool contract, and randomization seed where feasible, but differs by one specified intervention—for example:
- an acknowledgement is lost with no side effect versus lost after the side effect commits;
- a tool is transiently unavailable versus permanently unavailable;
- a fallback-equivalent tool exists versus all valid paths are blocked;
- a state change is stale-but-benign versus a true conflicting write.

The acting policy receives only runtime-observable evidence. The evaluator keeps the intervention label and ground-truth effect ledger hidden.

Use repeated paired rollouts when stochastic model sampling prevents exact trajectory matching. Report uncertainty rather than treating one pair as a deterministic causal truth.

### Proposed search mechanism

1. Evaluate each candidate on paired fault twins and estimate the *interventional outcome delta* for policy components/operators, not just the raw score of one rollout.
2. Use verified causal deltas to rank candidate edit targets and update the operator-selection distribution.
3. Preserve policies that are complementary across fault families and task structures, while rejecting candidates that violate hard invariants.
4. Select on a preregistered training/validation split; evaluate once on held-out combinations of fault semantics × task topology × tool contract.

This is a sketch, not a final algorithm. The exact estimator, credit assignment, operator update rule, and archive design must be specified and ablated.

## 4. What would make it a substantive EC contribution?

At least one of the following must be demonstrated, and it must survive direct ablation:

- **Causal edit credit:** counterfactual evidence identifies which policy substructure or operator caused a performance change more reliably than trajectory-only LLM blame.
- **Transferable operator control:** the learned operator-selection policy transfers to held-out task/fault families better than uniform selection, probability matching/adaptive pursuit, UCB-style AOS, and self-adaptation.
- **Compositional generalization:** the evolved policy improves on unseen combinations of individually observed fault primitives and task structures, not merely on new seeds or more training cases.

If the gains arise only because the method runs more rollouts, uses a stronger proposer, or gets access to hidden labels, reject it. Finite-budget efficiency is not the main contribution; budgets must nevertheless be matched to avoid confounding.

## 4. A more precise mechanism hypothesis

The generic version—use paired outcome deltas to update operator probabilities—is too close to ordinary adaptive operator selection. The only variant worth carrying to the next prior-art gate is **interventional operator-interaction-guided variation**.

### Objects and estimands

Let a policy genome be a typed recovery state machine with editable loci (conditions, transitions, actions, guards). Let \(g\) be a parent, \(o_i\) an edit operator applied to locus \(i\), and \(z\) a controlled task/fault-twin scenario. Let \(Y(g,z)\) be the outcome vector, measured from the external effect ledger and task oracle. Hard safety violations are a separate feasibility gate, not a score that can be traded against task success.

For a single edit, estimate the paired effect:
\[
\widehat{\tau}_{i}(z)=Y(g\oplus o_i,z)-Y(g,z).
\]

For two candidate edits, evaluate the four matched variants (parent, edit i, edit j, both edits) and estimate the non-additive interaction:
\[
\widehat{\kappa}_{ij}(z)=Y(g\oplus o_i\oplus o_j,z)-Y(g\oplus o_i,z)-Y(g\oplus o_j,z)+Y(g,z).
\]

Estimate these quantities separately for success, false-abort rate, and duplicate/unsafe side effects across fault families and task topologies. The safety gate remains external: any candidate violating a hard invariant on the designated validation suite is infeasible regardless of its success score.

### Search rule to test

1. Run matched fault-twin evaluations for the parent and candidate edits. The acting policy never sees the intervention label.
2. Build a policy-edit interaction graph: nodes are typed editable loci/operators; edges are retained only when the estimated interaction is stable across resamples and has a beneficial direction on preregistered outcomes.
3. Use the graph to propose co-mutations of interacting loci; use a held-out validation split to select survivors. When no reliable interaction is found, fall back to a baseline mutation/selection rule rather than forcing linkage.
4. Keep the interaction graph and operator rewards training-only. Evaluate on held-out combinations of fault semantics × task-DAG topology × tool-contract affordance.

This is not yet an approved algorithm. The graph threshold, estimator uncertainty rule, multiobjective survivor selection, and transfer protocol must be preregistered. The method must be compared with ordinary paired-fitness AOS and classical linkage-learning GAs, not only with random mutation.

### Why this may be more distinct—and why it may still fail

- EVOTOOL attributes failures to policy modules and mutates the blamed module; it does not, in the reviewed method description, estimate factorial causal interaction effects between edits.
- Causal Agent Replay estimates causal effects of trajectory-step interventions and Shapley contributions; it is not an evolutionary operator-linkage algorithm.
- Classical AOS adapts operator probabilities from historical performance; linkage-learning GAs infer variable dependencies from the population. The proposed mechanism would need to show that controlled interventional interaction estimates add information not captured by either baseline.
- If the graph is simply a noisy reward-correlation matrix, if paired differences alone explain all gains, or if standard linkage learning matches it, reject the candidate.

## 5. Minimum falsification plan

| Gate | Required comparison | Stop condition |
|---|---|---|
| F0 — Prior-art gate | EVOTOOL, Causal Agent Replay, Counterfactual Planning, classical AOS, self-adaptation, Sentry, Bench2Robust. | No explicit algorithmic distinction beyond combining known components. |
| F1 — Oracle integrity | Hidden-label leakage tests; deterministic effect ledger; pair construction validation; property tests for solvability and safety. | Candidate can infer hidden fault labels or evaluator outcomes are not independently grounded. |
| F2 — Credit validity | Compare interventional edit credit with LLM blame, trajectory heuristics, random target selection, and no attribution. | Causal edit credit does not better predict out-of-sample policy improvements. |
| F3 — Search value | Uniform/random mutation, greedy one-child edits, static EA, classical AOS, EVOTOOL-style baseline, and a fixed-policy baseline. Match model calls, rollouts, and seed/task sets. | EA or counterfactual guidance does not improve held-out outcomes. |
| F4 — Transfer | Hold out combinations of fault semantics, topology, and tool-contract affordances; where feasible, transfer to another base model without tuning on test tasks. | Gains are only in-distribution or disappear when fault labels are hidden. |
| F5 — Safety and robustness | Report task completion, duplicate/unsafe side effects, false aborts, recovery actions, invariant violations, confidence intervals, and seed sensitivity. | Success gains trade away hard safety or are driven by one task family/seed. |

## 6. Data and code feasibility findings from the current audit

- **Atomix:** official repository declares Apache-2.0; it contains the Python runtime, fixed baseline implementations, tests, and local experiment configurations. It is the best immediately inspectable runtime baseline, though we have not executed its suite in this session.
- **ResiliBench:** the linked repository contains supplementary JSON tool/task registries but no top-level license file/license metadata and no full experiment runner in the inspected tree. Do not redistribute or rely on it as a reproducible primary benchmark until terms and the complete evaluation implementation are verified.
- **Vera:** the official repository contains LEGAL.md but no top-level software license file was present in the inspected root. Do not assume that the code/data are permissively licensed.
- **Harmony Harness:** the arXiv paper page did not provide an author-linked official code repository in the inspected material. The GitHub repository found during the search is a third-party implementation/extension, not evidence of an official reproduction.
- **Sentry:** an MIT-licensed source package is available; the paper’s benchmark setup has substantial environment and API dependencies. It is a baseline candidate, not yet independently run here.
- **LIMBO, Bench2Robust, Cordon, Agentic Transaction, and Verified Tool Calls:** their inspected paper pages did not provide a confirmed official runnable code/data link. Treat their claims as prior-art evidence, but do not label them reproducible baselines until a canonical release is located.

## 7. Current decision

**Candidate E (generic transaction-aware recovery-controller evolution) is downgraded.** The space is directly covered by Atomix, Cordon, Agentic Transaction, AIR, LIMBO, Verified Tool Calls, Bench2Robust, Sentry, ResiliBench, and related work; a controller genome and a safety/functionality score alone do not make it a novel method.

**Candidate F (counterfactual-evidence-guided evolutionary search) is the next hypothesis to falsify, not an approved topic.** It is more algorithm-centered: its possible contribution is to use measured interventions to guide evolutionary credit assignment and operator/target selection. However, Causal Agent Replay, Counterfactual Planning, EVOTOOL, and mature AOS are direct overlaps. The exact combination may still be incremental; Gate F0 must decide this before implementation.

Do not populate the thesis–paper map yet. If F fails Gate F0, broaden the search again rather than forcing the transactional recovery theme.
