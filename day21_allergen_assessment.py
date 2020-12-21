from time import time
from collections import defaultdict

data = [i[:-1] for i in open("input/day21.txt", "r").readlines()]


def solve(lines):

    # Completely misunderstood the entire problem
    # Completely lost my momentum from the earlier days
    #   Part 1 is almost identical to Day 6
    #   Part 2 is almost identical to Day 16
    # This pains me so much, hopefully I'll be able to get >0 points in the next 4 days

    cand = defaultdict(list)
    ing = defaultdict(int)
    for i in lines:
        a, b = i[:-1].split(" (contains ")
        for j in b.split(", "):
            cand[j].append(set(a.split()))
        for j in a.split():
            ing[j] += 1

    uncertain = set()
    used = set()
    known = {}
    for allergen in cand:
        bad = cand[allergen][0]
        for i in cand[allergen]:
            bad &= i
        uncertain |= bad
        if len(bad) == 1:
            known[allergen] = next(iter(bad))
            used.add(known[allergen])

    while len(cand) != len(known):
        for allergen in cand:
            if allergen not in known:
                bad = cand[allergen][0] - used
                for i in cand[allergen]:
                    bad &= i
                if len(bad) == 1:
                    known[allergen] = next(iter(bad))
                    used.add(known[allergen])

    p1 = sum(cnt for i, cnt in ing.items() if i not in uncertain)
    p2 = ",".join(j for i, j in sorted(known.items()))
    return p1, p2

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %s" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
