# HOML chapter map

*Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*, Géron, 3rd ed.

Free official notebooks: https://github.com/ageron/handson-ml3

## Part I — The Fundamentals of Machine Learning (scikit-learn)

Your current `.venv` covers all of this.

| Ch | Title | What you actually learn |
|----|-------|-------------------------|
| 1 | The Machine Learning Landscape | Vocabulary and the map of the field. No real code. Read it properly — it is where the terms get defined. |
| 2 | End-to-End Machine Learning Project | **The most important chapter in the book.** A complete project start to finish on California housing data. Do every step by hand. |
| 3 | Classification | MNIST digits. Precision, recall, ROC curves — why accuracy alone lies to you. |
| 4 | Training Models | What is happening *inside* `.fit()`. Gradient descent, linear/logistic regression. The most mathematical chapter; also the one that makes everything else click. |
| 5 | Support Vector Machines | SVMs and the kernel trick. |
| 6 | Decision Trees | Simple, visualisable models. Good intuition builders. |
| 7 | Ensemble Learning and Random Forests | Combining weak models into strong ones. Random forests, boosting. Very practical. |
| 8 | Dimensionality Reduction | PCA. Handling data with too many features. |
| 9 | Unsupervised Learning Techniques | k-means, DBSCAN, Gaussian mixtures. Learning without labels. |

## Part II — Neural Networks and Deep Learning (Keras/TensorFlow)

Needs a TensorFlow-capable setup — see `tensorflow-note.md`.

| Ch | Title |
|----|-------|
| 10 | Introduction to Artificial Neural Networks with Keras |
| 11 | Training Deep Neural Networks |
| 12 | Custom Models and Training with TensorFlow |
| 13 | Loading and Preprocessing Data with TensorFlow |
| 14 | Deep Computer Vision Using Convolutional Neural Networks |
| 15 | Processing Sequences Using RNNs and CNNs |
| 16 | Natural Language Processing with RNNs and Attention |
| 17 | Autoencoders, GANs, and Diffusion Models |
| 18 | Reinforcement Learning |
| 19 | Training and Deploying TensorFlow Models at Scale |

## How to read this book

It is a *hands-on* book and rewards being treated that way:

1. Read the chapter once without touching the keyboard.
2. Read it again, typing every code example yourself. Not copy-paste — typing.
   You will make typos, and fixing them teaches you what the code means.
3. Do the exercises at the end. Solutions are in Appendix A and in the repo.
4. Break something on purpose. Change a parameter, see what gets worse, ask why.

Chapter 2 and chapter 4 are the two that matter most. If you are short on time,
give those two double the attention and skim the rest.
