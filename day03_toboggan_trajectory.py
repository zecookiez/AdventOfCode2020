from time import time

# Learned my lesson for not taking out the extra newline.
data = [i[:-1] for i in open("input/day03.txt", "r").readlines()]


def solve(data):

    def count(dx, dy):
        x = y = tot = 0
        while x < len(data):
            # Use modulo to perform the wrap-around, saving memory.
            tot += data[x][y % len(data[0])] == "#"
            x += dx
            y += dy
        return tot

    part1 = part2 = count(1, 3)
    for slope in (1, 1), (1, 5), (1, 7), (2, 1):
        part2 *= count(*slope)

    return part1, part2


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
