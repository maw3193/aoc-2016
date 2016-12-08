#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-03")
parser.add_argument("input_file")
args = parser.parse_args()

edge_combinations = [
[0, 1, 2],
[1, 2, 0],
[0, 2, 1]
]

# A triangle is possible if no one side is longer than the
# othe two.
def verify_triangle(edges):
    print(edges)
    for combo in edge_combinations:
        if int(edges[combo[0]]) + int(edges[combo[1]]) <= int(edges[combo[2]]):
            return False
    return True

valid_triangles = 0    
words = []
total_lines = 0
with open(args.input_file, "r") as f:
    for line in f:
        w = line.split()
        words.append(w)
        total_lines += 1

if total_lines % 3 != 0:
    sys.exit("Number of lines is not divisible by 3!")

for row in range(0, total_lines, 3):
    for col in range(0, 3):
        if verify_triangle([words[row][col], words[row+1][col], words[row+2][col]]):
            valid_triangles += 1
print(valid_triangles)
