import sys

Coordinate = tuple[int, int]
AntennaMap = dict[str, set[Coordinate]]


def read_antennae() -> tuple[AntennaMap, int, int]:
    width = 0
    height = 0
    antennae = {}

    for line in sys.stdin.readlines():
        if len(line) > 0:
            width = len(line) - 1
            for x in range(width):
                c = line[x]
                if c != ".":
                    if c not in antennae:
                        antennae[c] = set()
                    antennae[c].add((height, x))
            height += 1

    return antennae, height, width


def part1(antennae: AntennaMap, height: int, width: int) -> int:
    antinodes = set()

    for freq, coordinates in antennae.items():
        for y1, x1 in coordinates:
            for y2, x2 in coordinates:
                rise = y2 - y1
                run = x2 - x1

                if rise == 0 and run == 0:
                    continue

                anti_y, anti_x = y2 + rise, x2 + run
                if anti_y in range(height) and anti_x in range(width):
                    antinodes.add((anti_y, anti_x))

                anti_y, anti_x = y1 - rise, x1 - run
                if anti_y in range(height) and anti_x in range(width):
                    antinodes.add((anti_y, anti_x))

    return len(antinodes)


if __name__ == "__main__":
    antennae, height, width = read_antennae()
    print(f"Part 1:\t{part1(antennae, height, width)}")
