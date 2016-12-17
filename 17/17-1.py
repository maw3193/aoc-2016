#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, re, md5

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-17")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

favourite_num = 0

MAP_WIDTH = 4
MAP_HEIGHT = 4

def path_is_open(x, y, code):
    if x >= MAP_WIDTH or x < 0 or y >= MAP_HEIGHT or y < 0:
        return False

    direction_mapping = {
        "U": 0,
        "D": 1,
        "L": 2,
        "R": 3
    }

    # md5sum passcode
    digest = md5.new(code[:-1]).hexdigest()
    direction = code[-1:]
    char = digest[direction_mapping[direction]]
    if ("b" in char or "c" in char or "d" in char
        or "e" in char or "f" in char):
        return True
    return False
    
def get_next_steps(state):
    x = state[0]
    y = state[1]
    code = state[2]
    next_steps = set()
    for delta in ((1, 0, "R"), (-1, 0, "L"), (0, 1, "D"), (0, -1, "U")):
            if path_is_open(x+delta[0], y+delta[1], code+delta[2]):
                next_steps.add((x+delta[0], y+delta[1], code+delta[2]))
    return next_steps

def find_ideal_state(states, ideal):
    for state in states:
        if state[0] == ideal_state[0] and state[1] == ideal_state[1]:
            return state[2]

state = (0, 0, "")
ideal_state = (MAP_WIDTH - 1, MAP_HEIGHT - 1)

def get_path(start, ideal):
    states = set([start])
    while True:
        new_states = set()
        for state in states:
            new_states |= get_next_steps(state)
        if len(new_states) == 0:
            print "There are no valid paths!"
            break
        ideal_find = find_ideal_state(new_states, ideal)
        if ideal_find:
            print "Found path %s" % ideal_find[len(start[2]):]
            print "A total of %d steps" % len(ideal_find[len(start[2]):])
            break
        states = new_states

with open(args.input, "r") as f:
    for line in f:
        state = (0, 0, line.strip())
        get_path(state, ideal_state)
