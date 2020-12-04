from time import time
import re

data = [i[:-1] for i in open("input/day04.txt", "r").readlines()]


def solve(lines):

    def chk_hgt(val):
        num = int(val[:-2] or "0")
        unit = val[-2:]

        if unit == "cm":
            return 150 <= num <= 193
        return unit == "in" and 59 <= num <= 76

    def chk_hcl(st):
        return re.fullmatch(r"#[0-9a-f]{6}", st)

    def chk_ecl(st):
        return st in "amb blu brn gry grn hzl oth".split()

    def chk_pid(st):
        return re.fullmatch(r"\d{9}", st)

    def chk_fields(cred):
        # Do fields exist? (Do not check for country ID)
        FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return all(i in cred.keys() for i in FIELDS)

    def is_valid(cred):

        if not chk_fields(cred):
            return False

        # Numerical checks
        for key, lower, upper in ("byr", 1920, 2002), ("iyr", 2010, 2020), ("eyr", 2020, 2030):
            if not lower <= int(cred[key]) <= upper:
                return False

        # Regex checks
        for key, func in ("hgt", chk_hgt), ("hcl", chk_hcl), ("ecl", chk_ecl), ("pid", chk_pid):
            if not func(cred[key]):
                return False

        return True

    # Parse input
    pt = part1 = part2 = 0
    while pt < len(lines):
        data = {}
        # Keep moving until we hit an empty line
        while pt < len(lines) and len(lines[pt]) >= 1:
            for field in lines[pt].split():
                key, value = field.split(":")
                data[key] = value
            pt += 1
        pt += 1
        part1 += chk_fields(data)
        part2 += is_valid(data)

    return part1, part2


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
