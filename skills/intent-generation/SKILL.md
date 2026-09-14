# Intent Generation

## Purpose

Convert an ambiguous engineering challenge into a concise, architecture-neutral problem specification.

The output should be sufficient for architecture work without requiring downstream stages to reread the original challenge.

## Inputs

* Original challenge or problem statement

## Method

Extract and organize:

1. Goal
2. Functional requirements
3. Non-functional requirements
4. Constraints
5. Assumptions
6. Acceptance criteria
7. Important ambiguities

## Guidance

### Goal

State the primary outcome the system must achieve.

Keep this to 1–2 sentences.

### Functional Requirements

Capture externally observable capabilities the system must provide.

Prefer statements of the form:

* The system must...
* The system should be able to...

Do not describe implementation.

### Non-Functional Requirements

Capture requirements such as:

* correctness
* reliability
* safety
* latency
* cost
* scalability
* auditability

Include only those that are stated or reasonably implied by the challenge.

### Constraints

Capture fixed boundaries such as:

* available time
* available tools
* required platforms or APIs
* provided repositories or datasets
* implementation environment
* explicit technology restrictions

### Assumptions

When the challenge is underspecified, make reasonable assumptions so work can continue.

For each assumption:

* state it explicitly
* keep it minimal
* avoid assumptions that unnecessarily constrain architecture

### Acceptance Criteria

Translate the challenge into observable conditions that determine whether the solution works.

Acceptance criteria should be:

* concrete
* testable
* architecture-independent

### Ambiguities

Identify unresolved questions only when they could materially affect:

* system scope
* architecture
* safety
* evaluation
* implementation feasibility

Do not list low-value questions that can be handled with a reasonable assumption.

## Guardrails

Do not:

* propose an architecture
* choose between ReAct, workflows, planners, or multi-agent systems
* select frameworks
* select models
* design tools
* define detailed components
* start implementation
* invent requirements without clearly labeling them as assumptions

Do not encode a preferred solution into the intent.

## Quality Check

Before finalizing, verify:

* Every important challenge requirement is represented.
* Assumptions are clearly separated from stated requirements.
* Acceptance criteria can be tested.
* No architecture decisions have leaked into the document.
* The document is concise enough for rapid human review.
* A downstream architecture stage could work from this artifact without rereading the original challenge.

## Output

Produce `INTENT.md` with:

# Intent

## Goal

## Functional Requirements

## Non-Functional Requirements

## Constraints

## Assumptions

## Acceptance Criteria

## Ambiguities

Target length: approximately one page.
