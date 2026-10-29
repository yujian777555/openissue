# Mandatory Repository Continuity Protocol

**This file is a permanent instruction for every ChatGPT research session in this repository.**

## Non-negotiable rule

Every time work is done on the master's thesis project, maintain continuity in `yujian777555/openissue`. Do not rely on chat memory alone. At the end of every substantive session, update the repository and prepare the next-session handoff prompt. This applies even if the work is mainly literature review, reasoning, planning, or a failed/negative result.

## Start of every session

1. Confirm repository `yujian777555/openissue`, default branch `main`; never silently switch to another project repository.
2. Fetch and read the latest `README.md`, `research/STATUS.md`, `research/DECISION_LOG.md`, `SESSION_HANDOFF.md`, `NEXT_SESSION_PROMPT.md`, and the current research note relevant to the next task.
3. Inspect the latest commits and relevant new/changed files before deciding what to do.
4. Summarize internally (and to the user when useful): current stage, last verified commit, confirmed facts, hypotheses, open gates, and the next incomplete action.
5. Do not ask the user to repeat information already recorded in the repository.

## During the session

- Keep source-verified facts, author claims, interpretation, hypotheses, and experiment results clearly separated.
- Record negative results and reasons for rejecting a candidate; do not hide them or restart disproved directions without new evidence.
- Do not mark literature audits, tests, experiments, API calls, or repository pushes as completed without evidence.
- Before changing an existing file, fetch its latest contents and blob SHA. Make focused edits; avoid overwriting unrelated work.
- After each meaningful research decision, update the relevant research artifact and `research/STATUS.md` and/or `research/DECISION_LOG.md`.
- Respect existing project boundaries. This repository is for the thesis proposal on Agent × evolutionary computation. Do not mix results from `agentfotagent`, `EvoPareto-Agent`, `CausalEvo-DSH`, `GLEPPO`, or other repositories.

## End of every session — mandatory checklist

- [ ] Update the relevant research file(s) with evidence, conclusions, uncertainties, and references.
- [ ] Update `research/STATUS.md` with the actual current stage, gate state, completed work, and next action.
- [ ] Update `research/DECISION_LOG.md` when a consequential decision, rejection, scope constraint, or gate change occurs.
- [ ] Update `SESSION_HANDOFF.md` with a concise but complete current-state summary.
- [ ] Update `NEXT_SESSION_PROMPT.md` with a copyable prompt reflecting the latest state and next unfinished task.
- [ ] Ensure `README.md` links to the current continuity files when the protocol or major stage changes.
- [ ] Commit the changes to the intended branch using the available GitHub integration.
- [ ] Fetch the changed files and inspect the latest commit list to verify that the writes actually landed.
- [ ] Report changed paths, commit SHA(s), verification status, current gate states, and the exact next action to the user.

If no new research evidence or decision emerged, still update the handoff/prompt with the verified current state and state explicitly that no substantive research result changed. Do not create meaningless edits just to simulate progress. If repository access or a write fails, report the failure clearly and do not claim success.

## Research-specific guardrails

- Immediate deliverable: the master's thesis opening report, not immediate implementation of a standalone paper.
- Evolutionary computation must be central; explicit EA parameter tuning/control must be addressed.
- Prefer two strong connected contributions over three weak or duplicated claims.
- Do not reject a topic merely because prior work exists; identify what can be improved, then falsify the proposed gap.
- Do not claim novelty until closest-work comparison is verified.
- Do not begin large or paid API experiments before the required method, benchmark, license, split, and baseline gates are passed.
- Communication-evolution topics remain excluded unless the user explicitly changes scope.
- OSLVC-R1 is a candidate hypothesis, not an approved innovation.

## Current file roles

- `README.md`: repository overview and links to the continuity protocol.
- `research/STATUS.md`: current research state and next actions.
- `research/DECISION_LOG.md`: durable consequential decisions and rationale.
- `SESSION_HANDOFF.md`: detailed handoff, context, constraints, and current gate states.
- `NEXT_SESSION_PROMPT.md`: copyable prompt to paste into a new ChatGPT session; update it every session.
- `research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md`: current thesis feasibility, method hypothesis, benchmark guardrails, and gate plan.

The user should not need to remind the assistant to maintain the repository or prepare a handoff prompt.
