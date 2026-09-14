# Stage 2 — Architecture

Read:

* `CHALLENGE.md`
* `INTENT.md`
* `AGENTS.md`

Your goal is to identify the simplest architecture that satisfies the requirements.

## Step 1 — Characterize the Problem

Briefly assess:

* How predictable is the workflow?
* Is the task mostly deterministic or open-ended?
* Is dynamic replanning required?
* Are there independent tasks that benefit from parallel execution?
* Is persistent or shared state required?
* How many tools or external systems are involved?
* Are any actions irreversible or high-risk?
* What kinds of failures must the system recover from?
* What is the expected latency / cost sensitivity?
* What can realistically be implemented in the available interview time?

## Step 2 — Generate Architecture Options

Propose 2–3 realistic architecture options.

Consider patterns such as:

* deterministic workflow
* single ReAct agent
* planner / executor
* planner with replanning
* router + specialist agents
* supervisor / multi-agent
* hybrid deterministic + agentic system

Only include patterns that are genuinely relevant to this problem.

For each option describe:

* high-level control flow
* where LLM reasoning is used
* where deterministic logic is used
* state requirements
* strengths
* weaknesses
* likely failure modes
* implementation complexity
* suitability for a 45-minute prototype

## Step 3 — Compare

Compare the options against the requirements and acceptance criteria in `INTENT.md`.

Prefer the simplest architecture that satisfies the requirements.

Do not introduce additional agents, planners, memory systems, frameworks, or infrastructure unless they solve a concrete requirement.

## Step 4 — Recommend

Recommend one architecture and explain why.

Also state:

* why the simpler alternative is insufficient, if applicable
* why the more complex alternative is unnecessary, if applicable
* the biggest risk in the recommended design

## Human Decision Gate

Do NOT make the final architecture decision on behalf of the user.

End with:

### Recommended Architecture

<recommendation>

### Decision Required

Architecture selection must be explicitly approved by the user before proceeding to detailed design.

Do not create `DESIGN.md`.
Do not start implementation.
Do not proceed to Stage 3.
