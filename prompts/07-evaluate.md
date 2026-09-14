# Stage 7 — Evaluate

Read:

* `REVIEW.md`
* current implementation
* `AGENTS.md`

Proceed only if `REVIEW.md` says:

`READY FOR EVALUATION`

## Goal

Determine whether the completed agentic system actually performs its intended task successfully and identify its most important failure modes.

## Process

1. Apply the `agent-evaluation` skill.
2. Define evaluation targets.
3. Create a small set of meaningful evaluation cases.
4. Define expected behavior before executing each case.
5. Run the system on the evaluation cases.
6. Capture relevant final outputs and trajectory behavior.
7. Score each case.
8. Analyze failed and partial cases.
9. Prioritize improvements.
10. Produce `EVAL_RESULTS.md`.

## Boundaries

Do not modify the implementation during evaluation.

Do not redefine success criteria after observing results.

If evaluation exposes failures, record them rather than fixing them inside this stage.

Fixes should begin a new iteration of the SDLC at the appropriate earlier stage.

## Output

`EVAL_RESULTS.md`

End with:

* overall result
* top failure modes
* highest-value next improvement

Stop after Stage 7.
