"""Alg week 9 — reference solutions."""

from itertools import permutations


# --- vertex cover, np slides 15-20 ----------------------------------------

def vertex_cover_approx(edges):
    """Slide 16, verbatim: while G still has edges, take any edge, put BOTH
    endpoints in C, and delete every edge incident to either."""
    remaining = sorted({tuple(sorted(e)) for e in edges})
    cover = set()
    while remaining:
        v, w = remaining[0]
        cover.add(v)
        cover.add(w)
        remaining = [e for e in remaining if v not in e and w not in e]
    return cover


def approximation_ratio(cost, optimum):
    if optimum == 0:
        return 1.0 if cost == 0 else float("inf")
    return cost / optimum


def tight_example(k):
    """np slide 20: a perfect matching. The algorithm takes both endpoints of
    every edge -- all 2k vertices -- while k of them suffice."""
    return [(f"u{i}", f"v{i}") for i in range(k)]


# --- TSP, np slides 21-26 -------------------------------------------------

def satisfies_triangle_inequality(graph):
    """Slide 21: c(u,v) + c(v,w) >= c(u,w) for every triple."""
    verts = list(graph)
    return all(graph[u][v] + graph[v][w] >= graph[u][w]
               for u in verts for v in verts for w in verts
               if u != v and v != w and u != w)


def mst_edges(graph):
    """Prim-Jarnik. Returns the tree's edges as sorted tuples."""
    verts = sorted(graph)
    if not verts:
        return []
    inside = {verts[0]}
    tree = []
    while len(inside) < len(verts):
        best = min(((graph[u][v], u, v) for u in inside for v in verts
                    if v not in inside), key=lambda t: (t[0], t[1], t[2]))
        _, u, v = best
        inside.add(v)
        tree.append(tuple(sorted((u, v))))
    return sorted(tree)


def mst_weight(graph):
    return sum(graph[u][v] for u, v in mst_edges(graph))


def tsp_tour(graph):
    """Slides 23-26. Build an MST, walk it (which is the Euler tour of the
    doubled tree), and skip vertices already visited."""
    verts = sorted(graph)
    if not verts:
        return []
    tree = mst_edges(graph)
    adjacency = {v: [] for v in verts}
    for u, v in tree:
        adjacency[u].append(v)
        adjacency[v].append(u)

    visited, tour = set(), []

    def walk(node):
        visited.add(node)
        tour.append(node)
        for nxt in sorted(adjacency[node]):
            if nxt not in visited:
                walk(nxt)

    walk(verts[0])
    return tour


def tour_cost(graph, tour):
    """The cost of the closed cycle visiting `tour` in order."""
    if len(tour) < 2:
        return 0
    return sum(graph[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


def optimal_tour_cost(graph):
    """Brute force over every permutation. Exponential, and only for testing."""
    verts = sorted(graph)
    if len(verts) < 2:
        return 0
    first, rest = verts[0], verts[1:]
    return min(tour_cost(graph, (first,) + p) for p in permutations(rest))
