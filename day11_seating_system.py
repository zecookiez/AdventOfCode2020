from time import time

data = [list(map("L#.".find, i[:-1])) for i in open("input/day11.txt", "r").readlines()]


def solve(data):

    # This is quite brutal to optimize...
    # Went from ~10 seconds to 448ms (110ms with PyPy)
    #
    # Notable optimizations:
    #  - Flattening the 2D array into 1D
    #  - Short-circuit the neighbor count if necessary
    #  - Applying updates instead of making a new grid
    #  - Keeping track of the seat indices (the rest are unnecessary)
    #    - Only check the seats that are recently updated
    #  - Use padding to stop checking for out-of-bounds

    N, M = len(data), len(data[0]) + 1
    arr = []
    for i in data:
        # Flattening the array could cause wraparound, so I padded with 3
        arr.extend(i + [3])
    arr.extend([3] * M)  # More padding to stop checking for out-of-bounds

    def calculate(grid, is_direct):

        seats = (i for i, val in enumerate(grid) if val <= 1)

        def next_grid(grid, is_direct):

            updates = []
            # Would not recommend this for anything other than marginal speed improvements
            update_append = updates.append
            MOVES = ~M, -M, -M + 1, -1, 1, M - 1, M, M + 1

            for i in seats:

                val = grid[i]
                target = 5 - is_direct  # 4 for part 1, 5 for part 2

                # Try all 8 neighbors
                for move in MOVES:
                    ind = i + move
                    while not is_direct and grid[ind] == 2:
                        ind += move
                    if grid[ind] == 1:
                        target -= 1
                        if val == 0:  # Will never satisfy the check
                            break
                        elif target == 0:  # Already satisfied
                            update_append(i)
                            break
                else:
                    if val == 0:
                        update_append(i)

            return updates

        seats = next_grid(grid, is_direct)
        while seats:
            for ind in seats:
                grid[ind] ^= 1  # Toggle empty/occupied
            seats = next_grid(grid, is_direct)

        return grid.count(1)

    return calculate(arr[:], True), calculate(arr, False)


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
