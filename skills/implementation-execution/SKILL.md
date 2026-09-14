# Implementation Execution

## Purpose

Implement an approved `IMPLEMENTATION_PLAN.md` as a working end-to-end system while preserving the approved design.

The goal is to execute the plan incrementally, verify progress continuously, and reach a working P0 vertical slice before adding optional functionality.

## Input

* `IMPLEMENTATION_PLAN.md`

Treat the plan as the authoritative implementation contract.

Do not reinterpret the original challenge or redesign the system.

## Method

### 1. Start With P0

Implement only P0 work until the end-to-end vertical slice works.

Do not begin P1 work early.

---

### 2. Work Incrementally

For each implementation step:

1. Read the step objective.
2. Make the smallest code change required.
3. Run the verification defined in the plan.
4. Inspect the actual result.
5. Fix blocking failures.
6. Confirm the step works before continuing.

Avoid implementing several major components before running anything.

---

### 3. Preserve Design Contracts

Respect:

* component responsibilities
* interfaces
* state ownership
* control flow
* LLM / deterministic boundaries
* safety gates
* stopping conditions

If implementation requires changing one of these, stop and surface the conflict.

Do not silently redesign.

---

### 4. Keep Interfaces Explicit

Prefer:

* structured inputs
* structured outputs
* clear error results
* explicit state transitions

Avoid relying on hidden conversational state when program state is required.

---

### 5. Validate External Actions

For side-effecting tools:

* inspect results
* verify success
* handle errors
* avoid duplicate execution when retries occur

Do not assume a tool call succeeded merely because it returned.

---

### 6. Keep the Code Simple

For interview-oriented implementations:

Prefer:

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

### 7. Test Critical Paths Early

At minimum validate:

* normal end-to-end path
* critical deterministic gates
* important tool failure behavior
* termination behavior

Do not wait until the entire implementation is complete before testing.

---

### 8. Stop at P0

Once the P0 vertical slice works:

* rerun the end-to-end path
* record known limitations
* identify incomplete P1 work

Do not automatically continue adding features.

## Guardrails

Do not:

* modify the architecture without approval
* modify the design silently
* expand scope
* implement P1 before P0 works
* accept generated code without running it
* hide failing tests
* replace broken behavior with hard-coded demo outputs

If upstream artifacts are inconsistent with implementation reality, surface the problem rather than silently working around it.

## Completion Criteria

Build is complete when:

* the P0 vertical slice runs end to end
* critical deterministic checks work
* expected outputs are produced
* blocking runtime failures are resolved
* known limitations are documented

## Output

Produce:

* working implementation
* relevant tests
* `BUILD_SUMMARY.md`

`BUILD_SUMMARY.md` should contain:

# Build Summary

## Implemented

## Verified

## Known Limitations

## P1 Not Implemented

## Deviations From Plan

If there were no deviations:

`None`

## Ready for Review

`YES` or `NO`
