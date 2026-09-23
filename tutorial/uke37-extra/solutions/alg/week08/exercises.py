"""Alg week 8 — reference solutions."""

from itertools import combinations


def normalise(edges):
    return sorted({tuple(sorted(e)) for e in edges})


def vertices_of(edges):
    return {v for e in edges for v in e}


def is_vertex_cover(edges, cover):
    cover = set(cover)
    return all(v in cover or w in cover for v, w in edges)


def verify_vertex_cover(edges, k, certificate):
    # The polynomial-time verifier: check the size, then check every edge.
    # This is what puts Vertex Cover in NP (slide 6).
    return len(set(certificate)) <= k and is_vertex_cover(edges, certificate)


def min_vertex_cover(edges, vertices=None):
    verts = sorted(vertices) if vertices is not None else sorted(vertices_of(edges))
    for size in range(len(verts) + 1):
        for candidate in combinations(verts, size):
            if is_vertex_cover(edges, candidate):
                return set(candidate)
    return set(verts)


def has_vertex_cover(edges, k, vertices=None):
    return len(min_vertex_cover(edges, vertices)) <= k


def is_independent_set(edges, subset):
    subset = set(subset)
    return not any(v in subset and w in subset for v, w in edges)


def complement(vertices, subset):
    return set(vertices) - set(subset)


def vertex_cover_to_set_cover(edges, vertices=None):
    """approx slide 14: ground set is the edges, and there is one subset per
    vertex containing every edge incident to it."""
    edges = normalise(edges)
    verts = sorted(vertices) if vertices is not None else sorted(vertices_of(edges))
    ground = set(edges)
    subsets = {v: {e for e in edges if v in e} for v in verts}
    return ground, subsets


def is_set_cover(ground, subsets, chosen):
    covered = set()
    for name in chosen:
        covered |= subsets[name]
    return covered >= set(ground)
