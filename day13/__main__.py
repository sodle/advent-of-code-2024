import sys
import re

from typing import NamedTuple, Optional

import networkx as nx

button_regex = re.compile(r"Button [AB]: X\+(\d+), Y\+(\d+)")
goal_regex = re.compile(r"Prize: X=(\d+), Y=(\d+)")


Coordinate = tuple[int, int]


class CraneMachine(NamedTuple):
    button_a: Coordinate
    button_b: Coordinate
    goal: Coordinate

    def generate_movesets(
        self,
        start: Coordinate = (0, 0),
        G: Optional[nx.DiGraph] = None,
    ) -> nx.DiGraph:
        if G is None:
            G = nx.DiGraph()

        start_x, start_y = start
        end_x, end_y = self.goal

        if start_x >= end_x or start_y >= end_y:
            # We've overshot the goal, stop generating.
            return G

        dx_a, dy_a = self.button_a
        step_a = (start_x + dx_a, start_y + dy_a)
        if step_a not in G:
            self.generate_movesets(start=step_a, G=G)
        G.add_edge(start, step_a, cost=3)

        dx_b, dy_b = self.button_b
        step_b = (start_x + dx_b, start_y + dy_b)
        if step_b not in G:
            self.generate_movesets(start=step_b, G=G)
        G.add_edge(start, step_b, cost=1)

        return G


def read_input() -> list[CraneMachine]:
    lines = sys.stdin.readlines()
    machines = []

    while lines:
        if not lines[0].strip():
            lines.pop(0)
            continue

        line_a = lines.pop(0).strip()
        line_b = lines.pop(0).strip()
        line_goal = lines.pop(0).strip()

        match_a = button_regex.match(line_a).groups()
        delta_a = tuple([int(n) for n in match_a])

        match_b = button_regex.match(line_b).groups()
        delta_b = tuple([int(n) for n in match_b])

        match_goal = goal_regex.match(line_goal).groups()
        goal = tuple([int(n) for n in match_goal])

        machines.append(CraneMachine(delta_a, delta_b, goal))

    return machines


def part1(machines: list[CraneMachine]) -> int:
    acc = 0

    for machine in machines:
        G = machine.generate_movesets()
        try:
            acc += nx.shortest_path_length(G, (0, 0), machine.goal, weight="cost")
        except nx.NetworkXNoPath:
            pass

    return acc


if __name__ == "__main__":
    machines = read_input()
    print(f"Part 1:\t{part1(machines)}")
