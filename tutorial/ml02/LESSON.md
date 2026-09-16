# ML Week 2 — Metrics, and why accuracy lies

**Source:** uke 36's decks, `3-metrics` and `4-ml-engineering`, in
[`../../weeks/uke36-ml/slides/`](../../weeks/uke36-ml/slides/).
**Book:** Géron ch. 3.
**Budget:** 3 hours. This is the densest week in module 1.

The lecturer revised both decks on 1 September, the day before the lecture, so
they are current. `3-metrics` opens with a slide titled *"Assignment 1 out"* —
the quiz on **11 September** is drawn from this material.

---

## 1. Four numbers, and everything else

Every classification metric in this course comes out of the confusion matrix.
Learn the four cells and you can derive the rest in the exam hall instead of
memorising formulas you might misremember.

For binary classification, with 1 as the positive class:

|  | predicted 0 | predicted 1 |
|---|---|---|
| **actually 0** | TN | FP |
| **actually 1** | FN | TP |

Read the names right-to-left: **the second word is what you predicted, the
first is whether you were right.** A "false positive" is a positive prediction
that turned out false.

That layout — rows true, columns predicted — is scikit-learn's, and the one on
the slide. The lecturer's own worked example:

```python
y_true = [0, 0, 0, 1, 0, 1]
y_pred = [0, 0, 1, 0, 1, 1]
confusion_matrix(y_true, y_pred)   # array([[2, 2],
                                   #        [1, 1]])
```

Check you can get that array by hand before going on. Two negatives called
correctly, two called positive by mistake, one positive missed, one caught.

## 2. The three metrics

$$\text{accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{precision} = \frac{TP}{TP + FP} \qquad \text{recall} = \frac{TP}{TP + FN}$$

Both precision and recall have TP on top. **The denominator is the whole
difference**, and you can point at it on the matrix:

- **Precision** divides by everything you *predicted* positive — the right-hand
  **column**. *"Of the things I flagged, how many were real?"*
- **Recall** divides by everything that *is* positive — the bottom **row**.
  *"Of the things that were real, how many did I find?"*

Column, row. If you remember only that, you can rebuild both.

## 3. Why accuracy alone lies

The most examinable idea this week, and the reason the slides move past
accuracy so quickly.

Take 1000 transactions, 10 of them fraudulent. A model that flags *nothing*:

- accuracy = 990/1000 = **99%**
- recall = 0/10 = **0%**

It is 99% accurate and has never once found the thing it exists to find.

Accuracy fails whenever the classes are **imbalanced** — which is most problems
worth solving. Fraud, disease, equipment failure, spam: the interesting class is
always the rare one. Quote accuracy on imbalanced data and you are hiding the
result, whether or not you mean to.

Exercise 5 makes you build exactly this model and watch it score 99%.

## 4. The trade-off, and the threshold

> "Most ML classifiers actually predict a decimal number between 0 and 1,
> leaving us to select a threshold."

A classifier gives you $f: \mathbf{x} \to [0,1]$. The 0.5 cutoff is a
*default*, not a law — and moving it is free. No retraining.

- **Lower** the threshold → flag more → recall up, precision down.
- **Raise** it → flag less → precision up, recall down.

You cannot maximise both. Which you want is a question about consequences, not
about statistics:

- **Cancer screening** — a missed tumour is far worse than a needless follow-up
  scan. Maximise **recall**.
- **Spam filtering** — a lost job offer is far worse than a spam email getting
  through. Maximise **precision**.

Plotting precision against recall for every threshold gives the
**precision-recall curve** on the slide.

**F1** collapses the two into one number:

$$F_1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}$$

It is the *harmonic* mean, and that matters. Precision 1.0 with recall 0.0
averages to 0.5 the ordinary way — rewarding a useless model. Harmonically it
is 0.0. The harmonic mean refuses to let either term collapse.

## 5. ROC

Same idea, different axes — and the more common plot:

$$\text{TPR} = \frac{TP}{TP + FN} \qquad \text{FPR} = \frac{FP}{FP + TN}$$

**TPR is recall under another name.** Both names appear; know they are the same
thing. FPR is the mirror: of the actual negatives, how many did I wrongly flag?

Sweep the threshold from 1 to 0, plot TPR against FPR:

- **(0, 0)** — threshold above everything, nothing flagged.
- **(1, 1)** — threshold below everything, everything flagged.
- **(0, 1)** — top left, the perfect classifier: every positive found, no false alarms.
- **the diagonal** — random guessing.

