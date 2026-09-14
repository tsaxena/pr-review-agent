# DESIGN.md — PR Review Agent

## 1. Design Thesis

A deterministic pipeline owns all control flow: it fetches the PR, builds the prompt, invokes a single LLM call, validates the output, and posts the review. The LLM's sole role is semantic reasoning — understanding intent, identifying issues, and generating comment text. All structural guarantees (validation, side-effect authorization, error handling) are enforced by deterministic code that wraps the LLM call.

---

## 2. Major Components

### 2.1 Input Parser
- **Responsibility**: Parse and validate the PR URL into a structured identifier.
- **Input**: raw string (e.g. `https://github.com/owner/repo/pull/123`)
- **Output**: `PRIdentifier { owner, repo, number }`
- **Boundary**: Rejects invalid URLs before any API call is made.

### 2.2 GitHub Client
- **Responsibility**: All GitHub API I/O — two reads and one write.
- **Input**: `PRIdentifier` + `GITHUB_TOKEN`
- **Output** (reads): `PRMetadata`, `list[FileDiff]`
- **Output** (write): `review_id`
- **Boundary**: Only component that touches the GitHub API. All calls are authenticated. Write call only happens after the validated comment list is produced.

### 2.3 Prompt Builder
- **Responsibility**: Assemble the LLM prompt from PR metadata and diff content.
- **Input**: `PRMetadata`, `list[FileDiff]`
- **Output**: formatted prompt string
- **Boundary**: Diff content is injected as a clearly delimited data block — not as instructions. Prevents prompt injection from PR content.

### 2.4 LLM Analyzer
- **Responsibility**: Single Claude API call that reasons over the PR and returns a structured review.
- **Input**: prompt string
- **Output**: raw JSON string conforming to `ReviewOutput` schema
- **Boundary**: LLM produces content only. It does not call tools, trigger API writes, or make control decisions.

### 2.5 Output Parser + Validator
- **Responsibility**: Parse LLM JSON, validate schema, then validate every comment's file and line reference against the actual diff.
- **Input**: raw LLM JSON string, `list[FileDiff]`
- **Output**: `ValidatedReview { summary, valid_comments, rejected_comments }`
- **Boundary**: Enforces groundedness. No comment may reference a file or line that does not appear in the diff. Runs deterministically before any write.

### 2.6 Review Poster
- **Responsibility**: POST the validated review to GitHub.
- **Input**: `PRIdentifier`, `ValidatedReview`
- **Output**: `review_id`
- **Boundary**: This is the only externally visible write action. It never runs before Output Validator completes successfully.

---

## 3. End-to-End Control Flow

```
[Input] PR URL string
    │
    ▼
[Input Parser]
  Parse URL → PRIdentifier
  FAIL: malformed URL → exit(1) with message
    │
    ▼
[GitHub Client: fetch_pr_metadata]
  GET /repos/{owner}/{repo}/pulls/{number}
  → PRMetadata { title, description, author, base_sha, head_sha }
  FAIL: 401 → "Check GITHUB_TOKEN" exit(1)
  FAIL: 404 → "PR not found" exit(1)
  FAIL: network → exit(1) with message
    │
    ▼
[GitHub Client: fetch_pr_diff]
  GET /repos/{owner}/{repo}/pulls/{number}/files
  → list[FileDiff]
  FAIL: same as above
  EDGE: empty diff → skip LLM; post "No changes found" summary → exit(0)
    │
    ▼
[Diff Size Check]                        ← P1: truncate or skip files if over
  check total patch tokens               ← token threshold; flag in summary
    │
    ▼
[Prompt Builder]
  Assemble prompt with metadata + diff
  → prompt string
    │
    ▼
[LLM Analyzer]
  POST to Claude API
  → raw JSON string
  FAIL: API error → exit(1) with message
  FAIL: malformed JSON → retry once → FAIL again → exit(1) with message
    │
    ▼
[Output Parser + Validator]
  1. Parse JSON → ReviewOutput struct
     FAIL: schema error → retry LLM once → FAIL again → exit(1)
  2. For each comment: check path ∈ changed files AND line ∈ added lines
     Drop invalid comments; log count
  3. Produce ValidatedReview
    │
    ▼
[Review Poster]
  POST /repos/{owner}/{repo}/pulls/{number}/reviews
  body = summary, comments = valid_comments, event = "COMMENT"
  FAIL (422 line error) → retry with summary only (no inline comments)
  FAIL (other) → exit(1) with message
    │
    ▼
[Report] print review URL + comment count → exit(0)
```

