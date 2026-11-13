-- Dat 158 Oblig 2

-- Problems 2:

5). 
    a). Local search algorithm

    Start time = 0

    Machine 1 => Job 1 [0-4] -> Job 2 [4-11] -> Job 3 [11-13] -> Job 4 [13-22] -> Job 5 [22-34] -> Job 6 [34-39] -> Job 7 [39-42]

    Machine 2 =>

    Machine 3 =>

    Makespan = 42, S_l = 39 -> move Job 7 [39-42] to Machine 2:

    Machine 1 => Job 1 [0-4] -> Job 2 [4-11] -> Job 3 [11-13] -> Job 4 [13-22] -> Job 5 [22-34] -> Job 6 [34-39]

    Machine 2 => Job 7 [0-3]

    Machine 3 =>

    Makespan = 39, S_l = 34 -> move Job 6 [34-39] to Machine 3:

    Machine 1 => Job 1 [0-4] -> Job 2 [4-11] -> Job 3 [11-13] -> Job 4 [13-22] -> Job 5 [22-34]

    Machine 2 => Job 7 [0-3]

    Machine 3 => Job 6 [0-5]

    Makespan = 34, S_l = 22 -> move Job 5 [22-34] to Machine 2:

    Machine 1 => Job 1 [0-4] -> Job 2 [4-11] -> Job 3 [11-13] -> Job 4 [13-22]

    Machine 2 => Job 7 [0-3] -> Job 5 [3-15]

    Machine 3 => Job 6 [0-5]

    Makespan = 22, S_l = 13 -> move Job 4 [13-22] to Machine 3:

    Machine 1 => Job 1 [0-4] -> Job 2 [4-11] -> Job 3 [11-13]

    Machine 2 => Job 7 [0-3] -> Job 5 [3-15]

    Machine 3 => Job 6 [0-5] -> Job 4 [5-14]

    Makespan = 15, S_l = 3 -> cannot optimise further as the last job, Job 5, starts at 3 and M1 (free at 13) and M3 (free at 14) both become free later than that. So no move helps.

    Result: C_max = 15. M1: J1, J2, J3 | M2: J7, J5 | M3: J6, J4

    b). Greedy algorithm 

    Start time = 0

    [J1, J2, J3, J4, J5, J6, J7]

    Machine 1 =>

    Machine 2 =>

    Machine 3 =>

    Job 1 [4] loads (0,0,0) -> Machine 1

    Machine 1 => Job 1 [0-4]

    Machine 2 =>

    Machine 3 =>

    Job 2 [7] loads (4,0,0) -> Machine 2

    Machine 1 => Job 1 [0-4]

    Machine 2 => Job 2 [0-7]

    Machine 3 =>

    Job 3 [2] loads (4,7,0) -> Machine 3

    Machine 1 => Job 1 [0-4]

    Machine 2 => Job 2 [0-7]

    Machine 3 => Job 3 [0-2]

    Job 4 [9] loads (4,7,2) -> Machine 3

    Machine 1 => Job 1 [0-4]

    Machine 2 => Job 2 [0-7]

    Machine 3 => Job 3 [0-2] -> Job 4 [2-11]

    Job 5 [12] loads (4,7,11) -> Machine 1

    Machine 1 => Job 1 [0-4] -> Job 5 [4-16]

    Machine 2 => Job 2 [0-7]

    Machine 3 => Job 3 [0-2] -> Job 4 [2-11]

    Job 6 [5] loads (16,7,11) -> Machine 2

    Machine 1 => Job 1 [0-4] -> Job 5 [4-16]

    Machine 2 => Job 2 [0-7] -> Job 6 [7-12]

    Machine 3 => Job 3 [0-2] -> Job 4 [2-11]

    Job 7 [3] loads (16,12,11) -> Machine 3

    Machine 1 => Job 1 [0-4] -> Job 5 [4-16]

    Machine 2 => Job 2 [0-7] -> Job 6 [7-12]

    Machine 3 => Job 3 [0-2] -> Job 4 [2-11] -> Job 7 [11-14]

    Result: C_max = 16. M1: J1, J5 | M2: J2, J6 | M3: J3, J4, J7

    c). Longest processing time

    Jobs        = [J1[4], J2[7], J3[2], J4[9], J5[12], J6[5], J7[3]] 

    Sorted Jobs = [J5[12], J4[9], J2[7], J6[5], J1[4], J7[3], J3[2]]

    Start time = 0

    [J5, J4, J2, J6, J1, J7, J3]

    Machine 1 =>

    Machine 2 =>

    Machine 3 =>

    Job 5 loads (0,0,0) -> Machine 1

    Machine 1 => Job 5 [0-12]

    Machine 2 =>

    Machine 3 =>

    Job 4 loads (12,0,0) -> Machine 2

    Machine 1 => Job 5 [0-12]

    Machine 2 => Job 4 [0-9]

    Machine 3 =>

    Job 2 loads (12,9,0) -> Machine 3

    Machine 1 => Job 5 [0-12]

    Machine 2 => Job 4 [0-9]

    Machine 3 => Job 2 [0-7]

    Job 6 loads (12,9,7) -> Machine 3

    Machine 1 => Job 5 [0-12]

    Machine 2 => Job 4 [0-9]

    Machine 3 => Job 2 [0-7] -> Job 6 [7-12]

    Job 1 loads (12,9,12) -> Machine 2

    Machine 1 => Job 5 [0-12]

    Machine 2 => Job 4 [0-9] -> Job 1 [9-13]

    Machine 3 => Job 2 [0-7] -> Job 6 [7-12]

    Job 7 loads (12,13,12) -> tie, job goes to lowesst number -> Machine 1

    Machine 1 => Job 5 [0-12] -> Job 7 [12-15]

    Machine 2 => Job 4 [0-9] -> Job 1 [9-13]

    Machine 3 => Job 2 [0-7] -> Job 6 [7-12]

    Job 3 loads (15,13,12) -> Machine 3

    Machine 1 => Job 5 [0-12] -> Job 7 [12-15]

    Machine 2 => Job 4 [0-9] -> Job 1 [9-13]

    Machine 3 => Job 2 [0-7] -> Job 6 [7-12] -> Job 3 [12-14]

    Result: C_max = 15. M1: J5, J7 | M2: J4, J1 | M3: J2, J6, J3

    d). Lower bound

    Lowerbound      = max(longest task, average load)

    longest task    = Job 5 [12]

    average load = total work time / number of machines
                    = 42 / 3
                    = 14

    Lowerbound      = max(12, 14)
                    = 14
    
    The longest job (12) has to run uninterrupted on one machine, so no schedule can possibly finish before t = 12.
    42 units of work spread across 3 machines means at the very least one machine must work >= 14.

    e). Is it possible to achieve the answer in d)?

    Yes it is possible to achieve:

    Machine 1: J5 [12] + J3 [2] = 14

    Machine 2: J2 [7] + J1 [4] + J7 [3] = 14

    Machine 3: J4 [9] + J6 [5] = 14


