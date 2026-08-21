# Machine Learning half

Weeks 34, 36, 39, 40, 43, 44, 47 — `../weeks/*-ml/`

## Modules

| Module | Weeks | Topic | HOML chapters |
|--------|-------|-------|---------------|
| 1 | 34, 36 | Introduksjon til maskinlæring | **1, 2, 3** |
| 2 | 39, 40 | Maskinlæringsmodeller | 4, 6, 7 (likely) |
| 3 | 43, 44 | End-to-end maskinlæringssystem | 2 revisited |
| ? | 47 | TBA | — |

**The examinable ML curriculum is HOML chapters 1, 2, 3, 4, 6, 7 and
Appendix A** — from the lecturer's curriculum document
([`../docs/canvas/files/FinalCurriculum_2025.pdf`](../docs/canvas/files/FinalCurriculum_2025.pdf),
2025 edition; a 26H version has not appeared yet).

Note what is **not** on it: chapter 5 (SVMs), chapters 8–9, and all of Part II.
Module 1 accounts for 1–3, so chapters 4, 6 and 7 must fall in module 2.

Module 1's chapter list is confirmed from the Canvas module page — it is
chapters **1, 2 and 3**, not chapter 1 alone as originally guessed here. That
front-loads the two most important chapters in the book, so do not treat these
first weeks as a gentle warm-up.

Chapter 1 is [free to read online](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/ch01.html).

### Module 1 learning objectives

Straight from Canvas:

- Understand basic concepts in ML, and recognise when ML is a good — or bad —
  choice for a task
- Understand the elements of a complete software product built around ML
- Be able to use libraries to train a model and make predictions on simple
  datasets

## Exercises live on GitHub, not in Canvas

> *"Oppgaver ligger ute under kursets GitHub-side"*

**https://github.com/HVL-ML/DAT158** — the lecturer's repo holds the weekly
exercises and the library install instructions. The final project is expected
to be delivered as a publicly accessible repo.

Cloned to `../reference/DAT158/` (gitignored). Module 1's exercises are
already there:

```
notebooks/DAT158-1.1-Simple_examples.ipynb          notebooks/DAT158-1.4-Multiclass_classification.ipynb
notebooks/DAT158-1.2-Intro_to_ML.ipynb             notebooks/DAT158-1.5-Regression.ipynb
notebooks/DAT158-1.3-Binary_classification.ipynb   notebooks/DAT158-1.6-Hyperparameter_optimization.ipynb
```

Refresh it weekly with `git -C ../reference/DAT158 pull`.

**Work on a copy in `../weeks/ukeNN-ml/exercises/`, never in `reference/`.**
Editing in place means the next `git pull` wipes your answers, and it keeps
them out of the version-controlled part of this repo.

Copying the `.ipynb` alone is not enough. The notebooks read `data/`,
`assets/` and `solutions/` as siblings, so a lone notebook fails the moment
1.5 reaches `data/vehicles/` or 1.3 tries to `%load` its solution. Module 1 is
already set up in [`../weeks/uke34-ml/exercises/`](../weeks/uke34-ml/exercises/):
the six notebooks and `utils.py` are real copies, and those three directories
are symlinks back into `reference/`. Your edits are versioned; the 1.6 MB of
course data is not, and it updates itself on the next pull.

To do the same for a later module:

```bash
cd weeks/ukeNN-ml/exercises
cp ../../../reference/DAT158/notebooks/DAT158-N.*.ipynb .
cp ../../../reference/DAT158/notebooks/utils.py .
for d in data assets solutions; do
    ln -sfn ../../../reference/DAT158/notebooks/$d $d
done
```

The symlinks dangle until `reference/DAT158` exists, so re-clone it first if you
have rebuilt this repo from scratch.

## Where the slides really live

