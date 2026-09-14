from dataclasses import dataclass, field


@dataclass
class PRIdentifier:
    owner: str
    repo: str
    number: int


@dataclass
class PRMetadata:
    title: str
    description: str
    author: str
    base_sha: str
    head_sha: str


@dataclass
class FileDiff:
    filename: str
    status: str       # added | modified | removed | renamed
    additions: int
    deletions: int
    patch: str        # unified diff hunks; empty string if absent


@dataclass
class InlineComment:
    path: str
    line: int
    body: str
    severity: str = "info"


@dataclass
class ReviewOutput:
    summary: str
    comments: list[InlineComment] = field(default_factory=list)


@dataclass
class ValidatedReview:
    summary: str
    valid_comments: list[InlineComment] = field(default_factory=list)
    rejected_count: int = 0


@dataclass
class RunResult:
    success: bool
    review_id: int | None = None
    review_url: str | None = None
    error: str | None = None
