"""DAT158 - Compulsory exercise, Algorithms number 1.

The two problems that ask for Python:

    Problem 2b - implement Boyer-Moore, run it on a Norwegian text, and
                 compare against the ~0.24 comparisons per character that the
                 theory predicts for a five character pattern.

    Problem 9  - the longest common subsequence, written recursively (a) and
                 with dynamic programming (b), and finding where the recursive
                 version becomes unusable (c).

The other seven problems are drawn by hand on paper.

Run this with:

    python assignment1.py

Problem 2b reads ../data/raw/sult-hamsun-no.txt - Knut Hamsun, "Sult" (1890),
Project Gutenberg #30027, public domain.

One comparison means one test of "is this text character equal to this pattern
character". A test that FAILS counts too. Building the last-occurrence table
costs no comparisons, as the problem says.
"""

import os
import random
import time


# ===========================================================================
# Problem 2b - Boyer-Moore on Norwegian text
# ===========================================================================

def last_occurrence(pattern):
    """For every character, the LAST position where it appears in pattern.

    We go left to right and overwrite, so later positions win.
    """
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore_all(text, pattern):
    """Find every occurrence of pattern in text, counting the comparisons.

    Boyer-Moore compares the pattern BACKWARDS, from its last character. On a
    mismatch it looks up where that text character last appears in the pattern
    and slides the pattern along so the two line up. If the character is not in
    the pattern at all, it skips past it completely.

    We find every occurrence rather than stopping at the first, because
    "comparisons per text character" only means something if we really scan the
    whole text.

    Returns (list of positions, number of comparisons).
    """
    n = len(text)
    m = len(pattern)
    if m == 0 or m > n:
        return [], 0

    last = last_occurrence(pattern)
    found = []
    comparisons = 0
    i = m - 1       # where we are in the text
    j = m - 1       # where we are in the pattern - start at the END

    while i < n:
        comparisons = comparisons + 1
        if text[i] == pattern[j]:
            if j == 0:
                found.append(i)      # i is the start of a full match
                i = i + m            # move the window on by one position
                j = m - 1
            else:
                i = i - 1            # keep walking backwards
                j = j - 1
        else:
            # Where does this text character appear in the pattern?
            # -1 means "nowhere", so we can skip past it entirely.
            if text[i] in last:
                l = last[text[i]]
            else:
                l = -1
            # min(j, 1 + l) stops the jump from moving i backwards, which it
            # would do whenever the character appears late in the pattern.
            i = i + m - min(j, 1 + l)
            j = m - 1

    return found, comparisons


def brute_force_all(text, pattern):
    """The same job by brute force. This is the baseline 2b compares against."""
    n = len(text)
    m = len(pattern)
    found = []
    comparisons = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons = comparisons + 1
            if text[i + j] != pattern[j]:
                break                # the failing test counts too
            j = j + 1
        if j == m:
            found.append(i)
    return found, comparisons


HERE = os.path.dirname(os.path.abspath(__file__))
TEXT_FILE = os.path.join(HERE, "..", "data", "raw", "sult-hamsun-no.txt")


def load_text():
    """The novel, with the Project Gutenberg header and footer removed."""
    f = open(TEXT_FILE, encoding="utf-8")
    raw = f.read()
    f.close()

    start = raw.find("*** START OF")
    end = raw.find("*** END OF")
    if start != -1:
        start = raw.index("\n", start) + 1
    else:
        start = 0
    if end == -1:
        end = len(raw)

    return raw[start:end].replace("\r\n", "\n").strip()


def show_problem_2b(samples=50):
    print("PROBLEM 2b - Boyer-Moore on Norwegian text")
    print()

    text = load_text()
    print("text:", len(text), "characters,", len(set(text)), "distinct")
    print(samples, "random patterns per length, taken from the text itself")
    print()
    print("length   BM per char   brute per char")

    generator = random.Random(0)
    for m in [2, 3, 4, 5, 6, 8, 10, 15, 20]:
        bm_total = 0
        bf_total = 0
        for _ in range(samples):
            at = generator.randrange(len(text) - m)
            pattern = text[at:at + m]
            bm_total = bm_total + boyer_moore_all(text, pattern)[1]
            bf_total = bf_total + brute_force_all(text, pattern)[1]
        bm = bm_total / samples / len(text)
        bf = bf_total / samples / len(text)
        print("%6d   %11.4f   %14.4f" % (m, bm, bf))

    print()
    print("The theory predicts about 0.24 for a five character pattern.")


# ===========================================================================
# Problem 9 - longest common subsequence
# ===========================================================================

# A SUBSEQUENCE keeps the order of the characters but they do not have to be
# next to each other: "ace" is a subsequence of "abcde". A SUBSTRING would
# have to be next to each other - a different problem.
#
# The rule both versions use, looking only at the LAST characters:
#
#   either string empty  ->  0
#   last characters same ->  1 + LCS(a without last, b without last)
#   otherwise            ->  the better of dropping one last character or the
#                            other


def lcs_recursive(a, b):
    """Problem 9a. The rule written straight out, remembering nothing."""
    if len(a) == 0 or len(b) == 0:
        return 0
    if a[-1] == b[-1]:
        return 1 + lcs_recursive(a[:-1], b[:-1])
    return max(lcs_recursive(a[:-1], b), lcs_recursive(a, b[:-1]))


def lcs_table(a, b):
    """Problem 9b. The same rule, written into a table instead.

    Cell [i][j] is the answer for the first i characters of a and the first j
    characters of b. Row 0 and column 0 stay zero, because an empty string has
    nothing in common with anything.
    """
    n = len(a)
    m = len(b)

    # Build the grid with a loop. Writing [[0] * (m + 1)] * (n + 1) would make
    # n+1 references to the SAME row, so changing one would change them all.
    table = []
    for i in range(n + 1):
        table.append([0] * (m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # character i of a sits at index i - 1
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table


def lcs_dynamic(a, b):
    """The answer is the bottom-right cell of the table."""
    table = lcs_table(a, b)
    return table[len(a)][len(b)]


def show_problem_9(budget=5.0):
    print("PROBLEM 9 - LCS, recursive against dynamic")
    print()
    print("Both give the same answer on the problem 8 strings:",
          lcs_recursive("babbabab", "bbabbaaab"),
          "and", lcs_dynamic("babbabab", "bbabbaaab"))
    print()
    print("Timing on random strings of growing length. The recursive version")
    print("is stopped once it goes past", budget, "seconds.")
    print()

    for alphabet in ["ab", "abcdefghij"]:
        print("alphabet:", alphabet, "-", len(alphabet), "different letters")
        print("  n    recursive      dynamic")

        generator = random.Random(0)
        still_running = True
        for n in range(8, 41):
            a = ""
            b = ""
            for _ in range(n):
                a = a + generator.choice(alphabet)
                b = b + generator.choice(alphabet)

            start = time.perf_counter()
            lcs_dynamic(a, b)
            dynamic_time = time.perf_counter() - start

            if still_running:
                start = time.perf_counter()
                lcs_recursive(a, b)
                recursive_time = time.perf_counter() - start
                print(" %2d  %10.4f s  %9.6f s"
                      % (n, recursive_time, dynamic_time))
                if recursive_time > budget:
                    print("  -> too slow from n =", n, "onwards")
                    still_running = False
        print()


# ===========================================================================

def main():
    print("=" * 60)
    show_problem_2b()
    print()
    print("=" * 60)
    show_problem_9()


if __name__ == "__main__":
    main()
