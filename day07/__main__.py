import sys


Equation = tuple[int, list[int]]


def read_equations() -> list[Equation]:
    equations = []

    for line in sys.stdin.readlines():
        if ":" in line:
            lhs, rhs = line.split(":")
            lhs = int(lhs)
            rhs = [int(n.strip()) for n in rhs.strip().split(" ")]
            equations.append((lhs, rhs))

    return equations


def part1(equations: list[Equation]) -> int:
    acc = 0

    for lhs, rhs in equations:
        candidates = [rhs]
        while len(candidates) > 0:
            candidate = candidates.pop(0)
            if len(candidate) == 1:
                if candidate[0] == lhs:
                    acc += lhs
                    break
            else:
                a, b = candidate[:2]
                remain = candidate[2:]

                candidates.append([a + b, *remain])
                candidates.append([a * b, *remain])

    return acc


def part2(equations: list[Equation]) -> int:
    acc = 0

    for lhs, rhs in equations:
        candidates = [rhs]
        while len(candidates) > 0:
            candidate = candidates.pop(0)
            if len(candidate) == 1:
                if candidate[0] == lhs:
                    acc += lhs
                    break
            else:
                a, b = candidate[:2]
                remain = candidate[2:]

                add = a + b
                mult = a * b
                cat = int(f"{a}{b}")

                if add <= lhs:
                    candidates.append([add, *remain])

                if mult <= lhs:
                    candidates.append([mult, *remain])

                if cat <= lhs:
                    candidates.append([cat, *remain])

    return acc


if __name__ == "__main__":
    equations = read_equations()
    print(f"Part 1:\t{part1(equations)}")
    print(f"Part 2:\t{part2(equations)}")