6).
    a). Verify the triangle inequality

    d(1,5) = 11

    condition: d(1,5) <= d(1,x) + d(x,5)

    d(1,5) <= d(1,2) + d(2,5) = 11 <= 4 + 7 -> True
    d(1,5) <= d(1,3) + d(3,5) = 11 <= 5 + 6 -> True
    d(1,5) <= d(1,4) + d(4,5) = 11 <= 10 + 3 -> True
    d(1,5) <= d(1,6) + d(6,5) = 11 <= 7 + 6 -> True

    Triangle inequality holds for all columns, and through 2 and 3 it holds with equality.

    b). Nearest addition algorithm

    Smallest distance and starting point = d(3,6) = 2

    Tour        = 3 -> 6 -> 3
    Tour length = 2 + 2 = 4

    Inside: {3, 6} Outside: {1, 2, 4, 5}

    from 3: 1 = 5, 2 = 9, 4 = 9, 5 = 6
    from 6: 1 = 7, 2 = 9, 4 = 9, 5 = 6

    Next vertex: d(3,1)

    Tour        = 3 -> 1 -> 6 -> 3 
    Tour length = 5 + 7 + 2 = 14 

    Inside: {1, 3, 6} Outside: {2, 4, 5}

    from 1: 2 = 4, 4 = 10, 5 = 11
    from 3: 2 = 9, 4 = 9, 5 = 6
    from 6: 2 = 9, 4 = 9, 5 = 6

    Next vertex = d(1,2)

    Tour        = 3 -> 1 -> 2 -> 6 -> 3
    Tour length = 5 + 4 + 9 + 2 = 20

    Inside {1, 2, 3, 6} Outside: {4, 5}

    We skipped vertices 4 and 5 but they would be added to the next two iterations.

    c). Double tree algorithm

    All edges     = [3-6 (2), 4-5 (3), 1-2 (4), 1-3 (5), 2-4 (6), 5-6 (6), 3-5 (6), 2-5 (7), 1-6 (7), 4-6 (9), 2-3 (9), 4-3 (9), 2-6 (9), 1-4 (10), 1-5 (11)]

    3-6 (2) -> take                         Edges = 1   {3-6}
    4-5 (3) -> take                         Edges = 2   {3-6 4-5}
    1-2 (4) -> take                         Edges = 3   {1-2 3-6 4-5}
    1-3 (5) -> take                         Edges = 4   {6-3-1-2 4-5}

    2-4 (6) -> take                         Edges = 5   {6-3-1-2-4-5} or, MST = 20
    5-6 (6) -> take                         Edges = 5   {4-5-6-3-1-2} or, MST = 20
    3-5 (6) -> take                         Edges = 5   {2-1-3-5-4}     MST = 20
                                                             |
                                                             6   
    
    Double tree -> walk through the entire tree, starting at vertex 1:

    Tree a: {6 - 3 - 1 - 2 - 4 - 5}

    Walk           -> 1 - 2 - 4 - 5 - 4 - 2 - 1 - 3 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 4 - 5 - 3 - 6 - 1
    Length        -> 4 + 6 + 3 + 6 + 2 + 7 = 28

    Tree b: {4 - 5 - 6 - 3 - 1 - 2}

    Walk          -> 1 - 2 - 1 - 3 - 6 - 5 - 4 - 5 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 3 - 6 - 5 - 4 - 1
    Length        -> 4 + 9 + 2 + 6 + 3 + 10 = 34

    Tree c: {2 - 1 - 3 - 5 - 4}
                     |
                     6
    
    Walk          -> 1 - 2 - 1 - 3 - 5 - 4 - 5 - 3 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 3 - 5 - 4 - 6 - 1
    Length        -> 4 + 9 + 6 + 3 + 9 + 7 = 38

    Best tour = Tree a, 1 - 2 - 4 - 5 - 3 - 6 - 1, with length 28
    Guarantee: tour <= 2 x MST = 2 x 20 = 40, and all three trees are within that. 

    d). Christofides

    All edges     = [3-6 (2), 4-5 (3), 1-2 (4), 1-3 (5), 2-4 (6), 5-6 (6), 3-5 (6), 2-5 (7), 1-6 (7), 4-6 (9), 2-3 (9), 4-3 (9), 2-6 (9), 1-4 (10), 1-5 (11)]

    3-6 (2) -> take                         Edges = 1   {3-6}
    4-5 (3) -> take                         Edges = 2   {3-6 4-5}
    1-2 (4) -> take                         Edges = 3   {1-2 3-6 4-5}
    1-3 (5) -> take                         Edges = 4   {6-3-1-2 4-5}

    2-4 (6) -> take                         Edges = 5   {6-3-1-2-4-5} or, MST = 20
    5-6 (6) -> take                         Edges = 5   {4-5-6-3-1-2} or, MST = 20
    3-5 (6) -> take                         Edges = 5   {2-1-3-5-4}     MST = 20
                                                             |
                                                             6   

    Tree a: {6 - 3 - 1 - 2 - 4 - 5}

    Odd degree = 5, 6 -> 5 - 6, length = 6
    Walk          -> 1 - 2 - 4 - 5 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 4 - 5 - 6 - 3 - 1
    Length        -> 4 + 6 + 3 + 6 + 2 + 5 = 26

    Tree b: {4 - 5 - 6 - 3 - 1 - 2}

    Odd degree = 2, 4 -> 2 - 4, length = 6
    Walk          -> 1 - 2 - 4 - 5 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 4 - 5 - 6 - 3 - 1
    Length        -> 4 + 6 + 3 + 6 + 2 + 5 = 26

    Tree c: {2 - 1 - 3 - 5 - 4}
                    |
                    6
    
    Odd degree = 2, 3, 4, 6 -> (2 - 3, 4 - 6) length = 18, (2 - 4, 3 - 6) length = 8, (2 - 6, 3 - 4) length = 18
    minimum matching = (2 - 4, 3 - 6)
    Walk          -> 1 - 2 - 4 - 5 - 3 - 6 - 3 - 1
    Shortcut tour -> 1 - 2 - 4 - 5 - 3 - 6 - 1
    Length        -> 4 + 6 + 3 + 6 + 2 + 7 = 28

    Best tour = tree a and b, 1 - 2 - 4 - 5 - 6 - 3 - 1, length = 26.

