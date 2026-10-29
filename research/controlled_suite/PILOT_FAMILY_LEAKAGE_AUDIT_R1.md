# Pilot Family-Leakage Audit R1

**Date:** 2026-10-29  
**Scope:** The 12 current pilot cases in `pilot_cases_r1.jsonl`; request/context wording, task mechanisms, tool overlap, reference trajectories, and whole-family split.  
**Status:** F08/F09 revisions committed in `3c8e58fc69f09534a5e36ef68c0bf16a4f81e83a`; allowlist helper/tests committed in `0a4c33a1f34f6d900c3e1d4b62821b7281736bed`. CI run [40880783510](https://github.com/yujian777555/openissue/actions/runs/40880783510) passed 33/33. Full 120-case leakage audit remains open.  
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

## Re-screen after the F08/F09 revisions

Using the same tokenization and stop-word rules as the initial screen, the highest observed overlaps after revision are:

| Pair | Split | Jaccard after revision | Interpretation |
|---|---|---:|---|
| F06 ↔ F12 | train ↔ test | 0.267 | Shared CRM/email vocabulary remains; the behavior contrast is required handoff vs minimal side effects. Keep flagged. |
| F05 ↔ F08 | train ↔ validation | 0.200 | Shared amount/account vocabulary remains, but F08 now tests `ledger.pay_bill` amount mismatch rather than another transfer. Keep flagged for semantic review. |
| F06 ↔ F07 | train ↔ validation | 0.200 | Shared customer/tier vocabulary remains; F07 is ambiguity-safe no-op, F06 is update-plus-email. |
| F04 ↔ F09 | train ↔ validation | 0.176 | Reduced from 0.357 after changing F09 wording and its reference trajectory to availability-check-only. |
| F01 ↔ F03 | train ↔ train | 0.167 | Same-split filesystem tasks, distinct read-before-write and read-back mechanisms. |

These scores are not directly comparable with arbitrary other tokenizers; the value here is the before/after comparison under the same normalization. The highest residual overlap is now F06/F12, which remains a known review item rather than being declared clean.

## Agent payload boundary

An `agent_payload_r1.py` helper is implemented and covered by unit tests as a strict allowlist contract: it returns only `task.user_request` and optional `task.context`, rejects unexpected keys inside `task`, and does not copy evaluator-only top-level fields. It is not integrated into a live Agent wrapper. The production prompt path therefore remains an open gate until integration tests exercise the actual serialized prompt and tool schemas.

## Interpretation and limits

- The whole-family split remains F01–F06 train, F07–F09 validation, F10–F12 test. The two revisions do not change family assignments.
- Shared tools across splits are not automatically leakage: the intended evaluation is transfer across task mechanisms with familiar tool schemas. The critical risk is near-identical task templates or an oracle/reward shortcut that makes the held-out mechanism predictable from surface wording.
- F06/F12 and F06/F07 remain flagged for review as the suite grows. Future variants must vary context and wording without changing the intended mechanism, and should include cross-domain realizations that are not just paraphrases.
- The 12-case pilot is too small to certify family-level independence. A full audit must compare all 120 tasks pairwise using normalized lexical similarity plus manual semantic/action-schema review, inspect shared initial-state templates and oracle structure, and freeze a hash after revisions.
- The production Agent prompt builder does not exist yet. The allowlist helper contract can be unit-tested, but an integration test is still required to prove evaluator-only state/oracle/split/trace/provenance/reference actions are not serialized on the actual Agent prompt path.

## Next action

1. Re-run the pilot reference trajectories and all near-miss tests after the F08/F09 revisions.
2. Recompute the lexical-overlap screen and record the revised top pairs.
3. Author the remaining 108 tasks under fixed family assignments.
4. Run the full pairwise/semantic family-leakage audit and prompt-data allowlist test before closing G1b.


## Batch 01 extension — 24-case overlap screen (2026-10-29)

**Scope extension:** the initial audit above covered the original 12 pilot cases. After batch 01, the same normalization/tokenizer was applied to all 24 task requests/contexts (12 pilot + 12 newly authored). This is still a heuristic screen, not a calibrated leakage detector.

### Changes made after screening

| Pair | Initial Jaccard | After revision | Revision |
|---|---:|---:|---|
| F01-D1-V1 ↔ F12-D1-V1 | 0.300 | 0.056 | Rephrased the minimal-side-effect task around setting a mode and preserving the rest of the filesystem, rather than repeating “replace/path/text” wording. |
| F04-D1-V1 ↔ F08-D1-V1 | 0.300 | 0.087 | Rephrased the invalid-precondition case around attempting a read and stopping on a missing source, avoiding repeated delete/unchanged-file wording. |
| F04-D1-V1 ↔ F07-D1-V1 | 0.238 | 0.174 | Rephrased the ambiguity case as identifying candidates and waiting for clarification. |
| F09-D3-V1 ↔ F11-D3-V1 | 0.290 | 0.171 | Changed the compensation task's SKU labels to SKU-X/SKU-Y and clarified the provisional/compensation sequence. |
| F06-D3-V1 ↔ F11-D3-V1 | 0.259 | 0.167 | Same SKU/wording revision reduced shared surface form. |

### Remaining overlap flags

The highest residual cross-family pairs in the 24-case screen include:

| Pair | Jaccard | Review note |
|---|---:|---|
| F06-D5-V1 ↔ F12-D5-V1 | 0.267 | Existing pilot pair: CRM/email handoff versus phone-only minimal side effect. Distinct intended mechanisms, but preserve for independent review. |
| F06-D3-V1 ↔ F09-D3-V1 | 0.241 | Inventory order creation/readback versus insufficient-stock safe no-op. Shared tool vocabulary is expected, but this pair needs a mechanism-level review. |
| F09-D2-V1 ↔ F03-D2-V1 | 0.211 | Calendar conflict avoidance versus create-and-read-back. |
| F05-D4-V1 ↔ F08-D4-V1 | 0.200 | Transfer replay versus exact bill-amount mismatch. |
| F06-D5-V1 ↔ F07-D5-V1 | 0.200 | Customer update/email versus ambiguous same-name entity. |
| F02-D5-V1 ↔ F06-D3-V1 | 0.200 | Search-result dependency versus order-ID handoff; shared “returned ID/retrieve” wording warrants review. |

Similarity is only a review priority. It does not by itself show that task mechanisms are duplicated or that a model can exploit a shortcut. The authoring protocol requires manual semantic/action-schema review before any family is declared sufficiently independent.

### Batch 01 verification and boundary

- New files: `CASE_AUTHORING_PROTOCOL_R1.md`, `authored_cases_r1.jsonl`, and `reference_actions_r1.jsonl`.
- Batch 01: 12 additional V1/standard cases, one per family. Each has one reference trajectory and one plausible near-miss fixture.
- Code/test commit: `d0b998116bb79277b8243d9cf9d23de171bdb93a`; CI [40887208453](https://github.com/yujian777555/openissue/actions/runs/40887208453) passed **36/36 tests**.
- F03 was revised to use a user-specified event ID and an exact ordered create/read-back trace, avoiding overlap with F06's returned-ID handoff. F07 now requires the exact candidate-list prefix. The F10 case keeps its reference entity only in task context, with a dedicated assertion.
- Current counts: 24 authored cases (12 pilot + 12 batch 01), 96 planned cases remain unauthored. Batch 01 is still pending independent review; the full 120-case semantic leakage audit, final hashes, live prompt-wrapper integration, and external adapter/scorer validation are not complete.
