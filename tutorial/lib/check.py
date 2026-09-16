"""The check harness. You never edit this file.

It exists so a week's tests can be written as data rather than as a pile of
asserts, and so an unimplemented stub reports as `todo` instead of `FAIL` —
you should be able to work one exercise at a time and watch the count climb.

No third-party dependencies. numpy is imported lazily, only if a comparison
actually involves an array, so the harness still runs in a bare interpreter.
"""

from __future__ import annotations

import math
import traceback


class Todo(Exception):
    """Raised by an unimplemented stub. Reported as `todo`, never as a failure."""


def todo():
    """Body of every stub you have not written yet."""
    raise Todo()


# --- comparison ------------------------------------------------------------

def _is_array(x) -> bool:
    return type(x).__module__ == "numpy" and hasattr(x, "shape")


def _same(got, want, tol: float) -> bool:
    """Structural equality, with a tolerance for anything float-shaped."""
    if _is_array(got) or _is_array(want):
        import numpy as np
        got, want = np.asarray(got), np.asarray(want)
        if got.shape != want.shape:
            return False
        if got.dtype.kind in "fc" or want.dtype.kind in "fc":
            return bool(np.allclose(got, want, rtol=tol, atol=tol))
        return bool(np.array_equal(got, want))

    if isinstance(got, float) or isinstance(want, float):
        try:
            if math.isnan(got) and math.isnan(want):
                return True
        except TypeError:
            return False
        try:
            return math.isclose(got, want, rel_tol=tol, abs_tol=tol)
        except TypeError:
            return False

    if isinstance(got, (list, tuple)) and isinstance(want, (list, tuple)):
        if type(got) is not type(want) or len(got) != len(want):
            return False
        return all(_same(g, w, tol) for g, w in zip(got, want))

    if isinstance(got, dict) and isinstance(want, dict):
        if set(got) != set(want):
            return False
        return all(_same(got[k], want[k], tol) for k in want)

    return got == want


def _show(x) -> str:
    s = repr(x)
    if _is_array(x):
        s = f"array({x.tolist()!r})" if x.size <= 12 else f"array(shape={x.shape})"
    return s if len(s) <= 220 else s[:217] + "..."


# --- the suite -------------------------------------------------------------

class Suite:
    """Collects checks, runs them, reports.

    Every check takes a *thunk* — a zero-argument lambda — so that a Todo
    raised inside a stub is caught here rather than at collection time.
    """

    def __init__(self, title: str):
        self.title = title
        self._checks: list[tuple[str, object, object, float, str]] = []

    def eq(self, label: str, thunk, expected, tol: float = 1e-9):
        """Assert the thunk returns `expected`."""
        self._checks.append((label, thunk, expected, tol, "eq"))

    def close(self, label: str, thunk, expected, tol: float = 1e-6):
        """Assert equality with a looser tolerance — for anything computed in floats."""
        self._checks.append((label, thunk, expected, tol, "eq"))

    def true(self, label: str, thunk):
        """Assert the thunk returns something truthy."""
        self._checks.append((label, thunk, True, 1e-9, "true"))

    def raises(self, label: str, thunk, exc):
        """Assert the thunk raises `exc`."""
        self._checks.append((label, thunk, exc, 1e-9, "raises"))

    # -- running --

    def run(self, quiet: bool = False) -> tuple[int, int, int]:
        passed = failed = pending = 0
        width = max((len(c[0]) for c in self._checks), default = 0)

        for label, thunk, expected, tol, kind in self._checks:
            try:
                got = thunk()
            except Todo:
                pending += 1
                if not quiet:
                    print(f"  todo  {label}")
                continue
            except Exception as exc:
                if kind == "raises" and isinstance(exc, expected):
                    passed += 1
                    if not quiet:
                        print(f"  ok    {label}")
                    continue
                failed += 1
                print(f"  FAIL  {label.ljust(width)}  raised {type(exc).__name__}: {exc}")
                for line in traceback.format_exc().strip().splitlines()[-3:-1]:
                    print(f"        {line.strip()}")
                continue

            if kind == "raises":
                failed += 1
                print(f"  FAIL  {label.ljust(width)}  expected {expected.__name__}, "
                      f"returned {_show(got)}")
            elif kind == "true":
                if got:
                    passed += 1
                    if not quiet:
                        print(f"  ok    {label}")
                else:
                    failed += 1
                    print(f"  FAIL  {label.ljust(width)}  expected something truthy, "
                          f"got {_show(got)}")
            elif _same(got, expected, tol):
                passed += 1
                if not quiet:
                    print(f"  ok    {label}")
            else:
                failed += 1
                print(f"  FAIL  {label}")
                print(f"        expected  {_show(expected)}")
                print(f"        got       {_show(got)}")

        return passed, failed, pending
