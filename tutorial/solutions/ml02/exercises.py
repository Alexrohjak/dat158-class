"""ML week 2 — reference answers.

Open AFTER you have tried. Every one of these is short; if yours is much
longer, that is worth a look, but a longer version that you understand beats a
short one you copied.
"""

import numpy as np


# -- 1 --

def counts(y_true, y_pred):
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    return tp, tn, fp, fn


# -- 2 --

def confusion_matrix(y_true, y_pred):
    tp, tn, fp, fn = counts(y_true, y_pred)
    # Rows = true, columns = predicted. Row 0 is the negatives (TN, FP),
    # row 1 the positives (FN, TP).
    return np.array([[tn, fp],
                     [fn, tp]], dtype=int)


# -- 3 --

def accuracy_from_cm(cm):
    total = cm.sum()
    return float((cm[0, 0] + cm[1, 1]) / total) if total else 0.0


def precision_from_cm(cm):
    tp, fp = cm[1, 1], cm[0, 1]          # the PREDICTED-positive column
    return float(tp / (tp + fp)) if (tp + fp) else 0.0


def recall_from_cm(cm):
    tp, fn = cm[1, 1], cm[1, 0]          # the ACTUALLY-positive row
    return float(tp / (tp + fn)) if (tp + fn) else 0.0


# -- 4 --

def f1(precision, recall):
    if precision + recall == 0:
        return 0.0
    return float(2 * precision * recall / (precision + recall))


# -- 5 --

def always_negative(y_true):
    return np.zeros(len(y_true), dtype=int)


# -- 6 --

def predict_at(probs, threshold):
    return (probs >= threshold).astype(int)


# -- 7 --

def sweep(y_true, probs, thresholds):
    out = []
    for t in thresholds:
        cm = confusion_matrix(y_true, predict_at(probs, t))
        out.append((t, precision_from_cm(cm), recall_from_cm(cm)))
    return out


# -- 8 --

def roc_points(y_true, probs, thresholds):
    out = []
    for t in thresholds:
        cm = confusion_matrix(y_true, predict_at(probs, t))
        tn, fp, fn, tp = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
        tpr = float(tp / (tp + fn)) if (tp + fn) else 0.0   # == recall
        fpr = float(fp / (fp + tn)) if (fp + tn) else 0.0
        out.append((fpr, tpr))
    return out


# -- 9 --

def multiclass_accuracy(y_true, y_pred):
    if len(y_true) == 0:
        return 0.0
    return float(np.mean(y_true == y_pred))     # the indicator sum, vectorised


# -- 10 --

def train_val_test(n, train_frac, val_frac):
    n_train = int(n * train_frac)
    n_val = int(n * val_frac)
    idx = np.arange(n)
    return idx[:n_train], idx[n_train:n_train + n_val], idx[n_train + n_val:]


# -- 11 --

def kfold_indices(n, k):
    idx = np.arange(n)
    # The first n % k folds get one extra sample, so nothing is dropped.
    sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
    folds, start = [], 0
    for size in sizes:
        val = idx[start:start + size]
        train = np.concatenate([idx[:start], idx[start + size:]])
        folds.append((train, val))
        start += size
    return folds
