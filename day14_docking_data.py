from time import time

data = [i[:-1] for i in open("input/day14.txt", "r").readlines()]


def solve(data):

    mem_1 = {}
    mem_2 = {}
    mask = data.pop(0).split()[-1]
    MASK = (1 << 36) - 1

    def write(mask, val):
        return int("".join(j if i == "X" else i for i, j in zip(mask, val)), 2)

    for i in data:
        if len(i) == 43:
            mask = i.split()[-1]
            continue
        add, val = map(int, i[4:].split("] = "))
        mem_1[add] = write(mask, bin(val)[2:].zfill(36))

        ## Part 2
        subm, ind = 0, 1
        for ch in mask[::-1]:
            if ch == "X":
                subm |= ind
                add &= MASK ^ ind
            elif ch == "1":
                add |= ind
            ind <<= 1

        ## Neat trick to iterate submasks of a bitmask
        mem_2[add] = val
        org_mask = subm
        while subm:
            mem_2[add | subm] = val
            subm = (subm - 1) & org_mask # Subtract 1, & the new mask

    return sum(mem_1.values()), sum(mem_2.values())


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
