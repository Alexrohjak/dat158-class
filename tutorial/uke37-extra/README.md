# Uke 37 extra — NP-completeness, approximation, set cover

Three tested weeks for uke 37's algorithms material, which the main tutorial
(`alg01`, … run by `../check.py`) does not cover yet:

| Week | Covers | Checks |
|---|---|:--:|
| `alg/week08` | NP-completeness: vertex cover, verifiers, the reduction to set cover | 53 |
| `alg/week09` | Approximation: the vertex-cover 2-approximation, metric TSP by MST | 40 |
| `alg/week10` | Set cover three ways: LP rounding, primal–dual, greedy | 43 |

They were written on another clone of this repo, with their own harness, so they
keep it: `lib/check.py` here and `check.sh` to run them. `../check.py` only picks
up folders named `alg01`/`ml01`, so it doesn't see this one.

```bash
cd tutorial/uke37-extra
./check.sh alg 8               # your exercises.py
./check.sh alg 8 --solution    # the reference, in solutions/
./check.sh alg 8 --repl        # a Python prompt with your code loaded
./check.sh --all               # all three, summarised
```

The week numbers (8–10) are from that other tutorial's numbering, where weeks
1–7 were uke 35's text processing. The main tutorial's `alg01` covers those now.
Everything is standard library only. As in the main tutorial, a stub reports
`todo`, not `FAIL`. Read `LESSON.md` first, and open `solutions/` only after
you've tried.

If these are rewritten for `../check.py` one day, they become `alg02`–`alg04`
and this folder goes away.
