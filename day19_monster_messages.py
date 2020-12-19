from time import time
import re

data = [i[:-1] for i in open("input/day19.txt", "r").readlines()]


def solve(lines):

    # Extract input
    rules = {}
    texts = []
    pt = 0
    while pt < len(lines):
        arr = []
        while pt < len(lines) and lines[pt]:
            arr.append(lines[pt])
            pt += 1
        pt += 1
        if len(rules) == 0:
            for i in arr:
                key, val = i.split(": ")
                rules[key] = val
        else:
            texts.extend(arr)

    # Apply the new rules
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    def solver(depth_lim):
        # Generate the required regex pattern
        # Quite a terrifying thought...
        # For part 2 I added a depth limit to break out of the infinite loop
        # Not a fully-working solution but it works for mine :)))
        memo = {}

        def helper(id, depth=depth_lim):
            if depth == 0:
                return ""
            if rules[id][0] == '"':
                memo[id] = rules[id][1:-1]
                return memo[id]
            # Concatenate the different patterns
            # | is still |
            # The others should be wrapped with ()
            pat = []
            for rule in rules[id].split():
                if rule == "|":
                    pat.append("|")
                elif rule == id:  # Looping rule
                    pat.append(helper(rule, depth - 1))
                else:
                    pat.append(helper(rule))
            memo[id] = "(%s)" % "".join(pat)
            return memo[id]
        pattern = helper("0")
        return sum(1 for st in texts if re.fullmatch(pattern, st))

    return solver(1), solver(5)

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
