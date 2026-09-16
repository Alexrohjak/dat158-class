#!/usr/bin/env python3
"""Run the tests for one week of the DAT158 tutorial.

    ./check.py ml01              run ML week 1's tests against YOUR exercises.py
    ./check.py ml1               same thing — the zero is optional
    ./check.py alg01 --solution  run them against the reference answers
    ./check.py --list            what weeks exist, and how far you are

Exit status is 0 only when every check passes and nothing is left todo.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from lib.check import Suite, Todo  # noqa: E402


def normalise(name: str) -> str:
    """ml1, ML01, alg-1 all mean the same folder."""
    m = re.fullmatch(r"(ml|alg)[-_]?0*(\d+)", name.strip(), re.I)
    if not m:
        return name
    return f"{m.group(1).lower()}{int(m.group(2)):02d}"


def weeks() -> list[str]:
    return sorted(p.name for p in HERE.iterdir()
                  if p.is_dir() and re.fullmatch(r"(ml|alg)\d\d", p.name))


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_week(week: str, solution: bool, quiet: bool) -> int:
    src = HERE / ("solutions/" + week if solution else week)
    ex_path = src / "exercises.py"
    tests_path = HERE / week / "tests.py"

    if not (HERE / week).is_dir():
        print(f"error: no such week: {week}", file=sys.stderr)
        print(f"       have: {', '.join(weeks()) or '(none)'}", file=sys.stderr)
        return 2
    if not ex_path.exists():
        what = "reference solution" if solution else "exercises.py"
        print(f"error: no {what} for {week}", file=sys.stderr)
        if solution:
            print("       some weeks ship without one on purpose — see tutorial/README.md",
                  file=sys.stderr)
        return 2

    # The week's own folder goes on the path first so `import exercises` inside
    # a test module resolves to the copy we were actually asked to run.
    sys.path.insert(0, str(src))
    ex = load(ex_path, "exercises")
    tests = load(tests_path, f"tests_{week}")

    suite = Suite(week)
    try:
        tests.build(ex, suite)
    except Todo:
        print(f"error: {week}/tests.py calls an exercise while building the suite,",
              file=sys.stderr)
        print("       so an unwritten stub stops it before any check can run.",
              file=sys.stderr)
        print("       Every call to an exercise must be inside a lambda. This is a",
              file=sys.stderr)
        print("       bug in the tests, not in your answers — please report it.",
              file=sys.stderr)
        return 2
    label = f"{week}  ({'reference solution' if solution else 'your answers'})"
    print(f"\n{label}\n{'-' * len(label)}")
    passed, failed, pending = suite.run(quiet=quiet)

    total = passed + failed + pending
    print(f"\n  {passed}/{total} passed", end="")
    if pending:
        print(f", {pending} todo", end="")
    if failed:
        print(f", {failed} FAILED", end="")
    print("\n")

    if failed:
        return 1
    if pending:
        return 1
    print("  All green. Next: read the checklist at the end of LESSON.md.\n")
    return 0


def summarise() -> int:
    print("\nDAT158 tutorial\n---------------")
    for w in weeks():
        has_lesson = (HERE / w / "LESSON.md").exists()
        has_sol = (HERE / "solutions" / w / "exercises.py").exists()
        stub = (HERE / w / "exercises.py")
        n_todo = (len(re.findall(r"^\s+todo\(\)\s*$", stub.read_text(), re.M))
                  if stub.exists() else 0)
        bits = []
        bits.append("lesson" if has_lesson else "no lesson")
        bits.append(f"{n_todo} stubs left" if n_todo else "no stubs left")
        bits.append("solutions" if has_sol else "no solutions (by design)")
        print(f"  {w:<7} {' · '.join(bits)}")
    print("\n  ./check.py <week>   to run one\n")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(add_help=True, description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("week", nargs="?", help="e.g. ml01, ml1, alg01")
    p.add_argument("-s", "--solution", action="store_true",
                   help="run against the reference answers instead of yours")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="only show what is not yet passing")
    p.add_argument("-l", "--list", action="store_true", help="list the weeks")
    args = p.parse_args()

    if args.list or not args.week:
        return summarise()
    return run_week(normalise(args.week), args.solution, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
