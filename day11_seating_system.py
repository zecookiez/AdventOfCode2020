from time import time

data = [list(map("L#.".find, i[:-1])) for i in open("input/day11.txt", "r").readlines()]


def solve(data):

    # This is quite brutal to optimize...
    # Went from ~10 seconds to 1.6s
    #
    # Notable optimizations:
    #  - Flattening the 2D array into 1D
    #  - Short-circuit the neighbor count if necessary
    #  - Applying updates instead of making a new grid
    #  - Keeping track of the seat indices (the rest are unnecessary)

    N, M = len(data), len(data[0]) + 1
    grid = []
    for i in data:
        # Flattening the array could cause wraparound, so I padded with -1
        grid.extend(i + [-1])
    seats = [i for i, val in enumerate(grid) if 0 <= val <= 1]

    def next_grid(grid, is_direct):

        updates = []
        length = len(grid)
        for i in seats:

            val = grid[i]
            target = 5 - is_direct  # 4 for part 1, 5 for part 2

            # Try all 8 neighbors
            for move in ~M, -M, -M + 1, -1, 1, M - 1, M, M + 1:
                ind = i + move
                while not is_direct and 0 <= ind < length and grid[ind] == 2:
                    ind += move
                if 0 <= ind < length and grid[ind] == 1:
                    target -= 1
                    if val == 0:  # Will never satisfy the check
                        break
                    elif target == 0:  # Already satisfied
                        updates.append(i)
                        break
            else:
                if val == 0:
                    updates.append(i)

        return updates

    part_1 = grid[:]
    part_2 = grid[:]

    updates = next_grid(part_1, True)
    while updates:
        for ind in updates:
            part_1[ind] ^= 1  # Toggle empty/occupied
        updates = next_grid(part_1, True)

    updates = next_grid(part_2, False)
    while updates:
        for ind in updates:
            part_2[ind] ^= 1
        updates = next_grid(part_2, False)

    return sum(part_1[i] for i in seats), sum(part_2[i] for i in seats)


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
