#!/usr/bin/python

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-09")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

lines = []

with open(args.input, "r") as f:
    for line in f:
        pos = 0
        newstr = ""
        while(pos < len(line)):
            if line[pos] != "(":
                newstr += line[pos]
                pos += 1
            else:
                m = re.match("\((\d+)x(\d+)\)", line[pos:])
                startpos = pos + len(m.group(0))
                sub = line[startpos:startpos + int(m.group(1))] * int(m.group(2))
                newstr += sub
                pos += len(m.group(0)) + int(m.group(1))
        lines.append(newstr.strip())
length = 0
for line in lines:
    length += len(line)
print(length)
