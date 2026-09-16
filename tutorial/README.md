# DAT158 — A self-study tutorial

A companion for **DAT158 Maskinlæring og vidaregåande algoritmer** (HVL, 10
studiepoeng). Built to run *alongside* the lectures, not to replace them.
Budget **2–4 hours per week**.

The course alternates between two halves, so the tutorial does too:
`ml01`, `ml02`, … track the machine-learning weeks, `alg01`, `alg02`, … the
algorithms weeks. They are independent — work whichever half the week is.

---

## How to use this

Every week is a folder with the same three things:

| File | What it is |
|---|---|
| `LESSON.md` | Read first. Concepts, worked examples, paper drills, a checklist. |
| `exercises.py` | Stubs to fill in. Every `todo()` is a task. |
| `tests.py` | The checks. You don't edit this. |
| `solutions/<week>/` | Reference answers + `PAPER.md`. Open **after** you've tried. |

The loop:

```bash
cd tutorial

./check.py ml01              # run ML week 1 against your answers
./check.py ml1               # the zero is optional
./check.py ml01 --solution   # run them against the reference
./check.py ml01 --quiet      # only show what isn't passing yet
./check.py --list            # what exists, and how far you are
```

Unimplemented stubs report as `todo`, not `FAIL`, so you can do one exercise at
a time and watch the count climb. Exit status is 0 only when everything passes.

**No new dependencies.** The harness is one stdlib-only file (`lib/check.py`).
numpy is the only import in the ML weeks, and it's already in the venv.
No pytest, nothing to install.

### The two feedback loops

1. **The tests** — instant, mechanical, correctness only.
2. **Me** — when a week is green, ask for a review. The tests cannot tell you
   that your 12-line loop should have been three lines of numpy, or that you
   computed precision where the question wanted recall and got lucky on the
   data. That gap is most of the difference between a C and an A.

---

## The weeks

| Week | Source | Topic | Checks |
|:--:|:--:|---|:--:|
| `ml01` | uke 34 · `1-intro`, `2-python` · HOML 1 | What ML is, numpy, first model | 54 |
| `ml02` | uke 36 · `3-metrics`, `4-ml-engineering` · HOML 3 | Confusion matrix, precision/recall, ROC, cross-validation | 61 |
| `alg01` | uke 35 · G&T ch. 9 | Pattern matching, tries, Huffman, LCS | 76 |

**191 checks across three weeks.** Every week has been verified green against a
working implementation, so a failing check is very likely you, not the test.

### Why no sklearn in the ML weeks

You implement the confusion matrix, precision, recall, ROC points and k-fold
yourself. Not because the library is bad — because **the exam is four hours,
written, with no aids**. `sklearn.metrics` will not be in the room; the ability
to derive precision from four numbers will. Once the checks are green, compare
yours against sklearn and confirm they agree.

### Why `alg01` has no reference solution

The compulsory exercise **Algorithms number 1** (due 4 September) asks you to
implement Boyer-Moore and both LCS versions in Python — exercises 3, 11 and 12
of that week. Shipping worked code for those before the deadline would be
handing you the assignment rather than teaching you.

The 76 checks are the feedback loop instead: they tell you *when* you're right
without telling you *what to write*. The test data is deliberately different
from the assignment's, so you learn the algorithm here and apply it there.

`PAPER.md` is present — it covers concepts, not the assignment's problems.
Ask me for a reference solution after the deadline.

---

## What this is not

- **Not a replacement for the lectures.** It follows them.
- **Not the weekly exercises.** Those are the lecturer's notebooks in
  `../weeks/ukeNN-ml/exercises/`, and they cover more ground. This is a third
  track: small, mechanical, and checkable in a way notebooks are not.
- **Not the assignments.** Those live in `../assignments/`.

---

## Where things live

```
tutorial/
  README.md          this file
  check.py           the runner
  lib/check.py       the harness (don't edit)
  ml01/  ml02/       LESSON.md, exercises.py, tests.py
  alg01/
  solutions/
    ml01/  ml02/     exercises.py + PAPER.md
    alg01/           PAPER.md only — see above
```

The repo's other folders stay yours: `../weeks/ukeNN-xx/code/` for code written
in class, `../assignments/` for graded work, `../scratch/` for experiments.

---

## Not yet built

`ml03`+ (module 2: models) and `alg02`+ (W&S ch. 1–2, NP-completeness) arrive
when their weeks do — uke 37 is the next algorithms week, uke 39 the next ML
one. Ask and I'll build the next one.

## If you get stuck

1. Read the exercise comment again. The specification is usually complete, and
   most failures are a misread rather than a missing idea.
2. Run `./check.py <week> --quiet` to see only what's still red.
3. Print the shapes. In the ML weeks, most confusion is a shape confusion.
4. Ask me. Paste your function *and* the failing check.

The habit worth building: **when a check fails, predict what the output will be
before you print it.** If your prediction is right, the bug is in your
understanding of the spec; if it's wrong, the bug is in the code. That tells you
where to look, and it is the difference between debugging and guessing.
