# Stage 5 — Build

Read:

* `IMPLEMENTATION_PLAN.md`
* `AGENTS.md`

Do not reread earlier artifacts.

Treat `IMPLEMENTATION_PLAN.md` as the authoritative handoff from Stage 4.

## Goal

Implement the P0 vertical slice and verify that it runs end to end.

## Process

1. Apply the `implementation-execution` skill.
2. Implement P0 steps in the order defined by `IMPLEMENTATION_PLAN.md`.
3. After each meaningful step, run the smallest focused verification needed.
4. If a step fails, apply the `debugging-loop` skill.
5. Continue until the P0 vertical slice is implemented or a blocking upstream issue is discovered.
6. Run one focused end-to-end smoke test.
7. Create `BUILD_SUMMARY.md`.

## Verification Boundary

Stage 5 is not responsible for exhaustive correctness validation.

Do not spend significant time on:

* broad regression testing
* exhaustive edge cases
* adversarial testing
* deep test-gap analysis
* full system evaluation

Those belong to later stages.

If verification is slow, blocked, flaky, or incomplete:

* record what was verified
* record what remains unverified
* do not block creation of `BUILD_SUMMARY.md`

## Required Build Summary

Always create `BUILD_SUMMARY.md`, even if:

* tests fail
* external tools are unavailable
* verification is incomplete
* the implementation is not ready for review

Include:

* Implemented
* Verified
* Verification Incomplete
* Known Limitations
* P1 Not Implemented
* Deviations From Plan
* Ready for Review: YES | NO

## Boundaries

Do not:

* redesign the system
* expand scope
* begin P1 work without approval
* perform exhaustive verification
* silently change the approved plan

If implementation requires a design change, stop and surface it.

## Output

Produce:

* P0 implementation
* focused tests needed for smoke verification
* `BUILD_SUMMARY.md`

Stop after Stage 5.
