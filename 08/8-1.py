#!/usr/bin/python

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-07")
parser.add_argument("--input_file", default="input.txt")
parser.add_argument("--width", default=50, type=int)
parser.add_argument("--height", default=6, type=int)
args = parser.parse_args()

def generate_pixmap(width, height):
    pixmap = []
    for line in range(0, height):
        l = []
        for pixel in range(0, width):
            l.append(False)
        pixmap.append(l)
    return pixmap

def draw_pixmap(pixmap):
    sys.stdout.write("\n")
    for line in pixmap:
        for pixel in line:
            if pixel:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")

pixmap = generate_pixmap(args.width, args.height)

transforms = []

def count_pixels(pixmap):
    pixels = 0
    for line in pixmap:
        for pixel in line:
            if pixel:
                pixels += 1
    return pixels

def do_rect(pixmap, x, y):
    for i in range(0, x):
        for j in range(0, y):
            pixmap[j][i] = True
    return True

def do_rotate_row(pixmap, row, shift):
    row_width = len(pixmap[0])
    old_row = pixmap[row][:]
    for pixel in range(0, row_width):
        pixmap[row][(pixel + shift) % row_width] = old_row[pixel]
    return True

def do_rotate_col(pixmap, col, shift):
    col_height = len(pixmap)
    old_col = []
    for line in range(0, col_height):
        old_col.append(pixmap[line][col])

    for line in range(0, col_height):
        pixmap[(line + shift) % col_height][col] = old_col[line]
    return True

def parse_transform(pixmap, transforms, line):
    match = re.findall("^rect (\d+)x(\d+)$", line)
    if len(match) > 0 and len(match[0]) == 2:
        transforms.append([do_rect, {"pixmap": pixmap,
                                     "x": int(match[0][0]),
                                     "y": int(match[0][1])}])
        return
    match = re.findall("^rotate row y=(\d+) by (\d+)$", line)
    if len(match) > 0 and len(match[0]) == 2:
        transforms.append([do_rotate_row, {"pixmap": pixmap,
                                           "row": int(match[0][0]),
                                           "shift": int(match[0][1])}])
        return
    match = re.findall("^rotate column x=(\d+) by (\d+)$", line)
    if len(match) > 0 and len(match[0]) == 2:
        transforms.append([do_rotate_col, {"pixmap": pixmap,
                                           "col": int(match[0][0]),
                                           "shift": int(match[0][1])}])
        return

with open(args.input_file, "r") as f:
    for line in f:
        parse_transform(pixmap, transforms, line.strip())

for transform in transforms:
    transform[0](**transform[1])

draw_pixmap(pixmap)
print(count_pixels(pixmap))
