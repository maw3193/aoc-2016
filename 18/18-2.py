#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-18")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()


def draw_row(row):
    for space in row:
        if space:
            sys.stdout.write("^")
        else:
            sys.stdout.write(".")
    print ""

# Map is 2x2 array, True if trap, False if safe
area = []

with open(args.input, "r") as f:
    for line in f:
        new_row = []
        for c in line.strip():
            if c == ".":
                new_row.append(False)
            elif c == "^":
                new_row.append(True)
            else:
                sys.exit("Unexpected character when reading line '%s'" % c)
        area.append(new_row)

def area_is_trap(pos, prevline):
    if pos == 0:
        left = False
    else:
        left = prevline[pos - 1]
    mid = prevline[pos]
    if pos == len(prevline) - 1:
        right = False
    else:
        right = prevline[pos + 1]

    if left and mid and not right:
        return True
    elif mid and right and not left:
        return True
    elif left and not mid and not right:
        return True
    elif right and not mid and not left:
        return True
    else:
        return False

lineno = 1
MAP_HEIGHT = 400000
prev_line = area[0]

safe_tiles = 0
for tile in prev_line:
    if not tile:
        safe_tiles += 1

while lineno < MAP_HEIGHT:
    newline = []
    for xpos in range(0, len(prev_line)):
        is_trap = area_is_trap(xpos, prev_line)
        if not is_trap:
            safe_tiles += 1
        newline.append(is_trap)
    lineno += 1
    prev_line = newline

print safe_tiles
