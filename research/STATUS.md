# Current Project Status

**Last updated:** 2026-10-23  
**Stage:** 2 — second-pass literature triage; mechanism-level audit pending  
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

- Added research/EC_ROLE_AND_PARAMETER_CONTROL.md to separate Agent-policy evolution, evolutionary-algorithm parameter control, and task/environment/evaluation settings.
- Inspected the official EVOTOOL repository (configs, SPEC.md, blame, mutation, selection, and evolution loop). Its central mechanism axes are blame/random/fixed/all/none mutation targets and diversity/greedy/top-k/static selection, with explicit trajectory/feedback ablations—not simply a numerical mutation-rate sweep.
- Added LLaMEA-HPO, Code World Models for Parameter Control, LLM mutation-control work, classical parameter-control references, and evolutionary recovery-controller work to the related-work matrix.
- Key methodological conclusion: structural/behavioural evolution and numerical hyperparameter tuning must be separated. Parameter control is mature EC prior art; no new method or thesis topic has been approved.

- Second-pass search expanded the related-work matrix from 15 to 37 core or adjacent papers/works, including 2026 work on tool-policy evolution, multi-agent evolution, skills, memory, planning, open-world shifts, and continual adaptation.
- Added research/CAPABILITY_GAP_REVIEW.md with field-crowding evidence, a provisional candidate comparison, and an explicit falsification plan.
- Found direct overlap for failure attribution (EVOTOOL/EvoMAS/HarnessEvolve), group/open-ended evolution (GEA/CORAL/EvE), skill and memory evolution (CoEvoSkills/Mem²Evolve/SkillComposer/ReMe/MCMA/MemEvolve), and planning (EvoPlan/APB/EvA/QD planning).
- No candidate is approved. The first candidate to audit is state-contingent recovery from unseen tool/environment failures, but it has significant overlap risk and must be rejected if it reduces to a small variant of EVOTOOL or existing recovery/planning methods.

- Initialized project charter, literature protocol, thesis–paper map, decision log, and session handoff.
- Performed a first-pass search across recent agent/EA papers and surveys.
- Registered a preliminary matrix of 15 papers or closely related works in research/RELATED_WORK_MATRIX.md.
- Wrote research/INITIAL_RESEARCH_MEMO.md to capture what is already crowded and which candidate questions require deeper auditing.
- Confirmed that broad claims about prompt evolution, multi-agent generation, modular agent search, workflow evolution, whole-agent configuration tuning, memory evolution, and cost-aware optimization have substantial prior art.

## Evidence state and caveats

This is a **first-pass map**, not a systematic review and not a novelty assessment. Some papers have been read at abstract/method/results level; not every paper, supplement, or codebase has been fully audited. Candidate research questions remain hypotheses. No innovation point is approved.

## Latest scope adjustment (2026-10-23)

The user considers finite-budget evaluation efficiency insufficiently compelling as the central thesis problem. Therefore:
- Do **not** promote evaluation-budget allocation, noisy-fitness estimation, or survivor selection under limited evaluation budget as the default thesis direction.
- Evaluation cost may remain a secondary constraint/metric when relevant, but must not drive topic selection merely because it is measurable.
- Refocus the next search on important agent capability/behavior limitations where evolutionary computation could enable a substantive improvement, while remaining open to borrowing and improving existing methods.
- Do not treat this scope adjustment as a rejection of all work on evaluation reliability; retain it as supporting background only if a stronger problem requires it.

## Next actions (ordered)

1. Finish the mechanism-level audit of EVOTOOL and record the actual ablations and their limitations.
2. Read LLaMEA-HPO and Code World Models for Parameter Control in full; compare structural evolution, static HPO, and online control.
3. Review classical parameter-control and adaptive-operator-selection literature, including self-adaptation.
4. Audit evolutionary robotics / genetic programming for recovery after unanticipated failures.
5. Decide whether the strongest contribution should be a constrained Agent-policy representation, a new variation/selection mechanism, or a genuinely distinct parameter controller; reject generic parameter tuning as the sole contribution.
6. Only then resume candidate ranking and thesis/paper decomposition.


1. Deep-read EVOTOOL, EvoMAS, EvA, HarnessEvolve, APB, and the 2026 quality-diversity planning paper; record representation, failure signals, recovery behavior, evolutionary unit, and generalization protocol.
2. Read CostBench and OpenAgent to separate planning errors, tool failures, infeasible tasks, and distribution shifts.
3. Inspect official code for the closest methods where available; verify what can actually be reproduced.
4. Search traditional evolutionary robotics, genetic programming for reactive policies, program synthesis, dynamic optimization, and adversarial/curriculum co-evolution.
5. Try to falsify the leading candidate (state-contingent recovery from unseen failures) against EVOTOOL and other baselines; if overlap is too high, compare compositional generalization and agent/environment co-evolution instead.
6. Produce a mechanism-level overlap table and revised candidate ranking. Do not draft final innovation claims before this is done.
7. Select a provisional umbrella problem only after the candidate survives the audit; then draft the proposal and 2–3 distinct paper plans.

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