-- Problems 3:

2).
    a). B = 10

    A(1) -> empty bag and item 1:

    {(0, 0), (3, 5)}

    A(2) -> add item 2:

    Before : {(0, 0), (3, 5), (2 ,3), (5, 8)}
    After  : {(0, 0), (3, 5), (2 ,3), (5, 8)} -> no changes because no dominance

    A(3) -> add item 3:

    Before : {(0, 0), (3, 5), (2, 3), (5, 8), (2, 2), (5, 7), (4, 5), (7, 10)}
    After  : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10)} out because of dominance -> (2, 2), (5, 7), (4, 5)

    A(4) -> add item 4: 

    Before : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10), (4, 5),  (7, 10), (6, 8), (9, 13), (11, 15)}
    After  : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10), (9, 13)} -> out because of dominance -> (4, 5), (6, 8), out because t > B -> (11, 15), out because of duplicates -> (7, 10)

    A(5) -> add item 5:
    Before : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10), (9, 13), (3, 4), (6, 9), (5, 7), (8, 12), (10, 14), (12, 17)} 
    After  : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10), (9, 13), (6, 9), (8, 12), (10, 14)} -> out because of dominance -> (3, 4), (5, 7), out because t > B -> (12, 17)

    A(6) -> add item 6:
    Before : {(0, 0), (3, 5), (2, 3), (5, 8), (7, 10), (9, 13), (6, 9), (8, 12), (10, 14), (1, 2), (4, 7), (3, 5), (6, 10), (8, 12), (10, 15), (7, 11), (9, 14), (11, 16)}
    After  : {(0, 0), (3, 5), (2, 3), (5, 8), (8, 12), (1, 2), (4, 7), (6, 10), (10, 15), (7, 11), (9, 14)} -> out because of dominance -> (6, 9), (7, 10), (10, 14), (9, 13), out because t > B -> (11, 16), out because of duplicates -> (3, 5), (8, 12)

    The algorithm shows that the largest possible legal w = 15 in (10, 15)

    b).

    After removing dominated pairs, no two pairs share the same size t (the one with the higher value would dominate). t is an integer with 0 <= t <= B, so there are at most B + 1 pairs in A(i). Our A(6) with B = 10 has exactly 11 pairs. 

    c). items = n, vi = value of item i, one item = (t, w) -> where t = total size, and w = total value of item

    After removing all the dominated pairs, no two pairs in A(i) share the same value w: if two pairs did have the same w, the one with the smaller t would dominate the other. Every value w is an integer 0 <= w <= V, from the empty bag (0, 0) up to taking every single item (V = Σ vi). So there are at most V + 1 pairs in A(i).

    The example is that in our question, all 6 items have a total value of = 5 + 3 + 2 + 5 + 4 + 2 = 21, so A(i) can never hold more than 22 pairs.

