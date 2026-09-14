# Implementation Review

## Purpose

Determine whether the implementation faithfully executes the approved implementation plan and is ready for system-level evaluation.

Focus on correctness, architecture fidelity carried through the plan, reliability, and unnecessary complexity.

## Inputs

* `IMPLEMENTATION_PLAN.md`
* `BUILD_SUMMARY.md`
* current implementation
* existing tests

## Method

### 1. Verify P0 Completion

For each P0 requirement in the implementation plan classify:

* PASS
* PARTIAL
* FAIL
* NOT VERIFIED

Use evidence from the code, tests, or actual execution.

Do not infer completion merely because code exists.

---

### 2. Check Plan Fidelity

Look for deviations from the approved plan.

Identify:

* missing P0 functionality
* changed interfaces
* changed control flow
* skipped deterministic gates
* unexpected components
* unnecessary P1 implementation
* undocumented deviations

Not every deviation is wrong, but every meaningful deviation should be understood.

---

### 3. Check Correctness

Inspect critical paths for:

* incorrect assumptions
* logic errors
* invalid state transitions
* malformed output handling
* incorrect tool-result handling
* failures incorrectly treated as success
* unsafe side effects

Prioritize behavior over style.

---

### 4. Check Agent Boundaries

Where LLM reasoning is used, verify that it has not taken control over guarantees better enforced deterministically.

Pay particular attention to:

* stopping conditions
* validation
* permissions
* retries
* success checks
* idempotency
* irreversible actions

---

### 5. Check Reliability

Review relevant behavior for:

* bounded execution
* retry limits
* timeout handling
* tool failures
* malformed model output
* repeated actions
* partial failure
* safe termination

Only require mechanisms relevant to the approved plan.

---

### 6. Check State

Verify that important state is:

* explicit
* updated consistently
* owned by a clear component
* available when later steps require it

Look for hidden dependence on conversational context or accidental global state.

---

### 7. Check Tool Boundaries

For important tools verify:

* inputs are valid
* outputs are checked
* errors are propagated or handled
* side effects are understood
* retries are safe
* success is verified

---

### 8. Check Complexity

Identify complexity that does not contribute to P0 behavior.

Examples:

* unused abstractions
* dead code
* speculative extensibility
* duplicate logic
* unnecessary frameworks

Do not request cleanup purely for aesthetic reasons.

---

## Output

Return:

### P0 Status

For each P0 item:

`PASS | PARTIAL | FAIL | NOT VERIFIED`

### Blockers

Issues that must be fixed before evaluation.

For each include:

* issue
* evidence
* impact
* smallest fix

### Important Issues

Non-blocking issues worth addressing if time permits.

### Plan Deviations

List meaningful deviations from `IMPLEMENTATION_PLAN.md`.

If none:

`None`

### Simplification Opportunities

Only significant unnecessary complexity.

### Status

Return exactly one:

`READY FOR EVALUATION`

or

`FIX BLOCKERS FIRST`

## Guardrails

Do not:

* redesign the architecture
* broaden scope
* add new features
* perform large refactors for style
* treat every code-quality issue as a blocker

Prefer small targeted fixes.
