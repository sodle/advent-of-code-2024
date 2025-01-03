import sys
from math import inf

from networkx import DiGraph, shortest_path_length, all_shortest_paths, NetworkXNoPath

from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


class Maze(NamedTuple):
    start: Coordinate
    end: Coordinate
    walls: list[Coordinate]

    @property
    def width(self) -> int:
        return max(*[x for x, _ in self.walls]) + 1

    @property
    def height(self) -> int:
        return max(*[y for _, y in self.walls]) + 1


def read_input() -> Maze:
    walls = []
    for y, line in enumerate(sys.stdin.readlines()):
        for x, char in enumerate(line):
            match char:
                case "#":
                    walls.append(Coordinate(x, y))
                case "S":
                    start = Coordinate(x, y)
                case "E":
                    end = Coordinate(x, y)
    return Maze(start, end, walls)


def part1(maze: Maze) -> int:
    start, end, G = build_graph(maze)

    start_oriented = (*start, "E")
    shortest = inf
    for end_direction in "NESW":
        end_oriented = (*end, end_direction)
        try:
            shortest_dir = shortest_path_length(G, start_oriented, end_oriented, "cost")
            if shortest_dir < shortest:
                shortest = shortest_dir
        except NetworkXNoPath:
            pass

    return shortest


def build_graph(maze) -> tuple[Coordinate, Coordinate, DiGraph]:
    start, end, walls = maze

    G = DiGraph()

    height = range(maze.height)
    width = range(maze.width)
    for y in height:
        for x in width:
            if (x, y) in walls:
                pass

            G.add_edge((x, y, "N"), (x, y, "E"), cost=1000)
            G.add_edge((x, y, "N"), (x, y, "W"), cost=1000)
            G.add_edge((x, y, "E"), (x, y, "N"), cost=1000)
            G.add_edge((x, y, "E"), (x, y, "S"), cost=1000)
            G.add_edge((x, y, "S"), (x, y, "E"), cost=1000)
            G.add_edge((x, y, "S"), (x, y, "W"), cost=1000)
            G.add_edge((x, y, "W"), (x, y, "N"), cost=1000)
            G.add_edge((x, y, "W"), (x, y, "S"), cost=1000)

            if x + 1 in width and (x + 1, y) not in walls:
                G.add_edge((x, y, "E"), (x + 1, y, "E"), cost=1)
            if x - 1 in width and (x - 1, y) not in walls:
                G.add_edge((x, y, "W"), (x - 1, y, "W"), cost=1)
            if y + 1 in height and (x, y + 1) not in walls:
                G.add_edge((x, y, "S"), (x, y + 1, "S"), cost=1)
            if y - 1 in height and (x, y - 1) not in walls:
                G.add_edge((x, y, "N"), (x, y - 1, "N"), cost=1)
    return start, end, G


def part2(maze) -> int:
    start, end, G = build_graph(maze)

    start_oriented = (*start, "E")
    paths_by_length: dict[int, set[Coordinate]] = {}
    for end_direction in "NESW":
        end_oriented = (*end, end_direction)
        try:
            length = shortest_path_length(G, start_oriented, end_oriented, "cost")
            if length not in paths_by_length:
                paths_by_length[length] = set()
            for path in all_shortest_paths(G, start_oriented, end_oriented, "cost"):
                for x, y, _ in path:
                    paths_by_length[length].add((x, y))
        except NetworkXNoPath:
            pass

    shortest = min(*paths_by_length.keys())
    return len(paths_by_length[shortest])


if __name__ == "__main__":
    maze = read_input()
    print(f"Part 1:\t{part1(maze)}")
    print(f"Part 2:\t{part2(maze)}")
