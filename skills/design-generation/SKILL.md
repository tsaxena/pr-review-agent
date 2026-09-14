# Design Generation

## Purpose

Turn an approved `ARCHITECTURE.md` into a concise, implementation-ready system design.

The design should explain exactly how the selected architecture will work without changing the architecture itself.

## Input

* `ARCHITECTURE.md`

Treat the approved architecture, invariants, and carried-forward constraints as authoritative.

## Method

### 1. Restate the Design Thesis

Summarize the selected architecture and the core implementation idea in 2–4 sentences.

Do not reconsider the architecture.

---

### 2. Define Major Components

Identify the minimum components required to implement the architecture.

For each component specify:

* responsibility
* inputs
* outputs
* important boundaries

Every component must solve a concrete requirement.

Avoid speculative components.

---

### 3. Define End-to-End Control Flow

Describe what happens from initial input to final output.

Show:

* major reasoning steps
* tool interactions
* deterministic gates
* state transitions
* stopping conditions
* external side effects

Use a simple diagram when useful.

---

### 4. Define Agent Responsibilities

If the architecture contains an agent or LLM, explicitly define what it may decide.

Examples:

* interpret input
* generate hypotheses
* select tools
* decide what information to inspect next
* synthesize findings

Also define what the LLM must NOT control.

Do not delegate deterministic guarantees to the model.

---

### 5. Define Tools

For every important tool specify:

* purpose
* input
* output
* side effects
* important failure modes

Keep contracts implementation-ready but avoid unnecessary framework-specific details.

Tools should expose clear success and failure results.

---

### 6. Define State

Specify the minimum state needed by the workflow.

Include:

* information that must survive across steps
* agent progress
* important observations
* outputs or artifacts produced
* retry or failure information when relevant

Keep state explicit.

Do not introduce persistent storage unless required by the architecture.

---

### 7. Separate LLM and Deterministic Logic

Create an explicit boundary.

#### LLM / Agent

Use for semantic judgment and reasoning.

#### Deterministic System

Use for guarantees such as:

* validation
* permissions
* state transitions
* schemas
* retries
* stopping conditions
* idempotency
* irreversible actions
* success / failure checks

Preserve the boundary established in `ARCHITECTURE.md`.

---

### 8. Design Failure Handling

Cover important failures only.

Consider:

* tool failure
* timeout
* malformed LLM output
* invalid tool arguments
* repeated actions
* retry exhaustion
* partial completion
* inability to make progress

Define safe stopping behavior.

Every agent loop must be bounded.

---

### 9. Define Safety Boundaries

Identify:

* untrusted inputs
* high-impact actions
* permissions
* external side effects

Use deterministic gates where appropriate.

---

### 10. Define Observability

Specify the minimum information needed to understand a run.

Examples:

* major agent decisions
* tool calls
* tool results
* errors
* retries
* final status

Avoid designing a full production observability platform for an interview prototype.

---

### 11. Define Evaluation Hooks

Make the system testable.

Identify what can be measured or asserted for:

* task success
* correctness
* important intermediate behavior
* tool use
* failure handling
* acceptance criteria inherited from the architecture

Do not build the full evaluation plan yet.

---

### 12. Define the Minimal Vertical Slice

Identify the smallest end-to-end implementation that demonstrates the architecture.

It should include:

* real input
* core reasoning
* essential tools
* critical deterministic gates
* final output

Defer everything else.

## Guardrails

Do not:

* change the selected architecture
* introduce additional agents without approval
* introduce planners, memory, databases, queues, or frameworks without architectural justification
* choose technology merely because it is familiar
* design speculative production infrastructure
* start implementation
* define file-by-file implementation order

If the approved architecture contains a blocking flaw, surface it for human review instead of silently fixing it.

## Output

Produce `DESIGN.md` containi
