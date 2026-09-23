# DAT158 — Exam spring 2025 (V2025), questions only

Source: `docs/canvas/files/V2025_Oppgaver_Uten_Løsning.pdf` (WISEflow export, 31 pages). Answers are not included.

## Summary

- **Points shown on the paper: 70.** Seksjon 1 (ML) = 50p, Seksjon 2 (ALG) = 20p. Seksjon 3, 4 and 5 (ALG) show **no point values**, so the full total cannot be read from the paper.
- **ML half:** 22 graded questions (Seksjon 1, Questions 1–22), plus one ungraded comments field (0p).
- **ALG half:** 24 graded sub-questions: Seksjon 2 a)–k) (11), Seksjon 3 a)–d) (4), Seksjon 4 a)–d) (4, Set Cover / ILP / LP), Seksjon 5 a)–e) (5, TSP). There is also an optional comments field at the start of Seksjon 2.
- **Question types:**
  - Free text (rich-text box). Q3 has a 1000-word limit, Seksjon 3–5 boxes and the comment fields have 10000-word limits, and the rest show no limit.
  - Single-answer multiple choice (A–D, some A–E/A–F, one A–C).
  - Matrix / grid choice (one radio per row): Seksjon 2 c, f, i, j, k.
  - Integer numeric answer: Seksjon 2 b.
  - Code-review free text: Q5.
  - Constructive / drawing-style free text: tries, ILP/LP/dual formulation, running Double Tree and Christofides on a given MST.
- Labels in Seksjon 2–5 are a), b), … on the paper. In the headings below they carry a section-number prefix (e.g. `2a`) so that every heading is unique.

---

## Seksjon 1

### Question 1 (3p) [ML]

Describe the differences between supervised learning, unsupervised learning, and reinforcement learning.

*(Free text.)*

### Question 2 (1p) [ML]

Under which of these circumstances may machine learning ***not*** be a good solution to a prediction task?

- A. When the task requires high precision and accuracy
- B. When the data has many features
- C. When collecting representative data is difficult
- D. When the dataset is large and complex with many patterns

### Question 3 (4p) [ML]

Give the definition of precision for a binary classification task, and give an example of a case where high precision may be preferable to high recall.

*(Free text, 1000 word limit.)*

### Question 4 (4p) [ML]

If a dataset contains missing values, how can it be modified to be suitable for machine learning?

*(Free text.)*

### Question 5 (6p) [ML]

A student wants to predict the value of apartments and houses, using a list of recently sold homes as training data. The data is read from a CSV file into a `pandas.DataFrame`, where the first 3 row looks like the following:

| id | square_meters | num_rooms | year_built | city | price_sold |
|---|---|---|---|---|---|
| 0 | 42 | 2 | 1971 | Oslo | 2710000 |
| 1 | 88 | 4 | 1980 | Lillestrøm | 4230000 |
| 2 | 70 | 3 | 2001 | Molde | 3405000 |

As a first attempt, the student has written the code shown below. Identify three problems in the code that will impact the expected performance of the model, and suggest how to fix them.

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('house_data.csv')
print(data.head(n=3))  # This prints the table above

X_train = data.drop['id']
y_train = data['price_sold']

model = RandomForestClassifier(n_estimators=100, max_depth=5)
model.fit(data)

preds_train = model.predict(X_train)

