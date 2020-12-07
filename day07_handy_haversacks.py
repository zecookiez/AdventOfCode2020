from time import time
from collections import defaultdict

data = [i[:-2] for i in open("input/day07.txt", "r").readlines()]


def solve(data):

    # Two adjacency lists (one for each direction of the edges)
    adj = defaultdict(list)
    rev_adj = defaultdict(list)

    for i in data:

        if "other" in i:  # Skip for no bag
            continue

        # Remove first occurence of bags, then split on contain
        parent, children = i.replace(" bags", "", 1).split(" contain ")

        for child in children.split(", "):

            # Split into 3 components: quantity, colour, "bag(s)"
            # Thanks python for extended unpacking

            qt, *col, _ = child.split()
            col = " ".join(col)
            adj[parent].append((int(qt), col))
            rev_adj[col].append(parent)

    # Returns the # of bags (including itself) for a specific colour
    def helper(bag):
        return 1 + sum(qt * helper(nxt) for qt, nxt in adj[bag])

    # BFS for part 1, we want to find all "reachable" bag colours from gold
    queue = ["shiny gold"]
    seen = set()
    for node in queue:
        for nxt in rev_adj[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)

    return len(seen), helper("shiny gold") - 1


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
