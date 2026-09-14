import os
import re
import sys

from pr_review.models import (
    PRIdentifier,
    ValidatedReview,
    RunResult,
)
from pr_review.github import fetch_pr_metadata, fetch_pr_diff, post_review
from pr_review.llm import build_prompt, llm_analyze
from pr_review.validator import validate_references

_PR_URL_RE = re.compile(
    r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)"
)


def parse_pr_url(url: str) -> PRIdentifier:
    m = _PR_URL_RE.match(url.strip().rstrip("/"))
    if not m:
        raise ValueError(
            f"Invalid PR URL: {url!r}\n"
            "Expected: https://github.com/owner/repo/pull/NUMBER"
        )
    return PRIdentifier(owner=m.group(1), repo=m.group(2), number=int(m.group(3)))


def run_pipeline(pr_url: str) -> RunResult:
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        return RunResult(success=False, error="GITHUB_TOKEN environment variable is not set")

    try:
        pr = parse_pr_url(pr_url)
    except ValueError as e:
        return RunResult(success=False, error=str(e))

    try:
        meta = fetch_pr_metadata(pr, github_token)
        print(f"  PR: {meta.title!r} by {meta.author}")
    except RuntimeError as e:
        return RunResult(success=False, error=str(e))

    try:
        diffs = fetch_pr_diff(pr, github_token)
        print(f"  Diff: {len(diffs)} file(s) changed")
    except RuntimeError as e:
        return RunResult(success=False, error=str(e))

    if not diffs:
        print("  Empty diff — posting no-changes summary")
        try:
            review_id, review_url = post_review(
                pr,
                ValidatedReview(summary="No changes found in this PR.", valid_comments=[]),
                github_token,
            )
        except RuntimeError as e:
            return RunResult(success=False, error=str(e))
        return RunResult(success=True, review_id=review_id, review_url=review_url)

    prompt = build_prompt(meta, diffs)

    try:
        output = llm_analyze(prompt)
        print(f"  LLM: {len(output.comments)} raw comment(s)")
    except RuntimeError as e:
        return RunResult(success=False, error=str(e))

    validated = validate_references(output, diffs)
    print(
        f"  Validation: {len(validated.valid_comments)} valid, "
        f"{validated.rejected_count} rejected"
    )

    try:
        review_id, review_url = post_review(pr, validated, github_token)
    except RuntimeError as e:
        return RunResult(success=False, error=str(e))

    return RunResult(success=True, review_id=review_id, review_url=review_url)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m pr_review <PR_URL>", file=sys.stderr)
        sys.exit(1)

    pr_url = sys.argv[1]
    print(f"Reviewing: {pr_url}")

    result = run_pipeline(pr_url)

    if result.success:
        print(f"Review posted: {result.review_url}")
        sys.exit(0)
    else:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
