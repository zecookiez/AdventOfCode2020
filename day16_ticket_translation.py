from time import time
import re

data = [i[:-1] for i in open("input/day16.txt", "r").readlines()]


def solve(lines):

    # Parse input
    grouped_data = []
    pt = 0
    while pt < len(lines):
        arr = []
        while pt < len(lines) and lines[pt]:
            arr.append(lines[pt])
            pt += 1
        pt += 1
        grouped_data.append(arr[len(grouped_data) != 0:])

    rules, ticket, nearby = grouped_data
    my_ticket = list(map(int, ticket[0].split(",")))

    def parse(field):
        return tuple(map(int, re.findall(r"\d+", field))), field.startswith("departure")

    rules = {parse(rule) for rule in rules}

    # Find valid tickets
    error_rate = 0
    valid_tickets = [[] for i in rules]
    for ticket in nearby:
        ticket = list(map(int, ticket.split(",")))
        for val in ticket:
            if not any(l1 <= val <= u1 or l2 <= val <= u2 for (l1, u1, l2, u2), dep in rules):
                error_rate += val
                break
        else:
            for ind, val in enumerate(ticket):
                valid_tickets[ind].append(val)

    # Slowly solve each field (if there is only 1 rule that works for a specific field, use it)
    # This can be done faster using a graph theory approach (topological sorting)
    tot = 1
    while rules:
        for id, ticket_val in enumerate(my_ticket):
            cand_rules = []
            for rule in rules:
                (low1, up1, low2, up2), depart = rule
                # This check can be replaced using binary search (after sorting)
                if all(low1 <= val <= up1 or low2 <= val <= up2 for val in valid_tickets[id]):
                    cand_rules.append(rule)
            if len(cand_rules) == 1:  # Only 1 rule works
                rule = cand_rules[0]
                rules.remove(rule)
                if rule[1]:
                    tot *= ticket_val

    return error_rate, tot

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
