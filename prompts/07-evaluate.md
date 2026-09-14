# Stage 7 — Evaluate

Read:

* `CHALLENGE.md`
* `INTENT.md`
* `DESIGN.md`
* `IMPLEMENTATION_PLAN.md`
* `REVIEW.md`
* `AGENTS.md`
* the current implementation
* existing tests

Your goal is to evaluate the agent as a complete system against the original challenge.

## Rules

* Evaluate behavior, not just whether the code runs.
* Tie every evaluation back to the acceptance criteria in `INTENT.md`.
* Prefer deterministic checks where possible.
* Use semantic or LLM-based judgment only when necessary.
* Do not change the architecture during evaluation.
* Do not hide failures; record them clearly.

## Step 1 — Define Evaluation Cases

Create a small but meaningful set of cases covering:

1. Happy path
2. Ambiguous input
3. Invalid or malformed input
4. Tool failure
5. Partial failure / retry
6. Repeated execution
7. Adversarial or misleading input
8. Hidden-test-style edge case

Only include cases relevant to this system.

## Step 2 — Define Expected Behavior

For each case specify:

* input
* expected agent behavior
* expected tool usage
* expected stopping condition
* expected final result
* failure conditions

## Step 3 — Run the Evaluation

Execute the system on each case.

Capture:

* final output
* important intermediate decisions
* tool calls
* retries
* failures
* latency if useful
* approximate model/tool cost if useful

## Step 4 — Score Results

For each case classify:

* PASS
* PARTIAL
* FAIL

Also evaluate relevant system-level metrics such as:

* task success
* correctness
* false positives
* false negatives
* grounding / evidence quality
* unnecessary tool calls
* trajectory length
* recovery from failure
* duplicate actions
* latency
* cost

Use only metrics that matter for the challenge.

## Step 5 — Analyze Failures

For each failed or partial case identify:

* what failed
* likely root cause
* whether the issue is in:

  * requirements
  * architecture
  * design
  * implementation
  * prompting
  * tool behavior
  * evaluation setup

Do not immediately redesign the system.

## Step 6 — Recommend Next Improvements

Prioritize improvements by impact:

### P0

Required to satisfy the original challenge.

### P1

High-value reliability or quality improvement.

### P2

Nice-to-have or production hardening.

## Output

Create `EVAL_RESULTS.md`.

End with:

### Overall Result

* PASS
* PARTIAL
* FAIL

### Top Failure Modes

List the most important observed failures.

### Highest-Value Next Step

Recommend the single most valuable improvement.

Stop after producing the evaluation report.