The Canvas front page links two decks. The published site
(https://hvl-ml.github.io/DAT158/) indexes the same two. **Both undersell what
is actually online** — every deck for the whole course is already served, just
unlinked, and reachable by URL:

| Module | Decks at `hvl-ml.github.io/DAT158/slides/…` |
|--------|---------------------------------------------|
| 1 — Introduction | `1-intro/1-intro`, `1-intro/2-python`, `1-intro/3-metrics`, `1-intro/4-ml-engineering` |
| 2 — Models | `2-models/lecture1` … `lecture4` |
| 3 — Systems | `3-systems/lecture1` … `lecture3` |
| 4 — Repetition | `4-repetition/lecture1` |

Plus two interactive widgets used by the metrics lecture:
`1-intro/roc_curve.html` and `1-intro/classification_threshold.html`.

Module 1's remaining two cover metrics (confusion matrix, precision/recall,
thresholds, ROC) and ML engineering (cross-validation, train/val/test, serving
a model with Gradio or Streamlit). Both mention **Assignment 1**.

### Read them, but do not trust them yet

The source is the `lectures` branch of the course repo — not `main`, which only
carries the notebooks:

```bash
git -C ../reference/DAT158 fetch origin lectures
git -C ../reference/DAT158 log --oneline FETCH_HEAD
```

That log is the honest record of what is current. Everything beyond
`1-intro`/`2-python` arrived in one bulk commit on 18 August whose contents
date to **November 2025 — last year's edition**. The lecturer revises a deck
in the days around teaching it (`1-intro` was touched on the 19th and again on
the 21st). So the later decks are a genuine preview of where the course goes,
and a poor guide to what will actually be said.

Nothing beyond module 1's first two decks is mirrored into `../weeks/` for that
reason: a stale copy in a week folder reads as authoritative and is not. Mirror
one when Canvas assigns it to a week.

### If you mirror one by hand

The decks reference `../../site_libs/...`, so a deck must sit two directories
below a copy of `site_libs/` — which is why `2-python.html` lives in
`../weeks/uke34-ml/slides/1-intro/` and not beside `1-intro.html`.

`1-intro.html` is the exception: it was mirrored before the lecturer's 21 August
rebuild, when paths carried a redundant `1-intro_files/` prefix that made the
flatter location work. Its content matches the live version exactly — only the
asset paths differ — so it is left alone.

Note also that `../weeks/uke34-ml/slides/lecture3.html` is `3-systems/lecture3`,
i.e. **module 3** material that landed in uke 34 only because Canvas's front
page happened to link it. It is not a uke 34 lecture.

## Textbook

**Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow**, Aurélien
Géron, **3. utg., O'Reilly, 2022** (xxv + 834 pages). Confirmed on the 2026/27
reading list, which says the ML half *"vil ta utgangspunkt i boken til Aurélien
Geron"*. Chapter-by-chapter notes:
[`book-homl/chapter-map.md`](book-homl/chapter-map.md).

**You can read it online for free.** The reading list marks it *"Tilgjengelig
fra Høgskulen på Vestlandet"* with a *"Les online"* link — HVL has a licence.
Go through Canvas → *Pensum/Litteratur* rather than buying a copy.

Official notebooks are cloned to `../reference/handson-ml3/` (Apache 2.0).

> **A warning about those notebooks.** Every chapter notebook contains the
> solutions to that chapter's exercises. They are one scroll away. Reading a
> solution before you have struggled with the problem feels like learning and
> is not. Attempt first, get stuck properly, then look.

## Environment

The `.venv` at the repo root covers all of HOML Part I (chapters 1–9,
scikit-learn). See `../docs/tensorflow-note.md` for Part II.

## Links

Add ML-specific links here — lecturer's repos, tutorials, videos.

| Link | What it is |
|------|------------|
| https://github.com/ageron/handson-ml3 | Official book notebooks |
| https://scikit-learn.org/stable/user_guide.html | scikit-learn user guide — genuinely well written |
| https://scikit-learn.org/stable/auto_examples/ | Worked examples with plots |
