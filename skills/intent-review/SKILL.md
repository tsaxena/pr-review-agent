# Intent Review

## Purpose

Validate that `INTENT.md` is a faithful, complete, architecture-neutral handoff from the original challenge.

The goal is to catch problems before architecture work begins.

## Inputs

* `CHALLENGE.md`
* draft `INTENT.md`

## Review Method

Check the draft for:

### 1. Missing Requirements

Identify important requirements from the challenge that are absent from `INTENT.md`.

Only flag omissions that could affect:

* scope
* architecture
* implementation
* evaluation

### 2. Unsupported Assumptions

Identify assumptions that:

* are not supported by the challenge
* unnecessarily constrain the solution
* should instead remain open for architecture

Distinguish reasonable assumptions from invented requirements.

### 3. Architecture Leakage

Flag decisions that belong in later stages, such as:

* ReAct
* planner/executor
* multi-agent
* specific frameworks
* specific models
* vector databases
* detailed component design
* tool implementation choices

`INTENT.md` should describe what the system must accomplish, not how it will accomplish it.

### 4. Acceptance Criteria Quality

Check whether acceptance criteria are:

* observable
* testable
* architecture-independent
* tied to the stated requirements

Flag criteria that are vague or subjective.

### 5. Scope Creep

Identify capabilities or requirements added by the draft that are not required by the challenge.

Do not flag clearly labeled, reasonable assumptions as scope creep.

### 6. Contradictions

Identify conflicts between:

* `CHALLENGE.md`
* requirements
* assumptions
* acceptance criteria

### 7. Material Ambiguities

Identify unresolved questions only when they could materially affect:

* architecture choice
* safety
* system boundaries
* evaluation
* implementation feasibility

Do not create a long list of low-value clarification questions.

## Output

Return:

### Required Fixes

Only issues that should be corrected before architecture.

For each issue include:

* what is wrong
* why it matters
* smallest correction

### Human Decisions

List only ambiguities that cannot be safely resolved with a reasonable assumption.

If none:

`None`

### Status

Return exactly one:

`APPROVED`

or

`NEEDS REVISION`

## Guardrails

Do not:

* propose architecture
* recommend agents or frameworks
* design components
* solve implementation problems
* broaden the scope
* rewrite the entire intent unless necessary

Prefer minimal corrections.

## Approval Standard

Return `APPROVED` when:

* all important challenge requirements are represented
* assumptions are explicit and reasonable
* acceptance criteria are testable
* no meaningful architecture decisions have leaked into intent
* no material contradiction remains
* downstream architecture work can proceed using `INTENT.md` alone
