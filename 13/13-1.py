#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, re, math

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-13")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

favourite_num = 0

def coord_is_wall(x, y):
    fancy_number = x * x + 3 * x + 2 * x * y + y + y * y + favourite_num
    bit_count = 0
    for i in range(0, int(math.floor(math.log(fancy_number, 2)) + 1)):
        if fancy_number & 1 == 1:
            bit_count += 1
        fancy_number >>= 1
    if bit_count % 2 == 1:
        return True
    else:
        return False

def get_next_steps(state):
    x = state[0]
    y = state[1]
    next_steps = set()
    for delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not coord_is_wall(x+delta[0], y+delta[1]):
                next_steps.add((x+delta[0], y+delta[1]))
    return next_steps


with open(args.input, "r") as f:
    favourite_num = int(f.read().strip())

state = (1, 1)
#ideal_state = (7, 4)
ideal_state = (31, 39)

# Fewest number of steps required, on an infinite map.
# On a breadth-first, the first one to get there is the shortest.
# How to do breadth-first? Have a queue of steps to take next.
# Keep a set of places I've already been, and make sure the heads
# know how many steps they've taken.
places_been = set([state])

#for y in range(0, 7):
#    for x in range(0, 10):
#        sys.stdout.write("#" if coord_is_wall(x, y) else ".")
#    print ""

states = set([state])

n_steps = 0
while True:
    new_states = set()
    for state in states:
        new_states |= get_next_steps(state)
    new_states -= places_been
    states = new_states
    places_been |= new_states
    n_steps += 1
    if ideal_state in states:
        print "Found ", ideal_state, "in %d moves" % n_steps
        break
