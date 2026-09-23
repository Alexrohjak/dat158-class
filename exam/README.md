# Exam

## 8 December 2026, 09:00

From the official course description, https://www.hvl.no/studier/studieprogram/emne/DAT158 —
**verify against Studentweb**, which is the authoritative source for time and room.

| | |
|---|---|
| **Date** | Tuesday 8 December 2026, 09:00 |
| **Form** | 4-hour written exam (skoleeksamen), on campus |
| **Language** | Questions in English; answer in Norwegian *or* English |
| **Aids** | **None** |
| **Grading** | A–F, F is fail |
| **Prerequisite** | Four obligatory exercises must be submitted by their deadlines and approved *before* you may sit the exam |

Both halves are examined, 5 studiepoeng each.

An **exam guide** is promised for **mid-November** — the lecturer says so in the
curriculum document. Watch for it.

### The four obligatory exercises

These gate the exam, so they matter more than their weight suggests. **Two of
the four are published** as of uke 36 — Algorithms number 1 (due 4. sep) and
ML assignment 1 (due 11. sep). Track all of them in
[`../assignments/`](../assignments/), which carries the deadlines and the
briefs.

## Revision

Both halves are examined. Keep the split visible:

- `ml-revision.md` — machine learning
- `alg-revision.md` — advanced algorithms

## Revision material

Four things, in order of usefulness:

1. **Past papers** — see below. V2025 is out. It's the closest thing to knowing the questions.
2. **The exercise notebooks** in `../reference/DAT158/notebooks/`, which have a
   `solutions/` folder. Working these is the ML half's revision.
3. **The slide decks** in `../weeks/*/slides/`, all archived offline. The exam
   is set from what was lectured.
4. **The exam guide** the lecturer promises for mid-November.

Since the exam allows **no aids**, recall matters — start before December.

## The drill room

[`interactive-revision.html`](interactive-revision.html). Open it in a browser
(`xdg-open exam/interactive-revision.html`), or use the private published copy
at <https://claude.ai/code/artifact/af4a67c4-2ea3-483d-ad36-a6b6af70aa06>,
which also works on a phone.

It has five modes: **Start here** (this week's checklist and a four-step
session routine), **Overview**, **Learn** (the concepts, with interactive
demos), **Drill** (answer before you see the model answer; exact answers are
marked by the page) and **Work** (paper exercises and the tutorial command).
It covers both halves, each with a V2025 past-exam week. Progress is kept in
`localStorage`, so it stays in that browser only.

**The published copy has been edited on its own before.** On 23 Sep it was
found ahead of this file. Before republishing, read the live version and merge
onto it, and add new weeks at the *end* of a half's list, because saved
progress is keyed by week position.

## Past papers

**V2025, questions only**, was posted on Canvas on 15 Sep 2026. The sync puts
it at [`../docs/canvas/files/V2025_Oppgaver_Uten_Løsning.pdf`](../docs/canvas/files/).
It is a printed WISEflow export with no text layer, so
[`V2025-questions.md`](V2025-questions.md) transcribes it verbatim, with no
answers added. It has 50 points of ML in 22 questions, and 20+ points of
algorithms (sections 3–5 are printed without points). The drill room's
past-exam weeks have model answers. Those answers are ours, not the lecturer's.

Earlier note: **Canvas has a `Tidligere eksamener` folder** containing one file plus a
subfolder `Oppgaver_Uten_Losning` ("problems without solutions"). As of
uke 34 **nothing in it was published to students**.

The API cannot list it either: students get a 403 on the course Files area, and
the Files tab is not in the course navigation. So `src/canvas_sync.py` will not
pull these automatically until the lecturer links them from a page — at which
point the sync picks them up on its own.

Worth asking the lecturer directly if they have not appeared by November. Drop
whatever you retrieve in this folder.
