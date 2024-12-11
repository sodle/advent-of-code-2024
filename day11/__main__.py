import sys
from functools import cache


def read_stones() -> list[int]:
    stones = []
    for line in sys.stdin.readlines():
        for tok in line.split():
            tok = tok.strip()
            if tok.isnumeric():
                stones.append(int(tok))
    return stones


def part1(stones: list[int]) -> int:
    acc = 0
    for stone in stones:
        acc += blink(stone, 25)
    return acc


@cache
def blink(stone: int, reps: int) -> int:
    for n in range(reps):
        if stone == 0:
            stone = 1
        else:
            strone = str(stone)
            strelone = len(strone)
            if strelone % 2 == 0:
                left = int(strone[: strelone // 2])
                right = int(strone[strelone // 2 :])
                return blink(left, reps - n - 1) + blink(right, reps - n - 1)
            else:
                stone *= 2024
    return 1


def part2(stones: list[int]) -> int:
    acc = 0
    for n, stone in enumerate(stones):
        acc += blink(stone, 75)
    return acc


if __name__ == "__main__":
    stones = read_stones()
    print(f"Part 1:\t{part1(stones)}")
    print(f"Part 2:\t{part2(stones)}")
