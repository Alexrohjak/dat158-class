"""Checks for ML week 2. You don't edit this file."""

import numpy as np

# The lecturer's own example, from the "Computing metrics" slide.
YT = np.array([0, 0, 0, 1, 0, 1])
YP = np.array([0, 0, 1, 0, 1, 1])


def build(ex, s):
    # -- 1: the four counts --
    s.eq("1  counts on the slide's example", lambda: ex.counts(YT, YP), (1, 2, 2, 1))
    s.eq("1  all correct -> no errors",
         lambda: ex.counts(np.array([1, 0]), np.array([1, 0])), (1, 1, 0, 0))
    s.eq("1  all wrong -> no hits",
         lambda: ex.counts(np.array([1, 0]), np.array([0, 1])), (0, 0, 1, 1))
    s.eq("1  they sum to n", lambda: sum(ex.counts(YT, YP)), 6)
    s.eq("1  returns plain ints", lambda: all(isinstance(v, int) for v in ex.counts(YT, YP)), True)

    # -- 2: confusion matrix --
    s.eq("2  matches the slide exactly",
         lambda: ex.confusion_matrix(YT, YP), np.array([[2, 2], [1, 1]]))
    s.eq("2  shape is 2x2", lambda: ex.confusion_matrix(YT, YP).shape, (2, 2))
    s.eq("2  rows are TRUE, columns PREDICTED",
         lambda: ex.confusion_matrix(np.array([0, 0, 0, 1]), np.array([1, 1, 1, 1])),
         np.array([[0, 3], [0, 1]]))
    s.eq("2  a perfect model is diagonal",
         lambda: ex.confusion_matrix(np.array([0, 1, 1]), np.array([0, 1, 1])),
         np.array([[1, 0], [0, 2]]))
    s.eq("2  entries sum to n", lambda: int(ex.confusion_matrix(YT, YP).sum()), 6)

    # -- 3: the three metrics --
    cm = np.array([[2, 2], [1, 1]])
    s.eq("3  accuracy matches the slide (0.5)", lambda: ex.accuracy_from_cm(cm), 0.5)
    s.eq("3  precision = TP/(TP+FP)", lambda: ex.precision_from_cm(cm), 1 / 3)
    s.eq("3  recall = TP/(TP+FN)", lambda: ex.recall_from_cm(cm), 0.5)
    s.eq("3  perfect model scores 1.0 on all three",
         lambda: (ex.accuracy_from_cm(np.array([[3, 0], [0, 2]])),
                  ex.precision_from_cm(np.array([[3, 0], [0, 2]])),
                  ex.recall_from_cm(np.array([[3, 0], [0, 2]]))),
         (1.0, 1.0, 1.0))
    s.eq("3  precision survives predicting nothing positive",
         lambda: ex.precision_from_cm(np.array([[5, 0], [3, 0]])), 0.0)
    s.eq("3  recall survives having no positives",
         lambda: ex.recall_from_cm(np.array([[5, 1], [0, 0]])), 0.0)
    s.eq("3  accuracy survives an empty matrix",
         lambda: ex.accuracy_from_cm(np.zeros((2, 2), dtype=int)), 0.0)

    # -- 4: F1 --
    s.close("4  f1 of 0.5 and 0.5", lambda: ex.f1(0.5, 0.5), 0.5)
    s.close("4  f1 of 1.0 and 1.0", lambda: ex.f1(1.0, 1.0), 1.0)
    s.close("4  harmonic, not arithmetic: f1(1.0, 0.0) is 0.0, not 0.5",
            lambda: ex.f1(1.0, 0.0), 0.0)
    s.close("4  f1 punishes imbalance: f1(1.0, 0.2) < 0.5",
            lambda: ex.f1(1.0, 0.2) < 0.5, True)
    s.close("4  f1 of 0.6 and 0.4", lambda: ex.f1(0.6, 0.4), 0.48)
    s.eq("4  both zero is 0.0, not a crash", lambda: ex.f1(0.0, 0.0), 0.0)

    # -- 5: why accuracy lies --
    imb = np.array([0] * 99 + [1])
    s.eq("5  always_negative returns all zeros",
         lambda: ex.always_negative(imb), np.zeros(100, dtype=int))
    s.eq("5  length matches the input", lambda: len(ex.always_negative(imb)), 100)
    s.close("5  ...and is 99% accurate",
            lambda: ex.accuracy_from_cm(ex.confusion_matrix(imb, ex.always_negative(imb))), 0.99)
    s.eq("5  ...with recall 0.0",
         lambda: ex.recall_from_cm(ex.confusion_matrix(imb, ex.always_negative(imb))), 0.0)

    # -- 6: thresholds --
    p3 = np.array([0.1, 0.5, 0.9])
    s.eq("6  threshold 0.5", lambda: ex.predict_at(p3, 0.5), np.array([0, 1, 1]))
    s.eq("6  a probability ON the threshold predicts positive",
         lambda: ex.predict_at(np.array([0.5]), 0.5), np.array([1]))
    s.eq("6  threshold 0.0 predicts everything positive",
         lambda: ex.predict_at(p3, 0.0), np.array([1, 1, 1]))
    s.eq("6  a threshold above every probability predicts nothing",
         lambda: ex.predict_at(p3, 1.1), np.array([0, 0, 0]))

    # -- 7: the sweep --
    yt = np.array([0, 0, 1, 1])
    pr = np.array([0.1, 0.4, 0.6, 0.9])
    s.eq("7  one row per threshold", lambda: len(ex.sweep(yt, pr, [0.0, 0.5, 1.1])), 3)
    s.eq("7  the threshold is carried through",
         lambda: [r[0] for r in ex.sweep(yt, pr, [0.0, 0.5, 1.1])], [0.0, 0.5, 1.1])
    s.close("7  at 0.5 the split is perfect",
            lambda: ex.sweep(yt, pr, [0.5])[0][1:], (1.0, 1.0))
    s.close("7  at 0.0 recall is 1.0 and precision is the base rate",
            lambda: ex.sweep(yt, pr, [0.0])[0][1:], (0.5, 1.0))
    s.close("7  above everything, recall is 0.0",
            lambda: ex.sweep(yt, pr, [1.1])[0][2], 0.0)
    s.close("7  raising the threshold cannot raise recall",
            lambda: ex.sweep(yt, pr, [0.5])[0][2] >= ex.sweep(yt, pr, [0.8])[0][2], True)

    # -- 8: ROC --
    s.close("8  perfect split reaches (0.0, 1.0)",
            lambda: ex.roc_points(yt, pr, [0.5])[0], (0.0, 1.0))
    s.close("8  predicting everything positive is (1.0, 1.0)",
            lambda: ex.roc_points(yt, pr, [0.0])[0], (1.0, 1.0))
    s.close("8  predicting nothing positive is (0.0, 0.0)",
            lambda: ex.roc_points(yt, pr, [1.1])[0], (0.0, 0.0))
    s.eq("8  one point per threshold",
         lambda: len(ex.roc_points(yt, pr, [0.0, 0.5, 1.1])), 3)
    s.close("8  TPR is recall under another name",
            lambda: ex.roc_points(yt, pr, [0.5])[0][1] == ex.sweep(yt, pr, [0.5])[0][2],
            True)
    s.close("8  a half-right split",
            lambda: ex.roc_points(np.array([0, 0, 1, 1]),
                                  np.array([0.2, 0.7, 0.3, 0.8]), [0.5])[0],
            (0.5, 0.5))

    # -- 9: multiclass --
    s.close("9  three classes, 3/4 right",
            lambda: ex.multiclass_accuracy(np.array([0, 1, 2, 2]), np.array([0, 1, 1, 2])), 0.75)
    s.eq("9  empty is 0.0", lambda: ex.multiclass_accuracy(np.array([]), np.array([])), 0.0)
    s.close("9  agrees with the binary case",
            lambda: ex.multiclass_accuracy(YT, YP), 0.5)
    s.close("9  all wrong", lambda: ex.multiclass_accuracy(np.array([0, 1]), np.array([1, 0])), 0.0)

    # -- 10: three-way split --
    s.eq("10 train block", lambda: ex.train_val_test(10, 0.6, 0.2)[0], np.arange(0, 6))
    s.eq("10 validation block", lambda: ex.train_val_test(10, 0.6, 0.2)[1], np.arange(6, 8))
    s.eq("10 test block", lambda: ex.train_val_test(10, 0.6, 0.2)[2], np.arange(8, 10))
    s.eq("10 nothing is lost to rounding",
         lambda: sum(len(p) for p in ex.train_val_test(7, 0.6, 0.2)), 7)
    s.eq("10 the blocks are consecutive and disjoint",
         lambda: np.concatenate(ex.train_val_test(13, 0.5, 0.25)), np.arange(13))

    # -- 11: k-fold --
    s.eq("11 3 folds of 6", lambda: len(ex.kfold_indices(6, 3)), 3)
    s.eq("11 first fold validates on [0,1]",
         lambda: ex.kfold_indices(6, 3)[0][1], np.array([0, 1]))
    s.eq("11 first fold trains on the rest",
         lambda: ex.kfold_indices(6, 3)[0][0], np.array([2, 3, 4, 5]))
    s.eq("11 last fold validates on [4,5]",
         lambda: ex.kfold_indices(6, 3)[2][1], np.array([4, 5]))
    s.eq("11 every sample validates exactly once",
         lambda: np.sort(np.concatenate([v for _, v in ex.kfold_indices(10, 4)])),
         np.arange(10))
    s.eq("11 uneven split: earlier folds take the extra",
         lambda: [len(v) for _, v in ex.kfold_indices(10, 4)], [3, 3, 2, 2])
    s.eq("11 train and validation never overlap",
         lambda: all(len(np.intersect1d(t, v)) == 0 for t, v in ex.kfold_indices(10, 4)), True)
    s.eq("11 they cover everything, every time",
         lambda: all(len(t) + len(v) == 10 for t, v in ex.kfold_indices(10, 4)), True)
    s.eq("11 k == n is leave-one-out",
         lambda: [len(v) for _, v in ex.kfold_indices(5, 5)], [1, 1, 1, 1, 1])
