from time import time

data = [int(i[:-1]) for i in open("input/day25.txt", "r").readlines()]


def solve(lines):

    # :(

    MOD = 20201227
    card, door = lines
    c = 7
    for i in range(2, MOD):
        c *= 7
        c %= MOD
        if c == card:
            return pow(door, i, MOD)

t_start = time()

part1 = solve(data)
print("Part 1: %d" % part1)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
