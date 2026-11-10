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

Job with lowest Processing time -> J2, and is released and works for t = 1

t = 1, job released : J3 (3)

current remaining work: J1 (6), J2 (4)

Job with lowest Processing time -> J3 is released and works for t = 1

t = 2, job released : J4 (1)

current remaining work: J1 (6), J2 (4), J3 (2)

Job with lowest Processing time -> J4 is released and works for t = 1 -> J4 complete at t = 3

t = 3, job released : J5 (4)

current remaining work: J1 (6), J2 (4), J3 (2)

Job with lowest processing time -> J3 is released and works for t = 1

t = 4, job released : J6 (2)

current remaining work: J1 (6), J2 (4), J3 (1), J5 (4), J6 (2)

Job with lowest Processing time -> J3 is released and works for t = 1 -> J3 complete at t = 5

t = 5, job released : None

current remaining work: J1 (6), J2 (4), J5 (4), J6 (2)

Job with lowest Processing time -> J6 is released and works for t = 2 -> J6 complete at t = 7

t = 7, job released : None

current remaining work: J1 (6), J2 (4), J5 (4)

Job with lowest Processing time -> J2 is released and works for t = 4 -> J2 complete at t = 11

t = 11, job released : None

current remaining work: J1 (6), J5 (4)

Job with lowest Processing time -> J5 is released and works for t = 4 -> J5 complete at t = 15

t = 15, job released : None

current remaining work; J1 (6)

Job with lowest Processing time -> J1 is released and works for t = 4

t = 19, job released : J7 (2)

current remaining work: J1 (2), J7 (2)

Job with lowest Processing time -> J1 is released and works for t = 2 -> J1 complete at t = 21

t = 21, job released : None

current remaining work: J7 (2)

Job with lowest Processing time -> J7 is released and works for t = 2 -> J7 complete at t = 23




 

    
