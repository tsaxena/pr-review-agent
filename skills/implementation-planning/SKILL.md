# Implementation Planning

## Purpose

Turn an approved `DESIGN.md` into a small, ordered implementation plan that delivers a working end-to-end vertical slice quickly.

The plan should specify what to build and in what order without changing the approved design.

## Input

* `DESIGN.md`

Treat the design, interfaces, invariants, and vertical slice as authoritative.

## Method

### 1. Identify the End-to-End Path

Identify the minimum path from real input to real output that proves the design works.

Include only the components required for that path.

---

### 2. Define Priorities

Split work into:

#### P0 — Required

Everything necessary for a working end-to-end system.

#### P1 — If Time Allows

Useful improvements that are not necessary to prove the architecture.

#### Out of Scope

Explicitly defer unnecessary functionality.

Optimize P0 for the available implementation time.

---

### 3. Define Implementation Steps

Break P0 into small ordered steps.

For each step specify:

* objective
* files or modules affected
* important interface being implemented
* expected behavior after the step
* how to verify that it works

Prefer steps that leave the repository in a runnable state.

---

### 4. Define Dependencies

Identify dependencies between implementation steps.

Prefer an order that minimizes blocking dependencies and produces useful feedback early.

---

### 5. Plan Incremental Verification

After each meaningful step define a concrete verification action.

Examples:

* run a function
* run a CLI command
* execute a focused test
* inspect structured output
* exercise one tool call
* run the vertical slice

Do not postpone all testing until the end.

---

### 6. Identify Implementation Risks

Identify only risks likely to block implementation.

Examples:

* authentication
* external APIs
* unclear tool behavior
* model output parsing
* environment setup
* state handling
* side-effecting operations

For each risk provide the simplest mitigation or fallback.

---

### 7. Define Done

Define exactly what must work before Stage 5 can be considered complete.

Tie this to the minimal vertical slice and design invariants.

## Guardrails

Do not:

* change the architecture
* redesign components
* add features not present in `DESIGN.md`
* introduce speculative infrastructure
* optimize prematurely
* turn P1 work into P0 without justification
* write implementation code

Prefer:

* thin vertical slices
* simple interfaces
* incremental verification
* working end-to-end behavior over completeness

## Output

Produce `IMPLEMENTATION_PLAN.md` containing:

# Implementation Plan

## Vertical Slice

## P0 — Required

## P1 — If Time Allows

## Out of Scope

## Implementation Steps

For each step:

* Goal
* Files / modules
* Key interface
* Verification

## Risks and Mitigations

## Definition of Done
