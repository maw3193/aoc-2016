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
    for combo in edge_combinations:
        if int(edges[combo[0]]) + int(edges[combo[1]]) <= int(edges[combo[2]]):
            return False
    return True

valid_triangles = 0    

with open(args.input_file, "r") as f:
    for line in f:
        edges = line.split()
        if verify_triangle(edges):
            valid_triangles += 1

print(valid_triangles)
