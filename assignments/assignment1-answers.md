# Algorithms number 1 — answers

DAT158, autumn 2026. All nine problems.

Code: [`assignment1.py`](assignment1.py) — **problems 2b and 9 only**, the two
the brief asks to be written in Python. Run `python assignment1.py` to
reproduce their numbers. The other seven problems are done by hand.

Throughout, **one comparison means one test of "is this text character equal to
this pattern character".** A test that *fails* counts too — it is the test that
told us it failed. Building the last-occurrence table and the failure function
costs no comparisons, as the problem says.

---

## Problem 1 — Brute force

Text `"aaabaadaabaaa"` (13 characters), pattern `"aabaaa"` (6 characters).

Brute force slides the pattern along one position at a time and compares left
to right until it either runs out of pattern or hits a mismatch.

```
index    0123456789012
text     aaabaadaabaaa

i=0      aabaaa           a=a  a=a  a≠b                     3 comparisons
i=1       aabaaa          a=a  a=a  b=b  a=a  a=a  d≠a      6
i=2        aabaaa         a=a  b≠a                          2
i=3         aabaaa        b≠a                               1
i=4          aabaaa       a=a  a=a  d≠b                     3
i=5           aabaaa      a=a  d≠a                          2
i=6            aabaaa     d≠a                               1
i=7             aabaaa    a=a  a=a  b=b  a=a  a=a  a=a      6   MATCH
```

**The pattern is found at index 7, after 24 comparisons.**

Notice where the cost is. Most positions die after one comparison, but `i=1`
costs six — it matches five characters before failing. A pattern made almost
entirely of `a`s against a text made almost entirely of `a`s keeps *nearly*
matching, and that is exactly what makes brute force expensive.

---

## Problem 2a — Boyer-Moore

Boyer-Moore does two things differently. It compares the pattern **backwards**,
from the last character, and on a mismatch it uses the **last-occurrence table**
to jump forwards.

Last-occurrence table for `"aabaaa"` — the last position of each character:

| character | a | b |
|---|---|---|
| last index | 5 | 2 |

```
index    0123456789012
text     aaabaadaabaaa

step 1   aabaaa           compare T[5], T[4], T[3]        3 comparisons
                          T[3]='b' ≠ P[3]='a'
                          'b' is last at index 2, so line them up: shift 1

step 2    aabaaa          compare T[6]                    1 comparison
                          T[6]='d' ≠ P[5]='a'
                          'd' is not in the pattern at all: skip past it

step 3          aabaaa    compare T[12] down to T[7]      6 comparisons
                          all six match                              MATCH
```

**The pattern is found at index 7, after 10 comparisons.**

The big win is step 2. The character `'d'` does not appear in the pattern
anywhere, so no alignment containing it can ever match — Boyer-Moore skips a
whole pattern width in one go, from position 1 straight to position 7.

---

## Problem 2b — Boyer-Moore on Norwegian text

**Text:** Knut Hamsun, *Sult* (1890), from Project Gutenberg (#30027, public
domain). After removing the Gutenberg header and footer: **329 982 characters,
93 distinct symbols.**

**Method:** 50 random patterns per length, taken from the text itself so that
every pattern really occurs. Each search scans the *whole* text and finds *all*
occurrences — a search that stops at the first match has not scanned the text,
so "comparisons per character" would mean nothing.

| pattern length | Boyer-Moore | brute force |
|---:|---:|---:|
| 2 | 0.5628 | 1.0744 |
| 3 | 0.3982 | 1.0812 |
| 4 | 0.3072 | 1.0832 |
| **5** | **0.2580** | 1.0837 |
| 6 | 0.2158 | 1.0840 |
| 8 | 0.1732 | 1.0841 |
| 10 | 0.1444 | 1.0842 |
| 15 | 0.1090 | 1.0842 |
| 20 | 0.0889 | 1.0842 |

**Measured 0.2580 comparisons per character for a five-character pattern.
The theory predicts about 0.24.** That is about 7% higher, which is a good
match — and the 0.24 figure was measured on English, not Norwegian.

Two things the table shows:

- **Boyer-Moore looks at less than a third of the text.** Fewer than one
  comparison per character means it finishes having never looked at most of the
  characters at all.
