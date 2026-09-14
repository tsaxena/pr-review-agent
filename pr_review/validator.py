import re

from pr_review.models import FileDiff, ReviewOutput, ValidatedReview, InlineComment

_HUNK_RE = re.compile(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def _added_lines(patch: str) -> set[int]:
    """Return the set of file line numbers that were added ('+' prefix) in the patch."""
    added: set[int] = set()
    if not patch:
        return added

    current_line = 0
    for raw_line in patch.splitlines():
        hunk_match = _HUNK_RE.match(raw_line)
        if hunk_match:
            current_line = int(hunk_match.group(1))
            continue
        if raw_line.startswith("-"):
            # Deletion: exists in old file only, does not advance new-file line counter
            continue
        if raw_line.startswith("+"):
            # Addition: this is an added line at current_line
            added.add(current_line)
            current_line += 1
        else:
            # Context line: exists in both old and new file
            current_line += 1

    return added


def _build_index(diffs: list[FileDiff]) -> dict[str, set[int]]:
    """Map filename → set of added line numbers."""
    return {d.filename: _added_lines(d.patch) for d in diffs}


def validate_references(review: ReviewOutput, diffs: list[FileDiff]) -> ValidatedReview:
    index = _build_index(diffs)
    valid: list[InlineComment] = []
    rejected = 0

    for comment in review.comments:
        added_lines = index.get(comment.path)
        if added_lines is None:
            # File not in diff
            rejected += 1
            continue
        if comment.line not in added_lines:
            # Line not an added line
            rejected += 1
            continue
        valid.append(comment)

    return ValidatedReview(
        summary=review.summary,
        valid_comments=valid,
        rejected_count=rejected,
    )
