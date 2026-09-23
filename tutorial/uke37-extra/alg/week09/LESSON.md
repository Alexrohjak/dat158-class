# Alg week 9 — Approximation algorithms

**Source: uke37, `NP-Completeness.pdf` slides 12–26 and `Chapter_1.pdf`
slides 3–9.** Budget: ~35 min reading, ~75 min exercises.

Last week ended with a problem nobody can solve efficiently. `Chapter_1.pdf`
slide 3 lists what you can do about it, and slide 5 picks one:

> **Relax the requirement of finding an optimal solution.** Try to find a
> solution that closely approximates the optimal one *in terms of its value*.

Not "nearly the same answer" — **provably within a factor of the best possible
answer**, and you can say what the factor is before you run it. That guarantee
is the subject.

---

## 1. What α means (np slide 13, Chapter 1 Definition 1.1)

An instance has a set of feasible solutions `F`, and each `S ∈ F` has a cost
`c(S)`. For a minimisation problem `OPT = min{c(T) : T ∈ F}`.

> An **α-approximation algorithm** runs in polynomial time and always returns a
> feasible `S` with `c(S) ≤ α·OPT`.

`α` is the **performance guarantee** (also approximation ratio, or factor).
Three words in that definition carry the weight:

- **polynomial time** — otherwise just solve it exactly;
- **always** — a guarantee, not an average. One bad instance breaks it;
- **feasible** — a fast wrong answer is not an approximation.

### The sign convention, and the warning

`Chapter_1.pdf` slide 7 sets `α > 1` for minimisation and `α < 1` for
maximisation, then adds:

> Other books may define `α > 1` also for maximization problems.

Know which convention is in front of you. Under this one, a 2-approximation for
a minimisation problem gives at most twice the optimum, and a ½-approximation
for a maximisation problem gives at least half.

Slide 14 gives the range: some problems admit no finite `α` at all, others
admit `α` as close to 1 as you like — for a price. That price has a name.

### PTAS (Chapter 1, Definition 1.2)

A **polynomial-time approximation scheme** is a family `{A_ε}`, one algorithm
per `ε > 0`, where `A_ε` is a `(1+ε)`-approximation for minimisation. Smaller
`ε`, longer running time. Knapsack and Euclidean TSP have one.

## 2. Vertex cover in 2 (np slides 15–20)

```
Algorithm VertexCoverApprox(G)
  C = Ø
  while G still has edges do
      select an edge e = (v, w)
      add BOTH v and w to C
      remove every edge incident to v or w
  return C
```

Adding *both* endpoints looks wasteful — one would have covered `e`. That waste
is exactly what buys the guarantee. Slide 19:

> At least one vertex of each selected edge has to be in *any* vertex cover,
> otherwise that edge is not covered. Hence the cover found cannot contain more
> than twice the optimal number.

The selected edges share no endpoints — they are a **matching** — so `OPT` must
contain at least one vertex per selected edge, and the algorithm used two.
`|C| ≤ 2·OPT`.

Note the shape of that argument, because it is the shape of every
approximation proof: you never compute `OPT`. You find a **lower bound** on it
(here: the matching size) and compare your answer to *that*.

### The factor 2 is tight (slide 20)

The proof shows `α ≤ 2`. To show it is not better, slide 20 asks for an
instance achieving it — and a **perfect matching** does. On `k` disjoint edges
the algorithm takes all `2k` vertices while `k` suffice. Ratio exactly 2, for
every `k`. That is `tight_example` below.

## 3. TSP in 2 (np slides 21–26)

Find the minimum-weight cycle visiting every vertex. In general this admits no
finite `α` at all — so slide 21 restricts to costs satisfying the **triangle
inequality**:

> `c(u,v) + c(v,w) ≥ c(u,w)` — the direct edge is never longer than the detour.

Then (slide 23):

1. build a **minimum spanning tree** `M` (Kruskal, Prim–Jarnik, Borůvka);
2. **duplicate every edge**, making all degrees even, so an **Euler tour** `E`
   exists;
3. build a tour `T` from `E` by **skipping already-visited vertices**.

Why it is a 2-approximation, in three lines:

- deleting one edge from the optimal tour leaves a spanning tree, so
  `MST ≤ OPT`;
- the doubled tree costs `2·MST`, and the Euler tour uses each edge once, so
  `E = 2·MST`;
- shortcutting only ever *shortens*, by the triangle inequality — so
  `T ≤ E = 2·MST ≤ 2·OPT`.

Step 3 is where the triangle inequality is spent. Without it, skipping a vertex
could cost more than visiting it, and the whole argument collapses.

In practice this does much better than 2. On the exercises' rectangle it returns
a tour of 16 against an optimum of 14 — a ratio of 1.14, not 2. The guarantee is
a promise about the worst case, not a prediction.

---

## Paper exercises

1. Run the vertex-cover algorithm on `a–b, b–c, c–d, d–a, a–c` by hand. How big
   is the cover? What is the true optimum? What ratio did you get?
2. Draw the perfect matching on 6 vertices and confirm the ratio is exactly 2.
3. For four points at the corners of a 3×4 rectangle, build the MST, double it,
   read off an Euler tour, and shortcut it. Compare with the best tour.
4. Where exactly does the TSP proof use the triangle inequality? Construct a
   non-metric instance where shortcutting makes the tour *worse*.

---

## The exercises

```bash
cd tutorial/uke37-extra && ./check.sh alg 9
```

A weighted graph is a dict of dicts: `graph[u][v]` is the cost of `(u, v)`,
symmetric, with `graph[u][u] == 0`.
