# Stage 6 — Review

Read:

* `CHALLENGE.md`
* `INTENT.md`
* `DESIGN.md`
* `IMPLEMENTATION_PLAN.md`
* `AGENTS.md`
* the current implementation
* existing tests

Your goal is to determine whether the implementation actually satisfies the intended system design and acceptance criteria.

## Rules

* Review the implementation critically.
* Do not assume generated code is correct because it runs.
* Compare implementation against upstream artifacts.
* Prefer targeted fixes over broad rewrites.
* Distinguish correctness issues from style preferences.
* Do not redesign the system unless there is a fundamental architectural flaw.
* Do not expand scope beyond the challenge.

## Step 1 — Check Requirements

Verify each important acceptance criterion from `INTENT.md`.

For each criterion classify it as:

* PASS
* PARTIAL
* FAIL
* NOT TESTED

Provide evidence from the implementation or tests.

## Step 2 — Check Architecture Fidelity

Compare the code against `DESIGN.md`.

Look for:

* architecture drift
* missing components
* incorrect control flow
* implicit state that should be explicit
* LLM decisions that should be deterministic
* deterministic logic incorrectly delegated to the LLM
* tool contracts that differ from the design

## Step 3 — Check Implementation Quality

Review for:

* incorrect assumptions
* brittle logic
* missing error handling
* unsafe side effects
* malformed LLM output handling
* unbounded loops or retries
* missing stopping conditions
* idempotency issues
* duplicate actions
* dead code
* unnecessary complexity
* hidden dependencies

## Step 4 — Check Tool Boundaries

For important tools verify:

* inputs are validated
* outputs are checked
* failures are handled
* side effects are understood
* retries are safe
* success is not assumed without verification

## Step 5 — Check Tests

Determine whether tests cover the critical P0 behavior.

Identify missing tests for:

* happy path
* failure path
* edge cases
* repeated execution
* critical deterministic gates

Do not generate a large test suite yet.

## Step 6 — Prioritize Findings

Group findings into:

### Blockers

Must be fixed before evaluation.

### Important

Should be fixed if time allows.

### Nice to Have

Non-critical improvements.

For each finding include:

* issue
* evidence
* why it matters
* smallest recommended fix

## Step 7 — Readiness Decision

End with one of:

* READY FOR EVALUATION
* FIX BLOCKERS FIRST

Explain the decision briefly.

## Output

Create `REVIEW.md`.

If blockers exist, fix only the blockers and rerun the relevant tests before declaring readiness.

Do not proceed to broader evaluation until blockers are resolved.
