#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-15")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

# discs have a number of positions, and their position at time=0 (an offset)

discs = []

with open(args.input, "r") as f:
    for line in f:
        m = re.match("Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).", line.strip())
        if not m:
            sys.exit("Error parsing line '%s'" % line)
        discs.append({"positions": int(m.group(1)), "offset": int(m.group(2))})

time = 0
while True:
    capsule_passed = True
    for i in range(0, len(discs)):
        # +1 bodged in because my array of discs starts at 0
        if (discs[i]["offset"] + time + i + 1) % discs[i]["positions"] != 0:
            capsule_passed = False
    if capsule_passed:
        print "Capsule passed at time=%d" % time
        break
    time += 1
