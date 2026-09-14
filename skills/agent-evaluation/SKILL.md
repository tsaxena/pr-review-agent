# Agent Evaluation

## Purpose

Evaluate whether an implemented agentic system actually performs its intended task successfully, reliably, and efficiently.

Evaluate the agent as a system, not merely as a collection of functions.

## Inputs

* `REVIEW.md`
* working implementation
* available test environment

Treat the system behavior and success criteria carried forward in `REVIEW.md` as authoritative.

## Method

### 1. Identify Evaluation Targets

Determine what matters for this particular agent.

Possible dimensions include:

* task success
* correctness
* completeness
* evidence grounding
* false positives
* false negatives
* tool selection
* trajectory quality
* recovery from failure
* unnecessary actions
* latency
* cost

Use only metrics relevant to the system.

Do not evaluate everything simply because it can be measured.

---

### 2. Create Evaluation Cases

Construct a small set of meaningful cases.

Consider:

#### Happy Path

Normal input the system should handle successfully.

#### Ambiguous Input

Input where the agent must reason before acting.

#### Invalid Input

Malformed or unsupported input.

#### Tool Failure

A required tool returns an error or unavailable result.

#### Partial Failure

Part of the workflow succeeds while another part fails.

#### Repeated Execution

Run the same or equivalent task again when duplicate actions could matter.

#### Adversarial / Misleading Input

Input or external content that may cause incorrect reasoning or unsafe behavior.

#### Hidden-Test-Style Case

A realistic case not obviously anticipated by the implementation.

Only include cases relevant to the system.

---

### 3. Define Expected Behavior Before Running

For each case define:

* inpu
