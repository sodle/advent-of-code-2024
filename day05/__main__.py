import sys


OrderingRule = tuple[int, int]
PageList = list[int]


def read_input() -> tuple[list[OrderingRule], list[PageList]]:
    rules = []
    lists = []

    for line in sys.stdin.readlines():
        if "|" in line:
            lhs, rhs = line.split("|")
            rules.append((int(lhs), int(rhs)))
        elif "," in line:
            lists.append([int(n) for n in line.split(",")])

    return rules, lists


def part1(rules: list[OrderingRule], lists: list[PageList]):
    acc = 0
    for update in lists:
        valid = True
        for lhs, rhs in rules:
            if lhs in update and rhs in update:
                il = update.index(lhs)
                ir = update.index(rhs)
                if ir < il:
                    valid = False
                    break
        if valid:
            mid = update[(len(update) // 2)]
            acc += mid
    return acc


if __name__ == "__main__":
    rules, lists = read_input()
    print(f"Part 1:\t{part1(rules, lists)}")
