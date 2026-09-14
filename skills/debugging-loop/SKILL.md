# Debugging Loop

## Purpose

Diagnose and fix implementation failures systematically without introducing unnecessary changes or architecture drift.

Use this skill when a build step, test, tool call, or end-to-end run fails.

## Inputs

* observed failure
* relevant code
* expected behavior from the current implementation plan

## Method

### 1. Capture the Failure

Record the actual:

* command or action
* input
* output
* error
* stack trace or tool result

Do not debug from assumptions when actual evidence is available.

---

### 2. Localize the Failure

Determine which boundary failed:

* environment
* input validation
* interface contract
* control flow
* state
* model output
* tool invocation
* external dependency
* deterministic gate
* test assumption

Prefer evidence over speculation.

---

### 3. Form a Small Number of Hypotheses

Generate the most likely explanations.

Rank them by:

* evidence
* likelihood
* ease of verification

Avoid broad speculative rewrites.

---

### 4. Test the Smallest Hypothesis

Use the cheapest focused check first.

Examples:

* inspect a variable
* run one function
* call one tool
* validate one schema
* reproduce with a minimal input
* run one test

---

### 5. Apply the Smallest Fix

Fix the root cause rather than masking the symptom.

Avoid unrelated cleanup while debugging.

---

### 6. Reproduce and Verify

Rerun:

1. the failing case
2. the relevant focused test
3. the previous successful path when regression risk exists

A fix is not complete until the original failure no longer reproduces.

---

### 7. Escalate When Necessary

Stop and surface the issue if the required fix would change:

* architecture
* major component boundaries
* approved design
* project scope

Do not silently redesign during debugging.

## Guardrails

Do not:

* make large rewrites before localizing the failure
* modify multiple unrelated areas simultaneously
* disable tests merely to obtain a passing run
* hard-code outputs for the current test case
* suppress errors without understanding them
* assume the LLM's first diagnosis is correct

Prefer one hypothesis, one test, one small fix.
