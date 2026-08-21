"""Search everything you have collected for this subject, in one place.

    python src/find.py tries              # where is this covered?
    python src/find.py "gradient descent" # phrases need quotes
    python src/find.py trie --context 3   # more surrounding lines
    python src/find.py --rebuild          # force re-extraction

Searches week records, the Canvas mirror, both textbooks, every slide deck and
every exercise notebook — and tells you the page or cell, so you can go
straight there.

`grep -r` only reads the markdown. The lecture content is in PDFs and notebooks,
which is exactly the material you want during revision, so this extracts those
too and caches the text. First run is slow (a 500-page book takes a few
seconds); later runs are instant until a file changes.

**Scanned PDFs are invisible here.** A PDF with no text layer cannot be
searched without OCR — `--sources` lists which ones are affected.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from paths import ROOT

CACHE = ROOT / ".searchcache"

# Where to look, and what to call it in the output.
SOURCES = [
    ("week record", "weeks/*/README.md"),
    ("canvas",      "docs/canvas/course.md"),
    ("guide",       "*.md"),
    ("guide",       "ml/**/*.md"),
    ("guide",       "alg/**/*.md"),
    ("guide",       "resources/*.md"),
    ("guide",       "exam/*.md"),
    ("slides",      "weeks/*/slides/*.pdf"),
    ("slides",      "weeks/*/slides/**/*.html"),
    ("textbook",    "reference/*.pdf"),
    ("notebook",    "reference/DAT158/notebooks/*.ipynb"),
    ("canvas file", "docs/canvas/files/*.pdf"),
]


def cache_path(path: Path) -> Path:
    key = re.sub(r"[^A-Za-z0-9]+", "_", str(path.relative_to(ROOT)))
    return CACHE / f"{key}.json"


def extract_pdf(path: Path) -> list[tuple[str, str]]:
    """[(locator, text)] per page. Empty list if there is no text layer."""
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pypdf is not installed — run: pip install pypdf cryptography")

    out = []
    try:
        reader = PdfReader(str(path))
        for n, page in enumerate(reader.pages, 1):
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""
            if text.strip():
                out.append((f"p.{n}", text))
    except Exception as exc:
        print(f"  ! {path.name}: {str(exc)[:70]}", file=sys.stderr)
    return out


def extract_notebook(path: Path) -> list[tuple[str, str]]:
    """[(locator, text)] per cell — markdown and code, outputs ignored."""
    try:
        nb = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return []
    out = []
    for n, cell in enumerate(nb.get("cells", []), 1):
        src = cell.get("source", [])
        text = "".join(src) if isinstance(src, list) else str(src)
        if text.strip():
            out.append((f"cell {n} ({cell.get('cell_type', '?')})", text))
    return out


def extract_text_file(path: Path) -> list[tuple[str, str]]:
    """Markdown and HTML, chunked by line so we can report line numbers."""
    try:
        raw = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    if path.suffix == ".html":
        raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
        raw = re.sub(r"<[^>]+>", " ", raw)
    return [(f"line {n}", line) for n, line in enumerate(raw.splitlines(), 1) if line.strip()]


def load(path: Path, rebuild: bool) -> list[tuple[str, str]]:
    """Extracted units for one file, cached against its mtime and size."""
    stat = path.stat()
    stamp = f"{int(stat.st_mtime)}:{stat.st_size}"
    cp = cache_path(path)

    if not rebuild and cp.exists():
        try:
            blob = json.loads(cp.read_text())
            if blob.get("stamp") == stamp:
                return [tuple(x) for x in blob["units"]]
        except Exception:
            pass

    if path.suffix == ".pdf":
        units = extract_pdf(path)
    elif path.suffix == ".ipynb":
        units = extract_notebook(path)
    else:
        units = extract_text_file(path)

    CACHE.mkdir(exist_ok=True)
    cp.write_text(json.dumps({"stamp": stamp, "units": units}))
    return units


def gather() -> list[tuple[str, Path]]:
    """Every file worth searching, deduped, with its label."""
    seen: dict[Path, str] = {}
    for label, pattern in SOURCES:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file() and path not in seen:
                seen[path] = label
    return [(label, path) for path, label in seen.items()]


def snippet(text: str, term: re.Pattern, width: int = 150) -> str:
    m = term.search(text)
    if not m:
        return " ".join(text.split())[:width]
    flat = " ".join(text.split())
    m2 = term.search(flat) or m
    start = max(0, m2.start() - width // 3)
    out = flat[start:start + width]
    return ("…" if start else "") + out + ("…" if start + width < len(flat) else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="text to look for (case-insensitive)")
    ap.add_argument("--rebuild", action="store_true", help="re-extract everything")
    ap.add_argument("--sources", action="store_true", help="list what is indexed")
    ap.add_argument("--context", type=int, default=1, help="hits to show per file")
    args = ap.parse_args()

    files = gather()

    if args.sources or not args.query:
        print(f"{len(files)} files indexed\n")
        blind = []
        by_label: dict[str, int] = {}
        for label, path in files:
            by_label[label] = by_label.get(label, 0) + 1
            if path.suffix == ".pdf" and not load(path, args.rebuild):
                blind.append(path)
        for label, n in sorted(by_label.items()):
            print(f"  {label:12} {n}")
        if blind:
            print("\nNot searchable — no text layer (scanned images, would need OCR):")
            for path in blind:
                print(f"  {path.relative_to(ROOT)}")
        if not args.query:
            print("\nGive a search term, e.g.  python src/find.py tries")
        return 0

    term = re.compile(re.escape(args.query), re.I)
    total = 0
    for label, path in files:
        hits = [(loc, text) for loc, text in load(path, args.rebuild) if term.search(text)]
        if not hits:
            continue
        total += len(hits)
        print(f"\n{path.relative_to(ROOT)}  [{label}] — {len(hits)} hit(s)")
        for loc, text in hits[:args.context]:
            print(f"    {loc}: {snippet(text, term)}")
        if len(hits) > args.context:
            print(f"    … {len(hits) - args.context} more (use --context)")

    print(f"\n{total} hit(s) across {len(files)} files."
          if total else f"\nNothing found for {args.query!r}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