- **Brute force is flat at about 1.08 whatever the pattern length**, while
  Boyer-Moore keeps improving. Brute force inspects essentially every character
  once, because on real text a mismatch nearly always comes on the very first
  character of the window. Boyer-Moore's skip gets longer as the pattern gets
  longer, so its cost falls roughly like `1/m`.

The 93-character alphabet is what makes this work: a mismatched character is
usually not in the pattern at all, so the jump is a full pattern width.

---

## Problem 3 — Knuth-Morris-Pratt

KMP never moves backwards in the text. On a mismatch it uses the **failure
function** to work out how much of the pattern it has already matched and can
keep.

`F[j]` is the length of the longest proper prefix of `P[0..j]` that is also a
suffix of `P[0..j]`. For `"aabaaa"`:

| j | `P[0..j]` | longest prefix that is also a suffix | F[j] |
|---|---|---|---|
| 0 | `a` | — | **0** |
| 1 | `aa` | `a` | **1** |
| 2 | `aab` | — | **0** |
| 3 | `aaba` | `a` | **1** |
| 4 | `aabaa` | `aa` | **2** |
| 5 | `aabaaa` | `aa` | **2** |

So `F = [0, 1, 0, 1, 2, 2]`.

The search:

```
 #   text     pattern                        what happens
--------------------------------------------------------------------
 1   T[0]=a   P[0]=a   match
 2   T[1]=a   P[1]=a   match
 3   T[2]=a   P[2]=b   MISMATCH   j goes 2 -> F[1] = 1,  i stays at 2
 4   T[2]=a   P[1]=a   match
 5   T[3]=b   P[2]=b   match
 6   T[4]=a   P[3]=a   match
 7   T[5]=a   P[4]=a   match
 8   T[6]=d   P[5]=a   MISMATCH   j goes 5 -> F[4] = 2,  i stays at 6
 9   T[6]=d   P[2]=b   MISMATCH   j goes 2 -> F[1] = 1,  i stays at 6
10   T[6]=d   P[1]=a   MISMATCH   j goes 1 -> F[0] = 0,  i stays at 6
11   T[6]=d   P[0]=a   MISMATCH   j already 0, so i moves to 7
12   T[7]=a   P[0]=a   match
13   T[8]=a   P[1]=a   match
14   T[9]=b   P[2]=b   match
15   T[10]=a  P[3]=a   match
16   T[11]=a  P[4]=a   match
17   T[12]=a  P[5]=a   match                                    MATCH
```

**The pattern is found at index 7, after 17 comparisons.**

Look at `i` in that trace: 0, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, … It never
goes down. Four separate attempts happen at position 6 without re-reading a
single character. That is why KMP is **O(n + m)** in the worst case, while both
of the others are O(nm).

### The three compared

| algorithm | comparisons | worst case |
|---|---:|---|
| Brute force | 24 | O(nm) |
| **Boyer-Moore** | **10** | O(nm) |
| KMP | 17 | **O(n+m)** |

Boyer-Moore wins here because the text contains a `'d'`, a character not in the
pattern, and it can skip straight past it. KMP has no such shortcut — it walks
through every character of the text once. But KMP is the only one of the three
with a *guaranteed* linear running time; Boyer-Moore is fast in practice, not
by promise.

---

## Problem 4 — Prefixes that are also suffixes

`P = "aaabbaaa"`.

| prefix | suffix of the same length | equal? |
|---|---|:--:|
| `a` | `a` | ✅ |
| `aa` | `aa` | ✅ |
| `aaa` | `aaa` | ✅ |
| `aaab` | `baaa` | ❌ |
| `aaabb` | `bbaaa` | ❌ |
| `aaabba` | `abbaaa` | ❌ |
| `aaabbaa` | `aabbaaa` | ❌ |

**Answer: 3** — namely `a`, `aa` and `aaa`.

A note on the wording: the problem says "nonempty prefixes", not "nonempty
*proper* prefixes". The whole string `"aaabbaaa"` is trivially both a prefix and
a suffix of itself, so on the strictest reading the answer is **4**. We take the
usual convention that a prefix here means a proper one, giving **3**.

