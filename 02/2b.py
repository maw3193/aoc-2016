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
' ', ' ', '1', ' ', ' ',
' ', '2', '3', '4', ' ',
'5', '6', '7', '8', '9',
' ', 'A', 'B', 'C', ' ',
' ', ' ', 'D', ' ', ' '
]
keypad_width = 5
keypad_height = 5
position = [0, 2]


def translate_position(pos):
    x = pos[0]
    y = pos[1]
    return keypad[y * keypad_width + x]

def can_move(pos):
    if pos[0] < 0:
        return False
    elif pos[0] >= keypad_width:
        return False
    elif pos[1] < 0:
        return False
    elif pos[1] >= keypad_height:
        return False
    elif translate_position(pos) == ' ':
        return False
    else:
        return True

def move_position(curpos, cmd):
    if cmd == "U":
        np = [curpos[0], curpos[1] - 1]
    elif cmd == "D":
        np = [curpos[0], curpos[1] + 1]
    elif cmd == "L":
        np = [curpos[0] - 1, curpos[1]]
    elif cmd == "R":
        np = [curpos[0] + 1, curpos [1]]
    else:
        sys.exit("Unexpected character, %s" % cmd)

    if can_move(np):
        return np
    else:
        return curpos[:]

with open(args.input_file, "r") as f:
    for line in f:
        for c in line:
            if c != "\n":
                position = move_position(position, c)
            else:
                print(translate_position(position))
