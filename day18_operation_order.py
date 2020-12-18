from time import time
import re

data = [i[:-1] for i in open("input/day18.txt", "r").readlines()]


def solve(lines):

    class Num:
        def __init__(self, num):
            self.num = num

        def __add__(self, other):
            return Num(self.num + other.num)

        def __sub__(self, other):
            return Num(self.num * other.num)

        def __xor__(self, other):
            return Num(self.num * other.num)

    # Operator overload with eval()...interesting combination

    part1 = part2 = 0
    for i in lines:
        i = re.sub(r"(\d+)", r"Num(\1)", i)
        # +/- have same precendence
        part1 += eval(i.replace("*", "-")).num
        # bitwise xor is evaluated after addition
        part2 += eval(i.replace("*", "^")).num
    return part1, part2

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
