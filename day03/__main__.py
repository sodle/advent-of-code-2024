import sys
import re

re_mul = re.compile(r"mul\((\d+),(\d+)\)")
re_instruction = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")


def read_instructions() -> list[str]:
    out = []
    for line in sys.stdin.readlines():
        out += [match.group(0) for match in re_instruction.finditer(line)]
    return out


def part1(instructions: list[str]) -> int:
    out = 0

    for instruction in instructions:
        if instruction.startswith("mul"):
            lhs, rhs = re_mul.match(instruction).groups()
            out += int(lhs) * int(rhs)

    return out


def part2(instructions: list[str]) -> int:
    enabled = True
    out = 0

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            lhs, rhs = re_mul.match(instruction).groups()
            out += int(lhs) * int(rhs)

    return out


if __name__ == "__main__":
    instructions = read_instructions()
    print(f"Part 1:\t{part1(instructions)}")
    print(f"Part 2:\t{part2(instructions)}")
