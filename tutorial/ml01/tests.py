"""Checks for ML week 1. You don't edit this file."""

import numpy as np


def build(ex, s):
    # -- 1: vanilla vs numpy --
    s.eq("1  double_python on [1,2,3]", lambda: ex.double_python([1, 2, 3]), [2, 4, 6])
    s.eq("1  double_python returns a list", lambda: type(ex.double_python([1])), list)
    s.eq("1  double_python on []", lambda: ex.double_python([]), [])
    s.eq("1  double_numpy on [1,2,3]",
         lambda: ex.double_numpy(np.array([1, 2, 3])), np.array([2, 4, 6]))
    s.eq("1  double_numpy returns an array",
         lambda: isinstance(ex.double_numpy(np.array([1])), np.ndarray), True)

    # -- 2: slicing --
    s.eq("2  middle of 0..4", lambda: ex.middle(np.array([0, 1, 2, 3, 4])),
         np.array([1, 2, 3]))
    s.eq("2  middle of a 2-element array",
         lambda: ex.middle(np.array([7, 9])), np.array([], dtype=int))
    s.eq("2  middle of 0..9", lambda: ex.middle(np.arange(10)), np.arange(1, 9))

    # -- 3: elementwise and broadcasting --
    s.eq("3  squares", lambda: ex.squares(np.array([1, 2, 3])), np.array([1, 4, 9]))
    s.eq("3  squares of negatives",
         lambda: ex.squares(np.array([-2, 5])), np.array([4, 25]))
    s.eq("3  centre a 2x2", lambda: ex.centre(np.array([[1., 2.], [3., 4.]])),
         np.array([[-1., -1.], [1., 1.]]))
    s.eq("3  centre leaves column means at zero",
         lambda: ex.centre(np.array([[1., 10.], [3., 20.], [8., 30.]])).mean(axis=0),
         np.array([0., 0.]))
    s.eq("3  centre keeps the shape",
         lambda: ex.centre(np.arange(6, dtype=float).reshape(3, 2)).shape, (3, 2))

    # -- 4: Mitchell's E, T, P --
    s.eq("4  role: the task", lambda: ex.role("flagging an incoming email as spam or not"), "T")
    s.eq("4  role: the measure", lambda: ex.role("the fraction of emails it flags correctly"), "P")
    s.eq("4  role: the experience", lambda: ex.role("a folder of past emails already marked spam"), "E")
    s.eq("4  role: unseen wording (measure)",
         lambda: ex.role("the percentage of tumours correctly identified"), "P")
    s.eq("4  role: unseen wording (experience)",
         lambda: ex.role("ten thousand labelled chest x-rays collected last year"), "E")
    s.eq("4  role: unseen wording (task)",
         lambda: ex.role("deciding which of ten digits a handwritten image shows"), "T")

    # -- 5: kinds of learning --
    s.eq("5  labelled + category -> classification",
         lambda: ex.learning_type({"labelled": True, "label_kind": "category"}), "classification")
    s.eq("5  labelled + number -> regression",
         lambda: ex.learning_type({"labelled": True, "label_kind": "number"}), "regression")
    s.eq("5  unlabelled -> unsupervised",
         lambda: ex.learning_type({"labelled": False, "label_kind": None}), "unsupervised")
    s.eq("5  reward -> reinforcement",
         lambda: ex.learning_type({"labelled": False, "label_kind": "reward"}), "reinforcement")

    # -- 6: X and y --
    rows = [{"age": 22, "fare": 7.25, "survived": 0},
            {"age": 38, "fare": 71.3, "survived": 1}]
    s.eq("6  split_xy gives X", lambda: ex.split_xy(rows, "survived")[0],
         np.array([[22., 7.25], [38., 71.3]]))
    s.eq("6  split_xy gives y", lambda: ex.split_xy(rows, "survived")[1], np.array([0, 1]))
    s.eq("6  X is 2-D", lambda: ex.split_xy(rows, "survived")[0].ndim, 2)
    s.eq("6  y is 1-D", lambda: ex.split_xy(rows, "survived")[1].ndim, 1)
    s.eq("6  columns come out sorted",
         lambda: ex.split_xy([{"b": 2., "a": 1., "t": 0}], "t")[0], np.array([[1., 2.]]))
    s.eq("6  a single feature still gives a 2-D X",
         lambda: ex.split_xy([{"x": 5., "t": 1}], "t")[0].shape, (1, 1))

    # -- 7: the split --
    X10, y10 = np.arange(10).reshape(10, 1), np.arange(10)
    s.eq("7  train gets 8 rows", lambda: ex.train_test_split(X10, y10, 0.2)[0].shape[0], 8)
    s.eq("7  test gets 2 rows", lambda: ex.train_test_split(X10, y10, 0.2)[1].shape[0], 2)
    s.eq("7  train is the first slice",
         lambda: ex.train_test_split(X10, y10, 0.2)[2], np.arange(8))
    s.eq("7  test is the rest",
         lambda: ex.train_test_split(X10, y10, 0.2)[3], np.arange(8, 10))
    s.eq("7  X and y stay aligned",
         lambda: (ex.train_test_split(X10, y10, 0.3)[0].ravel()
                  == ex.train_test_split(X10, y10, 0.3)[2]).all(), True)
    s.eq("7  a 0.5 split halves it", lambda: ex.train_test_split(X10, y10, 0.5)[0].shape[0], 5)

    # -- 8: accuracy --
    s.eq("8  accuracy 3/4",
         lambda: ex.accuracy(np.array([1, 0, 1, 1]), np.array([1, 0, 0, 1])), 0.75)
    s.eq("8  all correct", lambda: ex.accuracy(np.array([1, 1]), np.array([1, 1])), 1.0)
    s.eq("8  none correct", lambda: ex.accuracy(np.array([1, 1]), np.array([0, 0])), 0.0)
    s.eq("8  empty input is 0.0, not a crash",
         lambda: ex.accuracy(np.array([]), np.array([])), 0.0)
    s.eq("8  returns a plain float",
         lambda: isinstance(ex.accuracy(np.array([1]), np.array([1])), float), True)

    # -- 9: nearest centroid --
    Xc = np.array([[0., 0.], [1., 0.], [10., 10.], [11., 10.]])
    yc = np.array([0, 0, 1, 1])
    s.eq("9  centroid of class 0", lambda: ex.fit_centroids(Xc, yc)[0], np.array([0.5, 0.]))
    s.eq("9  centroid of class 1", lambda: ex.fit_centroids(Xc, yc)[1], np.array([10.5, 10.]))
    s.eq("9  one centroid per class", lambda: sorted(ex.fit_centroids(Xc, yc)), [0, 1])
    s.eq("9  predicts the near class",
         lambda: ex.predict_centroids(ex.fit_centroids(Xc, yc), np.array([[0.4, 0.1]])),
         np.array([0]))
    s.eq("9  predicts the far class",
         lambda: ex.predict_centroids(ex.fit_centroids(Xc, yc), np.array([[9.5, 9.9]])),
         np.array([1]))
    s.eq("9  predicts a whole batch",
         lambda: ex.predict_centroids(ex.fit_centroids(Xc, yc),
                                      np.array([[0., 0.], [11., 11.], [2., 1.]])),
         np.array([0, 1, 0]))
    s.eq("9  it recovers its own training labels",
         lambda: ex.predict_centroids(ex.fit_centroids(Xc, yc), Xc), yc)
    s.eq("9  a tie goes to the smaller label",
         lambda: ex.predict_centroids({0: np.array([0., 0.]), 1: np.array([2., 0.])},
                                      np.array([[1., 0.]])),
         np.array([0]))
    s.eq("9  works with three classes",
         lambda: ex.predict_centroids(
             ex.fit_centroids(np.array([[0.], [5.], [10.]]), np.array([0, 1, 2])),
             np.array([[4.9], [9.5]])),
         np.array([1, 2]))

    # -- 10: diagnosis --
    s.eq("10 clear overfit", lambda: ex.diagnose(0.99, 0.72), "overfitting")
    s.eq("10 bad on both", lambda: ex.diagnose(0.60, 0.58), "underfitting")
    s.eq("10 healthy", lambda: ex.diagnose(0.91, 0.88), "good fit")
    s.eq("10 gap is checked before the low-accuracy rule",
         lambda: ex.diagnose(0.65, 0.40), "overfitting")
    s.eq("10 a gap of exactly 0.10 is not yet overfitting",
         lambda: ex.diagnose(0.90, 0.80), "good fit")