6). Approximation algorithm based on Shortest Remaining Processing Time for preemptive scheduling.

Phase 1: SRPT table

t = 0, jobs released : J1 (6), J2 (5)

Job with lowest remaining processing time -> J2, and is released and works for t = 1

t = 1, job released : J3 (3)

current remaining work: J1 (6), J2 (4)

Job with lowest remaining processing time -> J3 is released and works for t = 1

t = 2, job released : J4 (1)

current remaining work: J1 (6), J2 (4), J3 (2)

Job with lowest remaining processing time -> J4 is released and works for t = 1 -> J4 complete at t = 3

t = 3, job released : J5 (4)

current remaining work: J1 (6), J2 (4), J3 (2)

Job with lowest remaining processing time -> J3 is released and works for t = 1

t = 4, job released : J6 (2)

current remaining work: J1 (6), J2 (4), J3 (1), J5 (4), J6 (2)

Job with lowest remaining processing time -> J3 is released and works for t = 1 -> J3 complete at t = 5

t = 5, job released : None

current remaining work: J1 (6), J2 (4), J5 (4), J6 (2)

Job with lowest remaining processing time -> J6 is released and works for t = 2 -> J6 complete at t = 7

t = 7, job released : None

current remaining work: J1 (6), J2 (4), J5 (4) -> J2 and J5 tie, go with lower number

