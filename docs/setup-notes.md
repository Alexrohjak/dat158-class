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

## Following the lecturer's setup.md

`reference/DAT158/setup.md` walks through Anaconda, `conda env update --file
environment.yml`, then `conda activate dat158`. **We did not do that**, and the
lecturer explicitly allows it: *"we don't care too much on how you do it, as
long as you are able to run the notebooks"*, listing "use the Python
installation already present on your computer" as a supported route.

Installing Anaconda would have meant a second multi-gigabyte Python beside a
working 3.14 venv, and every script in `src/` assumes `.venv`. So the venv is
the `dat158` environment, and only the genuinely missing pieces were added.

What `environment.yml` and the course `requirements.txt` ask for, against what
was already here:

| Package | Status |
|---------|--------|
| numpy, pandas, scikit-learn, scipy, matplotlib, seaborn | already installed |
| jupyterlab, ipython, ipykernel | already installed |
| **gradio** | added — module 1 lecture 4 serves a model with it |
| **openpyxl** | added — lets pandas read `.xlsx` |
| **ipywidgets** | added — interactive notebook controls |

`notebook` (the classic interface) was skipped; setup.md accepts `jupyter lab`
as the alternative, and JupyterLab was already installed.

Step 6 of setup.md registers a named kernel, which is the one part that lives
outside the venv:

    python -m ipykernel install --user --name dat158 --display-name "DAT158"

That writes `~/.local/share/jupyter/kernels/dat158/kernel.json`, pointing at
`.venv/bin/python`. Pick **DAT158** from the kernel menu when a notebook opens.
`check_setup.py` verifies it is registered.

Step 7 is the lecturer's own acceptance test, `notebooks/0.0-test.ipynb`
(last revised 18.08.2026). It was executed end to end against the `dat158`
kernel: 49 cells, zero errors, three plots, random forest at 97.9% on the
breast-cancer set. Re-run it yourself any time with:

    jupyter lab reference/DAT158/notebooks/0.0-test.ipynb

Note it needs a network connection — two cells pull datasets over HTTP.

### A wrinkle in the lock file

`requirements-lock.txt` is `pip freeze`, minus the seven packages that exist
only for `src/ocr_scans.py` (onnxruntime, opencv-python, rapidocr-onnxruntime,
flatbuffers, protobuf, pyclipper, shapely). Those are ~300 MB and
`requirements.txt` calls them deliberately optional, so putting them in the
lock would force every rebuild to download them. Regenerate the lock with:

    pip freeze | grep -vEi '^(flatbuffers|onnxruntime|opencv-python|protobuf|pyclipper|rapidocr-onnxruntime|shapely)==' > requirements-lock.txt

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
