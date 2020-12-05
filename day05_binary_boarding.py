from time import time
import re

data = [i[:-1] for i in open("input/day05.txt", "r").readlines()]


def solve(data):

    def convert(id, one, zero):
        return int(id.replace(one, "1").replace(zero, "0"), 2)

    # The "binary space partitioning" can be modelled with base-2 integers

    seen = set()
    for i in data:
        row, col = convert(i[:7], "B", "F"), convert(i[7:], "R", "L")
        seen.add(row * 8 + col)

    for id in seen:
        if id - 1 not in seen and id - 2 in seen:
            return max(seen), id - 1

    raise ValueError("Invalid input")


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