Job with lowest remaining processing time -> J2 is released and works for t = 4 -> J2 complete at t = 11

t = 11, job released : None

current remaining work: J1 (6), J5 (4)

Job with lowest remaining processing time -> J5 is released and works for t = 4 -> J5 complete at t = 15

t = 15, job released : None

current remaining work; J1 (6)

Job with lowest remaining processing time -> J1 is released and works for t = 4

t = 19, job released : J7 (2)

current remaining work: J1 (2), J7 (2) -> J1 and J7 tie, go with lower number

Job with lowest remaining processing time -> J1 is released and works for t = 2 -> J1 complete at t = 21

t = 21, job released : None

current remaining work: J7 (2)

Job with lowest remaining processing time -> J7 is released and works for t = 2 -> J7 complete at t = 23

Completion order: J4 = 3, J3 = 5, J6 = 7, J2 = 11, J5 = 15, J1 = 21, J7 = 23

Sum of tasks    : 3 + 5 + 7 + 11 + 15 + 21 + 23 = 85

Phase 2: no pausing

J4 (2, 1), Start = max(2, 0), End = 2 + 1 = 3

J3 (1, 3), Start = max(1, 3), End = 3 + 3 = 6 

J6 (4, 2), Start = max(4, 6), End = 6 + 2 = 8

J2 (0, 5), Start = max(0, 8), End = 8 + 5 = 13

J5 (3, 4), Start = max(3, 13), End = 13 + 4 = 17

J1 (0, 6), Start = max(0, 17), End = 17 + 6 = 23

J7 (19, 2), Start = max(19, 23), End = 23 + 2 = 25

Sum of tasks     : 3 + 6 + 8 + 13 + 17 + 23 + 25 = 95

Phase 1 sum (85) <= OPT <= Phase 2 sum (95) <= 2 x 85


-- Problems 4

