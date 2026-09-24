"""ML week 1 — Module 1, part 1. Uke 34: `1-intro` and `2-python`.

    ../check.py ml01

Every `todo()` is a task. Delete it and write the body.

Rule for this week: no scikit-learn. Everything here is either plain Python or
numpy, because the point is to understand what the library does before you let
it do it for you. The exam is closed-book — `sklearn.metrics` will not be there.
"""

import numpy as np

from lib.check import todo

# ---------------------------------------------------------------------------
# Exercise 1  —  the slide the lecturer opened numpy with
#
# "Given a list of numbers, make a new list where all the elements are
#  multiplied by 2."  (2-python, slide "numpy arrays")
#
# Write it twice. First the vanilla-Python way, with an explicit loop or a
# comprehension. Then the numpy way, with no loop at all.
#
#   double_python([1, 2, 3])  ==  [2, 4, 6]          <- a real list
#   double_numpy(np.array([1, 2, 3]))                <- an array([2, 4, 6])
#
# The second one is the whole reason numpy exists: the loop moves into C.
# ---------------------------------------------------------------------------

def double_python(xs: list) -> list:
    doubles = []
    for x in xs:
        doubles.append(x * 2)
    return doubles

    # return [x * 2 for x in xs]


def double_numpy(a: np.ndarray) -> np.ndarray:
    return a * 2

# ---------------------------------------------------------------------------
# Exercise 2  —  slicing
#
# Zero-based, and the stop index is NOT included. This trips everyone once.
#
#   middle(np.array([0, 1, 2, 3, 4]))   ==  array([1, 2, 3])
#
# Return everything except the first and last element. Do it with ONE slice,
# not a loop. Your answer should work for any length >= 2.
# ---------------------------------------------------------------------------

def middle(a: np.ndarray) -> np.ndarray:
    return a[1:-1]


# ---------------------------------------------------------------------------
# Exercise 3  —  element-by-element, and then broadcasting
#
# "Operations on arrays are typically done element-by-element."
#
#   squares(np.array([1, 2, 3]))            ==  array([1, 4, 9])
#   centre(np.array([[1., 2.], [3., 4.]]))  ==  array([[-1., -1.], [1., 1.]])
#
# `centre` subtracts each COLUMN's mean from that column. The array is
# (n_samples, n_features) — rows are datapoints, columns are features, which is
# the shape every dataset in this course arrives in.
#
# Do it without a loop. `a.mean(axis=0)` gives you one mean per column, and
# subtracting a shape-(2,) array from a shape-(2,2) array broadcasts.
# Getting `axis` right is the exercise; if you get an array of the wrong shape,
# print `a.mean(axis=0)` and `a.mean(axis=1)` and look at the difference.
# ---------------------------------------------------------------------------

def squares(a: np.ndarray) -> np.ndarray:
    return a ** 2


def centre(a: np.ndarray) -> np.ndarray:
    return a - a.mean(axis=0)


# ---------------------------------------------------------------------------
# Exercise 4  —  Mitchell's definition, as code
#
# "A computer program is said to learn from experience E with respect to some
#  task T and some performance measure P, if its performance on T, as measured
#  by P, improves with experience E."   (2-python, "What is machine learning?")
#
# This is the definition to have ready for the exam. Here it is as a filing
# problem: given one of the three phrases below, say whether it is the E, the
# T or the P of a spam filter.
#
# Return exactly one of the strings: "E", "T", "P"
#
#   role("flagging an incoming email as spam or not")         == "T"
#   role("the fraction of emails it flags correctly")          == "P"
#   role("a folder of past emails already marked spam")        == "E"
#
# Match on what the phrase DESCRIBES, not on keywords — the tests use wordings
# you have not seen. Experience is the data; the task is the thing being done;
# the performance measure is the number you would put in a report.
# ---------------------------------------------------------------------------

def role(phrase: str) -> str:
    p = ["fraction", "score", "percentage", "rate", "accuracy", "how often", "proportion"]
    e = ["data", "past", "labelled", "labeled", "marked", "tagged", "collected", "gathered", "examples", "records", "historical"]
   
    for word in p:
        if word in phrase:
            return "P"
    for word in e:
        if word in phrase:
            return "E"

    return "T"

# P words -> number, fraction, score, percentage, accuracy, rate...
# E words ->  data, emails, videos, images, points, counts, numbers...
# T words -> deciding, predicting, calculating, examining, sorting...


# ---------------------------------------------------------------------------
# Exercise 5  —  which kind of learning?
#
# From "Different types of machine learning". Given a description, return one of:
#
#   "classification"   supervised, the label is a category
#   "regression"       supervised, the label is a number
#   "unsupervised"     no labels; the model groups similar points
#   "reinforcement"    an agent acting, rewarded or penalised
#
# The supervised/unsupervised split is decided by ONE question: does each
# datapoint come with a label attached? The classification/regression split by
# a second: is that label a category or a number?
#
# The input is a dict, so you are reading structure rather than prose:
#
#   {"labelled": True,  "label_kind": "category"}  -> "classification"
#   {"labelled": True,  "label_kind": "number"}    -> "regression"
#   {"labelled": False, "label_kind": None}        -> "unsupervised"
#   {"labelled": False, "label_kind": "reward"}    -> "reinforcement"
# ---------------------------------------------------------------------------