---

## Problem 5 — Standard trie

Words: `{abab, baba, ccccc, bbaaaa, caa, bbaacc, cbcc, cbca}`

Every edge is one character. A `*` marks the end of a stored word.

```
a
└── b
    └── a
        └── b *

b
├── a
│   └── b
│       └── a *
└── b
    └── a
        └── a
            ├── a
            │   └── a *
            └── c
                └── c *

c
├── a
│   └── a *
├── b
│   └── c
│       ├── a *
│       └── c *
└── c
    └── c
        └── c
            └── c *
```

**27 nodes**, counting the root.

---

## Problem 6 — Compressed trie

The same words. Every run of nodes with only one child is collapsed into a
single edge carrying the whole substring.

A node may be joined to its only child **only if** it has exactly one child
**and** is not itself the end of a word — joining through an end marker would
lose that word.

```
abab *

b
├── aba *
└── baa
    ├── aa *
    └── cc *

c
├── aa *
├── bc
│   ├── a *
│   └── c *
└── cccc *
```

**13 nodes instead of 27 — 14 saved.**

Every internal node now has at least two children. That is why a compressed
trie needs only `O(number of words)` nodes, no matter how long the words are,
while a standard trie needs one node per character.

---

## Problem 7 — Huffman

String: `"dogs do not spot hot pots or cats"` — **33 characters, 12 distinct.**

### Frequency table

The spaces are characters and go in the table like everything else. There are
seven of them, which ties them for most frequent.

| char | ` ` | `o` | `t` | `s` | `d` | `p` | `a` | `c` | `g` | `h` | `n` | `r` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| freq | 7 | 7 | 5 | 4 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |

### Building the tree

Repeatedly take the two lowest-frequency nodes and join them under a parent
whose frequency is their sum:

```
 1 + 1 -> 2      g + n
 1 + 1 -> 2      h + r
 1 + 1 -> 2      c + a
 2 + 2 -> 4      d + p
 2 + 2 -> 4      (gn) + (hr)
 2 + 4 -> 6      (ca) + s
 4 + 4 -> 8      (dp) + (gn hr)
 5 + 6 -> 11     t + (ca s)
 7 + 7 -> 14     o + space
 8 + 11 -> 19
14 + 19 -> 33    the root
```

### The tree

Left edge is `0`, right edge is `1`. Numbers in brackets are frequencies.

```
                            (33)
                 0 /                 \ 1
                (14)                 (19)
             0 /    \ 1          0 /      \ 1
            o(7)   ' '(7)        (8)       (11)
                              0 /   \ 1   0 /  \ 1
                             (4)    (4)  t(5)  (6)
                           0/  \1  0/ \1     0/  \1
                         d(2) p(2) (2) (2)   (2)  s(4)
                                  0/\1 0/\1  0/\1
                                  g  n h  r  c  a
```

Every character sits at a **leaf**, which is what makes the code prefix-free.

### The codes

Reading each path from the root:

| char | freq | code | bits | freq × bits |
|---|---:|---|---:|---:|
| `o` | 7 | `00` | 2 | 14 |
| ` ` | 7 | `01` | 2 | 14 |
| `t` | 5 | `110` | 3 | 15 |
| `s` | 4 | `1111` | 4 | 16 |
| `d` | 2 | `1000` | 4 | 8 |
| `p` | 2 | `1001` | 4 | 8 |
| `g` | 1 | `10100` | 5 | 5 |
| `n` | 1 | `10101` | 5 | 5 |
| `h` | 1 | `10110` | 5 | 5 |
| `r` | 1 | `10111` | 5 | 5 |
| `c` | 1 | `11100` | 5 | 5 |
| `a` | 1 | `11101` | 5 | 5 |
| | | | | **105 bits** |

**Total encoded length: 105 bits.**

With 12 distinct characters a fixed-length code needs 4 bits each, so
4 × 33 = **132 bits**. Huffman saves about 20%.

Two things worth saying:

- **The code is prefix-free** — no code is the start of another — because every
  character sits at a *leaf* of the tree. That is what lets the encoded stream
  be decoded with no separators between characters.
