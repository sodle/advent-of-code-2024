import sys
from typing import NamedTuple


class File:
    def __init__(self, id: int, start: int, size: int):
        self.id = id
        self.start = start
        self.size = size

    def copy(self) -> "File":
        return File(self.id, self.start, self.size)

    def __repr__(self):
        return f"file {self.id} - start {self.start} - size {self.size}"


class Disk(NamedTuple):
    files: list[File]
    blanks: list[File]

    def copy(self) -> "Disk":
        return Disk(
            [file.copy() for file in self.files],
            [blank.copy() for blank in self.blanks],
        )

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


def read_disk() -> Disk:
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


def part1(disk: Disk) -> int:
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


def part2(disk: Disk) -> int:
    for file in reversed(disk.files):
        fitting_blanks = [
            blank
            for blank in disk.blanks
            if blank.size >= file.size and blank.start < file.start
        ]
        if len(fitting_blanks) == 0:
            continue

        original_start = file.start

        blank = fitting_blanks[0]
        file.start = blank.start
        blank.size -= file.size
        blank.start += file.size

        if blank.size == 0:
            disk.blanks.pop(disk.blanks.index(blank))

        disk.blanks.append(File(-1, original_start, file.size))

    acc = 0
    for file in disk.files:
        for n in range(file.size):
            acc += file.id * (file.start + n)

    return acc


if __name__ == "__main__":
    disk = read_disk()
    print(f"Part 1:\t{part1(disk.copy())}")
    print(f"Part 2:\t{part2(disk.copy())}")
