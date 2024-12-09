import sys
from typing import NamedTuple


class File:
    def __init__(self, id: int, start: int, size: int):
        self.id = id
        self.start = start
        self.size = size

    def __repr__(self):
        return f"file {self.id} - start {self.start} - size {self.size}"


class Disk(NamedTuple):
    files: list[File]
    blanks: list[File]

    def copy(self) -> "Disk":
        return Disk(self.files.copy(), self.blanks.copy())

    def __repr__(self):
        size = sum([f.size for f in self.files] + [b.size for b in self.blanks])
        r = [" "] * size

        for f in self.files:
            for n in range(f.size):
                r[f.start + n] = str(f.id)

        for b in self.blanks:
            for n in range(b.size):
                r[b.start + n] = "."

        return "".join(r)


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


def read_disk_2pt0() -> Disk:
    disk = Disk(files=[], blanks=[])

    input_string = sys.stdin.read().strip()

    blank = False
    pointer = 0

    for digit in input_string:
        size = int(digit)
        if blank:
            disk.blanks.append(File(-1, pointer, size))
        else:
            disk.files.append(File(len(disk.files), pointer, size))
        pointer += size
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


def part1_2pt0(disk: Disk) -> int:
    while len(disk.blanks) > 0:
        first_blank = disk.blanks[0]
        last_blank = disk.blanks[-1]
        last_file = disk.files[-1]

        if last_blank.start > last_file.start:
            disk.blanks.pop()
            continue

        move_size = min(first_blank.size, last_file.size)
        if move_size == 0:
            disk.blanks.pop(0)
            continue

        first_blank.size -= move_size
        last_file.size -= move_size
        disk.files.insert(0, File(last_file.id, first_blank.start, move_size))
        first_blank.start += move_size

        if first_blank.size == 0:
            disk.blanks.pop(0)
        if last_file.size == 0:
            disk.files.pop()

    acc = 0
    for file in disk.files:
        for n in range(file.size):
            acc += file.id * (file.start + n)

    return acc


if __name__ == "__main__":
    disk = read_disk_2pt0()
    print(f"Part 1:\t{part1_2pt0(disk.copy())}")