- **Ties are not decided by the algorithm.** When two nodes have the same
  frequency, which one you pick first is up to you, so a different but equally
  correct tree can give different code *strings*. What is always the same is the
  **total encoded length of 105 bits** — that is what "optimal" means here.

---

## Problem 8 — Longest common subsequence by dynamic programming

`a = "babbabab"` and `b = "bbabbaaab"`.

A **subsequence** keeps the order of the characters but they do not have to be
next to each other. (A sub*string* would have to be — a different problem.)

Build a table where cell `[i][j]` is the LCS length of the first `i` characters
of `a` and the first `j` characters of `b`:

- if the two characters match, `table[i][j] = table[i-1][j-1] + 1`
- if they do not, `table[i][j] = max(table[i-1][j], table[i][j-1])`

Row 0 and column 0 are all zeros, because an empty string has nothing in common
with anything.

|   | – | b | b | a | b | b | a | a | a | b |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **–** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **b** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **a** | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **b** | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 |
| **b** | 0 | 1 | 2 | 2 | 3 | 4 | 4 | 4 | 4 | 4 |
| **a** | 0 | 1 | 2 | 3 | 3 | 4 | 5 | 5 | 5 | 5 |
| **b** | 0 | 1 | 2 | 3 | 4 | 4 | 5 | 5 | 5 | 6 |
| **a** | 0 | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 6 | 6 |
| **b** | 0 | 1 | 2 | 3 | 4 | 5 | 5 | 6 | 6 | **7** |

**The longest common subsequence has 7 characters.** The answer is the
bottom-right cell — all of `a` against all of `b`.

One such subsequence is **`"babbaab"`**, found by walking back from the bottom
right: step diagonally where the two characters match, otherwise step to the
bigger neighbour. Several different subsequences of length 7 exist; only the
*length* is unique.

The table has 9 × 10 = 90 cells and each takes constant work, so this is
`O(nm)`.

---

## Problem 9 — LCS in Python

### a) Recursive

```python
def lcs_recursive(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    if a[-1] == b[-1]:
        return 1 + lcs_recursive(a[:-1], b[:-1])
    return max(lcs_recursive(a[:-1], b), lcs_recursive(a, b[:-1]))
```

### b) Dynamic

```python
def lcs_table(a, b):
    n = len(a)
    m = len(b)

    table = []
    for i in range(n + 1):
        table.append([0] * (m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table


def lcs_dynamic(a, b):
    return lcs_table(a, b)[len(a)][len(b)]
```

This is the function that produced the table in problem 8. Both versions were
checked against each other on 200 random string pairs and always agree.

### c) When does the recursive version become too slow?

Both versions were timed on random strings of growing length.

**When the two strings have nothing in common** — the worst case, because then
every call splits into two:

| n | recursive | dynamic |
|---:|---:|---:|
| 12 | 0.64 s | 0.000018 s |
| 13 | 2.26 s | 0.000036 s |
| 14 | 8.50 s | 0.000026 s |
| 15 | **30.6 s** | 0.000027 s |

**Every extra character multiplies the time by about 3.6.**

| alphabet | too slow from about | time there |
|---|---|---|
| 10 different letters | **n ≈ 15** | 5.6 s |
| 2 different letters | **n ≈ 30** | 6.9 s |

**Answer: the recursive version becomes unusable at around n = 15 for a large
alphabet, and around n = 30 for a two-letter one. The dynamic version is still
instant at n = 40.**

Why so different? Because the recursion re-solves the same small problems over
and over. With no matches the number of calls is

$$\binom{2n}{n} \approx \frac{4^n}{\sqrt{\pi n}}$$

which is where the factor of ~3.6 per character comes from. The table version
solves each subproblem **once**: at `n = 15` that is 256 cells against roughly
155 million calls.

The alphabet matters because **a match uses up a character from both strings in
one call, while a mismatch creates two calls.** With only two letters, about
half of all character pairs match, so a lot of the work collapses instead of
splitting. With ten letters that happens only a tenth of the time.

Both versions use exactly the same rule. The only difference is whether an
answer already worked out is written down or thrown away — and that is the
whole idea of dynamic programming.
