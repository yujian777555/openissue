# Controlled-Suite Case Authoring Protocol R1

**Status:** Frozen for batch authoring; initial batch 01 is pending independent review.  
**Scope:** The 120 planned case IDs in `family_manifest_r1.json`, five deterministic tool domains, and whole-family train/validation/test splits.

## 1. Identity and split are immutable

- Treat `family_manifest_r1.json` as the source of truth for `case_id`, `family_id`, `split`, `domain_id`, `variant_id`, and `difficulty`. Do not invent IDs, move cases between splits, or change family assignments to improve results.
- The design has 12 families × 5 domains × 2 variants = 120 planned cases. Train contains families F01–F06, validation F07–F09, and test F10–F12. The split is by entire family, not by random case rows.
- V1 is standard difficulty. V2 is hard and must add a genuine decision/interaction complication, not merely longer wording, changed IDs, or larger numbers.
- Keep the 12 original pilot cases in `pilot_cases_r1.jsonl`. Add newly authored cases to `authored_cases_r1.jsonl` in bounded batches. Update only the matching manifest status to `authored_batch_NN_pending_review` until the batch has passed automated checks and independent review.

## 2. Mechanism validity

Each case must instantiate its named family mechanism in its selected domain:

- F01 — Read-before-write: inspect the relevant current object before a mutation; the trace must make the order observable.
- F02 — Sequential dependency: a downstream tool argument must depend on a prior tool result; use `required_arg_match` whenever the dependency is expressible.
- F03 — Postcondition verification: mutate state, then read back the changed object; the final-state oracle alone is insufficient.
- F04 — Numeric or threshold constraint: success or safe no-op depends on an explicit numeric threshold. State the threshold and make the initial state decisive.
- F05 — Idempotency and duplicate prevention: distinguish a true replay from a second mutation or a conflicting payload. Do not score only the final state when trace status is material.
- F06 — Cross-tool handoff: a producer tool's result is consumed by a distinct downstream tool; verify the handoff with `required_arg_match` when possible.
- F07 — Ambiguous entity / safe no-op: create at least two plausible targets and require preservation until ambiguity is resolved.
- F08 — Invalid precondition or policy conflict: make the invalid condition observable; the safe trajectory must not produce a prohibited mutation. If the case expects a tool error, distinguish schema-valid business errors from malformed arguments.
- F09 — Resource or availability conflict: make a concrete capacity, stock, interval, or occupancy conflict; no partial reservation or unintended substitute is allowed.
- F10 — Cross-turn reference resolution: the referenced entity must appear in `task.context`, not be leaked in `user_request`; the correct action must resolve the reference from the allowed context.
- F11 — Partial failure and compensation: one mutation succeeds, a later step fails, and a compensating action restores the specified business invariant. State clearly whether compensation is semantic rather than byte-for-byte rollback.
- F12 — Minimal side-effect plan: the requested change is narrow; the oracle checks the entire relevant state so unrelated writes/deletes/notifications are rejected.

A task that only mentions its family mechanism without making it necessary for success is not a valid family instance.

## 3. Task record and prompt boundary

- Validate every task against `task_case_schema_r1.json`. Use only the schema's allowed fields.
- Keep user-visible instruction in `task.user_request`; use `task.context` only for information legitimately available from prior conversation.
- Keep `initial_state`, `oracle`, `trace_constraints`, `provenance`, reference actions, and near-miss trajectories evaluator-side. Never put reference actions or expected results in the Agent-visible task payload.
- `agent_payload_r1.py` is the current allowlist contract (request + optional context only). It is not yet wired into a production Agent wrapper; prompt isolation must remain marked unverified until an integration test exercises the actual prompt serialization and tool profile.
- Cases must be independently authored. Do not copy external benchmark task text. Record provenance honestly; public release licensing is a separate decision.

## 4. Oracle and trace design

- Every case needs at least one deterministic reference trajectory that passes both state and trace checks.
- Every case needs at least one plausible near-miss trajectory that fails for the intended mechanism. Prefer a near-miss that would otherwise look superficially successful (wrong target, omitted readback, wrong argument handoff, duplicate mutation, partial order, or extra side effect).
- Reference and near-miss actions belong in `reference_actions_r1.jsonl`, separate from the case record. Each fixture contains `case_id`, `reference_actions`, and `near_miss_actions` only.
- Prefer exact state invariants for fixed state and partial `contains` invariants for implementation-generated IDs. Avoid overfitting to a chosen idempotency-key string or generated ID unless the task explicitly tests that behavior.
- Trace constraints must encode only necessary behavioral requirements. Do not force an arbitrary tool call if a safe, equivalent trajectory should be accepted. Conversely, if the mechanism is about order, replay, error handling, or handoff, state-only scoring is insufficient.
- Include unrelated state in fixtures when it helps detect side effects, but avoid huge fixtures that obscure the intended mechanism. Use JSON Pointer escaping correctly.

## 5. Batch gates

For every batch, automated checks must establish:

1. Unique IDs and exact agreement with the frozen manifest.
2. Schema conformance and valid domain/tool-profile assignment.
3. Reference trajectory passes the deterministic oracle and trace checker.
4. The near-miss trajectory is rejected.
5. The payload helper emits only allowed task fields.
6. Lexical similarity screening across all authored user requests/contexts, followed by manual mechanism-level review of the highest-overlap cross-family pairs.
7. CI passes, and all changed paths, commit SHA, and gate status are recorded.

A green test suite does not replace independent human review. Do not mark a batch final or close G1b merely because the reference/near-miss tests pass.

## 6. Research validity safeguards

- Do not tune task wording, split assignments, or oracles after observing Agent/evolution results without recording a versioned change and rerunning the full audit.
- Do not run formal Agent/evolution experiments, paid API calls, or expose held-out task content to controller development until G0/G1 approvals are explicitly satisfied.
- Record task counts separately as planned, authored, schema-valid, oracle-verified, independently reviewed, and frozen. Never report planned IDs as completed tasks.
