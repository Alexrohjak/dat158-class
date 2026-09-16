# The weekly routine

DAT158 alternates whole weeks between its two halves — seven ML weeks, seven
algorithms weeks. So there is no "do a bit of both": each week is one subject,
and the week's job is to close that subject's loop before the next one starts.

Two lectures a week (**Wednesday** and **Friday**), a lab **Wednesday 12:15**,
and 2–4 hours of your own on the tutorial. That is the whole commitment.

Four obligatory exercises gate the exam. The exam itself is **8 December,
09:00, four hours, written, no aids** — which is why so much of the practice
below is on paper.

---

## The week at a glance

| When | What | Command |
|---|---|---|
| **Monday** | Orient — which half, what's due | `python src/week.py` |
| Monday | Pull anything new from Canvas | `python src/canvas_sync.py` |
| **Wednesday** | Lecture, then lab 12:15 | — |
| Wednesday pm | Re-sync; file code written in class | `python src/canvas_sync.py` |
| **Friday** | Lecture | — |
| Friday pm | Re-sync | `python src/canvas_sync.py` |
| **Two evenings** | The tutorial — the actual learning | `cd tutorial && ./check.py <week>` |
| **Sunday** | Commit the week; ask for the next tutorial week | `git add -A && git commit -m "uke NN"` |

---

## 1. Monday — orient (5 minutes)

```bash
cd ~/code/dat158-class
python src/week.py
```

Tells you the ISO week, which half it is, what has been filed so far, and what
is due. Then:

```bash
python src/canvas_sync.py
```

Read-only — it GETs from Canvas and never submits anything. New slide decks land
in `weeks/ukeNN-xx/slides/`, an assignment brief lands in `assignments/`, and
each week folder's `README.md` is regenerated to record what was posted.

If `week.py` shows a week as empty, the material almost certainly is not
published yet. Future weeks are never reported as missing.

## 2. Wednesday — lecture, then lab

The slides are already in `weeks/ukeNN-xx/slides/` from Monday's sync. Open them
from there rather than from Canvas, so what you annotate is what you keep.

**The lab at 12:15 is the highest-value hour of the week** and the one most
easily wasted. Arrive with specific stuck points, not "I'm behind". The tutorial
is what generates specific stuck points — which is the argument for doing it
*before* the lab where the calendar allows.

Code written in class goes in `weeks/ukeNN-xx/code/`. Scratch experiments go in
`scratch/`, which has no rules.

## 3. Friday — lecture

Same again. Re-sync afterwards; the lecturer often posts the deck after
speaking, not before.

## 4. Two evenings — the tutorial

This is where the learning actually happens. Per week, in order:

1. **Read `LESSON.md`.** Concepts and worked examples, 20–30 minutes.
2. **Do the paper drills.** Actual paper. The exam has no computer, and the
   algorithms assignments are mostly hand-drawn tries, tables and traces.
3. **Fill in `exercises.py`.** Edit in place — that file is yours. Run
   `./check.py <week> --quiet` until nothing is left.
4. **Ask for a review once it is green.** The tests check correctness and
   nothing else. They cannot tell you that your twelve-line loop should have
   been three lines of numpy, or that you computed precision where the question
   wanted recall and got lucky on the data. That gap is most of the difference
   between a C and an A.

The loop in VS Code: edit, <kbd>Ctrl</kbd>+<kbd>S</kbd>, click the terminal,
<kbd>↑</kbd> <kbd>Enter</kbd>.

Unimplemented stubs report as `todo`, not `FAIL`, so you can do one exercise at
a time and watch the count climb.

## 5. Sunday — close the week

```bash
git add -A && git commit -m "uke NN"
```

Then ask me to build the next tutorial week. They are written one at a time,
against the slides the lecturer has actually posted, so `ml03` and `alg02` do
not exist until their weeks do.

---

## When an assignment appears

`canvas_sync.py` downloads the brief into `assignments/` automatically. Your
work sits flat beside it, named after the assignment —
`assignment1.py`, `assignment1-answers.md`, and an `assignment1-notes.md`
saying what is required and what you have done.

Assignments are groups of up to three. The tutorial week that matches the
assignment's material is the preparation for it: learn the algorithm on the
tutorial's data, then apply it to the assignment's. Do not do it the other way
round — you will end up debugging the assignment instead of understanding the
algorithm.

## Revision, later

```bash
python src/find.py tries
```

Searches the week records, the Canvas mirror, both textbooks, every slide deck,
every exercise notebook and every assignment brief, and reports the page or cell
so you can go straight there. `grep` only reads the markdown; the lecture
content is in PDFs and notebooks, which is what you actually want in December.

## What to ask me for

- **A review** when a tutorial week goes green — the second feedback loop.
- **The next tutorial week** when a new week's slides land.
- **A walkthrough** of anything in a `LESSON.md` that did not land.
- **A reference solution for `alg01`** — after the 4 September deadline.
- **Exam drilling** from November, once there is enough material to drill.

---

## The three tracks, kept separate

| Track | Where | Whose |
|---|---|---|
| Lecture material and in-class code | `weeks/ukeNN-xx/` | the lecturer's |
| Self-study exercises | `tutorial/ukeNN/exercises.py` | mine, for you |
| Graded work | `assignments/NN-name/` | counts |

They do not overlap, and nothing you write in one belongs in another. The full
"where does this file go" table is in the [repo README](../README.md).
