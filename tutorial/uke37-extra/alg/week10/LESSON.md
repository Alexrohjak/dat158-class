# Alg week 10 — Set cover: greedy, rounding, primal–dual

**Source: uke37, `Chapter_1.pdf` slides 12–44 and `NP-Completeness.pdf` slide
27.** Budget: ~40 min reading, ~75 min exercises. This closes uke37.

Week 9 approximated two specific problems. This week takes **one** problem and
attacks it **three** ways — greedy, linear-programming rounding, and
primal–dual. That is the real shape of `Chapter_1.pdf`: it is not a tour of
problems, it is a tour of *techniques*, and set cover is the specimen they are
all demonstrated on.

---

## 1. The problem (slide 12)

- a **ground set** `E = {e₁,…,eₙ}`;
- **subsets** `S₁,…,S_m ⊆ E`, each with a nonnegative **weight** `w_j`;
- find `I ⊆ {1,…,m}` minimising `Σ_{j∈I} w_j` subject to `⋃_{j∈I} S_j = E`.

With all `w_j = 1` it is the **unweighted** set cover problem.

Slide 14 says why this one and not another: it is *"an abstraction of several
types of problems"* — including antivirus signature selection, and vertex
cover, which you reduced to it in week 8.

Two quantities from the instance drive every bound below:

| | |
|---|---|
| `f` | the most subsets any single **element** appears in |
| `g` | the size of the largest **subset**, `max_j |S_j|` |

## 2. LP relaxation (slides 19, 25–26)

As an integer program:

```
minimize    Σ_j w_j x_j
subject to  Σ_{j : e_i ∈ S_j} x_j ≥ 1     for every element i
            x_j ∈ {0, 1}
```

`x_j = 1` means "take subset `j`", and the constraint says every element is
covered. Integer programming is NP-hard, so **relax** `x_j ∈ {0,1}` to
`x_j ≥ 0`. Now it is a linear program, solvable in polynomial time.

Slide 26 is labelled "very important", and it is:

> Every feasible ILP solution is still feasible for the LP with the same value.
> So `Z*_LP ≤ Z*_ILP = OPT`.

The LP optimum is a **lower bound on OPT** you can actually compute. That is
the same move as week 9's matching and MST — find a computable lower bound,
compare against that, never against `OPT` itself. Three techniques, one idea.

## 3. Deterministic rounding (slides 28–30)

Solve the LP, get fractional `x*`, then:

> Include `S_j` **if and only if** `x*_j ≥ 1/f`.

**It covers everything** (Lemma 1.5): each element's constraint sums at most
`f` terms to at least 1, so some term is at least `1/f` and gets rounded up.

**It costs at most `f·OPT`** (Theorem 1.6): every chosen `j` has `1 ≤ f·x*_j`,
so `Σ_{j∈I} w_j ≤ f·Σ_j w_j x*_j = f·Z*_LP ≤ f·OPT`.

Slide 28's instance has `S₁={1,2}, S₂={1,3}, S₃={2,4}, S₄={2,3,4}` and `f = 3`,
because element 2 appears in three sets.

## 4. The dual, and primal–dual (slides 31–39)

Charge each element a price `y_i ≥ 0`. Prices are *reasonable* when no subset is
overcharged: `Σ_{i : e_i ∈ S_j} y_i ≤ w_j`. Maximising total price gives the
**dual LP**.

**Weak duality**: any feasible dual value ≤ any feasible primal value, so
`Σ y_i ≤ OPT` — another computable lower bound, and this one needs no solver at
all:

```
y ← 0 ;  I ← ∅
while some element e is uncovered:
    raise y_e until some ℓ with e ∈ S_ℓ has Σ_{i ∈ S_ℓ} y_i = w_ℓ   (ℓ goes tight)
    I ← I ∪ {ℓ}
```

Take a set exactly when its constraint becomes **tight**. Theorem 1.9: this is
an `f`-approximation — the same guarantee as rounding, with no LP to solve.
Slide 33's point exactly: *special purpose algorithms are often much faster*.

## 5. Greedy (slides 40–44)

```
I ← ∅ ;  Ŝ_j ← S_j for all j
while I is not a set cover:
    ℓ = argmin over j with Ŝ_j ≠ ∅ of  w_j / |Ŝ_j|
    I ← I ∪ {ℓ}
    Ŝ_j ← Ŝ_j − S_ℓ  for all j
```

Cheapest **per newly covered element** — not cheapest, and not largest.

**Theorem 1.11:** greedy is an `H_n`-approximation, `H_n = 1 + ½ + ⅓ + … + 1/n`.
**Theorem 1.12** improves it to `H_g` using the dual, where `g` is the largest
subset size — better because `g ≤ n` always.

`H_n` grows like `ln n`: about 2.9 at `n = 10`, 5.2 at `n = 100`. Worse than the
`f` of the other two when `f` is small — and better when it is large. Which
algorithm wins depends on the *instance*, and knowing which bound applies is
the examinable skill.

> **Slides 45–46 add the sting:** these bounds are essentially the best
> possible. Unless P = NP, no polynomial algorithm approximates set cover better
> than `Θ(ln n)`. Greedy is not a placeholder for something cleverer. It is,
> up to constants, the end of the road.

---

## Paper exercises

1. Write slide 28's instance as an ILP, then as its LP relaxation. Confirm
   `f = 3`.
2. Run greedy on it by hand with all weights 1. Which sets, in what order?
3. Run primal–dual on it. Which element goes tight first, and against which set?
4. Build an instance where greedy is strictly worse than optimal. (Weights that
   differ make this much easier.)
5. For `n = 10` and `g = 3`, compare `H_n`, `H_g` and `f`. Which bound would you
   quote?

---

## The exercises

```bash
cd tutorial/uke37-extra && ./check.sh alg 10
```

`round_lp_solution` is handed an LP solution rather than solving one — a
simplex implementation is not the lesson, and the repo's tutorial deliberately
needs nothing outside the standard library. Greedy and primal–dual you write in
full, and neither needs a solver.
