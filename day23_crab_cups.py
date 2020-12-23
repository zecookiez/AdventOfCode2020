from time import time
from collections import defaultdict

data = "653427918"


def solve(line):

    # A continuation from day 22:
    #
    # Completely lost my momentum from the earlier days
    #   Part 1 couldn't debug fast enough
    #   Part 2 ran into linked list issues
    # This pains me so much, hopefully I'll be able to get >0 points in the next 2 days

    # Array-based linked list approach (NXT[1] => The node after Node 1)
    NXT = [0] * 1000001
    P1  = [0] * 10
    pval = -1
    for i in map(int, line):
        if pval != -1:
            NXT[pval] = P1[pval] = i
        else:
            cur = i
        pval = i
    P1[pval] = p1_cur = cur
    for id in range(10, 1000001):
        NXT[pval] = pval = id
    NXT[pval] = cur

    # Part 1
    for i in range(100):
        A = P1[p1_cur]
        B = P1[A]
        C = P1[B]
        dest = p1_cur - 1
        while dest == 0 or dest == A or dest == B or dest == C:
            if dest == 0:
                dest = 9
            else:
                dest -= 1
        P1[p1_cur] = p1_cur = P1[C]
        P1[C] = P1[dest]
        P1[dest] = A

    # Get the entire array
    p1_ans = 0
    p1_c = P1[1]
    while p1_c != 1:
        p1_ans = 10 * p1_ans + p1_c
        p1_c = P1[p1_c]

    # Part 2
    MX = 1000000
    for i in range(9900000):  # The last 1e5 iterations are useless
        # Grab next 3
        A = NXT[cur]
        B = NXT[A]
        C = NXT[B]
        dest = cur - 1
        # The sad part is that this is faster than using a set
        while dest == 0 or dest == A or dest == B or dest == C:
            if dest == 0:
                dest = MX
            else:
                dest -= 1
        NXT[cur] = cur = NXT[C]
        NXT[C] = NXT[dest]
        NXT[dest] = A

    return p1_ans, NXT[1] * NXT[NXT[1]]

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
