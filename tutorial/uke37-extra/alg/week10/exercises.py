"""Alg week 10 — set cover, three ways. Read LESSON.md first.

    cd tutorial/uke37-extra && ./check.sh alg 10

An instance is three things:

    ground  = {1, 2, 3, 4}                     the elements
    subsets = {"S1": {1, 2}, "S2": {1, 3}}     name -> set of elements
    weights = {"S1": 1, "S2": 1}               name -> nonnegative weight

A solution is a set of subset names.
"""

from check import todo


def cover_weight(weights, chosen):
    """Total weight of the chosen subsets. Empty selection costs 0."""
    raise todo("cover_weight")


def is_set_cover(ground, subsets, chosen):
    """Do the chosen subsets cover every element of `ground`?"""
    raise todo("is_set_cover")


def max_frequency(ground, subsets):
    """f -- the largest number of subsets any single element appears in.

    Slide 28's instance has f = 3, because element 2 is in three sets. Return 0
    for an empty ground set.
    """
    raise todo("max_frequency")


def max_subset_size(subsets):
    """g = max_j |S_j| (slide 44). 0 when there are no subsets."""
    raise todo("max_subset_size")


def optimal_set_cover(ground, subsets, weights):
    """A minimum-weight cover, by trying every collection of subsets.

    Exponential, and only here so the tests can measure the approximations
    against something true.

    Careful: do *not* stop at the smallest collection that covers. With unequal
    weights, three cheap subsets can beat two expensive ones -- you are
    minimising weight, not count.
    """
    raise todo("optimal_set_cover")


def harmonic(n):
    """H_n = 1 + 1/2 + 1/3 + ... + 1/n, as a float. H_0 = 0."""
    raise todo("harmonic")


def greedy_set_cover(ground, subsets, weights):
    """Slide 41. Returns the chosen subset names.

    Repeatedly take the subset minimising

        weight / (number of elements it covers that are not covered yet)

    Not the cheapest subset, and not the biggest -- the best *rate*. Skip any
    subset covering nothing new (its ratio is undefined, not infinite).

    Break ties by name so the answer is deterministic. Stop if nothing left can
    cover anything, rather than looping forever on an instance with no cover.
    """
    raise todo("greedy_set_cover")


def round_lp_solution(subsets, x, f):
    """Slide 28: include S_j exactly when x[j] >= 1/f.

    `x` is an optimal LP solution, given to you as a dict -- you are not
    expected to write a simplex. Return the chosen names. With f = 0 return the
    empty set rather than dividing by zero.
    """
    raise todo("round_lp_solution")


def primal_dual_set_cover(ground, subsets, weights):
    """Slide 35. Returns the chosen subset names.

        y = 0 for every element;  I = empty
        while some element e is uncovered:
            raise y[e] until some set containing e goes tight,
                i.e. until sum of y over its elements equals its weight
            add every set that just went tight

    To do the "raise until" step: for each subset containing e, its slack is
    weight minus the prices already on its elements. Raise y[e] by the smallest
    slack, and every subset whose slack was that small is now tight.

    Pick uncovered elements in a deterministic order so your answer is stable.
    """
    raise todo("primal_dual_set_cover")
