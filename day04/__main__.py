import sys


def read_grid() -> list[str]:
    return [line for line in sys.stdin.readlines() if len(line) > 0]


def part1(grid: list[str]) -> int:
    count = 0

    width = len(grid[0])
    height = len(grid)

    for x in range(width):
        for y in range(height):
            if grid[y][x] == "X":
                # try right
                if x + 3 < width:
                    if (
                        grid[y][x + 1] == "M"
                        and grid[y][x + 2] == "A"
                        and grid[y][x + 3] == "S"
                    ):
                        count += 1
                # try left
                if x - 3 >= 0:
                    if (
                        grid[y][x - 1] == "M"
                        and grid[y][x - 2] == "A"
                        and grid[y][x - 3] == "S"
                    ):
                        count += 1
                # try up
                if y - 3 >= 0:
                    if (
                        grid[y - 1][x] == "M"
                        and grid[y - 2][x] == "A"
                        and grid[y - 3][x] == "S"
                    ):
                        count += 1
                # try down
                if y + 3 < height:
                    if (
                        grid[y + 1][x] == "M"
                        and grid[y + 2][x] == "A"
                        and grid[y + 3][x] == "S"
                    ):
                        count += 1
                # try downright
                if x + 3 < width and y + 3 < height:
                    if (
                        grid[y + 1][x + 1] == "M"
                        and grid[y + 2][x + 2] == "A"
                        and grid[y + 3][x + 3] == "S"
                    ):
                        count += 1
                # try downleft
                if x - 3 >= 0 and y + 3 < height:
                    if (
                        grid[y + 1][x - 1] == "M"
                        and grid[y + 2][x - 2] == "A"
                        and grid[y + 3][x - 3] == "S"
                    ):
                        count += 1
                # try upright
                if x + 3 < width and y - 3 >= 0:
                    if (
                        grid[y - 1][x + 1] == "M"
                        and grid[y - 2][x + 2] == "A"
                        and grid[y - 3][x + 3] == "S"
                    ):
                        count += 1
                # try upleft
                if x - 3 >= 0 and y - 3 >= 0:
                    if (
                        grid[y - 1][x - 1] == "M"
                        and grid[y - 2][x - 2] == "A"
                        and grid[y - 3][x - 3] == "S"
                    ):
                        count += 1
                pass

    return count


def part2(grid: list[str]) -> int:
    count = 0

    width = len(grid[0])
    height = len(grid)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if grid[y][x] == "A":
                if set([grid[y - 1][x - 1], grid[y + 1][x + 1]]) == {"M", "S"} and set(
                    [grid[y + 1][x - 1], grid[y - 1][x + 1]]
                ) == {"M", "S"}:
                    count += 1

    return count


if __name__ == "__main__":
    grid = read_grid()
    print(f"Part 1:\t{part1(grid)}")
    print(f"Part 2:\t{part2(grid)}")