score = accuracy_score(
    y_true=y_train,
    y_pred=preds_train
)
print('The mean squared error of the model predictions is:', score)
```

*(Free text.)*

### Question 6 (1p) [ML]

In the context of machine learning, what does *generalization* mean?

- A. The capability of the model to perform well on the training data.
- B. The capability of the model to perform well on new, unseen data.
- C. The process of transforming data to make it suitable for model training.
- D. The action of removing irrelevant features from the dataset.

### Question 7 (2p) [ML]

What is this loss function called, and what task is it best used for?

$$L = \frac{1}{m}\sum_{i=1}^{m}\left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

- A. Cross entropy. Used for regression.
- B. Cross entropy. Used for classification.
- C. Mean absolute error. Used for unsupervised learning.
- D. Mean squared error. Used for regression.

### Question 8 (2p) [ML]

You have trained a model that achieves 99% accuracy on your training data, but only 65% accuracy on the test data. What is the most likely problem your model is suffering from?

- A. Underfitting
- B. Overfitting
- C. Poor data quality
- D. Model complexity is too low
- E. The training and testing datasets contain unequal number of features

### Question 9 (2p) [ML]

What is the primary purpose of a *validation set* in the model selection process?

- A. To train the final production model after hyperparameters have been selected.
- B. To compare the performance of different models and hyperparameter combinations to select the best one.
- C. To provide the model with more training data to improve its accuracy.
- D. To check for and remove outliers from the raw dataset.

### Question 10 (1p) [ML]

As an alternative to scikit-learn's `GridSearchCV`, you consider using `RandomizedSearchCV`. What is the primary advantage of `RandomizedSearchCV`?

- A. It guarantees finding the absolute best hyperparameters for the model.
- B. It is better at exploring a wide range of values for a large number of hyperparameters within a fixed computational budget.
- C. It automatically determines which hyperparameters are most important to tune.
- D. It trains the model on the full dataset without needing a separate test set.

### Question 11 (1p) [ML]

What is the fundamental principle of k-fold cross-validation?

- A. It splits the data into a single training set and a single validation set.
- B. It uses `k` different models to train on the same data and averages their predictions.
- C. It splits the training data into `k` smaller sets (folds) and trains and evaluates the model `k` times, using a different fold for evaluation each time and the remaining `k-1` folds for training.
- D. It is a method for visualizing high-dimensional data in `k` dimensions.

### Question 12 (1p) [ML]

What are decision trees mainly used for?

- A. Dimensionality reduction
- B. Classification and regression tasks
- C. Clustering of data
- D. Estimation of probabilities

### Question 13 (1p) [ML]

What is the reason behind using random subsets of features in each tree in a Random Forest?

- A. To enhance interpretability of the model.
- B. To reduce the computational cost significantly.
- C. To ensure that the individual trees are decorrelated from each other.
- D. To make sure all trees receive the same information.

### Question 14 (1p) [ML]

What is *information gain* in the context of decision trees?

- A. The measure of how much information is missing from the dataset.
- B. A metric used to measure the effectiveness of a node split in terms of impurity reduction.
- C. The total amount of information present in a specific feature.
- D. The ratio of the number of nodes to the depth of a tree.

### Question 15 (2p) [ML]

What is the main disadvantage of decision trees compared to ensemble methods like Random Forest?

- A. Slower in making predictions.
- B. They are very sensitive to noisy data and can easily overfit, especially with deep trees.
- C. They cannot handle missing values in the dataset.
- D. They are harder to interpret than ensembles.

### Question 16 (2p) [ML]

What are *hyperparameters* in the context of machine learning models?

- A. Parameters learned from data during model training
- B. Variables that define the structure or configuration of the model and are set before training starts
- C. The output results from a trained model
- D. The dataset features used for training

### Question 17 (1p) [ML]

Which hyperparameter is important for controlling overfitting in decision trees?

- A. Number of input features
- B. Learning rate
- C. Maximum depth of the tree
- D. Feature importance

### Question 18 (1p) [ML]

Which of the following is true about Stochastic Gradient Descent (SGD)?

- A. It uses the entire dataset to compute each gradient update.
- B. It updates the model parameters after examining one training example at a time.
- C. It does not update the parameters until all data is processed.
- D. It always finds the global minimum.

### Question 19 (1p) [ML]

When using Gradient Descent, what problem might occur if the learning rate is set too high?

- A. The algorithm may get stuck in a local minimum.
- B. The algorithm may converge too slowly.
- C. The algorithm may overshoot the minimum and fail to converge.
- D. The algorithm will definitely find the global minimum.

### Question 20 (2p) [ML]

What is the main goal of *regularization* in machine learning models?

- A. A) To improve the model's performance on the training data
- B. B) To prevent the model from becoming too complex
- C. C) To decrease the variance of the model
- D. D) Both B and C

*(The option texts repeat their own letter prefix on the paper, as reproduced.)*

### Question 21 (1p) [ML]

How does *offline learning* typically handle the training process?

- A. By incrementally updating the model with each new data point
- B. By using all available data to train the model in one go
- C. By using dynamic models that evolve continuously
- D. By discarding the oldest data once new data arrives

### Question 22 (10p) [ML]

You are hired as a consultant to help improve a machine learning project at an insurance company. The goal of the project is to improve customer retention -- this means to identify customers who are likely to switch to a different insurance provider, and implement measures to make them stay. The project is not going very well, and this is why your consulting services are needed.

You know the following about the project:

- Data has been collected from 30% the company's own customers. 200 data points are from customers who have left in the last 5 years, while 1800 data point are from customers who (so far) have stayed.
- Performance has been measured in accuracy, on a test set that has same class distribution as the training set.
- The first model to be tested was a decision tree, which had an accuracy of 90% on the training dataset. No further testing was done, since this performance was considered sufficient.
- All features in data are either numerical or categorical, so feature engineering was not considered necessary.

With your knowledge of the ML project lifecycle, suggest how the project should be structured in order to improve performance on new data.

*(Free text.)*

### Comments (0p) [ML]

In this ungraded question, you can write any comments you have to the ML section of the exam. You can also leave it blank.

*(Free text, 10000 word limit. Ungraded.)*

---

## Seksjon 2

### For comments (no points) [ALG]

This response field is optional. Use it if you need to state any assumptions for the following problems in this section.

*(Free text, 10000 word limit.)*

### 2a) (1p) [ALG]

We have a textstring *T* with *n* characters, where $n \geq 4$. What is the **most fitting** description of the relation between the number of prefixes and the number of suffixes in T?

- A. They are always equal
- B. The number of prefixes are always smaller than the number of suffixes
- C. The number of prefixes are always larger than the number of suffixes
- D. The number of prefixes are always smaller or equal to the number of suffixes
- E. The number of prefixes are always larger or equal to the number of suffixes
- F. None of the others (no relation)

### 2b) (2p) [ALG]

How many comparisons of characters will the Boyer-Moore algorithm do before it decides that the pattern P = "abbb" is **not** in the text T = "abbcabccaabc"?

Answer (an integer): ____

### 2c) (2p — "2 points 1 point for each correct answer") [ALG]

Consider the Pattern Matching problem where we want to decide if a text of length $n$ contains a pattern of length $m$. What is the running time in the worst case for following algorithms?

*(Grid: choose one column per row.)*

|   | $O(m+n)$ | $O(mn)$ | $O(m^2)$ | $O(n^2)$ |
|---|---|---|---|---|
| A. Knuth-Morris-Pratt | ○ | ○ | ○ | ○ |
| B. Boyer-Moore | ○ | ○ | ○ | ○ |

### 2d) (2p) [ALG]

We want to support very many pattern matching queries on the same text. What is the most efficient algorithm?

- A. suffixTrieMatch algorithm
- B. Brute Force algorithm
- C. Boyer-Moore altgorithm
- D. Knuth-Morris-Pratt algoritm

### 2e) (1p) [ALG]

We have *n* strings where the characters are from an alphabet of size *d*. The strings are organized in a standard trie. What is the running time to search for a string of size *m*?

- A. $O(dmn)$
- B. $O(dm)$
- C. $O(mn)$
- D. $O(dn)$

### 2f) (2p — "2 points (0.5 points for each correct answer)") [ALG]

Determine whether the following decision problems are in the class P or NPC (NP complete).

*(Grid: choose P or NPC per row.)*

|   | P | NPC |
|---|---|---|
| A. Given a graph G and an integer *k*. Is it possible to color the nodes in G with 2 colors? | ○ | ○ |
| B. Given a text T and a pattern P. Is P a substring of T? | ○ | ○ |
| C. Given a graph G. Does G have an Eulerian Tour? | ○ | ○ |
| D. Given a graph G and an integer *k*. Does G have a Vertex Cover of at most k? | ○ | ○ |

### 2g) (1p) [ALG]

When we have an optimization problem, ideally, we want to find the optimal solution in polynomial time and for any instance. An approximation algorithm relaxes one of these requirements. Which?

- A. Optimal solution
- B. Polynomial time
- C. For any instance

### 2h) (2p) [ALG]

We consider a maximization problem. What does it mean to have a randomized $\frac{1}{2}$-aproximation algorithm for the problem.

- A. The expected value of the solution produced is at least $\frac{1}{2}$ of the optimal value.
- B. The algorithm finds the optimal solution at least half of time
- C. The value of the solution produced is always at least $\frac{1}{2}$ of the optimal value.
- D. The value of the solution produced is always at least $\frac{1}{2}$ of the optimal value half of the time.

### 2i) (2p) [ALG]

In the Knapsack Problem, we have a set of items $I = \{1, 2, \ldots, n\}$ where each item *i* has a value $v_i \geq 0$ and a size $0 \leq s_i \leq B$ where *B* is the size of the knapsack. In the dynamic programming algorithm a pair $(t, w)$ indicates that there exists a subset *S* of *I* where $\sum_{i \in S} s_i = t \leq B$ and $\sum_{i \in S} v_i = w$. A pair may dominate another pair. What is the relation between the pairs below?

*(Grid: choose one column per row.)*

|   | C dominates D | D dominates C | No relation |
|---|---|---|---|
| C = (4, 3), D = (5, 3) | ○ | ○ | ○ |
| C = (7, 2), D = (6, 4) | ○ | ○ | ○ |
| C= (3,7), D = (4, 8) | ○ | ○ | ○ |
| C = (8, 8), D = (9, 9) | ○ | ○ | ○ |

### 2j) (3p) [ALG]

We have a MAX SAT problem where we have listed the first clauses. They include all clauses containing variables $x_1, x_2$, and $x_3$. Assign true/false to the variables $x_1, x_2$, and $x_3$ (in that order) using the derandomized algorithm we have seen in lectures / compulsory assignments.

$C_1 = 1\,(x_1 \lor x_2 \lor \overline{x_3} \lor \overline{x_4})$

$C_2 = 1\,(\overline{x_1} \lor \overline{x_2})$

$C_3 = 1\,(\overline{x_2} \lor \overline{x_3})$

$C_4 = 2\,(x_3 \lor x_4)$

...

*(Grid: choose True or False per variable.)*

|   | True | False |
|---|---|---|
| $x_1$ | ○ | ○ |
| $x_2$ | ○ | ○ |
| $x_3$ | ○ | ○ |

### 2k) (2p — "2 points, 1 for each answer") [ALG]

We have an instance of the Bin Packing problem where we have the following list of pieces $\{0.6,\ 0.6,\ 0.3,\ 0.3,\ 0.4,\ 0.4,\ 0.25,\ 0.25,\ 0.3,\ 0.25\}$. How many bins will the First-Fit and the First-Fit-Decreasing algorithms use to pack the items?

*(Grid: choose one column per row.)*

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| First-Fit | ○ | ○ | ○ | ○ | ○ | ○ |
| First-Fit-Decreasing | ○ | ○ | ○ | ○ | ○ | ○ |

---

## Seksjon 3

*(No point values are shown for this section.)*

### 3a) (points not shown) [ALG]

Given the following set of strings S = {aaa, abab, abacc, abcb}. Construct a standard trie for S.

*(Free text.)*

### 3b) (points not shown) [ALG]

If we add the string "ababc" to S, we will have a problem. What is the problem and how can we solve it?

*(Free text, 10000 word limit.)*

### 3c) (points not shown) [ALG]

What is the main idea behind Compressed tries? Redraw the trie from a) as a compressed trie.

*(Free text, 10000 word limit.)*

### 3d) (points not shown) [ALG]

Give an example of a problem where tries are useful.

*(Free text, 10000 word limit.)*

---

## Seksjon 4

*(No point values are shown for this section.)*

**Set Cover**

You work for a startup company that needs to build competency in six key areas of expertise, labled $1, 2, 3, 4, 5, 6$. We are given a list of $4$ applicants, $S_1,\ S_2,\ S_3,\ S_4$, each with skills in a subset of these areas and a salary requirement $w_1,\ w_2,\ w_3,\ w_4$, as shown below:

$S_1 = \{1,\ 2,\ 3,\ 4,\ 5\},\ w_1 = 10$

$S_2 = \{1,\ 6\},\ w_2 = 3$

$S_3 = \{2,\ 3,\ 4\},\ w_3 = 5$

$S_4 = \{4,\ 5,\ 6\},\ w_4 = 4$

You are given the following task: Formulate this problem as an Integer Linear Program ILP to determine how the startup can hire a group of applicants that together cover all six areas, while keeping the total salary as low as possible?

### 4a) (points not shown) [ALG]

Formulate the corresponding Set Cover (mengde dekke) problem as an integer linear program (ILP). You can write x1 in stead of $x_1$ and use <= and >= in stead of $\leq$ and $\geq$.

*(Free text, 10000 word limit.)*

### 4b) (points not shown) [ALG]

i) Write the LP relaxation of the ILP from part a).

ii) Briefly explain how the optimal solution of the LP relaxation relates to the optimal solution of the ILP from part a).

*(Free text, 10000 word limit.)*

### 4c) (points not shown) [ALG]

i) Write the dual of the LP relaxation from part b).

ii) Briefly explain how a feasible (mulig) solution to the dual relates to the optimal solution of the LP from part b).

*(Free text, 10000 word limit.)*

### 4d) (points not shown) [ALG]

After two hours, you return to the hiring manager and say:

*"I solved the task as you asked. I even wrote a program that can turn any similar hiring problem into an ILP and solve it. But I do not think all that work was needed, unless we expect larger problems of this kind in the future."*

The manager looks confused and says:

*"But Set Cover is NP-complete. To solve this instance as quickly as possible, we had to use an ILP solver."*

How is NP-completeness misunderstood in this conversation? Who understands the situation better, and why?

*(Free text, 10000 word limit.)*

---

## Seksjon 5

*(No point values are shown for this section.)*

### 5a) (points not shown) [ALG]

Formulate the Travelling Salesperson Problem (TSP). You can assume you have a graph with *n* vertices.

*(Free text, 10000 word limit.)*

### 5b) (points not shown) [ALG]

The Double Tree algorithm is an approximation algorithm for the TSP-problem. Give the main steps in this algorithm.

*(Free text, 10000 word limit.)*

### 5c) (points not shown) [ALG]

Run the Double Tree algorithm on a graph with the following minimum spanning tree. You can assume that distances between the vertices are the distances on the paper/screen. Show/explain intermediate steps.

**Figure (minimum spanning tree, 8 vertices, 7 edges, drawn on a grid):**

```
        (1)       (2)
         |         |