---

## 4. LLM Responsibilities

### LLM MAY decide:
- What the PR is trying to accomplish (inferred from title, description, diff)
- Which files and lines contain bugs, logic errors, security risks, or missing tests
- What comment text to write for a specific location
- What to include in the overall summary

### LLM MUST NOT control:
- Whether a review is posted
- Whether a line reference is valid
- API call sequencing or retries
- Whether to truncate the diff
- The review verdict (always `COMMENT`, set deterministically)
- Any error handling

---

## 5. Tool Contracts

### `fetch_pr_metadata(owner, repo, number) → PRMetadata`
- **API**: `GET /repos/{owner}/{repo}/pulls/{number}`
- **Output**:
  ```
  PRMetadata {
    title: str
    description: str       # PR body, may be empty
    author: str
    base_sha: str
    head_sha: str
  }
  ```
- **Failure modes**: 401 auth, 403 rate limit, 404 not found, network error
- **Side effects**: none (read)

### `fetch_pr_diff(owner, repo, number) → list[FileDiff]`
- **API**: `GET /repos/{owner}/{repo}/pulls/{number}/files` (paginated; max 300 files per GitHub docs)
- **Output**:
  ```
  FileDiff {
    filename: str          # path relative to repo root
    status: str            # added | modified | removed | renamed
    additions: int
    deletions: int
    patch: str             # unified diff hunk(s); absent for binary files
  }
  ```
- **Failure modes**: same as above; `patch` may be absent for binary or too-large files
- **Side effects**: none (read)

### `llm_analyze(prompt) → str`
- **API**: Anthropic Claude (messages endpoint)
- **Output**: JSON string matching `ReviewOutput` schema
- **Failure modes**: API error, rate limit (429), timeout, malformed JSON
- **Side effects**: billable API call; latency ~2–10s
- **Retry**: caller retries once on JSON parse or schema failure

### `post_review(owner, repo, number, summary, comments) → int`
- **API**: `POST /repos/{owner}/{repo}/pulls/{number}/reviews`
- **Payload**:
  ```
  {
    "body": summary,
    "event": "COMMENT",
    "comments": [
      {
        "path": str,       # must match FileDiff.filename
        "line": int,       # file line number of an added line (side = RIGHT)
        "side": "RIGHT",
        "body": str
      }
    ]
  }
  ```
- **Output**: `review_id` (int) on 200
- **Failure modes**:
  - 422: one or more `line` values rejected by GitHub → fallback: retry with `comments = []`
  - 401 / 403 / network: exit with error
- **Side effects**: creates a review visible on the PR page; **irreversible**

---

## 6. Data Schemas

### LLM Output Schema (`ReviewOutput`)
```json
{
  "summary": "string",
  "comments": [
    {
      "path": "string",
      "line": 42,
      "body": "string",
      "severity": "bug | risk | test | info"
    }
  ]
}
```

`severity` is advisory only; it does not change posting behavior.

### In-Memory Run State
```
PRIdentifier    { owner, repo, number }
PRMetadata      { title, description, author, base_sha, head_sha }
FileDiff[]      { filename, status, additions, deletions, patch }
ReviewOutput    { summary, comments[] }
ValidatedReview { summary, valid_comments[], rejected_comments[] }
RunResult       { success, review_id?, error? }
```

No state is persisted across invocations.

---

## 7. LLM / Deterministic Boundary

| Responsibility | Owner |
|---|---|
| Parse input URL | Deterministic |
| Fetch PR metadata and diff | Deterministic |
| Check and truncate diff size | Deterministic |
| Assemble LLM prompt | Deterministic |
| Separate instructions from PR content in prompt | Deterministic |
| Understand PR intent | LLM |
| Identify bugs, risks, missing tests | LLM |
| Generate comment text and summary | LLM |
| Choose which files and lines to annotate | LLM |
| Parse LLM JSON response | Deterministic |
| Validate JSON schema | Deterministic |
| Validate file/line references against diff | Deterministic |
| Set review verdict to COMMENT | Deterministic |
| Post review to GitHub | Deterministic |
| Retry on LLM failure | Deterministic |
| Retry on GitHub 422 | Deterministic |
| Exit on unrecoverable error | Deterministic |

