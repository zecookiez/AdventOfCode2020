from time import time

data = [int(i[:-1]) for i in open("input/day10.txt", "r").readlines()]


def solve(data):

    # Did not expect to see dynamic programming, but that saved me for part 2 :^)

    # Dynamic programming is similar to bruteforce, but everything is saved to "states" to reduce recalculating
    #   For this problem, we saved it to `dp`
    #   and defined dp[i] to be the # of valid combinations for the first `i` items.
    #
    # Now how do we calculate dp[i]? Find all adapters that match (<= diff of 3) and add those respective dp values.
    # 1, 3, 4 => DP[2] = DP[0] + DP[1]
    # 1, 4, 5 => DP[2] = DP[1], DP[1] = DP[0], DP[0] = 1
    # 5 => DP[0] = 0 (cannot connect to initial adapter of 0)
    # This initial solution will run in O(N^2) [For every DP[i], find all adapters that match]
    #
    # Upping the Ante: Solve this in O(N log N) [N log N comes from the sorting]
    #   Observation 1: For every adapter, there will be a subarray that will match it
    #   Observation 2: The subarray's left endpoint will only move towards the right [sorted property]
    #
    # Observation 1 allows us to use prefix sums again (see day 9's O(N) solution)
    #   Side note: We can do even better and use one integer to keep track of the subarray's sum
    #
    # Observation 2 allows us to use 2-pointers to find the subarray in amortized O(N) time

    adapters = sorted(data)
    adapters.append(adapters[-1] + 3)  # Add

    prev_ad = pt = subarray_sum = 0
    dp = [0] * len(adapters)
    diff = []
    for ind, adapter in enumerate(adapters):
        diff.append(adapter - prev_ad)

        # 2-pointer, find the lower bound of the subarray
        while pt < ind and adapters[pt] < adapter - 3:
            subarray_sum -= dp[pt] # Remove from subarray sum
            pt += 1

        # +1 if they can connect to [0]
        dp[ind] = subarray_sum + (adapter <= 3)
        subarray_sum += dp[ind]  # Add to subarray sum
        prev_ad = adapter

    # Final answer would be the last dp value
    return diff.count(1) * diff.count(3), dp[-1]


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
