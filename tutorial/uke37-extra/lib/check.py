"""The tutorial test harness. You never edit this file.

A week's `tests.py` builds a `Check`, calls `.eq` / `.true` / `.close` once per
thing worth verifying, and calls `.done()`. Nothing here imports anything the
standard library does not already have, so the tutorial runs with no install
step and no virtual environment.

Three outcomes, and the difference between the last two is the point:

    ok      your answer matched
    FAIL    your answer ran and was wrong
    todo    you have not written it yet

A stub that still raises `NotImplementedError` reports as `todo`, not `FAIL`,
so you can work one exercise at a time and watch the ok count climb instead of
staring at a wall of red. Exit status is 0 only when everything is ok.

Anything else your code raises is caught and shown with its type and message —
a crash is a failure, but it should never take the whole run down with it, or
one broken exercise would hide the fifty that pass.
"""

from __future__ import annotations

import sys
import traceback

# Only colour a real terminal. Piped into a file or a pager, this would just
# leave escape sequences in the text.
_TTY = sys.stdout.isatty()


def _paint(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _TTY else text


def _show(value: object, limit: int = 68) -> str:
    """A value, short enough to sit on one line of the report."""
    try:
        text = repr(value)
    except Exception:                     # a __repr__ of your own that raises
        text = f"<unreprable {type(value).__name__}>"
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


class Check:
    def __init__(self, title: str):
        self.title = title
        self.ok = 0
        self.failed: list[str] = []
        self.todo: set[str] = set()
        print()
        print(_paint(title, "1"))
        print("-" * len(title))

    # -- the three verdicts ------------------------------------------------

    def _pass(self, label: str) -> None:
        self.ok += 1

    def _fail(self, label: str, detail: str) -> None:
        self.failed.append(label)
        print(f"  {_paint('FAIL', '31;1')}  {label}")
        for line in detail.splitlines():
            print(f"          {line}")

    def _todo(self, label: str, name: str) -> None:
        # One `todo` line per unimplemented function, however many checks it
        # has. Fifty identical "not written yet" lines teach you nothing.
        if name not in self.todo:
            self.todo.add(name)
            print(f"  {_paint('todo', '33')}  {name} — not written yet")

    # -- the assertions a tests.py calls -----------------------------------

    def eq(self, label: str, thunk, want) -> None:
        """`thunk()` must equal `want`. Pass a lambda, not a value: the harness
        has to be the one to call it, or an unimplemented stub would raise
        before it ever reached here.

        `want` may itself be a callable, for the case where the expected value
        has to be computed from the student's own code — comparing two ways of
        building the same trie, say. It is then called inside the same guard,
        so an unwritten stub on either side still reports `todo`."""
        try:
            got = thunk()
            if callable(want):
                want = want()
        except NotImplementedError as exc:
            self._todo(label, str(exc) or label)
            return
        except Exception as exc:
            self._fail(label, f"raised {type(exc).__name__}: {exc}\n"
                              f"{_last_frame()}")
            return
        if got == want:
            self._pass(label)
        else:
            self._fail(label, f"expected  {_show(want)}\ngot       {_show(got)}")

    def true(self, label: str, thunk) -> None:
        """`thunk()` must be truthy. For properties, where naming the expected
        value would give the answer away."""
        try:
            got = thunk()
        except NotImplementedError as exc:
            self._todo(label, str(exc) or label)
            return
        except Exception as exc:
            self._fail(label, f"raised {type(exc).__name__}: {exc}\n"
                              f"{_last_frame()}")
            return
        if got:
            self._pass(label)
        else:
            self._fail(label, f"expected something truthy, got {_show(got)}")

    def close(self, label: str, thunk, want: float, tol: float = 1e-9) -> None:
        """`thunk()` must be within `tol` of `want`. For anything with a float
        in it — accuracies, ratios, approximation factors."""
        try:
            got = thunk()
        except NotImplementedError as exc:
            self._todo(label, str(exc) or label)
            return
        except Exception as exc:
            self._fail(label, f"raised {type(exc).__name__}: {exc}\n"
                              f"{_last_frame()}")
            return
        try:
            near = abs(float(got) - float(want)) <= tol
        except (TypeError, ValueError):
            self._fail(label, f"expected a number near {want}, got {_show(got)}")
            return
        if near:
            self._pass(label)
        else:
            self._fail(label, f"expected  {want} (±{tol})\ngot       {_show(got)}")

    # -- the report --------------------------------------------------------

    def done(self) -> int:
        total = self.ok + len(self.failed) + len(self.todo)
        print()
        bits = [f"{self.ok} ok"]
        if self.failed:
            bits.append(_paint(f"{len(self.failed)} FAIL", "31;1"))
        if self.todo:
            bits.append(_paint(f"{len(self.todo)} todo", "33"))
        print(f"  {' · '.join(bits)}   ({self.ok}/{self.ok + len(self.failed)} "
              f"of what you have written)")

        if self.todo and not self.failed and self.ok == 0:
            print()
            print("  Nothing written yet. Start with the first todo above.")
        elif self.todo and not self.failed:
            print()
            print("  Everything you have written is correct. Keep going.")
        elif not self.todo and not self.failed and total:
            print()
            print(_paint("  Week complete.", "32;1"))
            print("  Now ask for an idiom review — the tests cannot tell you")
            print("  that your twenty lines should have been five.")
        print()
        return 1 if (self.failed or self.todo) else 0


def _last_frame() -> str:
    """The line in *your* code where it blew up, not the harness's stack."""
    frames = traceback.extract_tb(sys.exc_info()[2])
    for frame in reversed(frames):
        if "lib/check.py" not in frame.filename.replace("\\", "/"):
            where = frame.filename.rsplit("/", 1)[-1]
            return f"at {where}:{frame.lineno}  {(frame.line or '').strip()}"
    return ""


def todo(name: str):
    """What an unwritten exercise raises. In `exercises.py`:

        def brute_force_match(text, pattern):
            raise todo("brute_force_match")
    """
    return NotImplementedError(name)
