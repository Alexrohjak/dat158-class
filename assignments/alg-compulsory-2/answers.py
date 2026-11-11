import random


# Problems 4

# Problem 2a

def random_assignment(n):
    return {i: random.random() < 0.5 for i in range(1, n + 1)}

def literal_is_true(literal, assignment):
    variable = abs(literal)
    value = assignment[variable]
    if literal > 0:
        return value
    else:
        return not value

def satisfied_weight(clauses, assignment):
    total = 0
    for weight, literals in clauses:
        for literal in literals:
            if literal_is_true(literal, assignment):
                total += weight
                break
    return total

clauses = [
      (3, [1, -2, 3]),
      (4, [1, -3]),
      (1, [-1, 2, -5]),
      (3, [-1, 3]),
      (2, [2, -4]),
      (7, [-2, 5, 9]),
      (2, [3, -4]),
      (3, [-4, -5, 21]),
      (5, [5, -12]),
  ]

for run in range(5):
      a = random_assignment(21)
      print("weight", satisfied_weight(clauses, a), "of 30")

# Problem 2b

