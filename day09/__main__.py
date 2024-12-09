import sys


def read_disk() -> list[int]:
    disk = []

    input_string = sys.stdin.read().strip()

    file_id = 0
    blank = False

    for digit in input_string:
        if blank:
            disk += [-1] * int(digit)
            file_id += 1
        else:
            disk += [file_id] * int(digit)

        blank = not blank

    return disk


def part1(disk: list[int]) -> int:
    while -1 in disk:
        if disk[-1] == -1:
            disk.pop()
        else:
            blank_index = disk.index(-1)
            disk[blank_index] = disk.pop()

    acc = 0
    for position, file_id in enumerate(disk):
        acc += position * file_id

    return acc


if __name__ == "__main__":
    disk = read_disk()
    print(f"Part 1:\t{part1(disk.copy())}")
