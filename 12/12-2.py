#!/usr/bin/python

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-12")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

# 4 registers, a, b, c, d
# instruction cpy x y (copies value of x into y)
# instruction inc x (increases x by 1)
# instruction dec x (decreases x by 1)
# instruction jnz x y (jumps y (positive or negative) steps if x isn't zero)

state = {"registers": {"a": 0, "b": 0, "c": 1, "d": 0},
         "pos": 0}
instructions = []

def do_copy(state, src, dest):
    if type(src) == int:
        state["registers"][dest] = src
    elif type(src) == str:
        state["registers"][dest] = state["registers"][src]
    else:
        sys.exit("Unexpected type in do_copy: %s" % str(type(src)))

def do_inc(state, reg):
    state["registers"][reg] += 1

def do_dec(state, reg):
    state["registers"][reg] -= 1

def do_jnz(state, reg, steps):
    if type(reg) == int:
        if reg == 0:
            return
    elif type(reg) == str:
        if state["registers"][reg] == 0:
            return
    else:
        sys.exit("Unexpected type in do_jnz: %s" % str(type(reg)))

    # Subtracting as horrible bodge
    state["pos"] += steps - 1

def parse_instruction(line):
    # Copy constant
    m = re.match("cpy (\d+) (\w)", line)
    if m:
        return [do_copy, {"src": int(m.group(1)), "dest": m.group(2), "state": state}]
    # Copy register
    m = re.match("cpy (\w) (\w)", line)
    if m:
        return [do_copy, {"src": m.group(1), "dest": m.group(2), "state": state}]
    # Increase register
    m = re.match("inc (\w)", line)
    if m:
        return [do_inc, {"reg": m.group(1), "state": state}]
    # Decrease register
    m = re.match("dec (\w)", line)
    if m:
        return [do_dec, {"reg": m.group(1), "state": state}]
    # Jump if non-zero (constant)
    m = re.match("jnz (\d+) (-?\d+)", line)
    if m:
        return [do_jnz, {"reg": int(m.group(1)), "steps": int(m.group(2)), "state": state}]
    # Jump if non-zero (register)
    m = re.match("jnz (\w) (-?\d+)", line)
    if m:
        return [do_jnz, {"reg": m.group(1), "steps": int(m.group(2)), "state": state}]

    sys.exit("Unhandled instruction '%s'" % line)

with open(args.input, "r") as f:
    for line in f:
        instructions.append(parse_instruction(line))

while(state["pos"] < len(instructions)):
    instruction = instructions[state["pos"]]
    instruction[0](**instruction[1])
    state["pos"] += 1

for register in state["registers"].iteritems():
    print(register)
