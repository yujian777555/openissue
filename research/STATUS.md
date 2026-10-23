# Current Project Status

**Last updated:** 2026-10-23  
**Stage:** 2 — second-pass literature triage and mechanism-level audit in progress  
**Overall status:** OPEN; topic not selected  
**Source of truth:** this repository

## Objective

Prepare a defensible graduate thesis proposal on evolutionary computation applied to AI agents, aiming for 2–3 connected innovation points and 2–3 small-paper submissions.

## Confirmed requirements

- The immediate milestone is the thesis proposal/opening report.
- The thesis should be built around 2–3 substantive, connected contributions.
- Each contribution should have a plausible path to an independently publishable paper.
- The research should use evolutionary computation as a central method.
- Related work may be borrowed and improved; novelty does not require being completely unrelated to prior work.
- Existing work must be examined carefully before accepting or rejecting an idea.
- This project must be resumable across new ChatGPT conversations using repository records.
- Do not import candidate directions or conclusions from unrelated projects or previous conversations.

## Not yet decided

- Exact research question and title.
- Whether the central object is a single-agent component, a multi-agent system, an evolutionary search mechanism, or another agent capability.
- Whether RSI is in scope for the final proposal.
- Candidate evolutionary algorithm(s), representation, base model, benchmarks, and evaluation metrics.
- Which papers or codebases will be the primary baselines.
- Final 2–3 innovation points and their mapping to papers.

## Research completed so far

- Added research/EC_PARAMETER_CONTROL_EXPERIMENT_PROTOCOL.md with a staged experiment plan: benchmark sanity, policy DSL, static EA, static HPO, then adaptive parameter/operator control. It defines parameter layers, initial pilot ranges, baselines, metrics, ablations, and stop criteria.
- Audited ToolMaze (arXiv 2026 + official repository) as a potential controlled evaluation substrate: task DAG complexity C1–C4, explicit/implicit × transient/permanent faults, deterministic injection, valid-path enumeration, and TSR/PRR/RC metrics. It remains a benchmark, not an EA contribution. The source-pinned audit now records that current code intentionally changed RC to hit-conditioned at commit `f8620d8`, while paper/README still describe all-run RC; report both definitions and exposure rate if adopted.
- Deep-read key sections of EVOTOOL's paper: its ablations show that targeted module selection, trajectory plus explicit feedback, and diversity-aware selection all matter; its prior-art overlap with generic failure-aware tool-policy evolution is therefore high.
- Read the method and limitations of Code World Models for Parameter Control and LLaMEA-HPO. CWM controls mutation strength in a classical (1+1)-RLS_k optimizer and depends on problem descriptions/structured transition statistics in harder settings; LLaMEA-HPO separates LLM algorithm-structure search from SMAC tuning of generated-heuristic parameters. Neither establishes that online EA parameter control helps an LLM Agent policy EA.
- Registered ToolMaze, hierarchical QD recovery, the 2025 adaptive-operator-selection survey, APB, EvA, τ²-bench, and BFCL V4 as P45–P51 in the related-work matrix. APB-guided refinement is a non-EA baseline; EvA's abstraction/rollback controller is adjacent prior art, not automatically a population-based EA. APB is not yet a license-cleared fallback: the inspected code tree and HF card lack explicit license metadata, and its HF viewer fails schema casting. The current τ²-bench repository declares MIT and BFCL code/data declare MIT/Apache-2.0 respectively; these are auxiliary external evaluations, not direct replacements for controlled fault injection.
- ToolMaze adoption remains blocked: Hugging Face exposes one split named `train` rather than a documented optimization train/validation/test protocol, its viewer currently fails nested-schema inference, and neither the code tree nor dataset card exposes an explicit license. The new `research/TOOLMAZE_BENCHMARK_AUDIT.md` specifies split-leakage prevention, dual RC reporting, and the license gate.
- Audited recent primary sources for Agent-World, SEAL, SENTINEL, COvolve, RLAnything, and the 2026 co-evolution survey. Generic agent–environment co-evolution and failure-driven task generation are too crowded to claim as novel. Added P52–P57 and `research/COEVOLUTION_CANDIDATE_AUDIT.md`; the only retained narrow hypothesis is typed recovery-program EA plus valid fault-program search for held-out fault-semantics × task-topology generalization. This remains speculative; Candidate D (meta-evolution of the search mechanism) also requires an overlap audit.


- Added research/EC_ROLE_AND_PARAMETER_CONTROL.md to separate Agent-policy evolution, evolutionary-algorithm parameter control, and task/environment/evaluation settings.
- Inspected the official EVOTOOL repository (configs, SPEC.md, blame, mutation, selection, and evolution loop). Its central mechanism axes are blame/random/fixed/all/none mutation targets and diversity/greedy/top-k/static selection, with explicit trajectory/feedback ablations—not simply a numerical mutation-rate sweep.
- Added LLaMEA-HPO, Code World Models for Parameter Control, LLM mutation-control work, classical parameter-control references, and evolutionary recovery-controller work to the related-work matrix.
- Key methodological conclusion: structural/behavioural evolution and numerical hyperparameter tuning must be separated. Parameter control is mature EC prior art; no new method or thesis topic has been approved.

