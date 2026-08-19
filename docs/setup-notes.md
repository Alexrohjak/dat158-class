# Setup notes

What was done to this repo and why, so future-you can rebuild it.

## Environment

Python 3.14.4 (system), venv at `.venv/`.

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

`requirements.txt` lists what was asked for. `requirements-lock.txt` pins every
transitive dependency for an exact rebuild:

    pip install -r requirements-lock.txt

Verify with `python src/check_setup.py` — it imports each package and trains a
small model end to end.

## Gotchas hit during setup

- **Renaming the project directory breaks the venv.** Absolute paths are baked
  into `.venv/bin/activate` and the script shebangs. If you move or rename this
  folder, delete `.venv` and rebuild from `requirements-lock.txt`.
- **TensorFlow has no Python 3.14 build.** See `tensorflow-note.md`.

## Git

Identity is set repo-locally rather than globally, because the machine has
repos under two different identities:

    git config user.name  "Alexander Rohde Jakobsen"
    git config user.email "alexander.rohde.jakobsen@gmail.com"

To make it the machine-wide default instead, add `--global`.
