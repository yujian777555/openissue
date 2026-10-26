# Capability-Gap Review — Second Pass (2026-10-23)

## Status

**State update (2026-10-26):** This is a historical second-pass candidate review, not the current decision source. Later audits downgraded Candidate E, Candidate F did not pass F0, and Candidate G's current formulation did not pass G0. See `STATUS.md`, `DECISION_LOG.md`, and `CANDIDATE_G_G0_REASSESSMENT.md`. Historical action labels below are not authorization to implement a candidate.

No thesis direction is approved. The second-pass literature map now includes recent 2026 work across tool-use policy evolution, multi-agent evolution, skills, memory, planning, open-world generalization, and continual adaptation. The user has explicitly deprioritized finite evaluation budget as the thesis core.

## 1. Crowded research areas

- **Tool-use policy evolution:** EVOTOOL combines modular policy decomposition, trajectory-grounded blame attribution, targeted mutation, and diversity-aware selection.
- **Multi-agent configuration evolution:** EvoMAS evolves structured configurations including prompts, model assignments, tools, and topology. GEA evolves groups with cross-branch experience sharing; CORAL enables autonomous long-running multi-agent search with shared memory.
- **Skills and memory:** CoEvoSkills evolves skills and a verifier; Mem2Evolve co-evolves capability assets and experience; SkillComposer learns skill creation, improvement, and merging; ReMe and MCMA refine memory abstraction and reuse; MAGNET handles changing GUI workflows.
- **Planning:** APB diagnoses long-horizon planning and tool-noise failures; EvoPlan searches over complete plans; EvA uses reusable quasi-symbolic abstractions and rollback; a 2026 QD paper evolves diverse embodied planning policies and switches policies after stalls.
- **Generalization and continual adaptation:** OpenAgent studies shifts in queries, actions, observations, and domains; HarnessEvolve addresses shortcut learning and catastrophic forgetting; EvA studies mid-episode shifts; other recent work covers skill transfer and memory-based continual learning.
- **Open-ended discovery:** CORAL, GEA, and EvE already explore agent autonomy, group/dual-population evolution, persistent knowledge, and co-evolving agent guidance/solutions.

Therefore, broad topics such as EA for tool use, memory, planning, topology, generalization, or self-improvement are not sufficient innovation statements.

## 2. Capability problems worth evaluating

1. **Recovery after tool/environment failure.** APB tests extraneous tools, broken tools, and infeasible tasks; CostBench tests dynamic blocking and cost changes; EVOTOOL diagnoses failures in tool-use trajectories. A potentially meaningful question is whether an agent can acquire and select robust state-contingent recovery behavior when the failure mode was not represented during optimization. This remains a candidate, not a recommendation: EVOTOOL, EvA, HarnessEvolve, APB, and QD planning must be compared carefully.
2. **Compositional generalization.** SkillsBench reports uneven skill gains and no average benefit from self-generated skills in its tested setting. SkillComposer, CoEvoSkills, Mem2Evolve, MCMA, and related work already address skills and transfer. A contribution must improve behavior composition under unseen combinations, not merely generate or merge more skills.
3. **Preserving prior capability during task shifts.** This is important, but HarnessEvolve, OpenAgent, EvA, and continual-memory studies directly address adjacent parts of the problem.
4. **Joint agent/environment co-evolution.** ScaleEnv and APB show that environment/task construction matters, but adversarial curricula and agent/environment co-evolution have a long prior history. Broader EC/RL review is required.

## 2A. New benchmark evidence and narrowed recovery question

