"""Algorithms week 1 — text processing. Uke 35: Goodrich & Tamassia ch. 9.

    ../check.py alg01

Every algorithm here is one the compulsory exercise asks about, but **none of
the test data is the assignment's data** — different strings throughout, on
purpose. Get these green and you will be able to do the assignment; you will
not have been handed it.

There are no reference solutions for this week. See ../README.md for why.

A note on counting comparisons. Several exercises ask for a count as well as an
answer, because "how many comparisons?" is exactly what the exam and the
assignment ask. **One comparison = one evaluation of `text[i] == pattern[j]`.**
Nothing else counts: not loop bookkeeping, not the last-occurrence table, not
the failure function. Increment your counter on the line where you compare two
characters, and nowhere else.
"""

from lib.check import todo

# ---------------------------------------------------------------------------
# Exercise 1  —  brute-force pattern matching
#
# Slide the pattern along the text one position at a time. At each position,
# compare left to right until a mismatch or a full match.
#
# Return (index, comparisons):
#   index        where the first match starts, or -1 if there is none
#   comparisons  how many character comparisons you made
#
#   brute_force("abacaabaccabacabaabb", "abacab")  ==  (10, 28)
#
# The algorithm, from the book:
#
#   for i in 0 .. n-m:
#       j = 0
#       while j < m and T[i+j] == P[j]:   # <- each test is one comparison
#           j += 1
#       if j == m: return i
#   return -1
#
# Careful with the `while`: the test that FAILS is still a comparison. If you
# count only the successful ones your total will be short by one per position.
# ---------------------------------------------------------------------------

def brute_force(text: str, pattern: str) -> tuple[int, int]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 2  —  the last-occurrence function
#
# Boyer-Moore's first heuristic needs to know, for each character, the LAST
# index at which it appears in the pattern.
#
#   last_occurrence("abacab")  ==  {"a": 4, "b": 5, "c": 3}
#
# Characters not in the pattern are simply absent from the dict; the matcher
# treats a missing character as -1.
#
# Build it by scanning the pattern left to right and overwriting — later
# positions win, which is what "last" means.
# ---------------------------------------------------------------------------

def last_occurrence(pattern: str) -> dict:
    todo()


# ---------------------------------------------------------------------------
# Exercise 3  —  Boyer-Moore
#
# The looking-glass heuristic: compare the pattern to the text BACKWARDS, from
# its last character. On a mismatch, use the last-occurrence table to jump.
#
# The book's algorithm, exactly:
#
#   L = last_occurrence(P)
#   i = m - 1;  j = m - 1
#   repeat:
#       if T[i] == P[j]:                  # <- one comparison
#           if j == 0: return i           # matched; i is the start
#           i -= 1;  j -= 1
#       else:
#           l = L.get(T[i], -1)
#           i = i + m - min(j, 1 + l)     # the character-jump
#           j = m - 1
#   until i > n - 1
#   return -1
#
#   boyer_moore("abacaabaccabacabaabb", "abacab")  ==  (10, 19)
#
# Return (index, comparisons), same rule as before.
#
# Why it can beat brute force: on a mismatch it often skips a whole pattern
# width instead of one position, so it can finish having looked at only a
# fraction of the text. The `min(j, 1 + l)` is what stops the jump ever moving
# i backwards — work out why that is needed and you understand the algorithm.
# ---------------------------------------------------------------------------

def boyer_moore(text: str, pattern: str) -> tuple[int, int]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 4  —  the KMP failure function
#
# F[j] = the length of the longest proper prefix of P[0..j] that is also a
# suffix of P[0..j]. "Proper" means it is not the whole thing.
#
#   failure_function("abacab")  ==  [0, 0, 1, 0, 1, 2]
#
# Read the last entry: "ab" (length 2) is both a prefix and a suffix of
# "abacab". That is what lets KMP resume mid-pattern instead of restarting.
#
#   F[0] = 0;  i = 1;  j = 0
#   while i < m:
#       if P[i] == P[j]:  F[i] = j + 1;  i += 1;  j += 1
#       elif j > 0:       j = F[j - 1]
#       else:             F[i] = 0;  i += 1
#
# Return a list of ints. These comparisons are NOT counted anywhere.
# ---------------------------------------------------------------------------

def failure_function(pattern: str) -> list[int]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 5  —  Knuth-Morris-Pratt
#
# Never move backwards in the text. On a mismatch, consult the failure function
# to find out how much of the pattern is still usable.
#
#   F = failure_function(P)
#   i = 0;  j = 0
#   while i < n:
#       if T[i] == P[j]:                     # <- one comparison
#           if j == m - 1: return i - m + 1
#           i += 1;  j += 1
#       elif j > 0: j = F[j - 1]             # no comparison, no i movement
#       else:       i += 1
#   return -1
#
#   kmp("abacaabaccabacabaabb", "abacab")  ==  (10, 19)
#
# Return (index, comparisons).
#
# On that one text and pattern, the three of them cost:
#
#     brute force   28 comparisons
#     Boyer-Moore   19
#     KMP           19
#
# — which is the comparison the assignment asks you to make, on its own data.
# Do not read too much into one example: BM and KMP tie here and will not in
# general. BM wins on large alphabets (English text), where a mismatched
# character is usually absent from the pattern and the jump is a full width.
# KMP wins on small alphabets with lots of repetition, where BM's jumps are
# short. Brute force has no case where it wins.
#
# The guarantee: i never decreases, so KMP is O(n + m) in the worst case, where
# brute force is O(nm). Boyer-Moore is usually faster in practice but has no
# such worst-case promise.
# ---------------------------------------------------------------------------

