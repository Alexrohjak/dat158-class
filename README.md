# DAT158-1 26H — Maskinlæring og vidaregåande algoritmer

HVL, autumn 2026. Everything for this subject lives here.

Canvas: https://hvl.instructure.com/courses/35853

## Start working

```bash
cd ~/code/dat158-class
source .venv/bin/activate     # every new terminal
jupyter lab                   # opens in the browser
```

Verify the environment: `python src/check_setup.py`. Leave it with `deactivate`.

## Semester plan

The course alternates whole weeks between the two halves. Week numbers are ISO
weeks, matching Canvas.

| Uke | Dates | Del | Tema | Folder |
|-----|-------|-----|------|--------|
| 34 | 17.–23. aug | ML | Modul 1: Introduksjon (HOML 1–3) | [`uke34-ml`](weeks/uke34-ml/) |
| 35 | 24.–30. aug | Alg | Tekstprosessering (G&T kap. 9) | [`uke35-alg`](weeks/uke35-alg/) |
| 36 | 31. aug–6. sep | ML | Modul 1: Introduksjon (HOML 1–3) | [`uke36-ml`](weeks/uke36-ml/) |
| 37 | 7.–13. sep | Alg | NP-completeness, Chapter 1 | [`uke37-alg`](weeks/uke37-alg/) |
| 38 | 14.–20. sep | Alg | Chapter 2 | [`uke38-alg`](weeks/uke38-alg/) |
| 39 | 21.–27. sep | ML | Modul 2: Maskinlæringsmodeller | [`uke39-ml`](weeks/uke39-ml/) |
| 40 | 28. sep–4. okt | ML | Modul 2: Maskinlæringsmodeller | [`uke40-ml`](weeks/uke40-ml/) |
| 41 | 5.–11. okt | Alg | Chapter 3 & 4 | [`uke41-alg`](weeks/uke41-alg/) |
| 42 | 12.–18. okt | Alg | *(TBA)* | [`uke42-alg`](weeks/uke42-alg/) |
| 43 | 19.–25. okt | ML | Modul 3: End-to-end maskinlæringssystem | [`uke43-ml`](weeks/uke43-ml/) |
| 44 | 26. okt–1. nov | ML | Modul 3: End-to-end maskinlæringssystem | [`uke44-ml`](weeks/uke44-ml/) |
| 45 | 2.–8. nov | Alg | Chapter 6 & 7 | [`uke45-alg`](weeks/uke45-alg/) |
| 46 | 9.–15. nov | Alg | *(TBA)* | [`uke46-alg`](weeks/uke46-alg/) |
| 47 | 16.–21. nov | ML | *(TBA)* | [`uke47-ml`](weeks/uke47-ml/) |
| — | — | — | **Eksamen: TBA** | [`exam/`](exam/) |

7 ML weeks, 7 Alg weeks. Plan is updated during the semester — re-check Canvas
and update this table when it changes.

## Where things go

| I have… | It goes in… |
|---|---|
| A lecture slide deck | `weeks/ukeNN-xx/slides/` |
| Notes from a lecture | `weeks/ukeNN-xx/notes.md` |
| Code I wrote this week | `weeks/ukeNN-xx/code/` |
| A weekly exercise | `weeks/ukeNN-xx/exercises/` |
| A graded assignment | `assignments/` |
| A useful link | `resources/links.md`, or `ml/` / `alg/` if it's half-specific |
| A dataset | `data/raw/` — and log it in `data/README.md` |
| Revision material | `exam/` |
| A half-formed idea | `scratch/` — no rules there |

## The two halves

- **[`ml/`](ml/)** — Machine Learning. Textbook is HOML; see
  [`ml/book-homl/chapter-map.md`](ml/book-homl/chapter-map.md).
- **[`alg/`](alg/)** — Advanced Algorithms. Textbook is Goodrich & Tamassia
  (edition still unconfirmed); see [`alg/README.md`](alg/README.md).

Week folders are tagged `-ml` or `-alg`, so:

```bash
ls weeks/*-ml      # every ML week
ls weeks/*-alg     # every algorithms week
grep -ri "overfitting" weeks/    # search all your notes
```

## Reference material

`reference/handson-ml3/` holds the official HOML notebooks (Apache 2.0, cloned
from github.com/ageron/handson-ml3). All 28 chapter notebooks plus two bonus
maths primers. Gitignored — it's a public repo, re-clone it anywhere:

```bash
git clone https://github.com/ageron/handson-ml3.git reference/handson-ml3
```

Note: the book's *text* is not in there and is not free. The *code* is.

## Environment

Python 3.14 + numpy, pandas, scikit-learn, matplotlib, seaborn, JupyterLab.
Covers all of HOML Part I. TensorFlow has no Python 3.14 build yet — see
[`docs/tensorflow-note.md`](docs/tensorflow-note.md). Not a problem before
ML modul 3 at the earliest.

## Repo rules

- **Private repo.** Lecture slides are the lecturer's copyright. Do not make
  this public, and do not push anything you'd be uncomfortable sharing.
- `data/`, `models/`, `.venv/` and `reference/` are gitignored — generated or
  re-downloadable, not source.
- Commit at the end of each week. `git add -A && git commit -m "uke NN"`.

## Syncing from Canvas

Canvas is the source of truth, and it changes weekly. `src/canvas_sync.py`
mirrors it into this repo — read-only, GETs only, it never submits or changes
anything on Canvas.

```bash
python src/canvas_sync.py              # refresh docs/canvas/course.md
python src/canvas_sync.py --download   # also pull new PDFs into weeks/*/slides/
```

Needs a Canvas API token in `.env` (gitignored — see `.env.example`). Generate
one at *Account → Settings → + New Access Token*.

Output lands in [`docs/canvas/course.md`](docs/canvas/course.md) — a flattened
mirror of every module page, announcement and assignment. **Don't edit it by
hand**; re-run the script. Your own writing goes in `weeks/*/notes.md`.

Three things the API cannot reach, because they are LTI external tools:
**Pensum/Litteratur**, **Panopto** and **Zoom**. Open those in a browser.
The course Files area is also blocked for students (403) — the script finds
files by scanning page links instead, so an uploaded-but-unlinked file stays
invisible until the lecturer links it.

## Exercises are on GitHub

The ML half's exercises are **not** in Canvas. They live in the lecturer's repo:

**https://github.com/HVL-ML/DAT158**

The final project is expected to be delivered as a publicly accessible repo.

## Where are we?

```bash
python src/week.py          # current week + what is filed so far
python src/week.py --all    # whole semester
```

Future weeks are never reported as missing. If a week is empty, the material
almost certainly is not published yet.
