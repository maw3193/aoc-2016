#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-06")
parser.add_argument("input_file")
args = parser.parse_args()

lines = []
with open(args.input_file, "r") as f:
    for line in f:
        lines.append(line.strip())

word_length = len(lines[0])
total_lines = len(lines)
decoded_word = ""
for x in range(0, word_length):
    lettersums = {}
    for y in range(0, total_lines):
        if lines[y][x] not in lettersums:
            lettersums[lines[y][x]] = 1
        else:
            lettersums[lines[y][x]] += 1
    decoded_word += sorted(lettersums.iteritems(), key=lambda i: i[1], reverse=False)[0][0]
print(decoded_word)
