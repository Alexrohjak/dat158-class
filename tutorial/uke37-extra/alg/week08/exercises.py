"""Alg week 8 — NP-completeness. Read LESSON.md first.

    cd tutorial/uke37-extra && ./check.sh alg 8

A graph is a list of edges, each a pair of vertices: [("a","b"), ("b","c")].
Vertices are whatever you like -- strings here. Functions that need to know
about isolated vertices take an explicit `vertices` argument.
"""

from check import todo


def normalise(edges):
    """Edges as a sorted list of sorted tuples, with duplicates removed.

        normalise([("b","a"), ("a","b"), ("b","c")]) == [("a","b"), ("b","c")]

    Undirected edges have no direction, so ("a","b") and ("b","a") are the
    same edge and must not be counted twice.
    """
    raise todo("normalise")


def vertices_of(edges):
    """Every vertex mentioned by an edge, as a set."""
    raise todo("vertices_of")


def is_vertex_cover(edges, cover):
    """Slide 15: does every edge have at least one endpoint in `cover`?

        is_vertex_cover([("a","b")], ["a"])  == True
        is_vertex_cover([("a","b")], ["c"])  == False
        is_vertex_cover([], [])              == True
    """
    raise todo("is_vertex_cover")


def verify_vertex_cover(edges, k, certificate):
    """The polynomial-time verifier that puts Vertex Cover in NP.

    Given a proposed cover, check it has at most k vertices and that it really
    covers every edge. Slide 6 walks through exactly this.

    Note what it does NOT do: search. Verifying is easy, finding is hard, and
    that gap is the whole of NP.
    """
    raise todo("verify_vertex_cover")


def min_vertex_cover(edges, vertices=None):
    """A smallest vertex cover, found by trying every subset.

    Try all subsets of size 0, then 1, then 2... and return the first that
    covers. `itertools.combinations` is the tool.

    This is exponential and that is the point -- it is the honest brute force
    the rest of the fortnight is trying to avoid. The tests keep the graphs
    tiny.
    """
    raise todo("min_vertex_cover")


def has_vertex_cover(edges, k, vertices=None):
    """The *decision* version: does G have a vertex cover of at most k vertices?

    Slide 4: a decision problem is one whose output is yes or no. This is the
    NP-complete one; `min_vertex_cover` is the optimisation version.
    """
    raise todo("has_vertex_cover")


def is_independent_set(edges, subset):
    """Is no edge entirely inside `subset`?

        is_independent_set([("a","b")], ["a"])      == True
        is_independent_set([("a","b")], ["a","b"])  == False
    """
    raise todo("is_independent_set")


def complement(vertices, subset):
    """The vertices not in `subset`, as a set."""
    raise todo("complement")


def vertex_cover_to_set_cover(edges, vertices=None):
    """The reduction on approx slide 14. Returns (ground, subsets).

    - the **ground set** is the set of edges;
    - there is **one subset per vertex**, containing every edge incident to it.

    Then a set cover corresponds exactly to a vertex cover: choosing vertex v's
    subset means putting v in the cover, and covering every edge means every
    edge has a chosen endpoint.

        vertex_cover_to_set_cover([("a","b")])
            == ({("a","b")}, {"a": {("a","b")}, "b": {("a","b")}})

    `subsets` is a dict keyed by vertex. Use normalised edges so the tuples in
    the ground set and in the subsets are the same objects.
    """
    raise todo("vertex_cover_to_set_cover")


def is_set_cover(ground, subsets, chosen):
    """Does the union of the chosen subsets contain every element of `ground`?

        is_set_cover({1,2}, {"x": {1}, "y": {2}}, ["x","y"]) == True
    """
    raise todo("is_set_cover")
