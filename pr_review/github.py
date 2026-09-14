import requests

from pr_review.models import PRIdentifier, PRMetadata, FileDiff, ValidatedReview

_BASE = "https://api.github.com"
_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _auth_headers(token: str) -> dict:
    return {**_HEADERS, "Authorization": f"Bearer {token}"}


def _check(resp: requests.Response, context: str) -> None:
    if resp.status_code == 401:
        raise RuntimeError(f"GitHub auth failed ({context}). Check GITHUB_TOKEN.")
    if resp.status_code == 403:
        raise RuntimeError(f"GitHub forbidden ({context}). Token may lack permissions or rate limit hit.")
    if resp.status_code == 404:
        raise RuntimeError(f"GitHub not found ({context}). Check the PR URL.")
    if not resp.ok:
        raise RuntimeError(f"GitHub error {resp.status_code} ({context}): {resp.text[:200]}")


def fetch_pr_metadata(pr: PRIdentifier, token: str) -> PRMetadata:
    url = f"{_BASE}/repos/{pr.owner}/{pr.repo}/pulls/{pr.number}"
    try:
        resp = requests.get(url, headers=_auth_headers(token), timeout=15)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error fetching PR metadata: {e}") from e
    _check(resp, "fetch_pr_metadata")
    data = resp.json()
    return PRMetadata(
        title=data.get("title", ""),
        description=data.get("body") or "",
        author=data.get("user", {}).get("login", ""),
        base_sha=data.get("base", {}).get("sha", ""),
        head_sha=data.get("head", {}).get("sha", ""),
    )


def fetch_pr_diff(pr: PRIdentifier, token: str) -> list[FileDiff]:
    files: list[FileDiff] = []
    page = 1
    while True:
        url = f"{_BASE}/repos/{pr.owner}/{pr.repo}/pulls/{pr.number}/files"
        try:
            resp = requests.get(
                url,
                headers=_auth_headers(token),
                params={"per_page": 100, "page": page},
                timeout=15,
            )
        except requests.RequestException as e:
            raise RuntimeError(f"Network error fetching PR diff: {e}") from e
        _check(resp, "fetch_pr_diff")
        batch = resp.json()
        if not batch:
            break
        for f in batch:
            files.append(
                FileDiff(
                    filename=f["filename"],
                    status=f.get("status", "modified"),
                    additions=f.get("additions", 0),
                    deletions=f.get("deletions", 0),
                    patch=f.get("patch", ""),
                )
            )
        page += 1
    return files


def post_review(pr: PRIdentifier, review: ValidatedReview, token: str) -> tuple[int, str]:
    url = f"{_BASE}/repos/{pr.owner}/{pr.repo}/pulls/{pr.number}/reviews"
    comments_payload = [
        {
            "path": c.path,
            "line": c.line,
            "side": "RIGHT",
            "body": c.body,
        }
        for c in review.valid_comments
    ]
    payload = {
        "body": review.summary,
        "event": "COMMENT",
        "comments": comments_payload,
    }

    def _post(p: dict) -> requests.Response:
        try:
            return requests.post(url, headers=_auth_headers(token), json=p, timeout=15)
        except requests.RequestException as e:
            raise RuntimeError(f"Network error posting review: {e}") from e

    resp = _post(payload)

    if resp.status_code == 422 and comments_payload:
        # Fallback: post summary only without inline comments
        resp = _post({"body": review.summary, "event": "COMMENT", "comments": []})

    _check(resp, "post_review")
    data = resp.json()
    review_id = data["id"]
    # Construct the review URL from the PR html_url
    pr_html = data.get("html_url", "")
    return review_id, pr_html
