from time import time


def solve():

    # Runs in 1000ms in Pypy
    # This is going to be hard to optimize ;-;

    arr = tuple(map(int, "9,6,0,10,18,2,1".split(",")))

    def simulate(amount):
        seen = [0] * amount
        for id, cur in enumerate(arr, 1):
            seen[cur] = id
        for id in range(len(arr), amount):
            seen[cur], cur = id, id - seen[cur] if seen[cur] else 0
        return cur

    return simulate(2020), simulate(30000000)

t_start = time()

part1, part2 = solve()
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
