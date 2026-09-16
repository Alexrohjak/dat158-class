# Algorithms Week 1 — Text processing

**Source:** uke 35, Goodrich & Tamassia ch. 9. Slides in
[`../../weeks/uke35-alg/slides/`](../../weeks/uke35-alg/slides/).
**Budget:** 3–4 hours. Twelve functions, and three of them are on the
compulsory exercise.

> The textbook chapter there is a **scan with no text layer**. Ctrl+F will not
> work in your PDF reader. Search it with `python ../src/find.py <term>` —
> the text was recovered by OCR into the search cache.

**Directly relevant to Algorithms number 1, due 4 September.** The exercises
here use different strings from the assignment on purpose: learn the algorithm
here, apply it there.

---

## 1. Pattern matching: three algorithms, one problem

Find pattern `P` (length m) in text `T` (length n). Three approaches, and the
difference between them is *what they do on a mismatch*.

### Brute force

Slide P along T one position at a time; at each, compare left to right.

```
for i in 0 .. n-m:
    j = 0
    while j < m and T[i+j] == P[j]:
        j += 1
    if j == m: return i
```

O(nm) worst case. On a mismatch it throws away everything it learned and shifts
by one. Both of the others are attacks on that waste.

**Counting comparisons.** One comparison = one evaluation of `T[i] == P[j]`.
The test that *fails* still counts — it is the comparison that told you it
failed. Off-by-one here is the most common error on this material.

### Boyer-Moore — look backwards, jump forwards

Two ideas:

1. **Looking-glass.** Compare P against T *backwards*, from P's last character.
2. **Character-jump.** On a mismatch at `T[i]`, look up where that character
   last appears in P and slide P so they line up. If it does not appear in P at
   all, slide past it entirely.

```
i = j = m - 1
repeat:
    if T[i] == P[j]:
        if j == 0: return i
        i -= 1; j -= 1
    else:
        l = L.get(T[i], -1)
        i = i + m - min(j, 1 + l)
        j = m - 1
until i > n - 1
```

The `min(j, 1 + l)` exists to stop `i` moving *backwards* when the mismatched
character occurs late in P. Work through a case where `l > j` and you will see
it; that is the detail worth understanding rather than memorising.

Why it is fast in practice: on English text, a mismatched character is usually
absent from the pattern, so you skip a full pattern width. It can finish having
looked at a *fraction* of the text. The book quotes ~0.24 comparisons per
character for a 5-character pattern on English — **less than one look per
character.**

Worst case is still O(nm). It is a practical win, not a guarantee.

### KMP — never re-read the text

Boyer-Moore attacks the shift. KMP attacks the *backtracking*: `i` never
decreases. On a mismatch, it asks how much of the pattern it has already
matched that it can keep.

The **failure function**:

> `F[j]` = the length of the longest **proper** prefix of `P[0..j]` that is
> also a **suffix** of `P[0..j]`.

For `P = "abacab"`: `F = [0, 0, 1, 0, 1, 2]`. The final 2 says `"ab"` is both a
prefix and a suffix, so on a mismatch after matching all six, two characters are
still good and matching resumes at `j = 2`.

O(n + m), guaranteed — the only one of the three with a linear worst case.

### Choosing between them

| | Worst case | Good when |
|---|---|---|
| Brute force | O(nm) | never, except as a baseline |
| Boyer-Moore | O(nm) | large alphabets — English text |
| KMP | **O(n+m)** | small alphabets, heavy repetition; guarantees needed |

On the tutorial's test input (`"abacaabaccabacabaabb"` / `"abacab"`) they cost
**28**, **19** and **19** comparisons. Don't over-read a single example — BM
and KMP tie there and generally will not.

## 2. Tries

A tree where each edge is one character and each root-to-node path spells a
prefix. Lookup is O(length of the word) — **independent of how many words are
stored.** A hash table matches that, but a trie also gives you every word with a
given prefix for free, which is why it is the autocomplete data structure.

The subtlety: a word can be a prefix of another. Storing `{"a", "ab"}` needs a
marker on the `a` node, or you cannot tell "a is a stored word" from "a is
merely on the way to ab". Here that marker is a `"$"` key.

A **compressed trie** collapses every non-branching chain into one edge labelled
with the whole substring. `{"abcd", "abce"}` becomes `abc → {d, e}`: three nodes
instead of five. The rule for merging a node into its only child is that it must
have **exactly one child and not itself be the end of a word** — merging through
an end marker would lose a word.

