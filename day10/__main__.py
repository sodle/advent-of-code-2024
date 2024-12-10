import sys
import networkx as nx
import itertools


Coordinate = tuple[int, int]
TrailMap = dict[Coordinate, int]


def read_trail_map() -> TrailMap:
    out = {}

    for y, line in enumerate(sys.stdin.readlines()):
        for x, char in enumerate(line):
            if char.isnumeric():
                out[y, x] = int(char)

    return out


def part1(trails: TrailMap) -> int:
    G = nx.DiGraph()
    zeros = []
    nines = []
    for coordinate, height in trails.items():
        if height == 0:
            zeros.append(coordinate)
        if height == 9:
            nines.append(coordinate)

        y, x = coordinate
        up = (y - 1, x)
        down = (y + 1, x)
        left = (y, x - 1)
        right = (y, x + 1)

        if up in trails and trails[up] == height + 1:
            G.add_edge(coordinate, up)
        if down in trails and trails[down] == height + 1:
            G.add_edge(coordinate, down)
        if left in trails and trails[left] == height + 1:
            G.add_edge(coordinate, left)
        if right in trails and trails[right] == height + 1:
            G.add_edge(coordinate, right)

    acc = 0
    for zero, nine in itertools.product(zeros, nines):
        if nx.has_path(G, zero, nine):
            acc += 1
    return acc


def part2(trails: TrailMap) -> int:
    G = nx.DiGraph()
    zeros = []
    nines = []
    for coordinate, height in trails.items():
        if height == 0:
            zeros.append(coordinate)
        if height == 9:
            nines.append(coordinate)

        y, x = coordinate
        up = (y - 1, x)
        down = (y + 1, x)
        left = (y, x - 1)
        right = (y, x + 1)

        if up in trails and trails[up] == height + 1:
            G.add_edge(coordinate, up)
        if down in trails and trails[down] == height + 1:
            G.add_edge(coordinate, down)
        if left in trails and trails[left] == height + 1:
            G.add_edge(coordinate, left)
        if right in trails and trails[right] == height + 1:
            G.add_edge(coordinate, right)

    acc = 0
    for zero, nine in itertools.product(zeros, nines):
        for _ in nx.all_simple_paths(G, zero, nine):
            acc += 1
    return acc


if __name__ == "__main__":
    trails = read_trail_map()
    print(f"Part 1:\t{part1(trails)}")
    print(f"Part 2:\t{part2(trails)}")
