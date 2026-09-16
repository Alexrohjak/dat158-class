# ML Week 2 — paper answers

**P1.** TN=90, FP=10, FN=20, TP=80.

- accuracy = (80+90)/200 = **0.85**
- precision = 80/(80+10) = 80/90 = **0.889**
- recall = 80/(80+20) = 80/100 = **0.80**
- F1 = 2(0.889 × 0.80)/(0.889 + 0.80) = 1.422/1.689 = **0.842**

F1 sits between the two, nearer the lower one. That is the harmonic mean doing
its job.

**P2.** Precision 0.95, recall 0.30: *"When it flags something it is almost
always right, but it misses seven out of ten."* A cautious model — only speaks
when sure.

Precision 0.30, recall 0.95: *"It finds nearly everything, but two out of three
of its alarms are false."* A trigger-happy model — useful only if false alarms
are cheap to dismiss.

**P3.**

(a) **Cancer screening → recall.** A missed cancer may be fatal; a false alarm
costs a follow-up scan and some fear. Asymmetric consequences, so accept many
false positives to miss nothing.

(b) **Work spam filter → precision.** Spam reaching the inbox is an annoyance;
a real email silently binned can cost a job or a contract. The cost of a false
positive is far higher than a false negative.

(c) **Fraud analyst, 50 reviews a day → precision**, and note the reason is
different: it's a **capacity constraint**. Recall above what 50 reviews can
cover is wasted — the extra flags are never looked at. Tune precision so the 50
they *do* review are worth reviewing. (A good answer names precision-at-k.)

(d) **Autoplay → precision.** Ten thousand candidates and one slot. You do not
care about finding every good video; you care that the one you pick is good.
Recall is close to meaningless here.

**P4.** 10,000 patients, 50 diseased. Flagged 40, of whom 30 truly have it.

- TP = 30 (flagged, has it)
- FP = 10 (flagged, doesn't)
- FN = 20 (has it, missed — 50 − 30)
- TN = 9,940 (the rest)

|  | pred 0 | pred 1 |
|---|---|---|
| **true 0** | 9,940 | 10 |
| **true 1** | 20 | 30 |

- accuracy = (30 + 9,940)/10,000 = **99.7%**
- precision = 30/40 = **75%**
- recall = 30/50 = **60%**

Put **precision and recall** in the paper — ideally both, plus the raw matrix.
The dishonest abstract says **99.7% accurate**, which is true and useless: it
has missed 40% of the sick people. Do-nothing accuracy here is 99.5%, so the
model's headline number beats doing nothing by 0.2 points.

**P5.**

(a) **Perfect:** straight up the left edge to (0,1), then right to (1,1).
Passes through the top-left corner. AUC = 1.

(b) **Random:** the diagonal from (0,0) to (1,1). AUC = 0.5.

(c) **Always exactly wrong:** bows *below* the diagonal, toward (1,0). AUC < 0.5.

What to do about (c): **flip the predictions.** A consistently wrong classifier
is a consistently right one with its labels swapped — it has found the signal
and mislabelled it. A model that is genuinely uninformative sits *on* the
diagonal; being reliably below it is information.

**P6.** 100 samples, 5-fold:

- **5 models** trained, one per fold.
- Each trains on **80** samples (4 folds of 20) and validates on **20**.
- Each sample is used for validation **exactly once**, and for training **4** times.

**P7.** Any three of:

1. **What is the class balance?** 94% is worthless if 94% of the data is one class.
2. **What are precision and recall?** — or just show me the confusion matrix.
3. **How many times have you looked at the test set?** If tuning happened
   against it, 94% is optimistic and the real number is unknown.
4. **How big is the test set?** 94% of 50 samples is ±3 samples of noise.
5. **What does a trivial baseline score?** Always-majority, or a single rule.
   If the baseline gets 93%, the model has bought you one point.
6. **Where does the data come from, and will production look like it?**