2).

    a). 
    
    find answers in answers.py

    b).

    x1 -> 

    C1 = 3(x1 || (not) x2 || x3)

    x1 = true  -> 3(True || open || open), weight = 3x1 = 3
    x1 = false -> 3(False || open || open), weight = 3 x (1-1/2²) = 3x3/4 = 2.25

    C2 = 4(x1 || (not) x3)

    x1 = true  -> 4(True || open), weight = 4x1 = 4
    x1 = false -> 4(False || open), weight = 4 x (1-1/2¹) = 4x1/2 = 2

    C3 = 1((not) x1 || x2 || (not) x5)

    x1 = true  -> 1(False || open || open), weight = 1 x (1-1/2²) = 1x3/4 = 0.75
    x1 = false -> 1(True || open || open), weight = 1 x 1 = 1

    C4 = 3((not) x1 || x3)

    x1 = true  -> 3(False || open), weight = 3 x (1-1/2¹) = 3x1/2 = 1.5
    x1 = false -> 3(True || open), weight = 3 x 1 = 3

    Sum of x1 = true -> 3 + 4 + 0.75 + 1.5 = 9.25
    Sum of x1 = false -> 2.25 + 2 + 1 + 3 = 8.25

    9.25 >= 8.25 -> x1 = true

    x2 -> x1 is locked to True

    C1 = 3(x1 || (not) x2 || x3)

    x2 = true  -> 3(True || False || open), weight = 3 x 1 = 3
    x2 = false -> 3(True || True || open), weight = 3 x 1 = 3

    C3 = 1((not) x1 || x2 || (not) x5)

    x2 = true  -> 1(False || True || open), weight = 1 x 1 = 1
    x2 = false -> 1(False || False || open), weight = 1 x (1-1/2¹) = 1x1/2 = 0.5

    C5 = 2(x2 || (not) x4)

    x2 = true  -> 2(True || open), weight = 2 x 1 = 2
    x2 = false -> 2(False || open), weight = 2 x (1-1/2¹) = 2x1/2 = 1

    C6 = 7((not) x2 || x5 || x9)

    x2 = true  -> 7(False || open || open), weight = 7 x (1-1/2²) = 7x3/4 = 5.25
    x2 = false -> 7(True || open || open), weight = 7 x 1 = 7

    Sum of x2 = true -> 3 + 1 + 2 + 5.25 = 11.25
    Sum of x2 = false -> 3 + 0.5 + 1 + 7 = 11.5

    11.25 <= 11.5 -> x2 = false

    x3 -> x1 is locked to True, x2 is locked to False

    C1 = 3(x1 || (not) x2 || x3)

    x3 = true  -> 3(True || True || True), weight = 3 x 1 = 3
    x3 = false -> 3(True || True || False), weight = 3 x 1 = 3

    C2 = 4(x1 || (not) x3)

    x3 = true  -> 4(True || False), weight = 4 x 1 = 4
    x3 = false -> 4(True || True), weight = 4 x 1 = 4

    C4 = 3((not) x1 || x3)

    x3 = true  -> 3(False || True), weight = 3 x 1 = 3
    x3 = false -> 3(False || False), weight = 3 x (1-1/2^0) = 3x0 = 0

    C7 = 2(x3 || (not) x4)

    x3 = true  -> 2(True || open), weight = 2 x 1 = 2
    x3 = false -> 2(False || open), weight = 2 x (1-1/2¹) = 2x1/2 = 1

    Sum of x3 = true -> 3 + 4 + 3 + 2 = 12
    Sum of x3 = false -> 3 + 4 + 0 + 1 = 8

    12 >= 8 -> x3 = true

    x4 -> x1 is locked to True, x2 is locked to False, x3 is locked to True

    C5 = 2(x2 || (not) x4)

    x4 = true  -> 2(False || False), weight = 2 x (1-1/2^0) = 2x0 = 0
    x4 = false -> 2(False || True), weight = 2 x 1 = 2

    C7 = 2(x3 || (not) x4)

    x4 = true  -> 2(True || False), weight = 2 x 1 = 2
    x4 = false -> 2(True || True), weight = 2 x 1 = 2

    C8 = 3((not) x4 || (not) x5 || x21)

    x4 = true  -> 3(False || open || open), weight = 3 x (1-1/2²) = 3x3/4 = 2.25
    x4 = false -> 3(True || open || open), weight = 3 x 1 = 3

    Sum of x4 = true -> 0 + 2 + 2.25 = 4.25
    Sum of x4 = false -> 2 + 2 + 3 = 7

    4.25 <= 7 -> x4 = false

    x5 -> x1 is locked to True, x2 is locked to False, x3 is locked to True, x4 is locked to false

    C3 = 1((not) x1 || x2 || (not) x5)

    x5 = true  -> 1(False || False || False), weight = 1 x (1-1/2⁰) = 1x0 = 0
    x5 = false -> 1(False || False || True), weight = 1 x 1 = 1

    C6 = 7((not) x2 || x5 || x9)

    x5 = true  -> 7(True || True || open), weight = 7 x 1 = 7
    x5 = false -> 7(True || False || open), weight = 7 x 1 = 7

    C8 = 3((not) x4 || (not) x5 || x21)

    x5 = true  -> 3(True || False || open), weight = 3 x 1 = 3
    x5 = false -> 3(True || True || open), weight = 3 x 1 = 3

    C9 = 5(x5 || (not) x12)

    x5 = true  -> 5(True || open), weight = 5 x 1 = 5
    x5 = false -> 5(False || open), weight = 5 x (1-1/2¹) = 5x1/2 = 2.5

    Sum of x5 = true -> 0 + 7 + 3 + 5 = 15
    Sum of x5 = false -> 1 + 7 + 3 + 2.5 = 13.5

    15 >= 13.5 -> x5 = true

    Result: x1 = true, x2 = false, x3 = true, x4 = false, x5 = true

