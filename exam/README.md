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

These gate the exam, so they matter more than their weight suggests (they are
pass/fail, and none published yet as of uke 34). Track them in
[`../assignments/`](../assignments/) with the deadline in each README.

## Revision

Both halves are examined. Keep the split visible:

- `ml-revision.md` — machine learning
- `alg-revision.md` — advanced algorithms

## Building revision notes as you go

The cheapest revision material is the one you already wrote. Each week's
`notes.md` has a "Questions I couldn't answer" section — those questions,
collected across 14 weeks, are your revision list. Do not start it in November.

## Past papers

**Canvas has a `Tidligere eksamener` folder** — confirmed to exist, containing
one file plus a subfolder named `Oppgaver_Uten_Losning` ("problems without
solutions").

The API cannot list it: students get a 403 on the course Files area, and the
Files tab is not in the course navigation. So `src/canvas_sync.py` will not
pull these automatically. Get at them by browsing Canvas directly, or ask the
lecturer for a link — once a file is linked from a page, the sync script picks
it up.

Drop whatever you retrieve in this folder.
