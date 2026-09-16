"""ML week 2 — Module 1, part 2. Uke 36: `3-metrics` and `4-ml-engineering`.

    ../check.py ml02

This is the most examinable week in module 1. Every metric below is defined on
a slide, and all of them come out of the four numbers in the confusion matrix.
Write them from those four numbers and you will not need to memorise formulas —
you will be able to derive them in the exam hall.

Still no sklearn. You are implementing what it does.
"""

import numpy as np

from lib.check import todo

# ---------------------------------------------------------------------------
# Exercise 1  —  the four numbers
#
# Everything this week is built from these. For a binary problem where 1 is the
# positive class:
#
#   TP  predicted 1, actually 1      TN  predicted 0, actually 0
#   FP  predicted 1, actually 0      FN  predicted 0, actually 1
#
# The names read as: "false positive" = a positive prediction that was false.
# The second word is what you SAID, the first is whether you were right.
#
# Return them in the order (tp, tn, fp, fn) as plain ints.
#
#   counts(np.array([0,0,0,1,0,1]), np.array([0,0,1,0,1,1]))  ==  (1, 2, 2, 1)
#
# That example is the lecturer's own, from the "Computing metrics" slide.
# ---------------------------------------------------------------------------

def counts(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 2  —  the confusion matrix
#
# Same information, laid out as a table. Use scikit-learn's convention, because
# that is what the slide shows and what you will read off a plot:
#
#       ROWS are the TRUE class, COLUMNS are the PREDICTED class.
#
#       [[TN, FP],
#        [FN, TP]]
#
#   confusion_matrix(np.array([0,0,0,1,0,1]), np.array([0,0,1,0,1,1]))
#     ==  array([[2, 2],
#                [1, 1]])
#
# Check it against the slide: the lecturer gets exactly this array.
#
# Return an integer array of shape (2, 2).
# ---------------------------------------------------------------------------

def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    todo()


# ---------------------------------------------------------------------------
# Exercise 3  —  accuracy, precision, recall
#
# Straight from the slides. Take the confusion matrix as input, so you are
# reading the definitions off the same four numbers the lecturer does.
#
#   accuracy   = (TP + TN) / (TP + TN + FP + FN)   "how many did we get right?"
#   precision  =  TP / (TP + FP)                   "of what I flagged, how much was real?"
#   recall     =  TP / (TP + FN)                   "of what was real, how much did I find?"
#
# Note which denominator each one has. Precision divides by everything you
# PREDICTED positive — it is a column of the matrix. Recall divides by
# everything that IS positive — a row. That is the whole difference, and it is
# worth being able to point at on the matrix.
#
# Return 0.0 rather than dividing by zero when a denominator is empty. That is
# a real case: a model that never predicts positive has undefined precision,
# and sklearn will warn you about it.
# ---------------------------------------------------------------------------

def accuracy_from_cm(cm: np.ndarray) -> float:
    todo()


def precision_from_cm(cm: np.ndarray) -> float:
    todo()


def recall_from_cm(cm: np.ndarray) -> float:
    todo()


# ---------------------------------------------------------------------------
# Exercise 4  —  F1
#
# Precision and recall trade off against each other, so a single number that
# refuses to let either collapse is useful:
#
#   F1 = 2 * (precision * recall) / (precision + recall)
#
# This is the HARMONIC mean, not the ordinary one, and the difference is the
# point. Ordinary mean of precision 1.0 and recall 0.0 is 0.5 — which would
# reward a useless model. The harmonic mean gives 0.0.
#
# Return 0.0 if precision and recall are both zero.
# ---------------------------------------------------------------------------

def f1(precision: float, recall: float) -> float:
    todo()


# ---------------------------------------------------------------------------
# Exercise 5  —  why accuracy alone lies
#
# The single most examinable idea this week.
#
# Build a "model" that ignores its input and always predicts the negative
# class, then report its accuracy on a dataset where only 1% are positive.
#
#   always_negative(np.array([0]*99 + [1]))  ==  array of 100 zeros
#   accuracy of that                         ==  0.99
#   recall of that                           ==  0.0
#
# 99% accurate and it has never once found the thing you built it to find.
# This is the fraud/cancer/spam case, and it is why the slides move straight
# from accuracy to precision and recall.
#
# `always_negative` takes y_true only so it knows how many to return.
# ---------------------------------------------------------------------------

def always_negative(y_true: np.ndarray) -> np.ndarray:
    todo()


# ---------------------------------------------------------------------------
# Exercise 6  —  thresholds
#
# "Most ML classifiers actually predict a decimal number between 0 and 1,
#  leaving us to select a threshold."
#
# Convert probabilities to hard labels: 1 if p >= threshold, else 0.
#
#   predict_at(np.array([0.1, 0.5, 0.9]), 0.5)  ==  array([0, 1, 1])
#
# Note `>=`, so a probability exactly on the threshold predicts positive. 0.5 is
# only a default — moving it is the cheapest way to trade precision against
# recall, with no retraining at all.
# ---------------------------------------------------------------------------

def predict_at(probs: np.ndarray, threshold: float) -> np.ndarray:
    todo()


# ---------------------------------------------------------------------------
# Exercise 7  —  the trade-off, as a table
#
# For each threshold, return (threshold, precision, recall).
#
#   sweep(y_true, probs, [0.0, 0.5, 1.1])
#     -> [(0.0, ..., ...), (0.5, ..., ...), (1.1, ..., ...)]
#
# Reuse what you already wrote — build the predictions, build the confusion
# matrix, read off the metrics. Do not re-derive them.
#
# Watch what happens at the ends. At threshold 0.0 everything is predicted
# positive: recall is 1.0 and precision is just the base rate. Above every
# probability, nothing is predicted positive: recall is 0.0 and precision is
# undefined (your 0.0). That shape — recall falling as precision rises — is the
# precision-recall curve on the slide.
# ---------------------------------------------------------------------------

def sweep(y_true: np.ndarray, probs: np.ndarray,
          thresholds: list[float]) -> list[tuple[float, float, float]]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 8  —  ROC
#
# "A more common option is to plot the true positive rate as a function of the
#  false positive rate."
#
#   TPR = TP / (TP + FN)     "how many positives did I get right"   (= recall)
#   FPR = FP / (FP + TN)     "how many negatives did I get wrong"
#
# TPR is recall under another name — worth knowing, because both appear.
#
# Return one (fpr, tpr) pair per threshold, in the order given.
#
# A perfect model reaches (0.0, 1.0): every positive found, no false alarms.
# The diagonal fpr == tpr is random guessing. A curve BELOW the diagonal is not
# a bad model — it is a good model wired up backwards.
# ---------------------------------------------------------------------------

def roc_points(y_true: np.ndarray, probs: np.ndarray,
               thresholds: list[float]) -> list[tuple[float, float]]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 9  —  more than two classes
#
# "Accuracy still means ratio of correct predictions, but let's redefine as
#  accuracy = (1/N) * sum of 1(y == y_hat)"
#
# The indicator-function form on the slide. It works for any number of classes,
# and for two classes it agrees with what you wrote last week.
#
#   multiclass_accuracy(np.array([0,1,2,2]), np.array([0,1,1,2]))  ==  0.75
#
# Return 0.0 for empty input.
# ---------------------------------------------------------------------------

def multiclass_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    todo()


# ---------------------------------------------------------------------------
# Exercise 10  —  the third set
#
# "In case we want to compare different models, we need a third set: the
#  validation set. The test set is still only for final evaluation."
#
# Split indices 0..n-1 into three consecutive blocks and return them as arrays:
#
#   train_val_test(10, 0.6, 0.2)
#     ==  (array([0,1,2,3,4,5]), array([6,7]), array([8,9]))
#
# Sizes: int(n * train_frac) for train, int(n * val_frac) for validation, and
# everything left over is test — so nothing is lost to rounding.
#
# The rule that matters more than the code: you tune on validation, and you
# touch test exactly once, at the end. Every time you look at the test set and
# then change something, you leak a little of it into your model, and your
# final number gets a little more optimistic than the truth.
# ---------------------------------------------------------------------------

def train_val_test(n: int, train_frac: float, val_frac: float):
    todo()


# ---------------------------------------------------------------------------
# Exercise 11  —  k-fold cross-validation
#
# "We can do even better estimates by rotating the training data."
#
# Split 0..n-1 into k consecutive folds. Each fold takes a turn as the
# validation set while the other k-1 are training. Return a list of
# (train_idx, val_idx) pairs, matching what `KFold.split` gives you.
#
#   kfold_indices(6, 3)
#     ==  [(array([2,3,4,5]), array([0,1])),
#          (array([0,1,4,5]), array([2,3])),
#          (array([0,1,2,3]), array([4,5]))]
#
# When k does not divide n, give the earlier folds the extra sample — the first
# n % k folds get one more each. That is what sklearn does, and it means no
# sample is ever dropped.
#
# Every sample is used for validation exactly once, and for training k-1 times.
# That is the whole trick: k estimates instead of one, at k times the compute.
# ---------------------------------------------------------------------------

def kfold_indices(n: int, k: int) -> list[tuple[np.ndarray, np.ndarray]]:
    todo()
