import sys
import re

re_mul = re.compile(r"mul\((\d+),(\d+)\)")


def read_mults() -> list[tuple[int, int]]:
    out = []
    for line in sys.stdin.readlines():
        out += [
            (int(match.group(1)), int(match.group(2)))
            for match in re_mul.finditer(line)
        ]
    return out


def part1(mults: list[tuple[int, int]]) -> int:
    out = 0
    for lhs, rhs in mults:
        out += lhs * rhs
    return out


if __name__ == "__main__":
    mults = read_mults()
    print(f"Part 1:\t{part1()}")
