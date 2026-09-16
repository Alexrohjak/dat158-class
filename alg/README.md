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

## The tutorial track

[`../tutorial/alg01/`](../tutorial/alg01/) covers uke 35's text processing —
brute force, Boyer-Moore, KMP, tries, Huffman and LCS, with 76 checks.

Three of those are what **Algorithms number 1** asks you to implement, so the
tutorial ships **without** a reference solution until the deadline has passed;
the test data differs from the assignment's on purpose. Learn the algorithm
there, apply it to the assignment's own strings.

## Textbooks

Canvas → *Pensum/Litteratur* lists **one** book for this half, for 2026/27:

> Williamsen & Shmoys, The Design of Approximation Algorithms,
> Gratis på: http://www.designofapproxalgs.com/

(That "Williamsen" is the reading list's own typo — the author is **Williamson**.)

Goodrich & Tamassia is **not** on the official reading list. The lecturer posts
its chapter 9 directly instead, so treat it as supplied material rather than a
book you are expected to own.

The per-chapter breakdown below comes from `Curriculum DAT158 Algorithm part`
([`../docs/canvas/files/FinalCurriculum_2025.pdf`](../docs/canvas/files/FinalCurriculum_2025.pdf)),
which is the **2025** document — the books are confirmed for 26H, the exact
sections are not. Re-check when this year's curriculum appears.

### 1. Williamson & Shmoys — *The Design of Approximation Algorithms*

The main text, and the one behind almost every "Chapter N" in the plan.

**Free and legal:** the authors publish the full book at
https://www.designofapproxalgs.com/book.pdf (2.3 MB). No need to buy it.

Already downloaded to
`../reference/williamson-shmoys-design-of-approximation-algorithms.pdf`
(gitignored — re-fetch with the command in the root README).

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

**Not on the reading list.** Used for **chapter 9 only** (Text Processing,
uke 35), and the lecturer posts the chapter itself, so there is nothing to buy:
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
