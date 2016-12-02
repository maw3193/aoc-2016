#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-02")
parser.add_argument("input_file")
args = parser.parse_args()

# The keypad goes
# 1 2 3
# 4 5 6
# 7 8 9
# and we start at 5.
keypad = [
1, 2, 3,
4, 5, 6,
7, 8, 9,
]
keypad_width = 3
keypad_height = 3
position = [1, 1]

def clamp(n, upper, lower):
    return max(lower, min(n, upper))

def translate_position(pos):
    x = pos[0]
    y = pos[1]
    return keypad[y * keypad_width + x]

def move_position(curpos, cmd):
    if cmd == "U":
        newpos = [curpos[0], clamp(curpos[1] - 1, keypad_height - 1, 0)]
    elif cmd == "D":
        newpos = [curpos[0], clamp(curpos[1] + 1, keypad_height - 1, 0)]
    elif cmd == "L":
        newpos = [clamp(curpos[0] - 1, keypad_width - 1, 0), curpos[1]]
    elif cmd == "R":
        newpos = [clamp(curpos[0] + 1, keypad_width - 1, 0), curpos[1]]
    else:
        sys.exit("Unexpected character, %s" % cmd)
    return newpos

with open(args.input_file, "r") as f:
    for line in f:
        for c in line:
            if c != "\n":
                position = move_position(position, c)
            else:
                print(translate_position(position))
