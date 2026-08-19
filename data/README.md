# Data

Contents of the subfolders are gitignored. This file is not — keep it updated.

## Rules

- **`raw/` is immutable.** Once a file lands there it is never edited or overwritten.
  If you need a cleaned version, write it to `processed/`.
- Every dataset gets a row in the table below. Six weeks from now you will not
  remember where a CSV came from, and an assignment that cites its source scores
  better than one that does not.
- Nothing in here is committed to git. If you move machines, re-download from the
  recorded source.

## Datasets

| File | Location | Source | Downloaded | Notes |
|------|----------|--------|------------|-------|
| _(example)_ `housing.csv` | `raw/` | HOML ch.2, github.com/ageron/data | — | California housing, 20 640 rows |

## Datasets that need no download

scikit-learn ships several small datasets used throughout HOML Part I. No files,
no network:

```python
from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer

X, y = load_iris(return_X_y=True)
```

Larger ones download on first use and cache to `~/scikit_learn_data`:

```python
from sklearn.datasets import fetch_california_housing, fetch_openml

housing = fetch_california_housing()          # HOML chapter 2
mnist = fetch_openml("mnist_784", version=1)  # HOML chapter 3
```
