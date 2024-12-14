import sys
import re

from typing import NamedTuple

robot_rex = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

Coordinate = tuple[int, int]


class Robot(NamedTuple):
    position: Coordinate
    velocity: Coordinate

    def run(self, steps: int) -> Coordinate:
        px, py = self.position
        vx, vy = self.velocity
        px += vx * steps
        py += vy * steps
        return (px % 101, py % 103)


def parse_input() -> list[Robot]:
    robots = []
    for line in sys.stdin.readlines():
        robot_match = robot_rex.match(line)
        if robot_match is None:
            continue
        px, py, vx, vy = [int(g) for g in robot_match.groups()]
        robots.append(Robot((px, py), (vx, vy)))
    return robots


def part1(robots: list[Robot]) -> int:
    new_coordinates = [r.run(100) for r in robots]

    quadrants = [
        (range(50), range(51)),
        (range(51, 103), range(51)),
        (range(50), range(52, 103)),
        (range(51, 103), range(52, 103)),
    ]

    acc = 1
    for qx, qy in quadrants:
        count = len([(px, py) for (px, py) in new_coordinates if px in qx and py in qy])
        acc *= count

    return acc


if __name__ == "__main__":
    robots = parse_input()
    print(f"Part 1:\t{part1(robots)}")
