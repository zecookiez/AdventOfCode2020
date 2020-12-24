from time import time
from collections import defaultdict

data = [i[:-1] for i in open("input/day24.txt", "r").readlines()]


def solve(lines):

    # A continuation from day 23:
    #
    # Completely lost my momentum from the earlier days
    #   Part 1 spent time looking for hexagonal coordinate systems and wasted time to testing the example
    #   Part 2 wasted time to testing the example
    # Hopefully I'll be able to get > 0 points on the last day :(

    # Parse the step instructions
    def tokenize(i):
        pt = 0
        arr = []
        while pt < len(i):
            if i[pt] in "ns":
                arr.append(i[pt] + i[pt + 1])
                pt += 2
            else:
                arr.append(i[pt])
                pt += 1
        return arr

    # Flattened to 1 dimension for speed
    WIDTH = 200
    ADJ = 1, -1, -WIDTH, WIDTH, 1 - WIDTH, WIDTH - 1

    grid = set()
    for i in lines:
        di = {
            "e": 1,
            "w": -1,
            "nw": -WIDTH,
            "se": WIDTH,
            "ne": 1 - WIDTH,
            "sw": WIDTH - 1,
        }
        id = sum(map(di.get, tokenize(i)))
        # Toggle
        if id not in grid:
            grid.add(id)
        else:
            grid.remove(id)

    part1 = len(grid)

    # Part 2
    for _ in range(100):
        rem = set()
        freq = defaultdict(int)
        for id in grid:
            cnt = 0
            for nid in ADJ:
                nid += id
                if nid in grid:
                    cnt += 1
                else:
                    freq[nid] += 1  # Update neighbor count
            if cnt == 0 or cnt > 2:
                rem.add(id)
        grid -= rem
        grid |= {id for id, j in freq.items() if j == 2}
    return part1, len(grid)

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
