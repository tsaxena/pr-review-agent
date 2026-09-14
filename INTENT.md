# INTENT.md — PR Review Agent

## Goal

Build an agentic system that, given a GitHub pull request, autonomously understands the intent of the change, analyzes the diff for meaningful issues (bugs, risks, missing tests), and posts actionable review comments back to the PR.

---

## Functional Requirements

1. **Accept a PR as input** — the system takes a PR identifier (URL or repo + number) and retrieves its metadata and diff.
2. **Understand change intent** — infer what the PR is trying to accomplish from the title, description, and changed code.
3. **Analyze the diff** — review changed files and lines for bugs, logic errors, security risks, and missing test coverage.
4. **Generate actionable comments** — produce specific, grounded feedback referencing actual files and line numbers, not generic observations.
5. **Post the review to GitHub** — submit comments and a summary review via the GitHub API, visible on the PR page.

---

## Non-Functional Requirements

1. **Signal-to-noise** — comments must be substantive; avoid trivial style nits that add no value.
2. **Groundedness** — every comment must be traceable to a specific location in the diff.
3. **Reliability** — handle API errors, empty diffs, and large PRs gracefully without crashing.
4. **Latency** — review should complete in a reasonable time for interactive use; should not require many minutes for a typical PR.

---

## Constraints

- Target VCS platform is **GitHub** (API + PR model assumed throughout).
- Must be deliverable within the interview scope (~45 min architecture, ~45 min implementation).
- Testing will use a provided example repository with real PRs; a final unseen PR will be used for evaluation.

---

## Assumptions

1. Input is a GitHub PR URL (e.g. `https://github.com/owner/repo/pull/123`) or equivalent identifiers.
2. GitHub API access is provided via a `GITHUB_TOKEN` environment variable.
3. The system is invoked manually per PR (not a webhook or always-on daemon).
4. Review scope is the changed files and surrounding context — not unrelated parts of the codebase.
5. The system may fetch additional file context beyond the raw diff when needed for understanding.
6. Comments should be posted as a formal GitHub review (not just issue comments), with inline annotations where applicable.
7. A top-level summary comment is always produced; inline comments are produced where a specific location is identified.
8. The review focuses on correctness, security, and test coverage — not formatting or style.

---

## Acceptance Criteria

| # | Criterion |
|---|-----------|
| 1 | Given a valid PR URL, the system retrieves the diff without manual steps. |
| 2 | For a PR containing a real bug or risk, at least one comment identifies it with a specific file and line reference. |
| 3 | All posted comments are grounded in the actual diff (no hallucinated line numbers or files). |
| 4 | The review appears on the GitHub PR page as a submitted review or comment set. |
| 5 | For a clean PR with no issues, the system posts a summary stating no significant issues were found (no false-positive flood). |
| 6 | The system exits cleanly on API errors or malformed input with a clear error message. |

---

## Ambiguities

1. **Input format** — PR URL vs. `owner/repo#number`? Assuming URL is the primary interface; short form is nice-to-have.
2. **Review verdict** — should the system approve, request changes, or only comment? Assuming "COMMENT" by default to avoid blocking merges unintentionally.
3. **Context window limits** — very large PRs (hundreds of files) may exceed LLM context; handling strategy TBD at architecture stage.
4. **Language/stack specificity** — challenge says any language; review logic should work across languages but may have varying depth.
5. **Credentials for the example repo** — assumed to be provided; if the example repo is private, a token with repo scope is needed.
6. **Re-review behavior** — if the system is run twice on the same PR, does it duplicate comments? Assumed to be out of scope for now.
