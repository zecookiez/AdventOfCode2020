from time import time

data = list(map(int, open("input/day01.txt", "r").readlines()))

def part1(data):

    # We can solve part 1 in linear time using set's O(1) insertion and lookup

    seen = set()
    for i in data:
        j = 2020 - i
        if j in seen:
            return i * j
        seen.add(i)


def part2(data):

    # Taking a similar approach to part 1, but with an extra nested loop
    # This problem is also known as 3SUM, which asks to find 3 items in the array that sum to 0
    # Solutions with subquadratic time complexity are possible, but are completely overkill for this

    seen = set()
    two_sum = []
    for i in data:
        for j in two_sum:
            k = 2020 - i - j
            if k in seen:
                return i * j * k
        seen.add(i)
        two_sum.append(i)


t_start = time()

print("Part 1: %d" % part1(data))
print("Part 2: %d" % part2(data))

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)