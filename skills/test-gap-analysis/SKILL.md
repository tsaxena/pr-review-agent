# Test Gap Analysis

## Purpose

Determine whether the existing tests provide enough confidence to move from implementation review to system-level evaluation.

Focus on critical behavior rather than maximizing test count.

## Inputs

* `IMPLEMENTATION_PLAN.md`
* current implementation
* existing tests

## Method

### 1. Identify Critical Behaviors

Extract the behaviors that must work for P0.

Prioritize:

* end-to-end happy path
* critical deterministic gates
* tool failures
* stopping conditions
* state transitions
* externally visible side effects

---

### 2. Map Existing Tests

For each critical behavior classify coverage as:

* COVERED
* PARTIALLY COVERED
* NOT COVERED

---

### 3. Identify High-Value Gaps

Prioritize missing tests that could reveal:

* incorrect success conditions
* unhandled tool failure
* malformed model output
* repeated execution
* unsafe side effects
* infinite or excessive loops
* invalid state

Do not generate exhaustive edge-case lists.

---

### 4. Recommend Minimal Tests

For every important gap specify:

* scenario
* expected behavior
* why the test matters

Prefer a few high-value tests over broad coverage.

## Output

### Coverage Summary

### Critical Gaps

### Recommended Tests

### Readiness

Return:

`SUFFICIENT FOR EVALUATION`

or

`TEST GAPS MUST BE FIXED`

## Guardrails

Do not:

* optimize for coverage percentage
* generate tests for trivial getters or plumbing
* require production-scale test infrastructure
* expand beyond the approved P0 behavior