3).

    a). ILP formulation

    C1 = 4(x1 || (not) x3), C2 = 3((not) x1 || x4), C3 = 2((not) x2 || x4), C4 = 1((not) x2 || (not) x3 || x4)

    maximize -> 4z1 + 3z2 + 2z3 + z4

    subject to:
    
        y1 + (1 - y3)            >= z1
        (1 - y1) + y4            >= z2
        (1 - y2) + y4            >= z3
        (1 - y2) + (1 - y3) + y4 >= z4

        yi is in {0, 1}, i = 1..4
        zj is in {0, 1}, j = 1..4

    b). LP formulation

    C1 = 4(x1 || (not) x3), C2 = 3((not) x1 || x4), C3 = 2((not) x2 || x4), C4 = 1((not) x2 || (not) x3 || x4)

    maximize -> 4z1 + 3z2 + 2z3 + z4

    subject to:

        y1 + (1 - y3)            >= z1
        (1 - y1) + y4            >= z2
        (1 - y2) + y4            >= z3
        (1 - y2) + (1 - y3) + y4 >= z4

        0 <= yi <= 1, i = 1..4
        0 <= zj <= 1, j = 1..4
    

-- Problems 5

1). Coloring a 3-colorable graph with O(sqrt(n)) colors

    Neighbors from the adjacency matrix:

        1: 3, 4, 6, 8
        2: 7, 9
        3: 1, 4, 6
        4: 1, 3
        5: 6, 9
        6: 1, 3, 5, 8
        7: 2, 8, 9
        8: 1, 6, 7
        9: 2, 5, 7

    n = 9 -> sqrt(n) = 3

    Round 1:

        Degrees: 1:4, 2:2, 3:3, 4:2, 5:2, 6:4, 7:3, 8:3, 9:3
        Lowest vertex with degree >= 3 -> vertex 1, new colors A, B, C

        1 = A

        2-color the neighbors {3, 4, 6, 8} with B and C, edges between them: 3-4, 3-6, 6-8

            3 = B (start), S = {3}
            4 = C (neighbor 3 is B)
            6 = C (neighbor 3 is B)
            8 = B (neighbor 6 is C)

        Remove 1, 3, 4, 6, 8

    Round 2:

        Left: 2, 5, 7, 9, edges: 2-7, 2-9, 5-9, 7-9
        Degrees: 2:2, 5:1, 7:2, 9:3
        Vertex 9 has degree 3 >= 3 -> new colors D, E, F

        9 = D

        2-color the neighbors {2, 5, 7} with E and F, edges between them: 2-7

            2 = E (start), S = {2}
            7 = F (neighbor 2 is E)
            5 = E (no neighbor in S, own component, start again)

        Remove 2, 5, 7, 9

    Last step:

        No vertices left -> the (Delta + 1) coloring has nothing to color

    Result: 1 = A, 2 = E, 3 = B, 4 = C, 5 = E, 6 = C, 7 = F, 8 = B, 9 = D

    Check: 1-3 A/B, 1-4 A/C, 1-6 A/C, 1-8 A/B, 2-7 E/F, 2-9 E/D, 3-4 B/C,
           3-6 B/C, 5-6 E/C, 5-9 E/D, 6-8 C/B, 7-8 F/B, 7-9 F/D -> all OK

    6 colors used <= 4 * sqrt(n) = 12 (Theorem 6.20)

