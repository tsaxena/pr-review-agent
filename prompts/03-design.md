# Stage 3 — Design

Read:

* `CHALLENGE.md`
* `INTENT.md`
* `AGENTS.md`
* the explicitly approved architecture decision

Your goal is to turn the approved architecture into a concise, implementation-ready `DESIGN.md`.

## Rules

* Preserve the architecture selected by the user.
* Do not silently replace it with a different architecture.
* If you identify a serious flaw, flag it clearly before proceeding.
* Do not start implementation.
* Avoid speculative future functionality.
* Optimize for a working interview prototype, not production completeness.
* Keep the design concise.

## DESIGN.md Structure

### 1. Design Thesis

Summarize the core architecture in 2–4 sentences.

### 2. High-Level Architecture

Describe the major components and how they interact.

Include a simple text diagram if useful.

### 3. Control Flow

Describe the end-to-end execution path.

### 4. Components and Responsibilities

For each major component define:

* responsibility
* inputs
* outputs

### 5. Agent Responsibilities

Define what decisions the agent/LLM is allowed to make.

Be explicit about what it must not control.

### 6. Tools

For each important tool define:

* purpose
* input
* output
* side effects
* important failure modes

### 7. State

Define the minimum state required by the workflow.

Explain where state lives and what must survive across steps.

### 8. LLM vs Deterministic Logic

Explicitly separate:

* reasoning delegated to the LLM
* guarantees enforced by deterministic code

### 9. Failure Handling

Cover only important failures such as:

* tool errors
* malformed outputs
* retries
* repeated actions
* timeout / max-step behavior
* partial failure

### 10. Safety / Guardrails

Identify any high-impact actions and how they are controlled.

### 11. Observability

Define the minimum logs or traces required to understand what the system did.

### 12. Evaluation

Define how success will be measured against the acceptance criteria in `INTENT.md`.

### 13. Minimal Vertical Slice

Describe the smallest end-to-end implementation that proves the architecture works.

## Output

Create `DESIGN.md`.

Target length:

* concise enough to review in a few minutes
* approximately 150–200 lines maximum

Stop after producing `DESIGN.md`.

Do not create an implementation plan yet.
Do not write code.
