import sys

from typing import NamedTuple


class Interpreter(NamedTuple):
    a: int
    b: int
    c: int
    program: list[int]

    def part1(self) -> str:
        a, b, c, program = self

        def combo_operand(operand: int) -> int:
            if operand < 4:
                return operand
            elif operand == 4:
                return a
            elif operand == 5:
                return b
            elif operand == 6:
                return c
            else:
                return -1

        pc = 0
        stdout = []

        def adv():
            nonlocal a, pc

            operand = combo_operand(program[pc + 1])
            a = a // pow(2, operand)

            pc += 2

        def bxl():
            nonlocal b, pc

            operand = program[pc + 1]
            b = b ^ operand

            pc += 2

        def bst():
            nonlocal b, pc

            operand = combo_operand(program[pc + 1])
            b = operand % 8

            pc += 2

        def jnz():
            nonlocal pc

            operand = program[pc + 1]
            if a == 0:
                pc += 2
            else:
                pc = operand

        def bxc():
            nonlocal pc, b

            b = b ^ c

            pc += 2

        def out():
            nonlocal pc, stdout

            operand = combo_operand(program[pc + 1])
            stdout.append(str(operand % 8))

            pc += 2

        def bdv():
            nonlocal b, pc

            operand = combo_operand(program[pc + 1])
            b = a // pow(2, operand)

            pc += 2

        def cdv():
            nonlocal c, pc

            operand = combo_operand(program[pc + 1])
            c = a // pow(2, operand)

            pc += 2

        while pc < len(program):
            opcode = program[pc]
            match opcode:
                case 0:
                    adv()
                case 1:
                    bxl()
                case 2:
                    bst()
                case 3:
                    jnz()
                case 4:
                    bxc()
                case 5:
                    out()
                case 6:
                    bdv()
                case 7:
                    cdv()

        return ",".join(stdout)


def read_input() -> Interpreter:
    for line in sys.stdin.readlines():
        if line.startswith("Register A:"):
            _, _a = line.split(": ")
            a = int(_a)
        if line.startswith("Register B:"):
            _, _b = line.split(": ")
            b = int(_b)
        if line.startswith("Register C:"):
            _, _c = line.split(": ")
            c = int(_c)
        if line.startswith("Program:"):
            _, _prog = line.split(": ")
            program = [int(op) for op in _prog.split(",")]
    return Interpreter(a, b, c, program)


if __name__ == "__main__":
    interpreter = read_input()
    print(f"Part 1:\t{interpreter.part1()}")