- Second-pass search expanded the related-work matrix from 15 to 37 core or adjacent papers/works, including 2026 work on tool-policy evolution, multi-agent evolution, skills, memory, planning, open-world shifts, and continual adaptation.
- Added research/CAPABILITY_GAP_REVIEW.md with field-crowding evidence, a provisional candidate comparison, and an explicit falsification plan.
- Found direct overlap for failure attribution (EVOTOOL/EvoMAS/HarnessEvolve), group/open-ended evolution (GEA/CORAL/EvE), skill and memory evolution (CoEvoSkills/Mem²Evolve/SkillComposer/ReMe/MCMA/MemEvolve), and planning (EvoPlan/APB/EvA/QD planning).
- No candidate is approved. State-contingent recovery remains a candidate to falsify; generic policy–curriculum co-evolution has been downgraded after direct overlap was found with COvolve, Agent-World, SEAL, SENTINEL, and RLAnything.

- Initialized project charter, literature protocol, thesis–paper map, decision log, and session handoff.
- Performed a first-pass search across recent agent/EA papers and surveys.
- Registered a preliminary matrix of 15 papers or closely related works in research/RELATED_WORK_MATRIX.md.
- Wrote research/INITIAL_RESEARCH_MEMO.md to capture what is already crowded and which candidate questions require deeper auditing.
- Confirmed that broad claims about prompt evolution, multi-agent generation, modular agent search, workflow evolution, whole-agent configuration tuning, memory evolution, and cost-aware optimization have substantial prior art.

## Evidence state and caveats

This is a **multi-pass preliminary map**, not a completed systematic review or novelty assessment. Some papers have been read at abstract/method/results level; not every paper, supplement, or codebase has been fully audited. Candidate research questions remain hypotheses. No innovation point is approved.

## Latest scope adjustment (2026-10-23)

The user considers finite-budget evaluation efficiency insufficiently compelling as the central thesis problem. Therefore:
- Do **not** promote evaluation-budget allocation, noisy-fitness estimation, or survivor selection under limited evaluation budget as the default thesis direction.
- Evaluation cost may remain a secondary constraint/metric when relevant, but must not drive topic selection merely because it is measurable.
- Refocus the next search on important agent capability/behavior limitations where evolutionary computation could enable a substantive improvement, while remaining open to borrowing and improving existing methods.
- Do not treat this scope adjustment as a rejection of all work on evaluation reliability; retain it as supporting background only if a stronger problem requires it.

## Next actions (ordered)

1. **Complete the meta-evolution prior-art audit:** read the primary papers and available code for PromptBreeder, Gödel Agent, HyperAgents, RQGM, and SIA; compare their adaptive decisions with classical adaptive operator selection and LLM mutation-control work.
2. **Close Gate G0 for the recovery candidate:** write a mechanism-by-mechanism difference table against COvolve, Agent-World, SEAL, SENTINEL, EVOTOOL, and HarnessEvolve. Decide whether typed fault-program search plus typed recovery-controller EA is genuinely distinct, rather than a domain-specific combination of known methods.
3. Continue the ToolMaze/APB code/data-rights and raw-loader checks. In parallel, assess τ²-bench (MIT) and BFCL V4 (Apache-2.0) only as auxiliary external tests. If no controlled benchmark has suitable terms, design an independent DAG/fault generator.
4. Only after Gates G0 and benchmark validity pass, specify the policy/fault grammar, evaluator contract, hidden-label isolation, and solvability/property tests.
5. Compare fixed rules, direct reflection/replanning, random structured mutation, greedy one-child mutation, static population EA, and the strongest reproducible prior-art baseline under matched model-call and rollout budgets.
6. Only if static EA shows repeatable held-out gains, test static HPO, deterministic schedules, classical AOS, and self-adaptation as separate later mechanisms.
7. Re-rank candidates and update the thesis–paper map only when one direction has a distinct falsifiable claim. No topic or novelty claim is approved yet.

## Definition of done for the next milestone

The literature-scouting milestone is complete only when there is:
- a cited and verifiable set of relevant papers;
- a taxonomy and comparison matrix;
- deep analyses of the closest prior work;
- a ranked shortlist with explicit uncertainty and reasons;
- a recommended provisional direction with a falsifiable research question;
- no unsupported claims that the direction is novel.

## Update protocol

At the end of every meaningful research session, update this file with what was verified, files and sources added, decisions made and why, unresolved questions, the next concrete action, and the relevant commit SHA when available.
