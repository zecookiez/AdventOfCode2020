from time import time

data = [set(i[:-1]) for i in open("input/day06.txt", "r").readlines()]


def solve(data):

    # Same input parsing method as day 4

    part1 = part2 = pt = 0
    while pt < len(data):
        response = []
        while pt < len(data) and data[pt]:
            response.append(data[pt])
            pt += 1
        pt += 1
        part1 += len(set.union(*response))
        part2 += len(set.intersection(*response))
    return part1, part2


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
