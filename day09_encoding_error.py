from time import time

data = [int(i[:-1]) for i in open("input/day09.txt", "r").readlines()]


def solve(lines):

    lines = list(map(int, lines))
    lines.sort()  # Quick and dirty sort does it again (reduced to 1ms from 6ms)

    def find_invalid(data):

        # This part seems to be taking the majority of the time
        # While this is technically O(N), we can optimize one of the loops out using dictionary and set
        # Hint: After every check, only 1 new item is added in and only 1 item is taken out

        for i in range(25, len(data)):
            if all(data[a] + data[b] != data[i] for a in range(i - 25, i) for b in range(i - 25, a)):
                return data[i]

        raise ValueError("No invalid numbers found.")

    tgt = find_invalid(lines)

    # O(N) approach
    # We can define the sum of a subarray using the difference of prefix sums
    #   sum(arr[0..R]) - sum(arr[0..L]) = sum(arr[L-1..R])
    #
    # This means that tgt = prefix[A] - prefix[B]
    #                 tgt + prefix[B] = prefix[A]
    #
    # We can solve this using a set()

    # Build prefix sums
    seen = {}
    prefix_sum = [0]
    for i in lines:
        prefix_sum.append(prefix_sum[-1] + i)

    for ind, val in enumerate(prefix_sum):
        # Check for prefix[A]'s existence
        if val in seen:
            left = seen[val]
            if ind - left > 1:  # Found subarray!
                return tgt, max(lines[left:ind+1]) + min(lines[left:ind+1])
        # Adding tgt + prefix[B] into the set
        seen[val + tgt] = ind

    raise ValueError("Invalid Input.")


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
