# Implementation Plan Review

## Purpose

Validate that `IMPLEMENTATION_PLAN.md` is a feasible, minimal execution plan for the approved `DESIGN.md`.

The goal is to catch scope creep, missing critical work, and poor implementation ordering before coding begins.

## Inputs

* `DESIGN.md`
* draft `IMPLEMENTATION_PLAN.md`

## Review Method

### 1. Design Fidelity

Check that the plan implements the approved design without changing:

* architecture
* component responsibilities
* control flow
* important interfaces
* deterministic boundaries
* design invariants

Flag design drift.

---

### 2. P0 Completeness

Check whether P0 includes everything required for the minimum end-to-end vertical slice.

Flag missing critical work.

---

### 3. Scope Control

Identify work in P0 that is not required to prove the design.

Look for:

* unnecessary abstractions
* premature infrastructure
* production hardening
* optional features
* speculative extensibility

Move such work to P1 or Out of Scope where appropriate.

---

### 4. Implementation Order

Check whether the sequence:

* respects dependencies
* produces runnable increments
* exposes failures early
* avoids building large disconnected pieces
* reaches end-to-end execution quickly

---

### 5. Verification Quality

Check that meaningful implementation steps have concrete verification.

Flag steps whose success cannot be observed.

---

### 6. Feasibility

Assess whether P0 is realistic within the stated implementation constraints.

For interview mode, optimize for approximately 45 minutes unless another constraint is specified.

Flag plans that are obviously too large.

---

### 7. Definition of Done

Check that completion criteria are concrete and tied to the vertical slice.

## Output

Return:

### Required Fixes

For each:

* issue
* why it matters
* smallest correction

### Scope Reductions

List unnecessary P0 work that should be deferred.

### Design Drift

List any departure from `DESIGN.md`.

If none:

`None`

### Human Decisions

Only decisions requiring meaningful scope or design judgment.

If none:

`None`

### Status

Return exactly one:

`APPROVED`

or

`NEEDS REVISION`

## Guardrails

Do not:

* redesign the system
* introduce new features
* write code
* optimize for production completeness
* rewrite the plan merely for style

Prefer the smallest plan that demonstrates the approved design.
