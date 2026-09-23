"""Alg week 10 — reference solutions."""

from itertools import combinations


def cover_weight(weights, chosen):
    return sum(weights[j] for j in chosen)


def is_set_cover(ground, subsets, chosen):
    covered = set()
    for j in chosen:
        covered |= set(subsets[j])
    return covered >= set(ground)


def max_frequency(ground, subsets):
    """f: the largest number of subsets any single element appears in."""
    if not ground:
        return 0
    return max(sum(1 for s in subsets.values() if e in s) for e in ground)


def max_subset_size(subsets):
    """g = max_j |S_j| (slide 44)."""
    return max((len(s) for s in subsets.values()), default=0)


def optimal_set_cover(ground, subsets, weights):
    # Every size is tried, not just the smallest that works: with unequal
    # weights a larger collection can be cheaper than a smaller one.
    names = sorted(subsets)
    best = None
    for size in range(len(names) + 1):
        for chosen in combinations(names, size):
            if is_set_cover(ground, subsets, chosen):
                cost = cover_weight(weights, chosen)
                if best is None or cost < best[0]:
                    best = (cost, set(chosen))
    return best[1] if best else set()


def harmonic(n):
    return sum(1.0 / k for k in range(1, n + 1))


def greedy_set_cover(ground, subsets, weights):
    """Slide 41: repeatedly take the set minimising weight per newly-covered
    element."""
    uncovered = set(ground)
    chosen = set()
    while uncovered:
        best = None
        for j in sorted(subsets):
            new = len(set(subsets[j]) & uncovered)
            if new == 0:
                continue
            ratio = weights[j] / new
            if best is None or ratio < best[0]:
                best = (ratio, j)
        if best is None:
            break                       # nothing left can cover anything
        chosen.add(best[1])
        uncovered -= set(subsets[best[1]])
    return chosen


def round_lp_solution(subsets, x, f):
    """Slide 28: include S_j exactly when x_j >= 1/f."""
    if f == 0:
        return set()
    return {j for j in subsets if x.get(j, 0) >= 1.0 / f}


def primal_dual_set_cover(ground, subsets, weights):
    """Slide 35. Raise the price of an uncovered element until some set
    containing it becomes tight, then take that set."""
    y = {e: 0.0 for e in ground}
    chosen = set()
    covered = set()
    while set(ground) - covered:
        e = sorted(set(ground) - covered, key=str)[0]
        # How much room is left under each set's weight.
        containing = [j for j in sorted(subsets) if e in subsets[j]]
        if not containing:
            break
        slack = {j: weights[j] - sum(y[i] for i in subsets[j] if i in y)
                 for j in containing}
        raise_by = min(slack.values())
        y[e] += raise_by
        for j in containing:
            if abs(slack[j] - raise_by) < 1e-12:
                chosen.add(j)
                covered |= set(subsets[j])
    return chosen