(3) --- (4) ----- (5) --- (6)
         |         |
        (7)       (8)
```

- Vertices 4 and 5 sit on the middle horizontal row, with 3 to the left of 4 and 6 to the right of 5.
- 1 is directly above 4, and 7 is directly below 4. 2 is directly above 5, and 8 is directly below 5.
- The edges are 1–4, 3–4, 4–7, 4–5, 2–5, 5–6 and 5–8.
- All edges are straight horizontal or vertical segments of roughly equal length. The 4–5 edge looks about the same length as the others, possibly slightly longer.

*(Free text, 10000 word limit.)*

### 5d) (points not shown) [ALG]

Christofides' algorithm is another approximation algorithm for the TSP-problem. Give the main steps in this algorithm.

*(Free text, 10000 word limit.)*

### 5e) (points not shown) [ALG]

Run Christofides' on a graph with the following minimum spanning tree.. Show/explain intermediate steps. You can assume that distances between the vertices are the distances on the paper/screen.

**Figure:** the same minimum spanning tree as in 5c:

```
        (1)       (2)
         |         |
(3) --- (4) ----- (5) --- (6)
         |         |
        (7)       (8)
```

The edges are 1–4, 3–4, 4–7, 4–5, 2–5, 5–6 and 5–8, with the same layout as in 5c.

*(Free text, 10000 word limit.)*
