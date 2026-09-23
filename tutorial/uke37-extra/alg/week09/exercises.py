"""Alg week 9 — approximation algorithms. Read LESSON.md first.

    cd tutorial/uke37-extra && ./check.sh alg 9

Unweighted graphs are edge lists, as in week 8. Weighted graphs are dicts of
dicts: graph[u][v] is the cost of the edge, symmetric, graph[u][u] == 0.
"""

from check import todo


# --- vertex cover ----------------------------------------------------------

def vertex_cover_approx(edges):
    """np slide 16. Returns a set of vertices.

    While edges remain: take one, add BOTH its endpoints, and remove every
    edge incident to either. Adding both is not a bug -- it is what makes the
    2-approximation proof work.

        vertex_cover_approx([("a","b")]) == {"a", "b"}
        vertex_cover_approx([])          == set()

    Take the edges in sorted order so your answer is deterministic; any
    selection rule is a valid 2-approximation, but the tests are easier to
    trust when the output does not wobble.
    """
    raise todo("vertex_cover_approx")


def approximation_ratio(cost, optimum):
    """cost / optimum, as a float.

    When optimum is 0, return 1.0 if cost is also 0 and float("inf") otherwise
    -- a nonzero answer to a zero-cost instance is infinitely bad.
    """
    raise todo("approximation_ratio")


def tight_example(k):
    """np slide 20: an edge list on which the algorithm achieves ratio exactly 2.

    A perfect matching -- k disjoint edges. The algorithm takes both endpoints
    of every edge, all 2k of them; k suffice.

        tight_example(2)   # 2 disjoint edges, 4 vertices

    Return exactly k edges sharing no vertices.
    """
    raise todo("tight_example")


# --- TSP -------------------------------------------------------------------

def satisfies_triangle_inequality(graph):
    """np slide 21: is c(u,v) + c(v,w) >= c(u,w) for every triple of distinct
    vertices?"""
    raise todo("satisfies_triangle_inequality")


def mst_edges(graph):
    """A minimum spanning tree, as a sorted list of sorted (u, v) tuples.

    Prim-Jarnik is easiest here: start from one vertex and repeatedly add the
    cheapest edge leaving the set you have. Break ties by vertex name so the
    answer is deterministic.

    A graph on n vertices gives exactly n-1 tree edges (0 for the empty graph).
    """
    raise todo("mst_edges")


def mst_weight(graph):
    """The total weight of the minimum spanning tree."""
    raise todo("mst_weight")


def tsp_tour(graph):
    """np slides 23-26. A list of vertices, each exactly once, starting from
    the alphabetically first.

    Build the MST, then walk it depth-first from that vertex, visiting
    neighbours in sorted order and skipping anything already seen. That walk is
    the Euler tour of the doubled tree with the repeats shortcut away, which is
    steps 2 and 3 of the slide in one pass.

    The tour is a *cycle*: the last vertex joins back to the first, and
    `tour_cost` closes it for you.
    """
    raise todo("tsp_tour")


def tour_cost(graph, tour):
    """The cost of the closed cycle visiting `tour` in order and returning to
    the start.

        tour_cost(g, ["a","b","c"]) == g["a"]["b"] + g["b"]["c"] + g["c"]["a"]

    A tour of fewer than 2 vertices costs 0.
    """
    raise todo("tour_cost")


def optimal_tour_cost(graph):
    """The true optimum, by trying every permutation.

    Fix the first vertex (every cycle can be rotated to start anywhere) and
    permute the rest. Exponential -- it exists so the tests can measure how good
    the approximation actually is.
    """
    raise todo("optimal_tour_cost")
