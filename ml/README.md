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

Clone it somewhere outside this repo and copy work into
`../weeks/ukeNN-ml/exercises/` as you go, or add it as a second remote — but
keep your own solutions in this repo, since that one will be updated.

## Textbook

**Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow**, Aurélien
Géron, 3rd ed. (O'Reilly, 2022). Chapter-by-chapter notes:
[`book-homl/chapter-map.md`](book-homl/chapter-map.md).

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
