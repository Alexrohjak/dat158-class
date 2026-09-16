"""Checks for Algorithms week 1. You don't edit this file.

None of this data is the assignment's data. If you are looking for the
assignment's answers they are not here, by design.
"""

T = "abacaabaccabacabaabb"
P = "abacab"


def build(ex, s):
    # -- 1: brute force --
    s.eq("1  finds the match", lambda: ex.brute_force(T, P)[0], 10)
    s.eq("1  counts 28 comparisons", lambda: ex.brute_force(T, P), (10, 28))
    s.eq("1  match at position 0", lambda: ex.brute_force("abcdef", "abc")[0], 0)
    s.eq("1  ...in exactly 3 comparisons", lambda: ex.brute_force("abcdef", "abc")[1], 3)
    s.eq("1  no match returns -1", lambda: ex.brute_force("aaaaa", "bb")[0], -1)
    s.eq("1  a failing test still counts", lambda: ex.brute_force("aaaaa", "bb"), (-1, 4))
    s.eq("1  finds the last position", lambda: ex.brute_force("xxxab", "ab")[0], 3)
    s.eq("1  single character", lambda: ex.brute_force("abc", "c"), (2, 3))

    # -- 2: last occurrence --
    s.eq("2  last index of each character",
         lambda: ex.last_occurrence("abacab"), {"a": 4, "b": 5, "c": 3})
    s.eq("2  later positions win",
         lambda: ex.last_occurrence("aaa"), {"a": 2})
    s.eq("2  absent characters are absent",
         lambda: "z" in ex.last_occurrence("abc"), False)
    s.eq("2  single character", lambda: ex.last_occurrence("x"), {"x": 0})

    # -- 3: Boyer-Moore --
    s.eq("3  finds the same match as brute force", lambda: ex.boyer_moore(T, P)[0], 10)
    s.eq("3  in 19 comparisons, not 28", lambda: ex.boyer_moore(T, P), (10, 19))
    s.eq("3  beats brute force on this input",
         lambda: ex.boyer_moore(T, P)[1] < ex.brute_force(T, P)[1], True)
    s.eq("3  no match returns -1", lambda: ex.boyer_moore("aaaaa", "bb")[0], -1)
    s.eq("3  a missing character jumps a whole width",
         lambda: ex.boyer_moore("a" * 20, "b" * 3), (-1, 6))
    s.eq("3  match at position 0", lambda: ex.boyer_moore("abcdef", "abc")[0], 0)
    s.eq("3  agrees with brute force wherever it matches",
         lambda: all(ex.boyer_moore(t, p)[0] == ex.brute_force(t, p)[0]
                     for t, p in [("hello world", "o w"), ("aaa", "aa"),
                                  ("abcabcabd", "abcabd"), ("xyz", "q")]), True)

    # -- 4: failure function --
    s.eq("4  failure of abacab", lambda: ex.failure_function("abacab"), [0, 0, 1, 0, 1, 2])
    s.eq("4  no repetition means all zeros",
         lambda: ex.failure_function("abcd"), [0, 0, 0, 0])
    s.eq("4  all-same climbs", lambda: ex.failure_function("aaaa"), [0, 1, 2, 3])
    s.eq("4  a repeating block", lambda: ex.failure_function("ababab"), [0, 0, 1, 2, 3, 4])
    s.eq("4  first entry is always 0", lambda: ex.failure_function("zzz")[0], 0)
    s.eq("4  length matches the pattern", lambda: len(ex.failure_function("abcde")), 5)

    # -- 5: KMP --
    s.eq("5  finds the same match", lambda: ex.kmp(T, P)[0], 10)
    s.eq("5  in 19 comparisons", lambda: ex.kmp(T, P), (10, 19))
    s.eq("5  no match returns -1", lambda: ex.kmp("aaaaa", "bb")[0], -1)
    s.eq("5  match at position 0", lambda: ex.kmp("abcdef", "abc")[0], 0)
    s.eq("5  beats brute force here",
         lambda: ex.kmp(T, P)[1] < ex.brute_force(T, P)[1], True)
    s.eq("5  agrees with brute force everywhere",
         lambda: all(ex.kmp(t, p)[0] == ex.brute_force(t, p)[0]
                     for t, p in [("hello world", "o w"), ("aaa", "aa"),
                                  ("abcabcabd", "abcabd"), ("xyz", "q"),
                                  ("aaaaab", "aab")]), True)

    # -- 6: borders --
    s.eq("6  ababab", lambda: ex.border_prefixes("ababab"), ["ab", "abab"])
    s.eq("6  none", lambda: ex.border_prefixes("abcd"), [])
    s.eq("6  aaa", lambda: ex.border_prefixes("aaa"), ["a", "aa"])
    s.eq("6  shortest first", lambda: ex.border_prefixes("abaaba"), ["a", "aba"])
    s.eq("6  proper only — the whole string never counts",
         lambda: "aa" in ex.border_prefixes("aa"), False)

    # -- 7: standard trie --
    s.eq("7  two words sharing a prefix",
         lambda: ex.build_trie(["ab", "ac"]),
         {"a": {"b": {"$": {}}, "c": {"$": {}}}})
    s.eq("7  a word that is a prefix of another",
         lambda: ex.build_trie(["a", "ab"]),
         {"a": {"$": {}, "b": {"$": {}}}})
    s.eq("7  one word", lambda: ex.build_trie(["hi"]), {"h": {"i": {"$": {}}}})
    s.eq("7  empty input", lambda: ex.build_trie([]), {})
    s.eq("7  disjoint words branch at the root",
         lambda: sorted(ex.build_trie(["ax", "bx"])), ["a", "b"])
    s.eq("7  a duplicate changes nothing",
         lambda: ex.build_trie(["ab", "ab"]) == ex.build_trie(["ab"]), True)

    # -- 8: compressed trie --
    s.eq("8  a branching run collapses",
         lambda: ex.compress(ex.build_trie(["abcd", "abce"])),
         {"abc": {"d": {"$": {}}, "e": {"$": {}}}})
    s.eq("8  a single word becomes one edge",
         lambda: ex.compress(ex.build_trie(["xy"])), {"xy": {"$": {}}})
    s.eq("8  a branch at the root is kept",
         lambda: ex.compress(ex.build_trie(["ax", "bx"])),
         {"ax": {"$": {}}, "bx": {"$": {}}})
    s.eq("8  it does NOT merge through an end marker",
         lambda: ex.compress(ex.build_trie(["a", "ab"])),
         {"a": {"$": {}, "b": {"$": {}}}})
    s.eq("8  empty stays empty", lambda: ex.compress({}), {})
    s.eq("8  a long chain becomes one label",
         lambda: ex.compress(ex.build_trie(["abcdef"])), {"abcdef": {"$": {}}})

    # -- 9: frequencies --
    s.eq("9  mississippi",
         lambda: ex.frequency_table("mississippi"), {"m": 1, "i": 4, "s": 4, "p": 2})
    s.eq("9  empty string", lambda: ex.frequency_table(""), {})
    s.eq("9  counts spaces too", lambda: ex.frequency_table("a b")[" "], 1)
    s.eq("9  totals to the length", lambda: sum(ex.frequency_table("hello").values()), 5)

    # -- 10: Huffman. Properties, not exact codes — ties are implementation-defined --
    def codes(f):
        return ex.huffman_codes(f)

    def prefix_free(f):
        cs = list(codes(f).values())
        return all(not a.startswith(b) for i, a in enumerate(cs)
                   for j, b in enumerate(cs) if i != j)

    def total(f):
        c = codes(f)
        return sum(f[ch] * len(c[ch]) for ch in f)

    s.eq("10 one code per character",
         lambda: sorted(codes({"a": 5, "b": 2, "c": 1})), ["a", "b", "c"])
    s.eq("10 the code is prefix-free",
         lambda: prefix_free({"a": 5, "b": 2, "c": 1}), True)
    s.eq("10 prefix-free on a bigger alphabet",
         lambda: prefix_free({"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}), True)
    s.eq("10 the encoding is optimal (a:5 b:2 c:1 costs 11 bits)",
         lambda: total({"a": 5, "b": 2, "c": 1}), 11)
    s.eq("10 optimal on the classic six-letter case",
         lambda: total({"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}), 224)
    s.eq("10 the commonest character gets a shortest code",
         lambda: len(codes({"a": 5, "b": 2, "c": 1})["a"])
                 <= min(len(v) for v in codes({"a": 5, "b": 2, "c": 1}).values()), True)
    s.eq("10 a rarer character never gets a shorter code",
         lambda: len(codes({"a": 5, "b": 2, "c": 1})["c"])
                 >= len(codes({"a": 5, "b": 2, "c": 1})["a"]), True)
    s.eq("10 four equal frequencies give four 2-bit codes",
         lambda: sorted(len(v) for v in codes({"a": 1, "b": 1, "c": 1, "d": 1}).values()),
         [2, 2, 2, 2])
    s.eq("10 a single character still gets a 1-bit code",
         lambda: len(codes({"a": 7})["a"]), 1)
    s.eq("10 it works on a real string",
         lambda: prefix_free(ex.frequency_table("mississippi")), True)

    # -- 11: LCS, recursively --
    s.eq("11 the textbook example", lambda: ex.lcs_recursive("AGGTAB", "GXTXAYB"), 4)
    s.eq("11 identical strings", lambda: ex.lcs_recursive("abc", "abc"), 3)
    s.eq("11 nothing in common", lambda: ex.lcs_recursive("abc", "xyz"), 0)
    s.eq("11 one empty", lambda: ex.lcs_recursive("abc", ""), 0)
    s.eq("11 both empty", lambda: ex.lcs_recursive("", ""), 0)
    s.eq("11 subsequence need not be contiguous",
         lambda: ex.lcs_recursive("abcde", "ace"), 3)

    # -- 12: LCS, dynamically --
    s.eq("12 same answer as the recursion",
         lambda: ex.lcs_dynamic("AGGTAB", "GXTXAYB"), 4)
    s.eq("12 non-contiguous", lambda: ex.lcs_dynamic("abcde", "ace"), 3)
    s.eq("12 nothing in common", lambda: ex.lcs_dynamic("abc", "xyz"), 0)
    s.eq("12 the table for AB/AB", lambda: ex.lcs_table("AB", "AB"),
         [[0, 0, 0], [0, 1, 1], [0, 1, 2]])
    s.eq("12 the table has a zero row and column",
         lambda: (ex.lcs_table("xy", "ab")[0], [r[0] for r in ex.lcs_table("xy", "ab")]),
         ([0, 0, 0], [0, 0, 0]))
    s.eq("12 the table is (n+1) x (m+1)",
         lambda: (len(ex.lcs_table("abc", "de")), len(ex.lcs_table("abc", "de")[0])), (4, 3))
    s.eq("12 the answer is the bottom-right cell",
         lambda: ex.lcs_table("AGGTAB", "GXTXAYB")[-1][-1], 4)
    s.eq("12 the two versions agree on many inputs",
         lambda: all(ex.lcs_recursive(a, b) == ex.lcs_dynamic(a, b)
                     for a, b in [("abcd", "abdc"), ("aaa", "aa"), ("xyz", ""),
                                  ("banana", "atana"), ("abcbdab", "bdcaba")]), True)
