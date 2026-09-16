"""ML week 1 — reference answers.

Open these AFTER you have tried. Reading a solution before you have struggled
with the problem feels like learning and is not.

Where there is a one-liner and a longer version, the one-liner is shown and the
longer one explained in the comment, because on a closed-book exam you want the
version you can reconstruct, not the cleverest one.
"""

import numpy as np


# -- 1 --

def double_python(xs: list) -> list:
    return [x * 2 for x in xs]


def double_numpy(a: np.ndarray) -> np.ndarray:
    return a * 2                      # no loop: numpy broadcasts the scalar


# -- 2 --

def middle(a: np.ndarray) -> np.ndarray:
    return a[1:-1]                    # -1 is "one before the end"


# -- 3 --

def squares(a: np.ndarray) -> np.ndarray:
    return a ** 2                     # np.power(a, 2) is the same thing


def centre(a: np.ndarray) -> np.ndarray:
    # axis=0 collapses the ROWS, leaving one mean per column — which is what
    # "the mean of each feature" means when rows are samples.
    return a - a.mean(axis=0)


# -- 4 --

def role(phrase: str) -> str:
    p = phrase.lower()
    # P: a number you could report. Look for the language of measurement.
    if any(w in p for w in ("fraction", "percentage", "proportion", "accuracy",
                            "rate", "how often", "correctly", "error")):
        return "P"
    # E: data that already exists, in bulk, usually already labelled.
    if any(w in p for w in ("folder", "collected", "past", "history", "dataset",
                            "labelled", "labeled", "examples", "archive", "x-rays")):
        return "E"
    # T: what the program does to one new input.
    return "T"


# -- 5 --

def learning_type(scenario: dict) -> str:
    if scenario["labelled"]:
        return "classification" if scenario["label_kind"] == "category" else "regression"
    return "reinforcement" if scenario["label_kind"] == "reward" else "unsupervised"


# -- 6 --

def split_xy(rows: list[dict], label_key: str) -> tuple[np.ndarray, np.ndarray]:
    features = sorted(k for k in rows[0] if k != label_key)
    X = np.array([[float(r[k]) for k in features] for r in rows], dtype=float)
    y = np.array([r[label_key] for r in rows], dtype=int)
    return X, y


# -- 7 --

def train_test_split(X: np.ndarray, y: np.ndarray, test_frac: float):
    n_train = int(len(X) * (1 - test_frac))
    return X[:n_train], X[n_train:], y[:n_train], y[n_train:]


# -- 8 --

def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) == 0:
        return 0.0
    return float(np.mean(y_true == y_pred))


# -- 9 --

def fit_centroids(X: np.ndarray, y: np.ndarray) -> dict:
    return {int(c): X[y == c].mean(axis=0) for c in np.unique(y)}


def predict_centroids(centroids: dict, X: np.ndarray) -> np.ndarray:
    labels = sorted(centroids)                       # sorted => ties break low
    C = np.array([centroids[c] for c in labels])     # (n_classes, n_features)
    # (n_samples, 1, n_features) - (n_classes, n_features) broadcasts to
    # (n_samples, n_classes, n_features); norm over the last axis gives every
    # sample-to-centroid distance in one shot.
    d = np.linalg.norm(X[:, None, :] - C[None, :, :], axis=2)
    return np.array([labels[i] for i in d.argmin(axis=1)])


# -- 10 --

def diagnose(train_acc: float, test_acc: float) -> str:
    if train_acc - test_acc > 0.10:      # the gap first — it is the real signal
        return "overfitting"
    if train_acc < 0.70:
        return "underfitting"
    return "good fit"
