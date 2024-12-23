import sys
from copy import copy, deepcopy

from dataclasses import dataclass, field


@dataclass
class Coordinate:
    x: int = 0
    y: int = 0


@dataclass
class Maze:
    walls: list[Coordinate] = field(default_factory=list)
    boxes: list[Coordinate] = field(default_factory=list)
    robot: Coordinate = field(default_factory=Coordinate)
    instructions: list[str] = field(default_factory=list)

    def left(self):
        cursor = copy(self.robot)
        cursor.x -= 1

        if cursor in self.walls:
            return

        if cursor not in self.boxes:
            self.robot.x -= 1
            return

        boxes_to_move = []
        while cursor in self.boxes:
            boxes_to_move.append(self.boxes[self.boxes.index(cursor)])
            cursor.x -= 1

        if cursor in self.walls:
            return

        for box in boxes_to_move:
            box.x -= 1
        self.robot.x -= 1

    def right(self):
        cursor = copy(self.robot)
        cursor.x += 1

        if cursor in self.walls:
            return

        if cursor not in self.boxes:
            self.robot.x += 1
            return

        boxes_to_move = []
        while cursor in self.boxes:
            boxes_to_move.append(self.boxes[self.boxes.index(cursor)])
            cursor.x += 1

        if cursor in self.walls:
            return

        for box in boxes_to_move:
            box.x += 1
        self.robot.x += 1

    def up(self):
        cursor = copy(self.robot)
        cursor.y -= 1

        if cursor in self.walls:
            return

        if cursor not in self.boxes:
            self.robot.y -= 1
            return

        boxes_to_move = []
        while cursor in self.boxes:
            boxes_to_move.append(self.boxes[self.boxes.index(cursor)])
            cursor.y -= 1

        if cursor in self.walls:
            return

        for box in boxes_to_move:
            box.y -= 1
        self.robot.y -= 1

    def down(self):
        cursor = copy(self.robot)
        cursor.y += 1

        if cursor in self.walls:
            return

        if cursor not in self.boxes:
            self.robot.y += 1
            return

        boxes_to_move = []
        while cursor in self.boxes:
            boxes_to_move.append(self.boxes[self.boxes.index(cursor)])
            cursor.y += 1

        if cursor in self.walls:
            return

        for box in boxes_to_move:
            box.y += 1
        self.robot.y += 1

    def part1(self) -> int:
        maze = deepcopy(self)

        for instruction in maze.instructions:
            match instruction:
                case "<":
                    maze.left()
                case ">":
                    maze.right()
                case "^":
                    maze.up()
                case "v":
                    maze.down()

        return sum([box.y * 100 + box.x for box in maze.boxes])


def read_input() -> Maze:
    maze = Maze()

    for y, line in enumerate(sys.stdin.readlines()):
        for x, char in enumerate(line):
            if char == "#":
                maze.walls.append(Coordinate(x, y))
            elif char == "O":
                maze.boxes.append(Coordinate(x, y))
            elif char == "@":
                maze.robot = Coordinate(x, y)
            elif char in "<>^v":
                maze.instructions.append(char)

    return maze


if __name__ == "__main__":
    maze = read_input()
    print(f"Part 1:\t{maze.part1()}")
