import sys
import networkx as nx


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


def part1(rules: list[OrderingRule], lists: list[PageList]) -> int:
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


def part2(rules: list[OrderingRule], lists: list[PageList]) -> int:
    G = nx.DiGraph()
    for a, b in rules:
        G.add_edge(a, b)

    acc = 0

    for page_list in lists:
        sG = nx.subgraph(G, page_list)

        start = None
        end = None

        for node, degree in sG.in_degree:
            if degree == 0:
                start = node

        for node, degree in sG.out_degree:
            if degree == 0:
                end = node

        sorted_pages = nx.dag_longest_path(sG, start, end)
        if sorted_pages != page_list:
            acc += sorted_pages[(len(sorted_pages) // 2)]

    return acc


if __name__ == "__main__":
    rules, lists = read_input()
    print(f"Part 1:\t{part1(rules, lists)}")
    print(f"Part 2:\t{part2(rules, lists)}")
