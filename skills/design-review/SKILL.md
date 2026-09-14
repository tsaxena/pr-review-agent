# Design Review

## Purpose

Validate that `DESIGN.md` is a faithful, complete, and implementable realization of the approved architecture.

Catch design problems before implementation planning begins.

## Inputs

* `ARCHITECTURE.md`
* draft `DESIGN.md`

## Review Method

### 1. Architecture Fidelity

Check that the design preserves:

* selected architecture
* control model
* LLM / deterministic boundary
* state model
* architectural invariants
* carried-forward constraints

Flag architecture drift.

Examples:

* single-agent architecture became multi-agent
* deterministic workflow became autonomous planning
* persistent memory was added without justification
* an LLM was given control over a deterministic safety gate

---

### 2. Requirement Coverage

Check whether the design provides a concrete mechanism for every important architectural requirement.

Identify missing paths or responsibilities.

---

### 3. Component Necessity

For every major component ask:

> What requirement or risk requires this component?

Flag:

* unnecessary abstractions
* speculative infrastructure
* redundant components
* unjustified agents
* premature scalability mechanisms

Prefer the simplest design that realizes the architecture.

---

### 4. Control Flow Completeness

Check whether the end-to-end path is clear.

Look for:

* missing transitions
* undefined branches
* unclear stopping conditions
* circular flows
* unbounded agent loops
* missing failure paths

---

### 5. Tool Contracts

Check important tools for:

* clear responsibility
* defined inputs
* defined outputs
* explicit failure behavior
* understood side effects

Flag tool interfaces that depend on vague natural-language contracts where structured contracts are needed.

---

### 6. State Consistency

Check that required state is explicit.

Look for:

* hidden dependence on conversation context
* state needed across steps but not represented
* duplicate sources of truth
* unnecessary persistent state
* unclear ownership of state

---

### 7. LLM / Deterministic Boundary

Check whether probabilistic reasoning is being used appropriately.

Flag cases where the LLM controls guarantees better handled deterministically, especially:

* permissions
* schema validation
* retries
* stopping conditions
* policy enforcement
* idempotency
* irreversible external actions
* success checks

Also flag unnecessary deterministic workflows for tasks that genuinely require semantic reasoning.

---

### 8. Reliability

Check for:

* bounded execution
* timeout behavior
* retry limits
* malformed model output
* tool failures
* repeated actions
* partial completion
* safe failure behavior

Only require mechanisms relevant to the system.

---

### 9. Testability

Check whether important behavior can be observed and evaluated.

The design should expose enough information to test:

* task success
* important state transitions
* tool usage
* deterministic gates
* failure behavior

---

### 10. Vertical Slice Feasibility

Verify that the proposed minimal vertical slice:

* exercises the real architecture
* works end to end
* covers the critical path
* is realistically implementable within the available time

Flag vertical slices that are either too large or too trivial to prove the architecture.

## Output

Return:

### Required Fixes

For each:

* issue
* why it matters
* smallest correction

### Architecture Drift

List any design decisions that change the approved architecture.

If none:

`None`

### Simplification Opportunities

Only meaningful complexity that can safely be removed.

### Human Decisions

Only issues requiring architecture-level judgment.

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
* introduce a different architecture
* expand scope
* start implementation
* rewrite the entire design for stylistic reasons

Prefer minimal corrections.
