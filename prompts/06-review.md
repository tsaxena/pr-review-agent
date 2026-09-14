# Stage 6 — Review

Read:

* `IMPLEMENTATION_PLAN.md`
* `BUILD_SUMMARY.md`
* current implementation
* existing tests
* `AGENTS.md`

Do not reread `DESIGN.md`, `ARCHITECTURE.md`, `INTENT.md`, or `CHALLENGE.md`.

Treat `IMPLEMENTATION_PLAN.md` as the implementation contract and `BUILD_SUMMARY.md` as the record of what was built.

## Goal

Determine whether the P0 implementation is correct and sufficiently tested to proceed to system-level evaluation.

## Process

1. Apply the `implementation-review` skill.
2. Apply the `test-gap-analysis` skill.
3. Identify only blockers that must be resolved before evaluation.
4. Apply targeted fixes for approved blockers.
5. Rerun the relevant focused tests.
6. Repeat review only for the affected areas.
7. Produce `REVIEW.md`.

## Boundaries

Do not:

* redesign the system
* expand scope
* implement P1 functionality
* perform broad refactoring
* fix purely stylistic issues

If review reveals a problem requiring a design or architecture change, stop and return the issue to the appropriate earlier stage.

## Output

Create `REVIEW.md
