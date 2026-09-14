# Stage 2 — Architecture

Read:

* `INTENT.md`
* `AGENTS.md`

Do not reread `CHALLENGE.md`.

Treat the approved `INTENT.md` as the authoritative problem contract.

## Goal

Produce an approved `ARCHITECTURE.md` that selects the simplest architecture capable of satisfying the intent.

## Process

1. Apply the `architecture-analysis` skill to `INTENT.md`.
2. Generate 2–3 realistic architecture options when useful.
3. Compare them against:

   * requirements
   * constraints
   * acceptance criteria
   * implementation feasibility
4. Recommend one architecture.
5. Present the recommendation and tradeoffs to the user.
6. Wait for the user to make or approve the final architecture decision.
7. Record the approved decision in `ARCHITECTURE.md`.

## Human Gate

The AI may recommend an architecture, but the human owns the final decision.

Do not proceed to detailed design until the architecture is explicitly approved.

## Output

`ARCHITECTURE.md`

The artifact should capture:

* problem characteristics relevant to architecture
* options considered
* selected architecture
* rationale and tradeoffs
* high-level control flow
* LLM vs deterministic boundary
* architectural state requirements
* key invariants
* constraints carried forward
* major risks
* explicit human approval

## Boundaries

Do not:

* create detailed component or class designs
* define implementation files
* write code
* silently change requirements from `INTENT.md`
* proceed to Stage 3 without approval

Stop after Stage 2.
