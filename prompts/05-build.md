# Stage 5 — Build

Read:

* `CHALLENGE.md`
* `INTENT.md`
* `DESIGN.md`
* `IMPLEMENTATION_PLAN.md`
* `AGENTS.md`

Your goal is to implement the approved P0 vertical slice.

## Rules

* Treat `INTENT.md`, `DESIGN.md`, and `IMPLEMENTATION_PLAN.md` as contracts.
* Do not redesign the architecture.
* Do not add unnecessary abstractions or infrastructure.
* Implement P0 before P1.
* Prefer small, working increments over large code generation.
* Run and validate the system incrementally.
* Fix blocking issues before adding features.
* Keep the implementation easy to explain in an interview.
* If the design appears fundamentally broken, stop and flag the issue rather than silently changing it.

## Build Loop

Repeat:

1. Select the next P0 item from `IMPLEMENTATION_PLAN.md`.
2. Implement the smallest change needed.
3. Run the relevant code or test.
4. Inspect the actual result.
5. Fix failures.
6. Confirm the step works before moving on.

Do not implement multiple major components without testing between them.

## Implementation Priorities

Prioritize:

1. End-to-end execution
2. Correct tool interfaces
3. Explicit state
4. Deterministic safety and validation gates
5. Error handling for critical paths
6. Basic observability
7. Tests for core behavior

Avoid polishing non-critical code before the vertical slice works.

## LLM-Generated Code

Do not assume generated code is correct.

After each meaningful implementation step, check:

* Does it match `DESIGN.md`?
* Does it satisfy the intended interface?
* Does it introduce hidden assumptions?
* Is the error path handled?
* Can the result be verified?

## Scope Control

If time becomes constrained:

* complete P0
* defer P1
* document remaining limitations
* do not broaden scope

## Output

Produce working code for the P0 vertical slice.

Update tests as needed.

When the vertical slice works, summarize:

* what was implemented
* what was tested
* what remains incomplete
* any known limitations

Stop after the implementation is working well enough to enter Stage 6 — Review.
