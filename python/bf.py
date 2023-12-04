#!/usr/bin/env python3
import ctypes
from enum import Enum
import re

file = open("test.bf", "r").read()
file = re.sub(r"[\n\t ]", "", file)

class Machine(object):
    def __init__(self) -> None:
        self.dp = 0
        self.tape = [ctypes.c_byte() for _ in range(3000)]
        self.dp_val = self.tape[0].value
        pass

    def inc_dp(self):
        self.dp += 1

    def dec_dp(self):
        self.dp -= 1

    def inc_val(self):
        self.tape[self.dp].value += 1

    def dec_val(self):
        self.tape[self.dp].value -= 1

    def print_val(self):
        print(self.tape[self.dp].value)

    def parse(self, input):
        commands = []
        for char in input:
            match char:
                case ">":
                    commands.append(self.inc_dp)
                case "<":
                    commands.append(self.dec_dp)
                case "+":
                    commands.append(self.inc_val)
                case "-":
                    commands.append(self.dec_val)
                case ".":
                    commands.append(self.print_val)
        self.commands = commands

    def run(self):
        for command in self.commands:
            command()

    class Char(Enum):
        Right = ">"
        Left = "<"
        Inc = "+"
        Dec = "-"
        Print = "."
        Input = ","
        StartLoop = "["
        EndLoop = "]"



machine = Machine()
machine.parse(file)
machine.run()
