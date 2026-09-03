# Assignments (Oppgåver)

Graded coursework goes here, one folder per assignment.

Weekly practice exercises live in the relevant `weeks/ukeNN-xx/exercises/`
instead — this folder is for things that count.

## Published in Canvas

Both appeared in Canvas → Oppgåver between 21. aug and 2. sep. These are **real
deadlines**, not the proposed dates below.

| Due | What | Points | Brief |
|-----|------|--------|-------|
| **4. sep 2026, 23:59** | Algorithms number 1 | 0 — pass/fail | [`Compulsory_1.pdf`](Compulsory_1.pdf) |
| **11. sep 2026, 23:59** | ML assignment 1 | 20 | *none attached yet* |

Canvas stores both as 21:59:59 UTC — that is 23:59 Norwegian time.

### Algorithms number 1 — due 4. sep

Groups of **at most three**. Does not count toward the final grade, but it is
one of the four that gate the exam. Nine problems on Goodrich & Tamassia ch. 9,
the uke 35 material:

| # | Problem | Kind |
|---|---------|------|
| 1 | Brute-force pattern matching, `"aaabaadaabaaa"` / `"aabaaa"` — draw it, count comparisons | by hand |
| 2a | Same for Boyer-Moore | by hand |
| 2b | Implement BM in Python, run on Norwegian text, compare against the ~0.24 comparisons/char the theory predicts | **code** |
| 3 | Same as 2a for Knuth-Morris-Pratt | by hand |
| 4 | Nonempty prefixes of `"aaabbaaa"` that are also suffixes | by hand |
| 5 | Standard trie for a given set of 8 strings | by hand |
| 6 | Compressed trie for the same set | by hand |
| 7 | Frequency table + Huffman tree for `"dogs do not spot hot pots or cats"` | by hand |
| 8 | LCS of `"babbabab"` / `"bbabbaaab"` by dynamic programming | by hand |
| 9 | Implement LCS recursively **and** dynamically in Python; find where the recursive one blows up | **code** |

Three of the nine want Python. Put that code in `assignment1.py`.

The uke 35 slides are the direct source —
[`../weeks/uke35-alg/slides/`](../weeks/uke35-alg/slides/). The scanned textbook
chapter there has no text layer, so search it with `python src/find.py`, not
Ctrl+F.

### ML assignment 1 — due 11. sep

20 points, no brief attached in Canvas yet. This is almost certainly the quiz
the lecturer proposed for 11. sep (see below) — the dates match. Re-run the sync
as the date nears; if a brief gets attached it lands here automatically.

## Layout

Everything for one assignment sits flat in this folder, named after it:

    assignments/
      Compulsory_1.pdf          <- downloaded by src/canvas_sync.py, don't rename
      assignment1-notes.md      <- what's required, what you've done
      assignment1-answers.md    <- the written answers
      assignment1.py            <- the code

`python src/canvas_sync.py` fetches any brief attached to a Canvas assignment.
Canvas → Oppgåver stays the source of truth for deadlines.

## Still to come

Four obligatory exercises gate the exam; **two are now published**, so two are
outstanding. The algorithms half has published its first, which suggests the
remaining split is one more per half.

## Proposed dates (ML half)

From the lecture 2 slides, 21 August
([`../weeks/uke34-ml/slides/1-intro/2-python.html`](../weeks/uke34-ml/slides/1-intro/2-python.html)).
The lecturer called these **proposed** — only the 11. sep one has since turned
into a real Canvas deadline.

| Date | What | Mandatory? | Status |
|------|------|-----------|--------|
| 11. sep | Quiz — multiple choice, after ML module 1 | Yes | **in Canvas** as ML assignment 1 |
| 2. okt | Competition | **No** — optional | not in Canvas |
| 29. okt | Project hand-in, after ML module 3 | Yes | not in Canvas |

The project is delivered as a publicly accessible repo, and the lecturer
suggests starting early rather than waiting for module 3.

## Lab

Wednesdays 12:15 — work on the exercises and get help. Same slide deck.