def kmp(text: str, pattern: str) -> tuple[int, int]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 6  —  prefixes that are also suffixes
#
# Return the nonempty PROPER prefixes of s that are also suffixes, shortest
# first. Proper = excludes s itself.
#
#   border_prefixes("ababab")  ==  ["ab", "abab"]
#   border_prefixes("abcd")    ==  []
#
# You can do this directly with slicing. Then notice: the failure function you
# just wrote already encodes this — F[m-1] gives the longest one, and following
# the chain F[F[m-1]-1] gives the next. Worth seeing that they are the same
# question.
# ---------------------------------------------------------------------------

def border_prefixes(s: str) -> list[str]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 7  —  a standard trie
#
# Store a set of strings in a tree where each edge is one character and each
# path from the root spells a prefix.
#
# Represent it as nested dicts, with "$" marking the end of a stored word:
#
#   build_trie(["ab", "ac"])
#     ==  {"a": {"b": {"$": {}}, "c": {"$": {}}}}
#
#   build_trie(["a", "ab"])
#     ==  {"a": {"$": {}, "b": {"$": {}}}}
#
# The second case is the one to get right: "a" is both a stored word and a
# prefix of another, so its node has BOTH the end marker and a child. Without
# the marker you could not tell "a is stored" from "a is only a prefix".
#
# Lookup is then O(length of the word) and independent of how many words are
# stored — the property that makes tries worth the space.
# ---------------------------------------------------------------------------

def build_trie(words: list[str]) -> dict:
    todo()


# ---------------------------------------------------------------------------
# Exercise 8  —  a compressed trie
#
# A standard trie wastes a node on every character in a non-branching run.
# Collapse each such chain into a single edge labelled with the whole substring.
#
#   compress(build_trie(["abcd", "abce"]))
#     ==  {"abc": {"d": {"$": {}}, "e": {"$": {}}}}
#
#   compress(build_trie(["xy"]))  ==  {"xy": {"$": {}}}
#
# A node may be merged with its single child only when it has exactly one child
# AND is not itself the end of a stored word. Merging through an end marker
# would lose the fact that a word finishes there.
#
# Work bottom-up: compress the children first, then look at whether this node
# can absorb its only child. Leave "$" keys alone — they are markers, not
# characters.
# ---------------------------------------------------------------------------

def compress(trie: dict) -> dict:
    todo()


# ---------------------------------------------------------------------------
# Exercise 9  —  a frequency table
#
#   frequency_table("mississippi")
#     ==  {"m": 1, "i": 4, "s": 4, "p": 2}
#
# Any dict with the right counts passes; key order does not matter.
# ---------------------------------------------------------------------------

def frequency_table(s: str) -> dict:
    todo()


# ---------------------------------------------------------------------------
# Exercise 10  —  Huffman coding
#
# Build the tree greedily: repeatedly take the two lowest-frequency nodes, join
# them under a new parent whose frequency is their sum, and put it back. Stop
# when one node remains. Then read codes off the tree — left is "0", right "1".
#
# Return a dict {character: code string}.
#
#   huffman_codes({"a": 5, "b": 2, "c": 1})
#     -> something like {"a": "0", "b": "11", "c": "10"}
#
# **Ties are not resolved by the algorithm**, so two correct implementations can
# produce different code STRINGS. The tests therefore check the properties that
# every correct answer shares:
#
#   - the code is prefix-free (no code is a prefix of another), which is what
#     makes it decodable without separators;
#   - the total encoded length, sum(freq[c] * len(code[c])), is minimal —
#     this is the number the assignment's Huffman problem is really about;
#   - a more frequent character never gets a longer code than a rarer one.
#
# Special case: a single distinct character has no branch to encode. Give it
# the code "0" — length 1, since a zero-length code cannot be transmitted.
# ---------------------------------------------------------------------------

def huffman_codes(freqs: dict) -> dict:
    todo()


# ---------------------------------------------------------------------------
# Exercise 11  —  longest common subsequence, recursively
#
# A SUBsequence keeps order but need not be contiguous — "ace" is a subsequence
# of "abcde". (A sub*string* would have to be contiguous. Different problem.)
#
# Return the LENGTH of the longest common subsequence.
#
#   lcs_recursive("AGGTAB", "GXTXAYB")  ==  4      ("GTAB")
#
# The recurrence:
#   - either string empty            -> 0
#   - last characters equal          -> 1 + LCS(a[:-1], b[:-1])
#   - otherwise                      -> max(LCS(a[:-1], b), LCS(a, b[:-1]))
#
# Write it directly, with no memoisation. It is exponential, and that is the
# point — you need the slow version to have something to compare against.
# ---------------------------------------------------------------------------

def lcs_recursive(a: str, b: str) -> int:
    todo()


# ---------------------------------------------------------------------------
# Exercise 12  —  the same thing, dynamically
#
# Same recurrence, but fill a table instead of recursing, so each subproblem is
# solved once rather than exponentially often.
#
# Build an (len(a)+1) x (len(b)+1) grid where cell [i][j] is the LCS length of
# the first i characters of a and the first j of b. Row 0 and column 0 are all
# zeros. Then:
#
#   if a[i-1] == b[j-1]:  table[i][j] = table[i-1][j-1] + 1
#   else:                 table[i][j] = max(table[i-1][j], table[i][j-1])
#
# The answer is the bottom-right cell.
#
#   lcs_dynamic("AGGTAB", "GXTXAYB")  ==  4
#   lcs_table("AB", "AB")             ==  [[0,0,0], [0,1,1], [0,1,2]]
#
# O(nm) instead of exponential. Return the full table from `lcs_table` — being
# able to draw and read that grid is exactly what the assignment's dynamic
# programming problem asks for.
# ---------------------------------------------------------------------------

def lcs_table(a: str, b: str) -> list[list[int]]:
    todo()


def lcs_dynamic(a: str, b: str) -> int:
    todo()
