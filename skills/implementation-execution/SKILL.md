# Implementation Execution

## Purpose

Implement an approved `IMPLEMENTATION_PLAN.md` as a working P0 vertical slice.

The goal is to make steady progress, verify the critical path, and hand off quickly to Review rather than exhaustively proving correctness during Build.

## Input

* `IMPLEMENTATION_PLAN.md`

Treat the plan as the authoritative implementation contract.

Do not reinterpret the original challenge or redesign the system.

## Method

### 1. Start With P0

Implement only P0 work until the vertical slice exists.

Do not begin P1 work early.

---

### 2. Work Incrementally

For each implementation step:

1. Read the step objective.
2. Make the smallest code change required.
3. Run the smallest useful verification.
4. Inspect the actual result.
5. Fix blocking failures.
6. Continue once the step is sufficiently demonstrated.

Avoid implementing several major components before running anything.

---

### 3. Preserve Design Contracts

Respect the approved:

* interfaces
* control flow
* state ownership
* component responsibilities
* deterministic gates
* stopping conditions

If implementation requires changing these, stop and surface the conflict.

Do not silently redesign.

---

### 4. Keep Interfaces Explicit

Prefer:

* structured inputs
* structured outputs
* explicit errors
* explicit state transitions

Avoid hidden dependence on conversational context when program state is required.

---

### 5. Validate External Actions Minimally but Safely

For side-effecting tools:

* inspect the returned result
* detect obvious failure
* avoid duplicate execution during retries
* verify critical preconditions before acting

Do not attempt exhaustive side-effect validation during Build.

Deeper correctness checks belong in Review.

---

### 6. Keep the Code Simple

For interview-oriented implementations prefer:

* small modules
* explicit control flow
* minimal dependencies
* readable code
* direct abstractions

Avoid:

* unnecessary frameworks
* speculative extensibility
* premature scalability infrastructure
* complex inheritance
* abstractions used only once

The implementation should be easy to explain.

---

### 7. Use Smoke Verification

During Build, verify enough to establish that the P0 path executes.

Prioritize:

* one happy-path end-to-end run
* critical deterministic gates
* obvious runtime failures
* basic termination behavior

Do not spend significant time on:

* broad regression testing
* exhaustive edge cases
* adversarial testing
* full failure injection
* comprehensive coverage

Those belong to later stages.

---

### 8. Handle Slow or Blocked Verification

If verification is:

* slow
* flaky
* blocked by authentication
* blocked by an external dependency
* expensive
* incomplete

do not stall indefinitely.

Record:

* what was verified
* what remains unverified
* why verification stopped

Then hand off to Review.

---

### 9. Stop at P0

Once the vertical slice is implemented and smoke-tested:

* stop adding features
* record known limitations
* record P1 work not completed
* create `BUILD_SUMMARY.md`

Do not continue polishing automatically.

## Guardrails

Do not:

* modify the architecture without approval
* modify the design silently
* expand scope
* implement P1 before P0 works
* accept generated code without running any verification
* hide failures
* replace broken behavior with hard-coded demo outputs
* let exhaustive verification consume the majority of Build time

If upstream artifacts conflict with implementation reality, surface the issue rather than working around it silently.

## Completion Criteria

Build is complete when:

* the P0 implementation exists
* the main execution path can be exercised
* at least one focused smoke verification has been attempted
* blocking runtime issues are either fixed or documented
* known limitations are recorded

Build does **not** require exhaustive correctness proof.

## Output

Produce:

* P0 implementation
* only the focused tests needed for smoke verification
* `BUILD_SUMMARY.md`

`BUILD_SUMMARY.md` must be created even if verification is incomplete.

It should contain:

# Build Summary

## Implemented

## Verified

## Verification Incomplete

## Known Limitations

## P1 Not Implemented

## Deviations From Plan

If none:

`None`

## Ready for Review

`YES` or `NO`
