from time import time
from collections import defaultdict
from itertools import product

data = [i[:-1] for i in open("input/day17.txt", "r").readlines()]


def solve(lines):

    def next_cycle(active):
        new_active = set()
        inactive = defaultdict(int)
        for pt in active:
            cnt = 0
            for neigh in product([-1, 0, 1], repeat=len(pt)):
                new_coord = tuple([a + d for a, d in zip(pt, neigh)])
                if new_coord in active:
                    cnt += 1
                else:  # Add to possible inactive->active
                    inactive[new_coord] += 1
            # Subtract 1 because one of the "neighbors" is the point itself
            if 2 <= cnt - 1 <= 3:
                new_active.add(pt)
        # There can be a lot of inactive neighboring cells
        # But we can mark the ones that can be activated
        # by going through the neighbors of active cells
        for coord, cnt in inactive.items():
            if cnt == 3:
                new_active.add(coord)
        return new_active

    active2 = {(x, y, 0, 0) for x, row in enumerate(lines)
               for y, ch in enumerate(row) if ch == "#"}
    active1 = {(i, j, k) for i, j, k, l in active2}
    for _ in range(6):
        active1 = next_cycle(active1)
        active2 = next_cycle(active2)

    return len(active1), len(active2)

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