2). Minimum vertex cover

    Edges: (1,2), (1,3), (1,5), (2,3), (2,5), (4,5)

    a). ILP formulation

    xi = 1 if vertex i is in the cover C, 0 if not

    minimize -> x1 + x2 + x3 + x4 + x5

    subject to:

        x1 + x2 >= 1
        x1 + x3 >= 1
        x1 + x5 >= 1
        x2 + x3 >= 1
        x2 + x5 >= 1
        x4 + x5 >= 1

        xi is in {0, 1}, i = 1..5

    (Optimal: 1-2-3 is a triangle so it needs 2 of them, and (4,5) needs one more -> OPT = 3, e.g. C = {1, 2, 5})

    b). LP relaxation

    minimize -> x1 + x2 + x3 + x4 + x5

    subject to:

        x1 + x2 >= 1
        x1 + x3 >= 1
        x1 + x5 >= 1
        x2 + x3 >= 1
        x2 + x5 >= 1
        x4 + x5 >= 1

        0 <= xi <= 1, i = 1..5

    c). Dual

    One dual variable y_ij for each edge (the "price" of the edge), one constraint for each vertex:
    the prices of the edges touching a vertex can't sum to more than its weight (1).

    maximize -> y12 + y13 + y15 + y23 + y25 + y45

    subject to:

        y12 + y13 + y15 <= 1      (vertex 1)
        y12 + y23 + y25 <= 1      (vertex 2)
        y13 + y23       <= 1      (vertex 3)
        y45             <= 1      (vertex 4)
        y15 + y25 + y45 <= 1      (vertex 5)

        y_ij >= 0 for all edges

    d). LP solution = 500 on a graph with 10.000 vertices

    The LP is a relaxation of the ILP (more solutions allowed), so it can only be as good or better
    for a minimization problem:

        Z_LP <= OPT -> OPT >= 500

    Rounding: put vertex i in the cover if xi >= 1/2. For every edge xi + xj >= 1, so at least one
    of them is >= 1/2 -> it is a vertex cover. Every chosen vertex costs 1 <= 2 * xi, so the
    rounded cover has size <= 2 * Z_LP = 1000 (f = 2, each edge is in 2 "sets").

    So: 500 <= OPT <= 1000. The minimum vertex cover has between 500 and 1000 vertices, and we can
    find a cover with at most 1000 vertices in polynomial time (2-approximation).
