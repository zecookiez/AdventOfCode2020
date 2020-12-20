from time import time
import re

data = [i[:-1] for i in open("input/day20.txt", "r").readlines()]


def solve(lines):

    # Backtracking approach
    # This method should take way more time than it did, 228ms???
    # Heck this has no reason to be as fast as it is

    # I have an alternative solution that works in O(N^2) where N = # of Tiles
    # It has a very heavy constant so I don't expect it to run faster than this one
    # Will upload it once I rewrite and clean it up

    def rot90(tile):
        return list(map("".join, zip(*tile)))[::-1]

    # Generate all transformations of tile
    def transform(tile):
        tiles = []
        for t in tile, rot90(tile)[::-1]:
            tiles.append(t)
            for _ in range(3):
                tiles.append(rot90(tiles[-1]))
        return tiles

    # Input parsing
    tiles = []
    pt = 0
    while pt < len(lines):
        arr = []
        while pt < len(lines) and lines[pt]:
            arr.append(lines[pt])
            pt += 1
        pt += 1
        ID = int(arr.pop(0).split()[1][:-1])
        tiles.append((ID, transform(arr)))

    # Print the final board
    def join_board(grid):
        FINAL = []
        for i in grid:
            row = [[] for _ in range(10)]
            for j in i:
                for ind, k in enumerate(j):
                    row[ind].append("".join(k)[1:-1])
            for j in row[1:-1]:
                FINAL.append("".join(j))
        return FINAL

    # Build image
    board = [[-1] * 12 for i in range(12)]
    image = [[-1] * 12 for i in range(12)]

    def helper(id, rem):
        if not rem:
            return True
        y, x = divmod(id, 12)
        for tile in rem:
            for grid in tiles[tile][1]:
                # Check if matches with tile on top
                if x > 0 and grid[0] != board[x - 1][y][-1]:
                    continue
                # Check if matches with tile on left
                if y > 0 and [a[0] for a in grid] != [a[-1] for a in board[x][y - 1]]:
                    continue
                # Throw it into the board, keep trying
                board[x][y] = grid
                image[x][y] = tiles[tile][0]
                if helper(id + 1, [i for i in rem if i != tile]):
                    return True
        return False

    assert helper(0, [*range(144)])

    FINAL = join_board(board)
    part1 = image[0][0] * image[0][-1] * image[-1][0] * image[-1][-1]
    pattern = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

    def count_sea_monster(grid):
        L = len(pattern)
        W = len(pattern[0])
        tot = 0
        for i in range(L, len(grid)):
            for j in range(W, len(grid[i])):
                good = 1
                for k in range(L):
                    for l in range(W):
                        if pattern[k][l] == " ":
                            continue
                        if grid[i-L+k][j-W+l] != "#":
                            good = 0
                            break
                tot += good
        return tot

    tot_sea = "".join(FINAL).count("#")
    for GRID in transform(FINAL):
        cnt = count_sea_monster(GRID)
        if cnt != 0:
            return part1, tot_sea - cnt * 15

    raise ValueError("Invalid image!")

t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