def learning_type(scenario: dict) -> str:
    todo()


# ---------------------------------------------------------------------------
# Exercise 6  —  X and y
#
# Structured data arrives as a table (the Titanic slide). Machine learning
# wants it as two things: a feature matrix X of shape (n_samples, n_features),
# and a label vector y of shape (n_samples,).
#
# `rows` is a list of dicts, all with the same keys. Split it, taking
# `label_key` out as y and keeping every other key — in sorted order, so the
# result is deterministic — as the columns of X.
#
#   rows = [{"age": 22, "fare": 7.25, "survived": 0},
#           {"age": 38, "fare": 71.3, "survived": 1}]
#   split_xy(rows, "survived")
#     ==  (array([[22.,  7.25],
#                 [38., 71.3 ]]),  array([0, 1]))
#
# Return X as a float array and y as an int array. Note the shapes: X is 2-D
# even when there is one feature; y is always 1-D. Getting this wrong is the
# single most common sklearn error you will hit all semester.
# ---------------------------------------------------------------------------

def split_xy(rows: list[dict], label_key: str) -> tuple[np.ndarray, np.ndarray]:
    todo()


# ---------------------------------------------------------------------------
# Exercise 7  —  hold out a test set
#
# Before you fit anything, put some data aside and do not look at it.
#
# Take the FIRST `1 - test_frac` of the rows as training data and the rest as
# test — no shuffling, so the result is reproducible and easy to check by hand.
# Round the training size DOWN with int().
#
#   X = np.arange(10).reshape(10, 1);  y = np.arange(10)
#   train_test_split(X, y, 0.2)  ->  X_train has 8 rows, X_test has 2
#
# Return (X_train, X_test, y_train, y_test) — the order sklearn uses, so the
# habit transfers.
#
# Real splits shuffle first; this one does not, deliberately. Ask yourself what
# would go wrong here if the rows were sorted by their label.
# ---------------------------------------------------------------------------

def train_test_split(X: np.ndarray, y: np.ndarray, test_frac: float):
    todo()


# ---------------------------------------------------------------------------
# Exercise 8  —  accuracy, by hand
#
# The fraction of predictions that are right.
#
#   accuracy(np.array([1, 0, 1, 1]), np.array([1, 0, 0, 1]))  ==  0.75
#
# One line with numpy. Return a float. An empty input should give 0.0 rather
# than dividing by zero.
# ---------------------------------------------------------------------------

def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    todo()


# ---------------------------------------------------------------------------
# Exercise 9  —  your first model
#
# A nearest-centroid classifier, which is about the simplest thing that
# genuinely learns from data:
#
#   fit   — for each class, compute the mean of its training points (its
#           "centroid"). Return a dict {class_label: centroid_array}.
#   predict — label each new point with the class whose centroid is nearest,
#           by ordinary Euclidean distance.
#
#   X = np.array([[0., 0.], [1., 0.], [10., 10.], [11., 10.]])
#   y = np.array([0, 0, 1, 1])
#   fit_centroids(X, y)  ==  {0: array([0.5, 0.]), 1: array([10.5, 10.])}
#   predict_centroids({...}, np.array([[0.4, 0.1]]))  ==  array([0])
#
# Break ties toward the smaller class label, so the result is deterministic.
#
# This is the shape of every model in the course: fit learns parameters from
# training data, predict applies them to new data. sklearn's estimators are
# this same pair of methods with more inside them.
# ---------------------------------------------------------------------------

def fit_centroids(X: np.ndarray, y: np.ndarray) -> dict:
    todo()


def predict_centroids(centroids: dict, X: np.ndarray) -> np.ndarray:
    todo()


# ---------------------------------------------------------------------------
# Exercise 10  —  reading the two numbers
#
# "Overfitting: the model gives perfect predictions on known data, but does not
#  generalise to new data."   (2-python, "Data challenges")
#
# Given training and test accuracy, return one of:
#
#   "overfitting"    good on train, clearly worse on test
#   "underfitting"   bad on both
#   "good fit"       good on both, and close together
#
# Use these thresholds so the answer is well-defined:
#   - a gap of MORE than 0.10 between train and test  -> "overfitting"
#   - otherwise, train accuracy below 0.70            -> "underfitting"
#   - otherwise                                       -> "good fit"
#
# The thresholds are arbitrary; the ordering is not. Check for the gap first —
# a model can be bad on both AND overfitting, and the gap is the more
# actionable diagnosis.
# ---------------------------------------------------------------------------

def diagnose(train_acc: float, test_acc: float) -> str:
    todo()