---

## 8. Failure Handling

| Failure | Action |
|---|---|
| Invalid PR URL | Parse error → exit(1) |
| GitHub 401 (auth) | "Check GITHUB_TOKEN" → exit(1) |
| GitHub 403/429 (rate limit) | Surface message → exit(1) |
| GitHub 404 (not found) | "PR not found" → exit(1) |
| Network error | Surface message → exit(1) |
| Empty diff | Skip LLM; post "No changes in this PR" summary → exit(0) |
| LLM API error | Surface message → exit(1) |
| Malformed JSON (1st attempt) | Retry LLM once with same prompt |
| Malformed JSON (2nd attempt) | exit(1) with message |
| Schema validation failure | Same as malformed JSON |
| All comments fail reference validation | Post summary-only review; log rejection count |
| GitHub 422 on review post | Retry without inline comments (summary only) |
| GitHub error on retry | exit(1) |

**Execution is strictly bounded**: at most 2 LLM calls (retry) and 2 GitHub write attempts (422 fallback) per run. No loops.

---

## 9. Safety Boundaries

### Untrusted Content
PR title, description, patch content, and code are untrusted. The prompt template uses explicit delimiters:

```
<instructions>
  ... system instructions ...
</instructions>

<pr_metadata>
  Title: {title}
  Description: {description}
</pr_metadata>

<diff>
{patch content}
</diff>
```

Content inside `<diff>` and `<pr_metadata>` is data. The LLM is instructed to treat it as material to analyze, not as directives.

### Write Authorization Gate
`post_review` is called only after `ValidatedReview` is produced. The validator is deterministic and runs in the same process as the caller. The LLM has no pathway to bypass it.

### Review Verdict
`event` is hardcoded to `"COMMENT"` in the posting code. The LLM output schema does not include a `verdict` field.

### Line Reference Validation
For a comment to pass validation:
1. `path` must match a `filename` in the fetched `list[FileDiff]`
2. `line` must be a file line number that appears as an added line (`+` prefix) in the file's `patch`

Parsing added lines from the patch hunk headers (`@@ -a,b +c,d @@`) gives the authoritative set of valid line numbers.

---

## 10. Observability

Minimum log output per run (stderr or structured):

| Event | Fields |
|---|---|
| Run start | pr_url |
| PR fetched | title, file_count, total_additions |
| Diff size | token_estimate, truncated (P1) |
| LLM call | model, attempt_number |
| LLM response | comment_count_raw |
| Validation | valid_count, rejected_count |
| Review posted | review_id, review_url |
| Error | step, message |
| Run complete | status (SUCCESS/FAILURE) |

No external telemetry system required.

---

## 11. Evaluation Hooks

| Test | Assertion |
|---|---|
| PR with known bug | ≥1 comment references the correct file + approximate line |
| Clean PR | ≤N comments (low false-positive count) |
| Groundedness | 100% of posted comments exist in the diff (file + line) |
| Empty diff | No LLM call; "no changes" review posted |
| Malformed LLM JSON | Retry logged; exits cleanly on second failure |
| Invalid PR URL | Exits immediately; no API calls made |
| Valid PR URL, bad token | 401 error surfaced; no review posted |
| GitHub 422 on post | Fallback summary-only review succeeds |
| Review visibility | GitHub PR page shows the review |

These assertions can be verified by inspecting `RunResult` and the log output. No eval framework required for P0.

---

## 12. Minimal Vertical Slice (P0)

The smallest implementation that proves the architecture:

1. **Input**: accept a GitHub PR URL from CLI argument
2. **Fetch**: retrieve metadata + diff from GitHub API using `GITHUB_TOKEN`
3. **Prompt**: build a prompt embedding title, description, and patch
4. **Analyze**: call Claude API, parse `ReviewOutput` JSON
5. **Validate**: check every comment's path and line against the diff
6. **Post**: submit review via GitHub API with `event=COMMENT`
7. **Report**: print success with review URL, or error with message

**Defer to P1**:
- Diff truncation for large PRs
- `owner/repo#number` short-form input
- LLM retry on JSON failure (acceptable to fail cleanly on first error for now)
- Per-rejection logging detail
- Token counting

The vertical slice is the full critical path. No stub components.

---

## Human Approval

Present for approval: `DESIGN.md`

Do not proceed to implementation planning until explicitly approved.
