#!/usr/bin/env bash
# Run the tests for one week of the DAT158 tutorial.
#
#   ./check.sh alg 1             run alg week 1's tests against YOUR exercises.py
#   ./check.sh ml 2              same, for the machine-learning track
#   ./check.sh alg 1 --solution  run them against the reference solution
#   ./check.sh alg 1 --repl      a Python REPL with your week-1 code loaded
#   ./check.sh --all             every week, both tracks, summarised
#
# Exit status is 0 only when every check passes.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"

# The repo venv if it exists, otherwise whatever python3 is on the PATH. The
# algorithms track needs nothing beyond the standard library, so it runs either
# way; the ML track needs the venv, and says so when it is missing.
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY="$(command -v python3)"
[ -n "$PY" ] || { echo "error: no python3 found" >&2; exit 2; }

usage() {
  echo "usage: $(basename "$0") <alg|ml> <week-number> [--solution|--repl]" >&2
  echo "       $(basename "$0") --all" >&2
  exit 2
}

need_numpy() {   # the ml track only
  "$PY" -c 'import numpy, sklearn' 2>/dev/null && return 0
  echo "error: the ml track needs numpy and scikit-learn, and this Python has neither." >&2
  echo "       $PY" >&2
  echo "  fix: source .venv/bin/activate   (or rebuild it, see docs/setup-notes.md)" >&2
  echo "  the alg track needs nothing outside the standard library and still works." >&2
  return 1
}

run_one() {   # track, week-dir, source-dir
  local track="$1" week="$2" src="$3"
  # PYTHONSAFEPATH stops Python prepending the script's own directory to
  # sys.path. Without it, tests.py sitting next to your exercises.py would
  # always import *your* file -- and --solution would silently test your code
  # instead of the reference one. Needs Python 3.11+; the repo venv is 3.14.
  PYTHONSAFEPATH=1 PYTHONPATH="$HERE/lib:$src" "$PY" "$HERE/$track/$week/tests.py"
}

# ---- --all ---------------------------------------------------------------
if [ "${1:-}" = "--all" ]; then
  worst=0
  for track in alg ml; do
    for dir in "$HERE/$track"/week*/; do
      [ -d "$dir" ] || continue
      week="$(basename "$dir")"
      if [ "$track" = ml ] && ! "$PY" -c 'import numpy, sklearn' 2>/dev/null; then
        printf '%-4s %-8s %s\n' "$track" "$week" "skipped — no numpy/scikit-learn"
        continue
      fi
      out="$(run_one "$track" "$week" "$dir" 2>&1)"
      status=$?
      # The summary line is the one with "ok" in it; show that and nothing else.
      line="$(echo "$out" | grep -E '^\s+[0-9]+ ok' | head -1 | sed 's/^ *//')"
      printf '%-4s %-8s %s\n' "$track" "$week" "${line:-no checks}"
      [ $status -gt $worst ] && worst=$status
    done
  done
  exit $worst
fi

[ $# -ge 2 ] || usage

TRACK="$1"
case "$TRACK" in alg|ml) ;; *) echo "error: track must be alg or ml" >&2; usage ;; esac

WEEK=$(printf 'week%02d' "$(( 10#${2#week} ))" 2>/dev/null) || {
  echo "error: '$2' is not a week number" >&2; exit 2; }
MODE="${3:-}"

SRC="$HERE/$TRACK/$WEEK"
[ -d "$SRC" ] || { echo "error: no such week: tutorial/$TRACK/$WEEK" >&2; exit 2; }

case "$MODE" in
  --solution|-s)
     SRC="$HERE/solutions/$TRACK/$WEEK"
     [ -d "$SRC" ] || { echo "error: no solution for $TRACK/$WEEK yet" >&2; exit 2; } ;;
  --repl|-r)
     # -i keeps the interpreter open after running the file, so every function
     # you have written is already defined and ready to poke at.
     exec env PYTHONSAFEPATH=1 PYTHONPATH="$HERE/lib:$SRC" "$PY" -i -c \
       "from exercises import *; print('exercises loaded — try tab-completion')" ;;
  "") : ;;
  *) echo "error: unknown option '$MODE'" >&2; exit 2 ;;
esac

[ "$TRACK" = ml ] && { need_numpy || exit 2; }

run_one "$TRACK" "$WEEK" "$SRC"
