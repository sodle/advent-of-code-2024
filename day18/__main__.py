import sys

from networkx import DiGraph, shortest_path_length, NetworkXNoPath

from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


def read_input() -> list[Coordinate]:
    out = []
    for line in sys.stdin.readlines():
        if "," in line:
            _a, _b = line.split(",")
            a = int(_a)
            b = int(_b)
            out.append(Coordinate(a, b))
    return out


def part1(walls: list[Coordinate]) -> int:
    width = max([x for x, _ in coordinates]) + 1
    height = max([y for _, y in coordinates]) + 1

    if len(walls) > 1024:
        walls = walls[:1024]
    else:
        walls = walls[:12]

    G = DiGraph()

    r_height = range(height)
    r_width = range(width)
    for y in r_height:
        for x in r_width:
            if (x, y) in walls:
                pass

            if x + 1 in r_width and (x + 1, y) not in walls:
                G.add_edge((x, y), (x + 1, y))
            if x - 1 in r_width and (x - 1, y) not in walls:
                G.add_edge((x, y), (x - 1, y))
            if y + 1 in r_height and (x, y + 1) not in walls:
                G.add_edge((x, y), (x, y + 1))
            if y - 1 in r_height and (x, y - 1) not in walls:
                G.add_edge((x, y), (x, y - 1))

    return shortest_path_length(G, (0, 0), (width - 1, height - 1))


def part2(walls: list[Coordinate]) -> str:
    width = max([x for x, _ in coordinates]) + 1
    height = max([y for _, y in coordinates]) + 1

    r_height = range(height)
    r_width = range(width)

    G = DiGraph()
    for y in r_height:
        for x in r_width:
            if x + 1 in r_width:
                G.add_edge((x, y), (x + 1, y))
            if x - 1 in r_width:
                G.add_edge((x, y), (x - 1, y))
            if y + 1 in r_height:
                G.add_edge((x, y), (x, y + 1))
            if y - 1 in r_height:
                G.add_edge((x, y), (x, y - 1))

    while len(walls) > 0:
        wall = walls.pop(0)
        try:
            G.remove_node(wall)
            shortest_path_length(G, (0, 0), (width - 1, height - 1))
        except NetworkXNoPath:
            x, y = wall
            return f"{x},{y}"


if __name__ == "__main__":
    coordinates = read_input()
    print(f"Part 1:\t{part1(coordinates)}")
    print(f"Part 2:\t{part2(coordinates)}")
