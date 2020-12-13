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
    MOVES = -1, 1, M - 1, M, M + 1, ~M, -M, -M + 1

    def simulate(grid, nxt):
        seats = (i for i, val in enumerate(grid) if val <= 1)
        while seats := nxt(grid, seats):
            for ind in seats:
                grid[ind] ^= 1  # Toggle empty/occupied
        return grid.count(1)

    def next_grid_pt_1(grid, seats):
        updates = []
        # Would not recommend this for anything other than marginal speed improvements
        update_append = updates.append
        for i in seats:
            if grid[i]:
                target = 4
                for move in MOVES:
                    if grid[i + move] == 1:
                        if target == 1:  # Already satisfied
                            update_append(i)
                            break
                        target -= 1
            elif not any(grid[i + move] == 1 for move in MOVES):
                update_append(i)
        return updates

    def next_grid_pt_2(grid, seats):
        updates = []
        update_append = updates.append
        for i in seats:
            if grid[i]:
                target = 5
                for move in MOVES:
                    ind = i + move
                    while (value := grid[ind]) == 2:
                        ind += move
                    if value == 1:
                        if target == 1:  # Already satisfied
                            update_append(i)
                            break
                        target -= 1
            else:
                for move in MOVES:
                    ind = i + move
                    while (value := grid[ind]) == 2:
                        ind += move
                    if value == 1:
                        break
                else:
                    update_append(i)
        return updates

    return simulate(arr[:], next_grid_pt_1), simulate(arr, next_grid_pt_2)


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
