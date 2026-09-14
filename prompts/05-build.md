# Stage 5 — Build

Read:

* `IMPLEMENTATION_PLAN.md`
* `AGENTS.md`

Do not reread `DESIGN.md`, `ARCHITECTURE.md`, `INTENT.md`, or `CHALLENGE.md`.

Treat the approved `IMPLEMENTATION_PLAN.md` as the authoritative handoff from Stage 4.

## Goal

Implement and verify the P0 vertical slice.

## Process

1. Apply the `implementation-execution` skill.
2. Execute P0 steps in the order defined by `IMPLEMENTATION_PLAN.md`.
3. After each meaningful step, run the defined verification.
4. If a step fails, apply the `debugging-loop` skill.
5. Continue until the P0 end-to-end path works or a blocking upstream issue is discovered.
6. Run the complete P0 vertical slice once more.
7. Create `BUILD_SUMMARY.md`.

## Boundaries

If implementation requires changing the approved plan or design:

* stop
* explain the conflict
* return the decision to the appropriate earlier stage

Do not silently redesign.

Do not begin P1 work unless explicitly approved.

## Output

Produce:

* working P0 implementation
* relevant tests
* `BUILD_SUMMARY.md`

Do not perform the formal implementation review yet.

Stop after Stage 5.
