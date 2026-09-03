# Algorithms number 1

**Due 4. september 2026, 23:59** (Canvas stores it as 21:59:59 UTC).
Groups of **at most three**. Pass/fail — does not count toward the final grade,
but it is one of the four compulsory exercises that gate the exam.

Brief: [`Compulsory_1.pdf`](Compulsory_1.pdf). Source material: uke 35,
Goodrich & Tamassia ch. 9, slides in [`../weeks/uke35-alg/slides/`](../weeks/uke35-alg/slides/).

Lecturer: Sven-Olai Høyland.

---

## The nine problems

| # | What | Kind | Tutorial prep | Done |
|---|---|---|---|:--:|
| 1 | Brute force on `"aaabaadaabaaa"` / `"aabaaa"` — draw the comparisons, count them | paper | `alg01` ex. 1 | **done** |
| 2a | Same figure and count for Boyer-Moore | paper | ex. 2–3 | **done** |
| 2b | Implement BM in Python, run on Norwegian text, compare against ~0.24 comparisons/char | **code** | ex. 3 | **done** |
| 3 | Same figure and count for KMP | paper | ex. 4–5 | **done** |
| 4 | Nonempty prefixes of `"aaabbaaa"` that are also suffixes — how many? | paper | ex. 6 | **done** |
| 5 | Standard trie for 8 given strings | paper | ex. 7 | **done** |
| 6 | Compressed trie for the same set | paper | ex. 8 | **done** |
| 7 | Frequency table + Huffman tree for `"dogs do not spot hot pots or cats"` | paper | ex. 9–10 | **done** |
| 8 | LCS of `"babbabab"` / `"bbabbaaab"` by dynamic programming | paper | ex. 12 | **done** |
| 9 | LCS recursively **and** dynamically in Python; find where the recursion blows up | **code** | ex. 11–12 | **done** |

Six on paper, three in Python. The tutorial's `alg01` covers every one of them on
*different* data — learn the algorithm there, apply it here.

---

## Things to decide before you write

**Problem 2a and 3 — what counts.** The brief says explicitly: do not count the
comparisons used to build the last-occurrence function or the failure function.
One comparison = one evaluation of `T[i] == P[j]`, and the test that *fails*
still counts. Same rule as the tutorial.

**Problem 2b — how to measure over a whole text.** "Comparisons per text
character" is only meaningful if the search scans the text. A matcher that stops
at the first hit two characters in gives a ratio that means nothing. Decide, and
state in your answer, whether you are searching for all occurrences, running on
patterns that do not occur, or averaging over many random 5-character patterns.
The 0.24 figure is for a **five-character** pattern — match that.

You also need a Norwegian text of reasonable length. Anything public-domain and
plain-text works; say in the answer what you used and how long it is.

**Problem 4 — state your reading.** The brief says "nonempty prefixes", not
"nonempty *proper* prefixes". `"aaabbaaa"` is trivially both a prefix and a
suffix of itself. Say which reading you took; either is defensible, silence is
not.

**Problem 7 — the spaces are characters.** `"dogs do not spot hot pots or cats"`
contains spaces, and they go in the frequency table like anything else. Dropping
them is the most common way this problem goes wrong. Also: ties in the Huffman
construction are not resolved by the algorithm, so a different-looking tree can
be equally correct — what is invariant is the total encoded length.

**Problem 9c — "approximately at what point".** Time both versions on strings of
growing length and report where the recursive one becomes unusable. Give the
numbers you measured, not just a claim.

---

## Layout

```
assignments/
  Compulsory_1.pdf          the brief — downloaded by canvas_sync.py, don't rename
  assignment1-notes.md      this file: what's required, what's done
  assignment1-answers.md    the written answers
  assignment1.py            the Python for problems 2b and 9
```

Hand-drawn figures for 1, 2a, 3, 5, 6, 7 and 8 can be photographed and included,
or redrawn — check what Canvas accepts before the deadline.

## Submission

Canvas → Oppgåver → *Algorithms number 1*. Confirm the accepted file types and
whether the group is registered in Canvas before uploading.
