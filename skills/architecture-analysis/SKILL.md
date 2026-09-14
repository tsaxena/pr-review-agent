# Architecture Analysis

## Purpose

Analyze an approved `INTENT.md` and identify the simplest system architecture that can satisfy the requirements.

This skill helps compare architectural patterns without prematurely designing implementation details.

## Input

* `INTENT.md`

Treat `INTENT.md` as the authoritative problem contract.

Do not reread or reinterpret the original challenge unless explicitly asked.

## Method

### 1. Characterize the Problem

Identify the characteristics that materially affect architecture:

* How predictable is the workflow?
* How much open-ended reasoning is required?
* Can the task be expressed as a fixed sequence of steps?
* Is dynamic replanning required?
* Are there independent tasks that could run in parallel?
* Is specialization across different reasoning tasks useful?
* How many external tools or systems are involved?
* Is long-lived or shared state required?
* Are any actions irreversible, expensive, or high-risk?
* What failures must the system recover from?
* What latency or cost constraints matter?
* What implementation constraints matter, including interview time?

Do not infer complexity unless required by the intent.

---

## 2. Determine the Required Level of Agency

First ask whether an agent is necessary at all.

Consider the spectrum:

### Deterministic Workflow

Prefer when:

* steps are known in advance
* branching is limited
* tool sequence is predictable
* correctness and reproducibility matter more than flexibility

### Single ReAct Agent

Consider when:

* the next action depends on observations
* investigation is open-ended
* tool selection must happen dynamically
* lightweight replanning is sufficient

### Planner / Executor

Consider when:

* the task benefits from an explicit multi-step plan
* steps have dependencies
* progress needs to be tracked
* execution is relatively structured after planning

### Planner with Replanning

Consider when:

* initial plans are likely to become invalid
* observations materially change the investigation path
* long-horizon work requires adaptation

### Router + Specialists

Consider when:

* requests fall into distinct categories
* different tasks require meaningfully different tools or expertise
* a lightweight routing decision can isolate workflows

### Multi-Agent / Supervisor

Consider only when:

* tasks are meaningfully separable
* specialization improves quality
* independent work can run in parallel
* different context windows or tool permissions are useful
* coordination overhead is justified

### Hybrid

Consider when:

* some reasoning must remain flexible
* critical control, validation, or side effects should remain deterministic

Do not assume that greater agency means better architecture.

---

## 3. Generate Plausible Options

Generate 2–3 architecture options only when there are genuinely meaningful alternatives.

For each option describe:

* high-level control flow
* where LLM reasoning occurs
* where deterministic logic occurs
* state requirements
* strengths
* weaknesses
* major failure modes
* implementation complexity
* suitability for the constraints

Do not generate options only for the sake of having three choices.

---

## 4. Compare the Options

Compare architectures against the actual intent.

Evaluate dimensions such as:

* requirement coverage
* simplicity
* flexibility
* failure recovery
* observability
* deterministic guarantees
* latency
* cost
* testability
* implementation effort
* ability to complete a working vertical slice

Prefer the least complex architecture that satisfies the requirements.

---

## 5. Define the LLM / Deterministic Boundary

For each serious option identify:

### LLM Responsibilities

Use LLM reasoning where semantic judgment or ambiguity is central, such as:

* interpretation
* hypothesis generation
* investigation decisions
* semantic comparison
* synthesis

### Deterministic Responsibilities

Prefer deterministic software for:

* validation
* permissions
* policy enforcement
* schema checks
* state transitions
* retries
* stopping conditions
* idempotency
* irreversible actions
* success / failure checks

Do not rely on LLM judgment for guarantees that can be enforced deterministically.

---

## 6. Evaluate State Requirements

Determine whether the architecture requires:

* no persistent state
* per-run state
* resumable state
* shared state across workers or agents
* long-term memory

Prefer the minimum state model necessary.

Do not introduce databases, queues, vector stores, or memory systems without a concrete requirement.

---

## 7. Identify Architectural Invariants

Identify the small number of constraints downstream design must preserve.

Examples:

* execution must be bounded
* external side effects require validation
* tool failures must be observable
* repository or retrieved content is untrusted
* duplicate actions must be prevented
* human approval is required before a high-impact action

Keep these architectural, not implementation-specific.

---

## 8. Recommend an Architecture

Recommend the architecture that best satisfies the intent.

Explain:

* why it fits the problem
* why a simpler option is insufficient, if applicable
* why a more complex option is unnecessary
* the most important tradeoff being accepted
* the biggest architectural risk

The recommendation is advisory.

The human owns the final architecture decision.

---

## Guardrails

Do not:

* write code
* create implementation files
* define detailed classes
* define exact tool schemas
* choose specific frameworks unless the intent requires them
* introduce multi-agent architecture without justification
* use persistent memory without justification
* redesign requirements
* silently make the final architecture decision for the user

Avoid architecture by buzzword.

Every architectural component must solve a requirement or mitigate a concrete risk.

---

## Output

Produce architecture analysis containing:

### Problem Characteristics

### Options Considered

### Comparison

### Recommended Architecture

### Why This Option

### LLM vs Deterministic Boundary

### State Requirements

### Key Architectural Invariants

### Major Risks

### Decision Required

End with:

`FINAL ARCHITECTURE REQUIRES HUMAN APPROVAL`
