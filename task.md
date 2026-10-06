# task.md — DAT158

Every code change in this repo corresponds to a task here. Closed tasks stay,
struck through, so the record of what was built and why survives the semester.

This file started on a second clone of the repo, which went its own way from
19 Aug until 23 Sep. That clone's full history, including its earlier tasks
(T-001 to T-008), is on the branch `backup/this-machine-2026-09-23`.

## Now

### T-010 — uke 39: ML modul 2 starts
- [x] Canvas sync: the modul 2 page, the Kaggle competition (closes 1 Oct 23:59),
      and two more uke 38 problem sheets
- [x] Modul 2 notebooks in `weeks/uke39-ml/exercises/`, set up like modul 1's.
      2.1, 2.2 and 2.4 run clean. 2.3's traps are in `ml/README.md`
- [x] Lecture 5 mirrored to `weeks/uke39-ml/slides/2-models/`, renders offline
- [x] Drill room: uke 39 week (9 concepts, 3 demos), a "This week" card, a uke 39
      Start-here checklist, and V2025 Q12–Q17 + Q20 as Quick-fire 3
- [x] `sudo apt install graphviz` (23 Sep)
- [ ] Work notebooks 2.1 → 2.4, "Your turn!" cells first
- [x] Mirror lecture 6 (`6-decision-trees`) — done in the 30 Sep sync (T-011)
- [x] uke 40: drill-room week for gradient descent — done 30 Sep (T-011)
- [ ] Tutorial `ml03` for modul 2. None of it has tested exercises yet

### T-011 — uke 40: gradient descent
- [x] 30 Sep sync. GitHub was already up to date, and `reference/DAT158` had no
      new commits. Canvas posted lecture 6's and lecture 7's notes and a lecturer
      summary of uke 39
- [x] Lecture 6 mirrored to `weeks/uke39-ml/slides/2-models/`, and lecture 7 to
      `weeks/uke40-ml/slides/2-models/` with its own `site_libs/`
- [x] Notebooks 2.5 and 2.6 run clean. Their quirks are in `ml/README.md`,
      folded away, because the Work tab asks you to find them
- [x] Drill room: uke 40 week (7 concepts and a gradient-descent demo), the
      V2025 Q18–Q19 as Quick-fire 4, a uke 40 Start-here checklist, a lecture 6
      item in uke 39's checklist, and 4 new auto-marked questions
- [ ] Work notebooks 2.5 and 2.6, "Your turn!" cells first
- [x] Friday 2 Oct: re-sync, and mirror Friday's deck once Canvas links it — done
      in the 6 Oct sync (T-012): lecture 8, `8-linreg`

### T-012 — uke 41: a split week, and ML assignment 2
- [x] 6 Oct sync. GitHub was up to date, and `reference/DAT158` had no new
      commits. Canvas posted the uke 41 algorithms page (`Chapter_3.pdf`,
      `Problems_3.pdf`), the ML modul 3 page, the lecturer's uke 40 summary,
      and **ML assignment 2** with its two report templates
- [x] The semester plan changed: uke 41 is ML on Wednesday (moved, 7 Oct
      10–12) and algorithms on Friday (9 Oct 12–14). uke 43 is the mirror image.
      `PLAN` in `src/week.py` and the README table say so. Folder names stay
- [x] Lecture 8 mirrored to `weeks/uke40-ml/slides/2-models/`, and lecture 9
      (`9-ml-project-lifecycle`) to `weeks/uke41-alg/slides/3-systems/` with its
      own `site_libs/`, because that is the week it is taught. Both render offline
- [ ] **ML assignment 2, due Fri 30 Oct 23:59, 20 points.** A group of 2–3
      builds an ML-backed website: public GitHub repo, a report (templates in
      `assignments/`), and a live deployment or a screencast. Everyone submits
      the repo link individually. Find the group and pick the idea first
- [ ] Algorithms: `Problems_3.pdf` problems 2 and 6 are part of the next
      compulsory. No Canvas assignment or deadline for it yet
- [ ] Drill room: alg Chapter 3 week, and lecture 8 (linear regression,
      regularisation, learning curves) for the ML half

### ~~T-009 — Reconcile the two clones~~ — done 23 Sep
The other clone and `origin/main` had diverged from 4c16768: 10 commits there,
19 here, largely rebuilding the same things (Canvas mirror, tutorial) twice.
This line was kept as the base. From the other clone came:

- [x] Notebook 1.1 answers (the only student work that existed only there)
- [x] The drill room and the V2025 transcription (`exam/`)
- [x] uke 37 tutorial weeks → `tutorial/uke37-extra/`, 136 checks, own runner
- [x] `hyperopt` in requirements (notebooks 1.6 and 2.6 import it)
- [ ] Not carried: its `week.py --resume` (it read per-week `notes.md` files,
      which this line dropped). Revisit if re-entry after a gap proves hard.
- [ ] Delete `backup/this-machine-2026-09-23` once nothing is missed — after
      the uke 40 week, say

## Next

- [ ] Drill room: alg Chapter 3–4 (uke 41) when it is taught
- [ ] Revisit the drill format when the mid-November exam guide appears
