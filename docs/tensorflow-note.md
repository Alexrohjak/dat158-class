# TensorFlow / Keras on this machine

## The situation

Your system Python is **3.14.4**, which is very new. TensorFlow does not publish
builds for it yet:

```
$ pip install tensorflow
ERROR: No matching distribution found for tensorflow
```

This is a packaging lag, not a broken machine. TensorFlow typically supports a new
Python version 6–12 months after release.

**This does not block you.** HOML Part I (chapters 1–9) is entirely scikit-learn and
works perfectly in your `.venv`. That is the whole scikit-learn half of the book and
realistically your entire first semester.

## When you reach chapter 10, pick one

### Option A — Google Colab (easiest, zero setup)

https://colab.research.google.com — free, runs in the browser, TensorFlow and Keras
pre-installed, free GPU access. The book's notebooks have "Open in Colab" buttons.

Best choice if you just want to follow the book. The only cost is that your work
lives in Google Drive rather than this repo. Download finished notebooks into
`weeks/ukeNN-ml/code/` when done.

### Option B — a second venv on an older Python

Install Python 3.12 alongside 3.14 (they coexist fine):

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv

cd ~/code/dat158-class
python3.12 -m venv .venv-dl
source .venv-dl/bin/activate
pip install tensorflow numpy pandas matplotlib jupyterlab ipykernel
```

Then register both as Jupyter kernels so you can pick per-notebook:

```bash
source .venv/bin/activate    && python -m ipykernel install --user --name dat158     --display-name "dat158 (sklearn)"
source .venv-dl/bin/activate && python -m ipykernel install --user --name dat158-dl  --display-name "dat158 (tensorflow)"
```

Best choice if you want everything local and reproducible.

### Option C — PyTorch instead

PyTorch *does* have Python 3.14 wheels and installs into your existing `.venv`:

```bash
pip install torch
```

Note this pulls ~3 GB of NVIDIA CUDA libraries. For CPU-only (much smaller):

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Only sensible if your course allows PyTorch. The concepts transfer completely —
layers, loss functions, optimisers, backpropagation are the same ideas — but the
book's code will not run as written, and you would be translating every example.
**Do not choose this just to avoid the setup.** Ask your lecturer first.

## Recommendation

Do nothing now. When you hit chapter 10, start with **Colab** (Option A) to keep
moving, and set up **Option B** in the background if you want local control.
