# ML Week 1 — What machine learning is, and numpy

**Source:** uke 34's decks, `1-intro` and `2-python`, mirrored in
[`../../weeks/uke34-ml/slides/`](../../weeks/uke34-ml/slides/).
**Book:** Géron (HOML) ch. 1.
**Budget:** 2–3 hours.

By the end you should be able to define machine learning the way the lecturer
does, sort any problem into the four kinds of learning, and manipulate arrays
without writing a loop.

---

## 1. The definition to memorise

The lecturer puts Tom Mitchell's 1997 definition on a slide of its own, which
is a strong hint about the exam:

> A computer program is said to learn from **experience E** with respect to some
> **task T** and some **performance measure P**, if its performance on T, as
> measured by P, improves with experience E.

Worth the memorisation because it forces three questions that are easy to skip:

- **What is the task, exactly?** "Improve the business" is not a task. "Label
  this email spam or not-spam" is.
- **What experience is available?** No data, no learning. This is where most
  real projects die.
- **How will you measure it?** Pick P *before* you train, or you will pick the
  measure that flatters the model you happen to have built.

Spam filter: E is a folder of emails already marked spam; T is flagging one new
email; P is the fraction flagged correctly.

## 2. Why this instead of ordinary programming

The two diagrams in `1-intro` ("Traditional (rule-based) programming" and
"Machine learning") are the same picture with two boxes swapped.

| | You supply | The computer produces |
|---|---|---|
| Rule-based | rules + data | answers |
| Machine learning | data + answers | **the rules** |

So machine learning is worth reaching for exactly when *you cannot write the
rules down* — not when the problem is hard, but when the rules are unknown,
too numerous, or keep changing. Spam is the classic case: the rules shift every
time a spammer adapts.

The corollary is the one people forget: if you *can* write the rules, write
them. A regular expression is faster, cheaper and debuggable.

## 3. The four kinds of learning

Two questions get you to the answer every time.

**Is each datapoint labelled?**

- **Yes → supervised.** Then: is the label a *category* or a *number*?
  - Category → **classification**. Spam/not-spam, which digit, which species.
  - Number → **regression**. House price, tomorrow's temperature.
- **No → unsupervised.** The model groups similar points itself. Customer
  segmentation, anomaly detection.
- **No, but there are rewards → reinforcement.** An agent acts, and is
  rewarded or penalised. Game playing, robot control.

The trap is that the *same data* supports different kinds. House data with
prices is regression; the same table with "sold/unsold" is classification; drop
the labels entirely and it is a clustering problem. **The labels decide, not
the data.**

## 4. Data, and how it arrives

Structured data is a table — the lecturer uses Titanic. Rows are **samples**,
columns are **features**, and one column is singled out as the **label**.

Machine learning wants that table as two objects, and this convention holds for
every model you will meet this semester:

```
X    shape (n_samples, n_features)    the features, always 2-D
y    shape (n_samples,)               the labels, always 1-D
```

`X` stays 2-D even with a single feature — shape `(100, 1)`, not `(100,)`.
Nearly every confusing sklearn error you hit this semester is this rule being
broken. When one bites, print `X.shape` first, before reading the traceback.

## 5. Two ways data goes wrong

From the "Data challenges" slide:

- **Too little data → overfitting.** The model memorises the training set and
  fails on anything new. Perfect training accuracy is a symptom, not a triumph.
- **Unrepresentative data.** New data doesn't look like the training data, so
  the model was never learning the thing you cared about.

Which is why you **hold out a test set before you train**, and do not look at
it. Two numbers, and the gap between them tells you more than either alone:

| Train | Test | Reading |
|---|---|---|
| high | high | good fit |
| high | low | **overfitting** — memorised, didn't generalise |
| low | low | **underfitting** — model too simple, or features too weak |

## 6. numpy, in one idea

> "The core of numpy is the array, on which we can do operations without
> explicit loops."

```python
a = [1, 2, 3]
b = [x * 2 for x in a]          # vanilla Python: the loop is yours

import numpy as np
a = np.array([1, 2, 3])
b = a * 2                       # numpy: the loop moved into C
```

This isn't only about speed. `a * 2` says *what* you want; the loop says *how*.
Every ML library is built on that shift, and code written the numpy way is
shorter and harder to get wrong.

**Slicing** is `[start:stop]`, zero-based, stop **excluded**:

```python
a = np.array([0, 1, 2, 3, 4])
a[2:4]      # array([2, 3])   — not element 4
a[1:-1]     # array([1, 2, 3]) — -1 means one before the end
a[:]        # everything
```

**Element-by-element** is the default:

```python
np.power(a, 2)     # or a ** 2
a * b              # NOT matrix multiplication — that's a @ b
```

**Broadcasting** stretches a smaller array to fit a bigger one:

```python
X = np.array([[1., 2.], [3., 4.]])
X.mean(axis=0)      # array([2., 3.])  — one mean per COLUMN
X - X.mean(axis=0)  # subtracts each column's mean from that column
```

`axis` is the axis that gets **collapsed**. Rows are samples, so `axis=0`
collapses samples and leaves one number per feature — which is almost always
what you want. If you get the wrong shape, print both `axis=0` and `axis=1` and
look; guessing wastes more time than checking.

---

## 7. Paper exercises

No computer. Write them out, then check.

**P1.** Give E, T and P for each:
  (a) a model predicting tomorrow's electricity price;
  (b) a model spotting fraudulent card transactions;
  (c) a chess engine that improves by playing itself.

**P2.** Classify each as classification, regression, unsupervised or
reinforcement:
  (a) grouping HVL students by which courses they take;
  (b) predicting how many minutes a bus will be late;
  (c) deciding whether an x-ray shows a fracture;
  (d) a robot learning to walk without falling;
  (e) predicting which of 26 letters a handwritten character is.

**P3.** A model scores 100% on training data and 62% on test data. Name the
problem, and give two different things you could do about it.

**P4.** Write the shapes. 500 houses, 8 features, predicting price.
What are `X.shape` and `y.shape`? Now with one feature?

**P5.** Without running it, what does each line give?
```python
a = np.array([0, 1, 2, 3, 4, 5])
a[1:4]
a[:-2]
a[::2]
a * a
a.mean(axis=0)
```

**P6.** You are asked to build a spam filter and given 10,000 emails, none
labelled. What kind of learning problem is this, and what is your first move?

Answers in [`../solutions/ml01/PAPER.md`](../solutions/ml01/PAPER.md).

---

## 8. Coding exercises

```bash
cd tutorial
./check.py ml01
```

**54 checks, 13 functions.** Exercises 1–3 are numpy drills — do them fast.
Exercises 6 and 9 are where the real learning is.

Exercise 9 builds a nearest-centroid classifier: `fit` learns one centroid per
class, `predict` labels each point by its closest centroid. It is a genuine
model, in about eight lines. Every estimator in sklearn is this same
`fit`/`predict` pair with more machinery inside — once you have written one by
hand, the library stops being magic.

No sklearn this week. Deliberately.

---

## 9. Checklist

- [ ] I can state Mitchell's definition from memory, all three letters
- [ ] I can say when ML is the *wrong* tool
- [ ] I can sort a problem into the four kinds without hesitating
- [ ] I know why `X` is 2-D and `y` is 1-D, even with one feature
- [ ] I can explain what `axis=0` collapses, and why that's the useful one
- [ ] I can read a train/test accuracy pair and name the failure
- [ ] All 54 checks pass

**Next week:** the confusion matrix, and why accuracy on its own lies to you.
