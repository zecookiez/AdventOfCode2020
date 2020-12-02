from time import time

data = open("input/day02.txt", "r").readlines()


def solve(data):

    part1 = part2 = 0
    for i in data:
        req, st = i.split(":")
        req, ch = req.split()
        lower, upper = map(int, req.split("-"))
        if lower <= st.count(ch) <= upper:
            part1 += 1
        if (st[lower] + st[upper]).count(ch) == 1:
            part2 += 1
    return part1, part2


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