A curve **below** the diagonal is not a terrible model. It is a good model
wired up backwards — flip its predictions and it is as good as its mirror image.

## 6. Two sets, then three

> "Evaluating a model should be done on an independent data set."

**Train/test** is the minimum. But the moment you compare two models on the test
set and keep the winner, you have used test data to make a decision — and your
final number is now optimistic. Hence:

> "In case we want to compare different models, we need a third set: the
> validation set. The test set is still only for final evaluation."

- **Train** — fit parameters.
- **Validation** — compare models, tune hyperparameters, choose.
- **Test** — touch **once**, at the very end, to report.

Every time you look at test and then change something, you leak a little of it
into your model. Nobody catches you; the number just quietly stops being true.

## 7. Cross-validation

> "We can do even better estimates by rotating the training data."

One validation split gives one estimate, and if it happens to be an easy split
you will believe a lie. **k-fold** splits the training data into k parts, and
each takes a turn as validation while the other k−1 train:

```python
from sklearn.model_selection import KFold
kf = KFold(n_splits=5)
for train_idx, val_idx in kf.split(X):
    ...
```

Every sample validates exactly once and trains k−1 times. You get k estimates —
a mean *and* a spread — for k times the compute. A large spread is itself the
finding: it means your estimate was never stable.

**Stratified** k-fold keeps each class in its original proportion in every
fold. On imbalanced data, use it: with 1% positives and 10 plain folds, a fold
can easily contain zero positives, and recall on that fold is undefined.

---

## 8. Paper exercises

No computer.

**P1.** From this matrix, compute accuracy, precision, recall and F1 by hand:

|  | pred 0 | pred 1 |
|---|---|---|
| **true 0** | 90 | 10 |
| **true 1** | 20 | 80 |

**P2.** A model has precision 0.95 and recall 0.30. Describe its behaviour in
one sentence, in plain language. Now the reverse: precision 0.30, recall 0.95.

**P3.** For each, say whether you would tune for precision or recall, and why:
(a) screening for a treatable but fatal cancer; (b) a spam filter for a work
inbox; (c) flagging transactions for a human fraud analyst who can review 50 a
day; (d) recommending which of 10,000 videos to autoplay next.

**P4.** 10,000 patients, 50 have the disease. Your model flags 40 people, 30 of
whom actually have it. Build the confusion matrix, then compute accuracy,
precision and recall. Which of the three would you put in the paper, and which
would you put in the abstract if you were being dishonest?

**P5.** Sketch the ROC curve for: (a) a perfect classifier; (b) random
guessing; (c) a classifier that is always exactly wrong. What does (c) tell you
to do?

**P6.** You have 100 samples and run 5-fold cross-validation. How many models
are trained? How many samples does each see in training? How many times is each
sample used for validation?

**P7.** Your colleague reports 94% test accuracy. What three questions do you
ask before believing the model is good?

Answers in [`../solutions/ml02/PAPER.md`](../solutions/ml02/PAPER.md).

---

## 9. Coding exercises

```bash
cd tutorial
./check.py ml02
```

**61 checks, 13 functions.** Exercise 1 and 2 use the lecturer's own example —
your `confusion_matrix` should reproduce the array on the slide exactly.

Exercise 5 is the one to sit with. You will build a model that does nothing and
watch it score 99%.

Exercises 7 and 8 want you to *reuse* what you built in 1–3 rather than
re-derive anything. If you find yourself recomputing TP inside `roc_points`,
back up — the point is that every metric falls out of the same four numbers.

Once green, check yourself against the real thing:

```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score
```

They should agree exactly. When they don't, it's nearly always the row/column
convention.

---

## 10. Checklist

- [ ] I can draw the confusion matrix and put TP/TN/FP/FN in the right cells
- [ ] I can derive precision and recall without looking them up
- [ ] I can say which is a column and which is a row
- [ ] I can explain in one sentence why 99% accuracy can be worthless
- [ ] I know which way the threshold moves precision and recall
- [ ] I know why F1 is the harmonic mean and not the ordinary one
- [ ] I know TPR is recall, and what FPR measures
- [ ] I can say why the test set is touched exactly once
- [ ] I can explain what k-fold buys and what it costs
- [ ] All 61 checks pass

**This is quiz material.** ML assignment 1 is due 11 September and this deck is
where it comes from.