## 3. Huffman coding

Fixed-length codes waste space when characters appear at wildly different rates.
Huffman gives frequent characters short codes and rare ones long codes.

Greedy, and provably optimal:

1. One leaf per character, weighted by frequency.
2. Repeatedly remove the two lowest-weight nodes and join them under a parent
   whose weight is their sum.
3. Stop at one node. Left edges are `0`, right edges `1`.

Because every character is a **leaf**, no code is a prefix of another — so the
encoded stream is decodable with no separators. That prefix-free property is the
whole point, and it is what makes the greedy construction work.

**Ties are not defined by the algorithm.** Two correct implementations can
produce different code strings. What is invariant is the **total encoded
length** $\sum_c f_c \cdot |code_c|$ — that is what "optimal" means, and what
the tests check.

## 4. Longest common subsequence

A **subsequence** keeps order but need not be contiguous: `"ace"` is a
subsequence of `"abcde"`. A sub*string* must be contiguous. Different problem —
do not mix them up.

The recurrence:

$$LCS(i,j) = \begin{cases}
0 & i = 0 \text{ or } j = 0 \\
LCS(i-1,j-1) + 1 & a_i = b_j \\
\max(LCS(i-1,j),\ LCS(i,j-1)) & \text{otherwise}
\end{cases}$$

Written **recursively**, it is exponential — it recomputes the same subproblems
over and over. Written as a **table**, each subproblem is solved once: O(nm).

Same recurrence. The only difference is whether you remember what you already
worked out. That is the entire idea of dynamic programming, and the assignment
makes you feel it: exercise 9c asks you to find the length at which the
recursive version becomes unusable while the table version stays instant.

---

## 5. Paper exercises

No computer — the exam has none either.

**P1.** Compute the failure function for `"abababca"` by hand.

**P2.** Give the last-occurrence table for `"needle"`.

**P3.** For text `"aaaaaaaaab"` and pattern `"aaab"`, roughly how many
comparisons does brute force make? Why is this close to its worst case, and
what property of the pattern causes it?

**P4.** Draw the standard trie for `{"car", "cat", "cart", "dog"}`. Now the
compressed trie. How many nodes did you save?

**P5.** Build the Huffman tree for frequencies `a:8, b:3, c:1, d:1, e:1`. Give
one valid code table and the total encoded length. Then give a *different*
valid code table with the same total, and say why both are correct.

**P6.** Fill the LCS table for `"abcbdab"` and `"bdcaba"` by hand. What is the
length? Read one actual subsequence back out of the table.

**P7.** Why is the recursive LCS exponential? Name the exact subproblem that
gets computed more than once for `"ab"` / `"ba"`.

**P8.** You must search one fixed pattern in a thousand different texts. Then:
a thousand different patterns in one fixed text. Which algorithm for each, and
why does the answer change?

Answers in [`../solutions/alg01/PAPER.md`](../solutions/alg01/PAPER.md).

---

## 6. Coding exercises

```bash
cd tutorial
./check.py alg01
```

**76 checks, 12 functions.** Order matters here — 2 feeds 3, and 4 feeds 5.

Exercises 3, 11 and 12 are the algorithms the compulsory exercise asks you to
implement. Get them green on *this* data, then write the assignment's answers
against *its* data. That is the honest version of practice, and it is also the
one that works.

**There is no reference solution for this week.** The compulsory exercise is
live; handing you working code two days before the deadline would not be
teaching you. The 76 checks are your feedback loop. See
[`../solutions/alg01/README.md`](../solutions/alg01/README.md).

---

## 7. Checklist

- [ ] I can run brute force by hand and count the comparisons correctly
- [ ] I can explain the two Boyer-Moore heuristics in one sentence each
- [ ] I know why `min(j, 1 + l)` is there
- [ ] I can define the failure function without looking it up
- [ ] I can say why KMP is O(n+m) and BM is not
- [ ] I can say which algorithm suits a large alphabet, and why
- [ ] I can draw a standard trie and compress it
- [ ] I know why a trie needs an end-of-word marker
- [ ] I can build a Huffman tree and say why the code is prefix-free
- [ ] I can write the LCS recurrence from memory
- [ ] I can explain why the table version is fast and the recursion is not
- [ ] All 76 checks pass

**Then:** the assignment. Its nine problems are broken down in
[`../../assignments/README.md`](../../assignments/README.md).