**ToolMaze** (June 2026 arXiv preprint; https://arxiv.org/abs/2606.05806; code: https://github.com/Zhudongsheng75/ToolMaze) provides a controlled testbed with DAG complexity C1–C4 crossed with explicit/implicit and transient/permanent perturbations. It deterministically injects faults at specified tool nodes and reports task success (TSR), perturbation recovery (PRR), and recovery cost (RC). This is a useful evaluation substrate, but it does not itself establish an evolutionary-method gap. Its runtime policy must not receive hidden fault labels.

The candidate question is narrowed to a staged test, not a method claim:

> First, does an explicit, typed recovery-policy representation give a static EA a useful search space? Only if yes, does adaptive operator/parameter control improve held-out generalization beyond a strong statically tuned EA and EVOTOOL-style blame-aware policy evolution?

The policy-genotype proposal would encode observable conditions and recovery actions (retry, verify, reroute, backtrack/replan, or terminate/clarify), with typed mutation/crossover operations whose realized edits can be logged. This differs in representation from free-text module prompts, but representation alone is not a novelty claim. EVOTOOL already uses module-level blame and diversity-aware selection; HarnessEvolve already uses reference-trajectory alignment, error clustering, quality gates, and anti-forgetting gates; hierarchical QD has long studied diverse recovery repertoires. A distinct capability/mechanism and controlled evidence are still required.

### ToolMaze metric version drift and dataset gate

The source-pinned audit is in [TOOLMAZE_BENCHMARK_AUDIT.md](TOOLMAZE_BENCHMARK_AUDIT.md). The paper Eq. (4) and current README define all-run RC (no-hit contributes zero), but official code HEAD `f8620d841b67a72ac921caee9df87af6ab9befbb` deliberately changed RC to hit-conditioned on 2026-10-20. This is a documented version change with stale paper/README definitions, not necessarily an accidental code bug. A synthetic example gives all-run RC 0.4 versus hit-conditioned RC 0.6; report both plus exposure rate if adopted.

The HF dataset page exposes only one split named `train`, not a documented optimization train/validation/test protocol, and the viewer currently fails to infer a consistent nested schema. The code tree has no root LICENSE and the dataset card declares no explicit license. Therefore ToolMaze is **on hold as a primary benchmark** until code/data terms and raw-file schema are validated. Any split must group all perturbation variants by base task ID/template to avoid leakage.

A staged experimental protocol is recorded in [EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md](EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md). It separates policy genes, EA meta-parameters, online controller parameters, and environment/evaluation settings; proposes static HPO, classical adaptive operator selection, self-adaptation, and optional CWM-style control baselines; and includes falsification/stop criteria.

## 3. Provisional candidate ranking

Scores are qualitative planning aids, not measurements or novelty claims.

| Candidate family | Importance | Novelty headroom | Feasibility | Potential for 2–3 papers | Status |
|---|---:|---:|---:|---:|---|
| State-contingent recovery from unseen tool/environment failures | 5 | 2.5 | 4 | 4 | First to audit, not selected |
| Compositional generalization across unseen skill combinations | 5 | 2 | 3 | 4 | Keep; high overlap |
| Continual adaptation without loss of prior capabilities | 5 | 1.5 | 4 | 4 | Important but crowded |
| Agent/environment co-evolution for robust adaptation | 4 | 2.5 | 3 | 4 | Keep only if a distinct EC gap emerges |
| Generic multi-agent topology/role evolution | 4 | 1 | 4 | 4 | Do not pursue in broad form |
| Prompt, memory, or skill evolution as such | 4 | 1 | 4 | 3 | Do not pursue in broad form |
| Finite-budget evaluation allocation | — | — | — | — | Deprioritized per user direction |

The first candidate has concrete, observable failures and can be externally verified. It is not the final thesis recommendation: EVOTOOL already performs failure localization and targeted policy edits, EvA studies mid-episode shifts, HarnessEvolve gates updates, APB diagnoses broken-tool/infeasible-task behavior, and QD planning uses stall detection, rollback, and policy switching. We must find a mechanism-level difference rather than combine ingredients.

## 4. Mechanism-level comparison required

For state-contingent recovery, compare:
- **Representation:** free-text prompts, modular instructions, workflows, code, state machines, or executable contingency rules.
- **Failure evidence:** terminal outcomes, trajectory symptoms, typed tool errors, environment state, or counterfactual evidence.
- **Recovery action:** retry, replan, switch policy, repair a call, abandon infeasible tasks, or recover corrupted state.
- **Generalization test:** failure types seen during optimization versus held-out types/environments or mid-episode changes.
- **Evolutionary role:** static configuration search, online recovery-policy evolution, behavior repertoire maintenance, or agent/environment co-evolution.
- **Baselines:** EVOTOOL, fixed retry/replan rules, non-evolutionary reflection/planning, and a standard EA baseline.
- **Failure criteria:** no held-out improvement, gains explained by extra inference, worse normal-case behavior, no benefit over simple heuristics, or failure to transfer.

If the candidate is simply EVOTOOL plus a state machine, reject it. If the audit identifies a distinct failure mode and principled representation/search mechanism, retain it.

## 5. Next actions (historical; superseded by later audits)

The following actions describe the initial second-pass plan. Current project direction is tracked in `STATUS.md` and `SESSION_HANDOFF.md`; do not treat this list as authorization to execute a recovery experiment.

1. Deep-read EVOTOOL, EvoMAS, EvA, HarnessEvolve, APB, and the 2026 quality-diversity planning paper.
2. Read CostBench and OpenAgent to distinguish planning errors, tool failures, infeasible tasks, and distribution shifts.
3. Inspect official code where available.
4. Search traditional evolutionary robotics, genetic programming for reactive policies, program synthesis, dynamic optimization, and adversarial/curriculum co-evolution.
5. Attempt to falsify the recovery candidate against the closest work; if overlap is too high, compare compositional generalization and agent/environment co-evolution instead.
6. Do not draft final innovation claims until a mechanism-level comparison identifies a real gap.


## 6. Reassessment after benchmark-source audit

The recovery-policy candidate remains **the first candidate to falsify**, not the selected thesis topic. The new ToolMaze audit lowers its immediate feasibility: ToolMaze and APB have unresolved explicit code/data licensing; ToolMaze's RC definition changed in code while paper/README remain stale; both HF viewers currently fail schema loading. A benchmark-dependent implementation should not begin until the data/rights gate is resolved.

| Candidate after this audit | Potential strength | Main risk / required falsification | Current action |
|---|---|---|---|
| **A. Evolution of state-contingent recovery policies** | Concrete capability failure; typed policy genotypes and executable external metrics can make EC's role testable. | High overlap with EVOTOOL, EvA, HarnessEvolve, APB-guided refinement, fixed reactive controllers and QD recovery; ToolMaze/APB data terms are unresolved. | Keep as first candidate to falsify; do not implement yet. |
| **B. Policy–failure-curriculum co-evolution** | Can adapt a recovery policy and the faults/tasks that reveal its blind spots. | **Generic formulation fails the novelty gate** after COvolve, Agent-World, SEAL, SENTINEL, and RLAnything. “Generate tasks from failures” and “co-evolve policy/environment” are already covered. | Downgrade. Retain only a narrower hypothesis: EA over typed recovery programs plus valid typed fault transformations, with held-out fault-semantics × DAG-topology generalization. See [COEVOLUTION_CANDIDATE_AUDIT.md](COEVOLUTION_CANDIDATE_AUDIT.md). |
| **C. Compositional generalization of skill/recovery programs** | Tests whether evolved primitives compose on unseen tool/skill combinations rather than memorizing whole tasks. | Direct overlap with skill composition, memory evolution, modular policy search and genetic programming; requires a precise compositional split and a distinct operator/representation contribution. | Keep as a fallback pending the new audit. |
| **D. Meta-evolution of the search mechanism** | Adapt which artifact/operator to evolve, when to trigger edits, and how to select or validate candidates. | **Generic formulation also fails the novelty gate.** Promptbreeder evolves mutation prompts; Gödel Agent, DGM, and HyperAgents evolve self-modification; RQGM co-evolves evaluators; SIA chooses between harness/weight updates; Meta-Harness and MetaBench-Harness search harness/benchmark-generation workflows; classical AOS is mature. | Downgrade. Keep only a narrower transferable search-controller hypothesis if it can beat classical AOS and these closest systems under matched budgets. See [META_EVOLUTION_CANDIDATE_AUDIT.md](META_EVOLUTION_CANDIDATE_AUDIT.md). |

### Candidate paper chain if A/B survives the audit (illustrative only)

- **Paper 1 — Search space and policy evolution:** show whether a typed, executable recovery-policy genotype improves over fixed rules, reflection/replanning, random edits and greedy mutation. If static EA does not help, stop this line.
- **Paper 2 — Policy–curriculum co-evolution:** only if Paper 1 establishes a useful policy search space, test whether evolving valid fault/task curricula improves held-out recovery generalization beyond policy-only EA and fixed/random curricula.
- **Paper 3 — Transfer and robustness:** test frozen policies on a distinct, clearly licensed external environment such as selected τ²-bench/BFCL tasks, with no evolution on final evaluation cases. This paper is optional and should be dropped if it merely reuses the same result or does not establish a separate claim.

This is a decomposition hypothesis, not an approved 2–3 paper plan. Do not populate the thesis–paper map until the closest-work audit establishes independent, defensible claims. Evaluation-budget allocation remains secondary and is not promoted.


## 7. Reassessment after co-evolution prior-art audit

The generic Candidate B is now **downgraded**. The primary-source review found direct tool-agent/environment adaptation in Agent-World and SEAL, failure-driven executable task generation in SENTINEL, and LLM policy/environment adversarial co-evolution in COvolve. RLAnything broadens the overlap to environment–policy–reward joint optimization. See [COEVOLUTION_CANDIDATE_AUDIT.md](COEVOLUTION_CANDIDATE_AUDIT.md) and P52–P57 in the related-work matrix.

The remaining narrow candidate is not “co-evolution” in general. It is the testable possibility that a *typed fault-program grammar* over valid task DAGs, jointly searched with an explicit executable recovery controller, produces better held-out **cross-combinations** of fault semantics and graph topology than:
- policy-only EA;
- failure-driven task generation / reflection;
- an EVOTOOL-style policy evolution baseline;
- a COvolve-style adversarial policy–environment baseline where reproducible;
- fixed and random curricula.

This distinction remains speculative. If its gains reduce to using more targeted tasks, a more expressive representation, or extra inference calls, it is not an EC contribution. The generator must be independently checked for solvability and must not expose hidden fault labels to the acting policy.

The generic Candidate D (meta-evolution of the search mechanism) is now also downgraded after auditing Promptbreeder, Gödel Agent, DGM, HyperAgents, RQGM, SIA, Meta-Harness, MetaBench-Harness, and MoMHa. The survey’s “early-stage” label does not mean its submechanisms are absent. Only a narrow transferable search-controller question remains speculative; see [META_EVOLUTION_CANDIDATE_AUDIT.md](META_EVOLUTION_CANDIDATE_AUDIT.md).

**Current research action:** complete G0 (mechanism-level differentiation) before any implementation. The thesis–paper map remains unpopulated.


## 8. Transaction-aware recovery policy candidate (Candidate E)

A third candidate is added after the second broadening pass: evolutionary synthesis of a bounded controller for **stateful tool workflows with partial effects, races, and irreversible actions**. The full audit is [TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md](TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md), with primary sources P66–P71.

| Candidate | Potential strength | Closest overlap / failure condition | Current action |
|---|---|---|---|
| **E. Transaction-aware recovery-controller evolution** | Concrete and measurable; immutable safety contracts and external state verification are possible. | **Broad novelty gate failed.** Atomix, Cordon, Agentic Transaction, AIR, LIMBO, Verified Tool Calls, Bench2Robust, Sentry, ResiliBench, and Harmony Harness cover the key runtime/recovery/evolution ingredients. A controller genome plus safety/functionality metrics is not sufficient. | Downgrade to a comparison setting, not a thesis topic. See the second-pass section of [TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md](TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md). |

### Required experimental distinction

- Keep the safety monitor/verifier immutable and outside the evolved genome; unsafe actions cannot be traded for higher task success.
- Evolve only a bounded decision controller around transaction-aware tools: verify, refresh, safe/idempotent retry, checkpoint, compensate, request confirmation, replan, or abort.
- Evaluate on controlled partial-effect, race, duplicate-call, and irreversible-action scenarios with explicit state invariants.
- Compare against Atomix + fixed rules, conservative abort, semantic-predicate guards, direct reflection/replanning, and Harmony-Harness-style multi-objective evolution where reproducible.
- Hold out combinations of race type × reversibility × task topology and report both unsafe attempts and false aborts. If only benchmark score improves without a better safe-completion frontier, reject the method.

Candidate E's broad novelty gate was later found to fail after the second-pass audit; it is now a comparison setting, not a thesis topic. See `TRANSACTIONAL_AGENT_ROBUSTNESS_CANDIDATE_AUDIT.md` and D-017 in `DECISION_LOG.md`.


## 9. Counterfactual-evidence-guided evolutionary search (Candidate F)

Candidate F was a method-level hypothesis, documented in [COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md](COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md), but the current formulation later **did not pass Gate F0** after direct overlap with counterfactual repair/attribution and linkage-learning EA. Do not implement it as written; see D-019 in `DECISION_LOG.md`.

| Candidate | Potential method contribution | Direct overlap / stop condition | Current action |
|---|---|---|---|
| **F. Interventional operator-interaction-guided evolution** | Estimate paired causal effects of typed policy edits and non-additive interactions between edit pairs; use a verified interaction graph to guide co-mutation and test held-out fault × topology generalization. | EVOTOOL does blame-guided targeted mutation; Causal Agent Replay estimates causal step attribution; Counterfactual Planning uses counterfactual rewards; classical AOS and linkage-learning GAs are mature. If interaction estimates reduce to reward correlation, or paired AOS/linkage learning matches it, reject it. | **Current formulation not approved; Gate F0 not passed. Do not implement as written.** See [COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md](COUNTERFACTUAL_EVOLUTION_CANDIDATE_AUDIT.md) and D-019. |

### Required Gate F0

1. Define the causal estimand for policy-edit/operator impact and explain how paired interventions handle stochastic model behavior.
2. Distinguish the method from EVOTOOL's trajectory-grounded blame, Causal Agent Replay's step-level interventions/Shapley attribution, Counterfactual Planning, and classical AOS/self-adaptation.
3. Decide whether the proposed signal changes evolutionary selection in a way that simple paired fitness differences, UCB/probability matching, or an LLM blamer cannot reproduce.
4. Only after a written mechanism-level difference is established should an independent simulator or Atomix-based pilot be considered.

