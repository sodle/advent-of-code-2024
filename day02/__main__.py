import sys


def read_reports() -> list[list[int]]:
    reports = []
    for line in sys.stdin.readlines():
        reports.append([int(n) for n in line.split()])
    return reports


def is_report_safe(report: list[int]) -> bool:
    tonic = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        if diff == 0:
            return False

        step = abs(diff)
        step_tonic = diff / step

        if step > 3:
            return False

        if tonic == 0:
            tonic = step_tonic
        elif tonic != step_tonic:
            return False
    return True


def dampened_reports(report: list[int]) -> list[list[int]]:
    out = []
    length = len(report)
    for n in range(length):
        copy = [report[i] for i in range(length) if i != n]
        out.append(copy)
    return out


def part1(reports: list[list[int]]) -> int:
    out = 0
    for report in reports:
        if is_report_safe(report):
            out += 1
    return out


def part2(reports: list[list[int]]) -> int:
    out = 0
    for report in reports:
        if is_report_safe(report):
            out += 1
        else:
            for dampened in dampened_reports(report):
                if is_report_safe(dampened):
                    out += 1
                    break
    return out


if __name__ == "__main__":
    reports = read_reports()
    print(f"Part 1:\t{part1(reports)}")
    print(f"Part 2:\t{part2(reports)}")
