# Alg week 8 — NP-completeness

**Source: uke37, `NP-Completeness.pdf` slides 1–11.** Budget: ~35 min reading,
~60 min exercises.

The text-processing half was about doing things fast. This half opens by
admitting that for some problems **nobody knows how**, and then asks what you do
about it. Week 9 is the answer; this week is the diagnosis.

---

## 1. Vertex cover, the running example

Slide 2 states it in one sentence:

> Given a graph `G`, a **vertex cover** is a subset `C` of the vertices such
> that for every edge `(v, w)`, `v ∈ C` **or** `w ∈ C` (possibly both). Does
> `G` have a vertex cover of at most `k` vertices?

Trivially easy to *state*. Nobody knows how to solve it efficiently. That gap —
simple to describe, apparently impossible to compute — is what the whole
fortnight is about.

## 2. Decision problems (slide 4)

> Computational problems whose intended output is either "yes" or "no".

Note the restriction. The complexity classes are defined over *decision*
problems, so "find the smallest vertex cover" is not in P or NP as stated —
"is there one of size at most `k`?" is. In the exercises, `min_vertex_cover` is
the optimisation version and `has_vertex_cover` is the decision version. Keep
the two straight; the exam will ask.

## 3. P and NP (slides 5–7)

**P** — decision problems solvable in worst-case polynomial time.

**NP** — contains P, and in addition every decision problem where you can
**verify a "yes" answer** in polynomial time.

Slide 6 does vertex cover explicitly:

> Have the graph `G` and a set of vertices `C`. Check that `C` contains at most
> `k` vertices. Run through all edges of `G` and verify at least one endpoint
> is in `C`. Hence Vertex Cover is in NP.

That is `verify_vertex_cover` in the exercises, and it is worth noticing how
*boring* it is — two loops. That is the point. **Verifying is easy. Finding is
hard.** All of NP lives in that gap.

> We do not know if P = NP, but most scientists believe P ≠ NP.

## 4. NP-complete (slides 8–9)

The hardest problems in NP: **if one of them is solvable in polynomial time,
all of them are.** To prove a problem NP-complete you must

1. show it is in NP, and
2. show a known NP-complete problem **reduces** to it in polynomial time.

Step 2 needs a starting point, and the **Cook–Levin theorem** supplies it:
Boolean satisfiability is NP-complete, proved from first principles. Every
later NP-completeness proof rests on it, directly or indirectly.

## 5. Reduction, concretely

Reductions sound abstract until you build one. Here is the one you will write,
from `Chapter_1.pdf` slide 14 — **vertex cover as set cover**:

| set cover | ← | vertex cover |
|---|---|---|
| ground set | is | the **edges** |
| one subset per… | | **vertex**, containing its incident edges |

Choosing vertex `v`'s subset means putting `v` in the cover. Covering the whole
ground set means every edge has a chosen endpoint. The two problems are the
same problem wearing different clothes — and that is what a reduction *is*.

## 6. Vertex cover and independent sets

One more fact, cheap and worth knowing: `C` is a vertex cover **if and only if**
`V \ C` is an independent set (no edge inside it). Proof in one line: an edge
inside `V \ C` is an edge with neither endpoint in `C`, which is exactly the
condition for `C` to fail.

So minimum vertex cover and maximum independent set are the same problem, and
solving one solves the other. That is a reduction too — the shortest one in the
chapter.

---

## Paper exercises

1. Draw a graph where the greedy "pick the highest-degree vertex" rule does
   **not** find a minimum vertex cover.
2. For `K₄` (4 vertices, all 6 edges), what is the minimum vertex cover?
   Generalise to `Kₙ`.
3. Write out the set-cover instance produced by reducing the 5-edge graph
   `a–b, b–c, c–d, d–a, a–c`. How many ground elements, how many subsets?
4. State in one sentence why "verify" and "solve" being different is the entire
   content of P vs NP.

---

## The exercises

```bash
cd tutorial/uke37-extra && ./check.sh alg 8
```

`min_vertex_cover` is deliberately exponential — you are writing the slow thing
so that next week's fast-but-approximate thing has something to be compared
against.
