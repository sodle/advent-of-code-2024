import sys


def read_lists() -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in sys.stdin.readlines():
        nl, nr = line.split()
        left.append(int(nl))
        right.append(int(nr))
    return left, right


def part1(left: list[int], right: list[int]) -> int:
    pairs = zip(sorted(left), sorted(right))
    result = 0
    for l, r in pairs:
        result += abs(l-r)
    return result


def part2(left: list[int], right: list[int]) -> int:
    result = 0
    for l in left:
        r = len([n for n in right if n==l])
        result += l*r
    return result


if __name__ == "__main__":
    left, right = read_lists()
    print(f"Part 1:\t{part1(left, right)}")
    print(f"Part 2:\t{part2(left, right)}")