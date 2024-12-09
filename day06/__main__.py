import sys
import math


Coordinate = tuple[int, int]


def read_maze() -> tuple[Coordinate, list[Coordinate], Coordinate]:
    guard_position = (0, 0)
    obstacles = []
    width = height = 0

    for line in sys.stdin.readlines():
        if len(line) > 0:
            width = len(line.strip())
            for i, x in enumerate(line):
                if x == "#":
                    obstacles.append((height, i))
                elif x == "^":
                    guard_position = (height, i)
            height += 1

    return guard_position, obstacles, (height, width)


def part1(
    guard_position: Coordinate, obstacles: list[Coordinate], dimensions: Coordinate
) -> int:
    height, width = dimensions

    y, x = guard_position
    visited = set()

    orientation = math.pi / 2  # guard starts facing up

    while x in range(width) and y in range(height):
        visited.add((y, x))

        look_x = x + int(math.cos(orientation))
        look_y = y - int(math.sin(orientation))

        if (look_y, look_x) in obstacles:
            orientation -= math.pi / 2
        else:
            x = look_x
            y = look_y

    return len(visited)


def part2(
    guard_position: Coordinate, obstacles: list[Coordinate], dimensions: Coordinate
) -> int:
    height, width = dimensions

    y, x = guard_position
    og_visited = set()

    orientation = math.pi / 2  # guard starts facing up

    while x in range(width) and y in range(height):
        og_visited.add((y, x))

        look_x = x + int(math.cos(orientation))
        look_y = y - int(math.sin(orientation))

        if (look_y, look_x) in obstacles:
            orientation -= math.pi / 2
        else:
            x = look_x
            y = look_y

    viable_obstacles = set()
    for new_obstacle in og_visited:
        if new_obstacle in obstacles or new_obstacle == guard_position:
            continue

        y, x = guard_position
        orientation = 90  # guard starts facing up

        visited = set()
        while x in range(width) and y in range(height):
            norm_orientation = orientation % 360
            if (y, x, norm_orientation) in visited:
                viable_obstacles.add(new_obstacle)
                break

            visited.add((y, x, norm_orientation))

            look_x = x + int(math.cos(math.radians(orientation)))
            look_y = y - int(math.sin(math.radians(orientation)))

            if (look_y, look_x) in [*obstacles, new_obstacle]:
                orientation -= 90
            else:
                x = look_x
                y = look_y

    return len(viable_obstacles)


if __name__ == "__main__":
    guard_position, obstacles, dimensions = read_maze()
    print(f"Part 1:\t{part1(guard_position, obstacles, dimensions)}")
    print(f"Part 2:\t{part2(guard_position, obstacles, dimensions)}")
