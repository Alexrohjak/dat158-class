"""Pull DAT158 material out of Canvas into this repo.

Read-only: this script only ever issues GET requests. It never submits, posts,
marks anything complete, or changes a single Canvas setting.

    python src/canvas_sync.py              # refresh the digest, no downloads
    python src/canvas_sync.py --download   # also fetch linked PDFs/slides
    python src/canvas_sync.py --quiet      # only report what changed

Needs a token in .env (gitignored) — see .env.example.

Why this exists: Canvas access disappears when the course ends, and the
lecturer publishes material week by week. Re-run this whenever something new
appears and the repo stays a complete offline archive.

A note on what is reachable. Students cannot enumerate the course Files area
(the API returns 403), so this script discovers files the only way it can:
by scanning module pages, announcements and assignments for links. A file the
lecturer has uploaded but not yet linked from a page is invisible here. That is
a Canvas permission boundary, not a bug.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from paths import ROOT

OUT = ROOT / "docs" / "canvas"
RAW = OUT / "raw"

# Which week folder a page belongs to, when the title says so.
WEEK_IN_TITLE = re.compile(r"[Vv]eke\s*(\d{2})")


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------

def load_env() -> dict[str, str]:
    env_file = ROOT / ".env"
    if not env_file.exists():
        sys.exit("No .env — copy .env.example to .env and add your Canvas token.")

    vals: dict[str, str] = {}
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            vals[key.strip()] = value.strip()

    token = vals.get("CANVAS_API_TOKEN", "")
    if not token or token == "paste_your_token_here":
        sys.exit("CANVAS_API_TOKEN is not set in .env.")
    if not re.match(r"^\d+~", token):
        sys.exit(
            "CANVAS_API_TOKEN doesn't look like a Canvas token — expected a "
            "numeric prefix then '~'. Check for stray characters from pasting."
        )
    return vals


# --------------------------------------------------------------------------
# api
# --------------------------------------------------------------------------

class Canvas:
    def __init__(self, base: str, token: str, course_id: str):
        self.base = base.rstrip("/")
        self.token = token
        self.cid = course_id

    def get(self, path: str, **params):
        """GET an API path. Returns (data, error) — never raises on HTTP error."""
        url = f"{self.base}/api/v1{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode()), None
        except urllib.error.HTTPError as exc:
            return None, f"HTTP {exc.code}"
        except Exception as exc:  # network, timeout, malformed JSON
            return None, str(exc)[:120]

    def download(self, url: str, dest: Path) -> str:
        """Fetch a file to dest. Returns a one-word status for the report."""
        if dest.exists():
            return "exists"
        dest.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                dest.write_bytes(resp.read())
            return "downloaded"
        except Exception as exc:
            return f"failed ({str(exc)[:60]})"


# --------------------------------------------------------------------------
# html -> text
# --------------------------------------------------------------------------

def to_text(raw: str | None) -> str:
    """Canvas page bodies are HTML. Flatten to something readable in markdown."""
    body = raw or ""
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</(p|div|li|h[1-6]|tr)>", "\n", body)
    body = re.sub(r"<li[^>]*>", "  - ", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    body = "\n".join(line.rstrip() for line in body.splitlines())
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def file_ids(raw: str | None) -> list[int]:
    """Canvas file ids linked from a page body, in order, without repeats.

    A single file is usually referenced twice — once by the visible link and
    once by a preview attribute — so dedupe or it downloads twice.
    """
    found = re.findall(r"/files/(\d+)", raw or "")
    return [int(fid) for fid in dict.fromkeys(found)]


def external_links(raw: str | None) -> list[str]:
    """Off-Canvas links worth keeping in resources/links.md."""
    found = re.findall(r'href="(https?://[^"]+)"', raw or "")
    return [
        html.unescape(url)
        for url in dict.fromkeys(found)
        if "instructure.com" not in url
    ]


# --------------------------------------------------------------------------
# collection
# --------------------------------------------------------------------------

def collect(api: Canvas) -> dict:
    """Everything the API will give us, in one dict."""
    snap: dict = {"pages": [], "modules": [], "announcements": [],
                  "assignments": [], "files": {}, "errors": []}

    course, err = api.get(f"/courses/{api.cid}")
    if err:
        sys.exit(f"Cannot read course {api.cid}: {err}")
    snap["course"] = {
        "name": course.get("name"),
        "code": course.get("course_code"),
        "id": course.get("id"),
    }

    tabs, err = api.get(f"/courses/{api.cid}/tabs")
    snap["tabs"] = [
        {"label": t.get("label"), "url": t.get("html_url"), "type": t.get("type")}
        for t in (tabs or [])
    ]
    if err:
        snap["errors"].append(f"tabs: {err}")

    modules, err = api.get(f"/courses/{api.cid}/modules", per_page=100)
    if err:
        snap["errors"].append(f"modules: {err}")
    for module in modules or []:
        items, item_err = api.get(
            f"/courses/{api.cid}/modules/{module['id']}/items", per_page=100
        )
        if item_err:
            snap["errors"].append(f"module {module['id']} items: {item_err}")
        entry = {"name": module.get("name"), "items": []}
        for item in items or []:
            entry["items"].append(
                {"title": item.get("title"), "type": item.get("type"),
                 "page_url": item.get("page_url"), "url": item.get("html_url")}
            )
            if item.get("page_url"):
                page, page_err = api.get(
                    f"/courses/{api.cid}/pages/{item['page_url']}"
                )
                if page_err:
                    snap["errors"].append(f"page {item['page_url']}: {page_err}")
                    continue
                body = page.get("body", "")
                snap["pages"].append({
                    "title": page.get("title"),
                    "slug": item["page_url"],
                    "module": module.get("name"),
                    "updated": page.get("updated_at"),
                    "text": to_text(body),
                    "file_ids": file_ids(body),
                    "links": external_links(body),
                })
        snap["modules"].append(entry)

    anns, err = api.get("/announcements", per_page=100,
                        **{"context_codes[]": f"course_{api.cid}"})
    if err:
        snap["errors"].append(f"announcements: {err}")
    for ann in anns or []:
        body = ann.get("message", "")
        snap["announcements"].append({
            "title": ann.get("title"),
            "posted": ann.get("posted_at"),
            "text": to_text(body),
            "file_ids": file_ids(body),
            "links": external_links(body),
        })

    assigns, err = api.get(f"/courses/{api.cid}/assignments", per_page=100)
    if err:
        snap["errors"].append(f"assignments: {err}")
    for a in assigns or []:
        body = a.get("description", "")
        snap["assignments"].append({
            "name": a.get("name"),
            "due_at": a.get("due_at"),
            "points": a.get("points_possible"),
            "url": a.get("html_url"),
            "text": to_text(body),
            "file_ids": file_ids(body),
        })

    # Resolve every file id we saw. Enumeration is 403 for students, so this
    # is the only way to learn a file's real name.
    seen: set[int] = set()
    for group in ("pages", "announcements", "assignments"):
        for entry in snap[group]:
            seen.update(entry.get("file_ids", []))
    for fid in sorted(seen):
        meta, err = api.get(f"/files/{fid}")
        if err:
            snap["errors"].append(f"file {fid}: {err}")
            continue
        snap["files"][str(fid)] = {
            "name": meta.get("display_name"),
            "size": meta.get("size"),
            "type": meta.get("content-type"),
            "url": meta.get("url"),          # capability URL — never committed
            "updated": meta.get("updated_at"),
        }
    return snap


# --------------------------------------------------------------------------
# output
# --------------------------------------------------------------------------

def week_folder_for(page: dict) -> Path | None:
    """Map a page like 'Veke 35 (24.08 - 30.08)' to weeks/uke35-alg/."""
    match = WEEK_IN_TITLE.search(page.get("title") or "")
    if not match:
        return None
    week = match.group(1)
    hits = sorted((ROOT / "weeks").glob(f"uke{week}-*"))
    return hits[0] if hits else None


def write_digest(snap: dict) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {snap['course']['name']}",
        "",
        "Mirrored from Canvas by `src/canvas_sync.py`. **Do not edit by hand** —",
        "re-run the script instead. Your own notes belong in `weeks/*/notes.md`.",
        "",
        f"Course: `{snap['course']['code']}` (id {snap['course']['id']})",
        "",
        "## Canvas sections",
        "",
        "| Section | Link |",
        "|---|---|",
    ]
    for tab in snap["tabs"]:
        lines.append(f"| {tab['label']} | {tab['url'] or ''} |")

    lines += ["", "## Modules", ""]
    for module in snap["modules"]:
        lines.append(f"### {module['name']}")
        lines.append("")
        for item in module["items"]:
            lines.append(f"- **{item['title']}** — {item['type']}")
        lines.append("")

    lines += ["## Pages", ""]
    for page in snap["pages"]:
        lines += [f"### {page['title']}", "",
                  f"*Module: {page['module']} · updated {page['updated']}*", ""]
        lines.append(page["text"] or "*(empty)*")
        if page["file_ids"]:
            lines += ["", "**Attached files:**"]
            for fid in page["file_ids"]:
                meta = snap["files"].get(str(fid))
                name = meta["name"] if meta else f"(unreadable file {fid})"
                lines.append(f"- {name}")
        if page["links"]:
            lines += ["", "**Links:**"]
            lines += [f"- {url}" for url in page["links"]]
        lines.append("")

    lines += ["## Announcements", ""]
    for ann in snap["announcements"]:
        lines += [f"### {ann['title']}", "", f"*Posted {ann['posted']}*", "",
                  ann["text"], ""]

    lines += ["## Assignments", ""]
    if not snap["assignments"]:
        lines.append("*None published yet.*")
    for a in snap["assignments"]:
        lines += [f"### {a['name']}", "",
                  f"*Due: {a['due_at'] or 'no date'} · {a['points']} points*", "",
                  a["text"], ""]

    if snap["errors"]:
        lines += ["", "## Not readable", "",
                  "Blocked by Canvas permissions or missing — not script failures:", ""]
        lines += [f"- {e}" for e in snap["errors"]]

    path = OUT / "course.md"
    path.write_text("\n".join(lines) + "\n")
    return path


def write_raw(snap: dict) -> Path:
    """The full snapshot, minus the capability URLs, which are secrets."""
    RAW.mkdir(parents=True, exist_ok=True)
    safe = json.loads(json.dumps(snap))
    for meta in safe["files"].values():
        meta.pop("url", None)
    path = RAW / "snapshot.json"
    path.write_text(json.dumps(safe, indent=2, ensure_ascii=False) + "\n")
    return path


def download_files(api: Canvas, snap: dict, quiet: bool) -> list[str]:
    """Put each linked file next to the week it belongs to."""
    report = []
    for page in snap["pages"]:
        target = week_folder_for(page)
        dest_dir = (target / "slides") if target else (OUT / "files")
        for fid in page["file_ids"]:
            meta = snap["files"].get(str(fid))
            if not meta or not meta.get("url"):
                report.append(f"  skip  file {fid} — no download URL")
                continue
            dest = dest_dir / meta["name"]
            status = api.download(meta["url"], dest)
            if status != "exists" or not quiet:
                report.append(f"  {status:11} {dest.relative_to(ROOT)}")
    return report


# --------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true",
                        help="also fetch linked PDFs into the week folders")
    parser.add_argument("--quiet", action="store_true",
                        help="only report changes")
    args = parser.parse_args()

    env = load_env()
    api = Canvas(env["CANVAS_BASE_URL"], env["CANVAS_API_TOKEN"],
                 env["CANVAS_COURSE_ID"])

    snap = collect(api)
    digest = write_digest(snap)
    raw = write_raw(snap)

    if not args.quiet:
        print(f"Course : {snap['course']['name']}")
        print(f"Pages  : {len(snap['pages'])}")
        print(f"Files  : {len(snap['files'])} linked")
        print(f"Notices: {len(snap['announcements'])}")
        print(f"Tasks  : {len(snap['assignments'])}")
        print()
        print(f"Wrote {digest.relative_to(ROOT)}")
        print(f"Wrote {raw.relative_to(ROOT)}")

    if args.download:
        print()
        print("Files:")
        for line in download_files(api, snap, args.quiet) or ["  nothing to do"]:
            print(line)

    if snap["errors"] and not args.quiet:
        print()
        print(f"{len(snap['errors'])} item(s) not readable — see the digest.")


if __name__ == "__main__":
    main()
