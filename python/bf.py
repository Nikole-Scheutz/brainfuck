#!/usr/bin/env python3
import ctypes

pointer = 0
tape = [ctypes.c_byte() for _ in range(3000)]
file = open("test.bf", "r").read()

def inc_dp():
    global pointer
    pointer += 1

def dec_dp():
    global pointer
    pointer -= 1

def inc_val():
    tape[pointer].value += 1

def dec_val():
    tape[pointer].value -= 1

def print_val():
    print(tape[pointer].value)

for line in file:
    for char in line:
        match char:
            case ">":
                inc_dp()
            case "<":
                dec_dp()
            case "+":
                inc_val()
            case "-":
                dec_val()
            case ".":
                print_val()

