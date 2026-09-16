# Algorithms Week 1 — paper answers

Concepts only. None of the assignment's own problems are worked here.

**P1.** Failure function for `"abababca"`:

| j | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P[j] | a | b | a | b | a | b | c | a |
| F[j] | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |

`F = [0, 0, 1, 2, 3, 4, 0, 1]`. It climbs while `"ababab"` keeps repeating,
collapses to 0 at `c` (nothing ending in `c` is a prefix), then returns to 1 at
the final `a`.

**P2.** Last-occurrence table for `"needle"`:

```
n: 0    e: 5    d: 3    l: 4
```

`e` appears at 1, 2 and 5 — only the **last** is kept. Any character not listed
(say `z`) is treated as −1, meaning "slide past it entirely".

**P3.** `T = "aaaaaaaaab"` (9 a's then b), `P = "aaab"`. **28 comparisons**,
matching at index 6.

Each of the first six alignments matches `aaa` and then fails on the `b` — four
comparisons wasted per position, and the shift is only one. This is brute
force's bad case, and the cause is that the pattern has a **long repeated
prefix**: every alignment does nearly the full work of a match before failing,
and learns nothing that carries to the next.

This is exactly the waste KMP removes — its failure function says how much of
the `aaa` is still valid, so it never re-reads those characters.

**P4.** Standard trie for `{car, cat, cart, dog}` — `$` marks a stored word:

```
root
├── c ── a ─┬── r ── $          (car)
│           │       └── t ── $  (cart)
│           └── t ── $          (cat)
└── d ── o ── g ── $            (dog)
```

Note `r` carries **both** a `$` and a child `t`: "car" is a word *and* a prefix
of "cart".

Compressed:

```
root
├── "ca" ─┬── "r" ─┬── $
│         │        └── "t" ── $
│         └── "t" ── $
└── "dog" ── $
```

`d-o-g` collapses to one edge. `c-a` collapses to `"ca"`. The `r` node cannot
absorb its `t` child, because `r` ends a word. Nine character-nodes become five
edges — and the saving grows with the length of the non-branching runs.

**P5.** Huffman for `a:8, b:3, c:1, d:1, e:1`.

Combine the two smallest repeatedly: `c+d = 2`; then `2 + e = 3`; then that
`3 + b = 6`; then `6 + a = 14`.

One valid code table:

```
a: 1        (length 1)
b: 00       (length 2)
e: 010      (length 3)
c: 0110     (length 4)
d: 0111     (length 4)
```

Total = 8(1) + 3(2) + 1(3) + 1(4) + 1(4) = **25 bits**. Fixed-length coding
would need 3 bits × 14 characters = 42.

A different valid table: swap every `0` and `1` (`a: 0`, `b: 11`, …), or swap
`c` and `d`, which are interchangeable at frequency 1. Both are correct because
Huffman **does not define how ties break** — and any tie-break gives the same
total of 25. Optimality is a claim about the total, not about the particular
strings.

**P6.** LCS of `"abcbdab"` and `"bdcaba"`. The table:

|  | – | b | d | c | a | b | a |
|---|---|---|---|---|---|---|---|
| **–** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **a** | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| **b** | 0 | 1 | 1 | 1 | 1 | 2 | 2 |
| **c** | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
| **b** | 0 | 1 | 1 | 2 | 2 | 3 | 3 |
| **d** | 0 | 1 | 2 | 2 | 2 | 3 | 3 |
| **a** | 0 | 1 | 2 | 2 | 3 | 3 | 4 |
| **b** | 0 | 1 | 2 | 2 | 3 | 4 | 4 |

Length **4**. Reading back from the bottom-right — move diagonally when the
characters match, otherwise toward the larger neighbour — gives `"bcba"`.
`"bdab"` is also length 4; the LCS is not unique, only its length is.

**P7.** The recursion branches into two calls whenever the last characters
differ, and those branches overlap.

For `"ab"` / `"ba"`: `LCS("ab","ba")` mismatches, so it calls `LCS("a","ba")`
and `LCS("ab","b")`. **`LCS("a","b")` is then computed by both** — once from
each branch. With longer strings the duplication compounds, giving O(2^(n+m)).

The table version computes `LCS("a","b")` exactly once, in one cell. Nothing
about the recurrence changed — only whether results are remembered.

**P8.** The two cases are not symmetric, and the reason is *where the
preprocessing cost lands.*

- **One pattern, a thousand texts → KMP.** The failure function depends only on
  the pattern, so you build it **once** and reuse it across all thousand. Its
  O(m) cost is amortised to nothing, and you get the O(n) guarantee every time.
  (Boyer-Moore's last-occurrence table is also pattern-only, so BM is a
  defensible answer too — say so, and say it wins on large alphabets.)

- **A thousand patterns, one text → neither, if you can help it.** Both
  preprocess the *pattern*, so you pay that cost a thousand times and get no
  reuse from the fixed text. The right move is to preprocess the **text**
  instead — build a suffix trie or suffix tree once, then each pattern is
  answered in O(m) regardless of how long the text is.

The general principle: **preprocess whichever side is reused.** That is also
why tries appear in the same chapter as these matchers — they are the answer to
the second question.
