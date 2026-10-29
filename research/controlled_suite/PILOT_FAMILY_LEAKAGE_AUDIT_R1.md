# Pilot Family-Leakage Audit R1

**Date:** 2026-10-29  
**Scope:** The 12 current pilot cases in `pilot_cases_r1.jsonl`; request/context wording, task mechanisms, tool overlap, reference trajectories, and whole-family split.  
**Status:** Initial screen and manual semantic review complete; full 120-case leakage audit is not possible until the remaining cases exist.  
**Boundary:** Lexical similarity is a screening signal, not ground-truth duplicate detection.

## Method

- Fetched the current 12 case records from the repository.
- Normalized file paths to a generic `path` token and integer literals to `number`.
- Lowercased request plus optional context, removed a small stop-word list, and computed pairwise token-set Jaccard similarity.
- Manually reviewed the highest-scoring cross-split pairs for mechanism overlap. The similarity calculation is a transparent heuristic; it is not calibrated to establish leakage or novelty.

## Initial high-overlap pairs

| Pair | Split | Jaccard | Manual interpretation |
|---|---|---:|---|
| F04 ↔ F09 | train ↔ validation | 0.357 | Both were calendar booking requests for room-A with numeric intervals. F04 targets a valid constrained booking; F09 targets avoiding a conflict with an existing reservation. Shared surface form was high enough to warrant reducing the template overlap. |
| F05 ↔ F08 (before revision) | train ↔ validation | 0.308 | Both used `ledger.transfer` from A to B; F05 tests duplicate prevention, F08 tests an overdraft precondition. This was unnecessary tool/action overlap for the pilot. F08 was revised to a bill-amount mismatch precondition. |
| F06 ↔ F12 | train ↔ test | 0.267 | Both mention customer/CRM/email concepts, but the behavior differs: F06 requires a cross-tool state update plus a confirmation email; F12 is a phone-only update with an explicit no-email/no-unrelated-mutation constraint. Keep flagged for the full family-template audit. |
| F06 ↔ F07 | train ↔ validation | 0.200 | Both mention a customer tier and “gold,” but F07 contains two same-name records and requires safe non-mutation under ambiguity; F06 is a single known customer plus email handoff. Semantic distinction exists, but should remain explicit in future variants. |
| F01 ↔ F03 | train ↔ train | 0.167 | Both involve filesystem read/write operations, but they are in the same training split and target different mechanisms (read-before-write vs postcondition read-back). This is not cross-split leakage in the current split. |

No exact duplicate user-request strings were found among the 12 cases. This does **not** establish that all 120 future tasks will be independent.

## Revisions made

### F08 — separate invalid-precondition task from idempotent transfer

Changed F08 from an attempted overdrawn `ledger.transfer` to a bill-payment amount mismatch:
- Bill `BILL-1` is unpaid and has amount 80.
- The request asks to pay 50 only if the amount exactly matches.
- The reference trajectory calls `ledger.pay_bill` with amount 50; the deterministic world returns `AMOUNT_MISMATCH` and leaves the ledger unchanged.
- The oracle requires the full ledger state to remain unchanged and checks the attempted tool/status/arguments.
- The adversarial near-miss pays 80 instead; it is rejected because it violates the user's requested amount and changes ledger state.

This retains the invalid-precondition/policy-conflict family while reducing direct action-template overlap with F05.

### F09 — do not force an unnecessary failed create call

Changed F09's reference trajectory to a successful `calendar.check_availability(room-A, 10, 12)` call only. Since the existing reservation occupies 9–11, the interval conflicts. The correct Agent may check availability and refrain from creation; the scorer no longer requires an unsuccessful `calendar.create_event` merely to pass. The oracle still forbids successful event creation and requires the calendar to remain unchanged.

The task wording was also revised to reduce the repeated “Book room-A...” phrase shared with F04.

## Interpretation and limits

- The whole-family split remains F01–F06 train, F07–F09 validation, F10–F12 test. The two revisions do not change family assignments.
- Shared tools across splits are not automatically leakage: the intended evaluation is transfer across task mechanisms with familiar tool schemas. The critical risk is near-identical task templates or an oracle/reward shortcut that makes the held-out mechanism predictable from surface wording.
- F06/F12 and F06/F07 remain flagged for review as the suite grows. Future variants must vary context and wording without changing the intended mechanism, and should include cross-domain realizations that are not just paraphrases.
- The 12-case pilot is too small to certify family-level independence. A full audit must compare all 120 tasks pairwise using normalized lexical similarity plus manual semantic/action-schema review, inspect shared initial-state templates and oracle structure, and freeze a hash after revisions.
- The production Agent prompt builder does not exist yet. The schema restricts task fields, but an integration allowlist test is still required to prove evaluator-only state/oracle/split/trace/provenance/reference actions are not serialized to the Agent.

## Next action

1. Re-run the pilot reference trajectories and all near-miss tests after the F08/F09 revisions.
2. Recompute the lexical-overlap screen and record the revised top pairs.
3. Author the remaining 108 tasks under fixed family assignments.
4. Run the full pairwise/semantic family-leakage audit and prompt-data allowlist test before closing G1b.
