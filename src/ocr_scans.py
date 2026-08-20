"""Give scanned PDFs a text layer, so src/find.py can search them.

    python src/ocr_scans.py --list     # which files need it
    python src/ocr_scans.py            # OCR them
    python src/ocr_scans.py --lang nor # for Norwegian scans

Some course material arrives as images of pages rather than text — a photocopied
textbook chapter, for instance. Those pages are invisible to search: `find.py`
reports them under "no text layer". This runs OCR over them and writes the
recognised text back into the same PDF, leaving the page images untouched. The
file still looks identical; it just becomes searchable.

Needs ocrmypdf and tesseract, which are system packages:

    sudo apt install ocrmypdf tesseract-ocr tesseract-ocr-nor

Originals are replaced in place. That is safe here — everything under
`weeks/*/slides/` came from Canvas and `canvas_sync.py` will not re-download a
file that already exists, so nothing gets clobbered on the next sync. If OCR
fails the original is left exactly as it was.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from paths import ROOT

# Where scanned course material plausibly lives.
SEARCH = ["weeks/*/slides/*.pdf", "docs/canvas/files/*.pdf", "reference/*.pdf"]


def has_text_layer(path: Path) -> bool:
    """True if any page yields extractable text."""
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pypdf is not installed — run: pip install pypdf cryptography")
    try:
        reader = PdfReader(str(path))
    except Exception:
        return True  # unreadable for other reasons; not our problem to fix
    for page in reader.pages:
        try:
            if (page.extract_text() or "").strip():
                return True
        except Exception:
            continue
    return False


def already_ocred(path: Path) -> bool:
    """True if this file's OCR text is already sitting in find.py's cache.

    Without this, --list keeps reporting an OCR'd scan as needing work — the
    PDF genuinely has no text layer, but the text has been recovered, and
    redoing 36 pages achieves nothing.
    """
    import find
    cp = find.cache_path(path)
    if not cp.exists():
        return False
    try:
        blob = json.loads(cp.read_text())
    except Exception:
        return False
    stat = path.stat()
    return (blob.get("ocr") is True
            and blob.get("stamp") == f"{int(stat.st_mtime)}:{stat.st_size}"
            and bool(blob.get("units")))


def scans() -> list[Path]:
    found: list[Path] = []
    for pattern in SEARCH:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file() and not has_text_layer(path):
                found.append(path)
    return found


def ocr(path: Path, lang: str) -> str:
    """OCR one PDF in place. Returns a status string for the report."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / path.name
        cmd = [
            "ocrmypdf",
            "--language", lang,
            "--rotate-pages",      # scans are often sideways
            "--deskew",            # and rarely straight
            "--optimize", "1",
            "--quiet",
            str(path), str(out),
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        except FileNotFoundError:
            sys.exit(
                "ocrmypdf is not installed. Run:\n"
                "    sudo apt install ocrmypdf tesseract-ocr tesseract-ocr-nor"
            )
        except subprocess.TimeoutExpired:
            return "timed out after 30 min — original left alone"

        if proc.returncode != 0 or not out.exists():
            detail = (proc.stderr or proc.stdout or "").strip().splitlines()
            return f"failed ({detail[-1][:80] if detail else 'unknown'}) — original left alone"

        before = path.stat().st_size
        shutil.move(str(out), str(path))
        after = path.stat().st_size
        return f"ok ({before // 1024} KB -> {after // 1024} KB)"


def ocr_to_cache(path: Path) -> str:
    """OCR without system packages, straight into find.py's cache.

    The PDF is left byte-identical — we rasterise each page with pdftoppm
    (poppler, already present), read it with a pip-installed ONNX OCR engine,
    and write the recognised text where find.py looks for it. Ctrl+F in a PDF
    reader still will not work; `python src/find.py` will.

    This exists because writing a real text layer needs ocrmypdf and tesseract,
    which are system packages needing root. This route needs neither.
    """
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        return "rapidocr not installed — pip install rapidocr-onnxruntime"

    import find  # cache location and key format live there

    engine = RapidOCR()
    units: list[tuple[str, str]] = []

    with tempfile.TemporaryDirectory() as tmp:
        stem = Path(tmp) / "page"
        proc = subprocess.run(
            ["pdftoppm", "-r", "200", "-png", str(path), str(stem)],
            capture_output=True, text=True, timeout=900,
        )
        if proc.returncode != 0:
            return f"pdftoppm failed ({(proc.stderr or '').strip()[:60]})"

        images = sorted(Path(tmp).glob("page*.png"))
        for n, image in enumerate(images, 1):
            try:
                result, _ = engine(str(image))
            except Exception as exc:
                return f"OCR failed on page {n} ({str(exc)[:50]})"
            text = " ".join(line[1] for line in (result or []) if len(line) > 1)
            if text.strip():
                units.append((f"p.{n}", text))
            print(".", end="", flush=True)

    if not units:
        return "no text recognised"

    stat = path.stat()
    find.CACHE.mkdir(exist_ok=True)
    find.cache_path(path).write_text(json.dumps({
        "stamp": f"{int(stat.st_mtime)}:{stat.st_size}",
        "units": units,
        "ocr": True,
    }))
    words = sum(len(t.split()) for _, t in units)
    return f"ok ({len(units)}/{len(images)} pages, ~{words} words -> search cache)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="show what needs OCR, change nothing")
    ap.add_argument("--lang", default="eng+nor",
                    help="tesseract languages, e.g. eng, nor, eng+nor (default: eng+nor)")
    ap.add_argument("--force", action="store_true",
                    help="redo files whose text is already cached")
    ap.add_argument("--no-sudo", action="store_true",
                    help="OCR into find.py's cache instead of writing a PDF text layer; "
                         "needs no system packages")
    args = ap.parse_args()

    targets = scans()
    if not targets:
        print("Every PDF already has a text layer — nothing to do.")
        return 0

    done = [p for p in targets if already_ocred(p)]
    todo = [p for p in targets if p not in done]

    print(f"{len(targets)} PDF(s) without a text layer:")
    for path in targets:
        pages = ""
        try:
            from pypdf import PdfReader
            pages = f"{len(PdfReader(str(path)).pages)} pages, "
        except Exception:
            pass
        state = "  [text already recovered into the search cache]" if path in done else ""
        print(f"  {path.relative_to(ROOT)}  ({pages}{path.stat().st_size // 1024} KB){state}")

    if args.list:
        if todo:
            print(f"\n{len(todo)} still to do. Run without --list to OCR them.")
        else:
            print("\nAll of them are searchable already — nothing to do.")
        return 0

    if not args.force:
        targets = todo
    if not targets:
        print("\nAll already OCR'd. Use --force to redo them.")
        return 0

    if args.no_sudo:
        print("\nOCR into the search cache (no system packages, PDF unchanged).")
        print("Slow — a dot per page.\n")
        for path in targets:
            print(f"  {path.name} ", end="", flush=True)
            print(" " + ocr_to_cache(path))
        print("\nDone. Search it with: python src/find.py <term>")
        print("Note: find.py --rebuild would discard this; re-run this script if you do.")
        return 0

    print(f"\nOCR with --language {args.lang}. This is slow — minutes per file.\n")
    for path in targets:
        print(f"  {path.name} … ", end="", flush=True)
        print(ocr(path, args.lang))

    print("\nDone. Re-index with: python src/find.py --rebuild")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
