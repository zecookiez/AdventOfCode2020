from time import time

data = [i[:-1] for i in open("input/day12.txt", "r").readlines()]


def solve(data):

    ship1_x = ship1_y = ship2_x = ship2_y = 0
    way_x = 1
    way_y = 10
    direction = "E"

    movement = {
        "N": (1, 0),
        "S": (-1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }

    for action in data:
        inst = action[0]
        value = int(action[1:])
        if inst == "L":
            # Neat trick for rotation: dx, dy = -dy, dx
            # Switch negative signs for other direction
            for _ in range(value // 90):
                direction = "NESW"["ESWN".find(direction)]
                way_x, way_y = way_y, -way_x
        elif inst == "R":
            for _ in range(value // 90):
                direction = "NESW"["WNES".find(direction)]
                way_x, way_y = -way_y, way_x
        elif inst == "F":
            dx, dy = movement[direction]
            ship1_x += dx * value
            ship1_y += dy * value
            ship2_x += way_x * value
            ship2_y += way_y * value
        else:
            dx, dy = movement[inst]
            ship1_x += dx * value
            ship1_y += dy * value
            way_x += dx * value
            way_y += dy * value

    return abs(ship1_x) + abs(ship1_y), abs(ship2_x) + abs(ship2_y)


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
