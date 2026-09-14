# ARCHITECTURE.md — PR Review Agent

## Problem Characteristics

- Workflow is fully predictable: fetch PR → analyze → post. No dynamic replanning required.
- Open-ended reasoning occurs only at the analysis step (semantic code understanding). All surrounding control is deterministic.
- One externally visible, non-trivially reversible side effect: posting a review to GitHub. Must be validated before posting.
- State is per-run only. No persistence, memory, or queuing needed.
- Tool surface is minimal: GitHub API reads (metadata, diff) and one GitHub API write (post review).
- Interview constraint (~45 min implementation) makes simplicity load-bearing.

---

## Options Considered

### Option 1: Deterministic Pipeline + Single LLM Analysis Call (Selected)

Control flow:
```
fetch_pr(url)
  → build_prompt(metadata, diff)
  → llm_call(prompt) → structured JSON
  → validate(comments, diff)   ← deterministic
  → post_review(github_api)
```

- Single structured LLM call produces all output: intent summary + inline comments + overall verdict.
- Deterministic orchestration wraps the LLM call end-to-end.
- Validation checks every referenced file and line exists in the actual diff before any post occurs.
- Large PR fallback (P1): truncate diff or skip oversized files above a configurable token threshold.

Strengths: simple, fast, debuggable, covers all AC. Weakness: context window limit on very large PRs (explicitly deferred to P1).

---

### Option 2: Deterministic Pipeline + Per-File LLM Calls

Same orchestration, but each changed file receives its own LLM analysis call, followed by a synthesis call for the summary. Better coverage on large PRs. Adds orchestration complexity, higher API cost, and more prompt engineering — not justified for typical interview PRs.

---

### Option 3: ReAct Agent with Tools

Agent loop dynamically decides to fetch additional file context, look up related code, or reason iteratively. Adds unpredictable latency, difficult stopping bounds, and significant implementation complexity. Not justified: the task requires no adaptive investigation; the diff is fully available at start.

---

## Selected Architecture

**Option 1: Deterministic Pipeline + Single LLM Analysis Call**

Approved by: human (explicit selection).

---

## Rationale and Tradeoffs

Option 1 is sufficient because the task has a fixed, known step sequence. The only open-ended element — reasoning over the diff — is well-served by a single focused LLM call with a structured output schema. Options 2 and 3 add complexity without satisfying any additional requirement for typical PR sizes.

The accepted tradeoff: very large PRs may exceed the context window. This is mitigated at P1 by truncating or skipping oversized diffs, which is architecturally simple and does not require redesign.

---

## High-Level Control Flow

```
1. [deterministic] Parse and validate input (PR URL or owner/repo/number)
2. [deterministic] Fetch PR metadata via GitHub API (title, description, author, base/head SHAs)
3. [deterministic] Fetch PR diff via GitHub API (list of changed files + patch hunks)
4. [deterministic] Check diff size; apply truncation if over token threshold (P1)
5. [LLM]           Single structured call: understand intent, identify issues, produce comments
6. [deterministic] Validate all comment file/line references exist in the actual diff
7. [deterministic] Post validated review to GitHub (summary + inline comments, verdict = COMMENT)
8. [deterministic] Report success or exit with error on API failure
```

---

## LLM vs Deterministic Boundary

| Responsibility | Owner |
|---|---|
| Input parsing and validation | Deterministic |
| GitHub API calls (read + write) | Deterministic |
| Diff size check and truncation | Deterministic |
| Understanding PR intent | LLM |
| Identifying bugs, risks, missing tests | LLM |
| Generating comment text and summary | LLM |
| Determining which files/lines to annotate | LLM |
| Validating file/line references before posting | Deterministic |
| Retry logic on API errors | Deterministic |
| Stopping conditions | Deterministic |

LLM output must be parsed into a structured schema before any action is taken. The LLM does not directly invoke the GitHub write API.

---

## State Requirements

Per-run only. No database, queue, vector store, or persistent memory required.

Intermediate state held in memory during a single invocation:
- PR metadata
- Raw diff
- LLM structured output
- Validated comment list

No state crosses invocation boundaries (re-review deduplication is out of scope per INTENT.md).

---

## Key Architectural Invariants

1. **Execution is bounded.** One LLM call per run; no agent loop; no unbounded retries.
2. **No post without validation.** All file and line references must be verified against the diff before the GitHub write call.
3. **Deterministic control, not LLM control.** The LLM produces content; deterministic code decides when to post.
4. **External content is untrusted.** PR title, description, diff content, and code are treated as untrusted input and must not override system prompts or tool behavior.
5. **Single review verdict.** Always COMMENT; never APPROVE or REQUEST_CHANGES (avoids blocking merges unintentionally).

---

## Major Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Diff exceeds LLM context window | Medium | P1: truncate or skip large files; flag in output |
| LLM returns malformed JSON | Low-Medium | Parse with schema validation; retry once; exit cleanly on failure |
| LLM references a file/line not in diff (hallucination) | Low-Medium | Deterministic post-processing validates all references before posting |
| GitHub API rate limit or auth failure | Low | Surface clear error message; exit cleanly |
| Prompt injection via PR content | Low | System prompt clearly separates instructions from untrusted content |

---

## Constraints Carried Forward

- Target platform: GitHub (GitHub REST API).
- LLM invoked via Anthropic Claude API (ANTHROPIC_API_KEY) or equivalent.
- GitHub token provided via GITHUB_TOKEN environment variable.
- Review verdict fixed at COMMENT.
- Input assumed to be a PR URL; short-form support (owner/repo#number) is P1.

---

## Human Approval

Architecture decision: **Option 1 — Deterministic Pipeline + Single LLM Analysis Call**

Approved by human on 2026-09-14.
