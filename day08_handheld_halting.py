from time import time

data = [i[:-1].split() for i in open("input/day08.txt", "r").readlines()]


def solve(input):

    def run_program(data):
        pt = accumulate = 0
        seen = set()
        while pt not in seen and pt < len(data):
            seen.add(pt)
            ins, val = data[pt]
            if ins == "nop":
                pt += 1
            elif ins == "acc":
                accumulate += int(val)
                pt += 1
            else:
                pt += int(val)
        return pt == len(data), accumulate

    def swap(inst, val):
        return ["jmp", "nop"][inst == "jmp"], val

    for pos in range(len(input)):
        if input[pos][0] == "acc":
            continue
        input[pos] = swap(*input[pos])
        verdict, output = run_program(input)
        input[pos] = swap(*input[pos])
        if verdict:
            return run_program(input)[1], output

    raise ValueError("Invalid program.")


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
