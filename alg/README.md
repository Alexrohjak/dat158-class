# Advanced Algorithms half

Weeks 35, 37, 38, 41, 42, 45, 46 — `../weeks/*-alg/`

## Plan

| Uke | Topic | Book |
|-----|-------|------|
| 35 | Tekstprosessering | **G&T** ch. 9 |
| 37 | NP-completeness, Chapter 1 | slides + **W&S** ch. 1 |
| 38 | Chapter 2 | **W&S** ch. 2 |
| 41 | Chapter 3 & Chapter 4 | **W&S** ch. 3, 4 |
| 42 | TBA | |
| 45 | Chapter 6 & 7 | **W&S** ch. 6, 7 |
| 46 | TBA | |

The chapter numbers run 1, 2, 3 & 4, 6 & 7 *and* 9 because there are **two**
books. The low numbers are Williamson & Shmoys; chapter 9 is Goodrich &
Tamassia.

## Textbooks — there are two

Confirmed from `Curriculum DAT158 Algorithm part`, written by the lecturer and
linked from the Canvas front page. A copy is in
[`../docs/canvas/files/FinalCurriculum_2025.pdf`](../docs/canvas/files/FinalCurriculum_2025.pdf).

**Caveat: that document is the *2025* curriculum.** The lecturer has not yet
posted a 26H version. Treat it as a very strong indication, not gospel, and
re-check when this year's appears.

### 1. Williamson & Shmoys — *The Design of Approximation Algorithms*

The main text, and the one behind almost every "Chapter N" in the plan.

**Free and legal:** the authors publish the full book at
https://www.designofapproxalgs.com/book.pdf (2.4 MB). No need to buy it.

Chapters on the 2025 curriculum:

| Chapter | Scope |
|---------|-------|
| 1, 2, 3 | in full |
| 4 | 4.1, 4.3 — 4.3 only as stated in the lecture notes |
| 5 | 5.1, 5.5, 5.10, 5.12 |
| 6 | 6.1, 6.2, 6.5 |
| 7 | 7.1 |

Note the plan has no uke for chapter 5, yet four of its sections are examinable.
It is probably folded into one of the TBA weeks (42 or 46).

### 2. Goodrich & Tamassia — *Algorithm Design: Foundations, Analysis and Internet Examples*

Used for **chapter 9 only** (Text Processing, uke 35). The lecturer posted the
chapter itself, so you do not need the whole book:
[`../weeks/uke35-alg/slides/Kapittel_9_GoodrichAndTammassia.pdf`](../weeks/uke35-alg/slides/)

### Also examinable

- **NP-completeness** — from the lecture slides, not from either book
- **All exercises**

An exam guide is promised for **mid-November**.

### Lecturer

Sven-Olai Høyland — he authors both the slides and the curriculum document.

## Topics to expect

Based on the plan, this half covers classical algorithm theory rather than ML:

- **Approximation algorithms** — the core of the half. What to do when a
  problem is intractable: settle for provably-close-to-optimal, and prove how
  close. LP relaxation, rounding, greedy and primal-dual methods.
- **String / text processing** — pattern matching, tries, edit distance (ch. 9)
- **NP-completeness** — complexity classes, reductions, what "intractable"
  means. This is *why* the rest of the half exists.

Where the two halves meet: complexity analysis explains *why* some ML methods
don't scale. Worth noting when you spot the connection.

## Links

| Link | What it is |
|------|------------|
| [`../weeks/uke35-alg/slides/`](../weeks/uke35-alg/slides/) | Chapter 9 PDF + lecture slides, pulled from Canvas |
| https://hvl.instructure.com/courses/35853/modules | Canvas → Modular, where each week's page appears |
| https://www.designofapproxalgs.com/book.pdf | **Williamson & Shmoys, free full text** |
| https://www.designofapproxalgs.com/ | The book's homepage — errata and extras |
| [`../docs/canvas/files/FinalCurriculum_2025.pdf`](../docs/canvas/files/FinalCurriculum_2025.pdf) | Lecturer's curriculum document (2025) |
