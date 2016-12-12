#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, re

class ItemType:
    CHIP = 1
    GEN = 2

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-11")
parser.add_argument("--input_file", default="input.txt")
args = parser.parse_args()

initial_state = {"E": 0, "floors": []}

with open(args.input_file, "r") as f:
    i = 0
    for line in f:
        floor = []
        for chip in re.findall("a (\w+)-compatible microchip", line):
            floor.append((ItemType.CHIP, chip))
        for gen in re.findall("a (\w+) generator", line):
            floor.append((ItemType.GEN, gen))
        initial_state["floors"].append(floor)

def gen_ideal_state(in_state):
    top_floor = len(in_state["floors"]) - 1
    ideal_state = {"E": top_floor, "floors": []}
    for i in range(0, len(in_state["floors"])):
        ideal_state["floors"].append([])
    for i in range(0, top_floor):
        for item in in_state["floors"][i]:
            ideal_state["floors"][top_floor].append(item)
    return ideal_state

def get_possible_item_combos(state):
    combos = set()
    floor_contents = state["floors"][state["E"]]
    for i in range(0, len(floor_contents)):
        combos.add(frozenset((floor_contents[i],)))
        for j in range(0, len(floor_contents)):
            if i != j:
                combos.add(frozenset((floor_contents[i], floor_contents[j])))
    return combos

def get_possible_floors(state):
    floors = []
    if state["E"] > 0:
        floors.append(state["E"] - 1)
    if state["E"] + 1 < len(state["floors"]):
        floors.append(state["E"] + 1)
    return floors

def is_state_identical(s1, s2):
    if len(s1["floors"]) != len(s2["floors"]):
        sys.exit("Comparing states with differing numbers of floors!")
    floorcount = len(s1["floors"])
    if s1["E"] != s2["E"]:
        return False
    for i in range(0, floorcount):
        if len(s1["floors"][i]) != len(s2["floors"][i]):
            return False
        for j in range(0, len(s1["floors"][i])):
            if s1["floors"][i][j] != s2["floors"][i][j]:
                return False
    return True

def is_state_valid(state, states):
    # No states we've already stepped through
    for s in states:
        if is_state_identical(s, state):
            print "Rejected! Identical to a previous state!"
            return False
    # No chips on a floor with non-counterpart generators
    for floor in state["floors"]:
        for item_1 in floor:
            if item_1[0] == ItemType.CHIP:
                chip_threatened = False
                chip_protected = False
                for item_2 in floor:
                    if item_2[0] == ItemType.GEN and item_1[1] != item_2[1]:
                        chip_threatened = True
                    if item_2[0] == ItemType.GEN and item_1[1] == item_2[1]:
                        chip_protected = True
                if chip_threatened == True and chip_protected == False:
                    print "Rejected! Chip destroyed by radiation!"
                    print floor
                    return False
    return True

def gen_new_state(old_state, moveto, items):
    new_state = {"E": moveto, "floors": []}
    floorcount = len(old_state["floors"])
    for n in range(0, floorcount):
        new_state["floors"].append(old_state["floors"][n][:])
    for item in items:
        new_state["floors"][moveto].append(item)
        new_state["floors"][old_state["E"]].remove(item)
    return new_state

ideal_state = gen_ideal_state(initial_state)

def try_move(states):
    current_state = states[len(states)-1]
    if len(states) > 11:
        return
    for combo in get_possible_item_combos(current_state):
        for floor in get_possible_floors(current_state):
            new_state = gen_new_state(current_state, floor, combo)
            print len(states), new_state
            if is_state_identical(new_state, ideal_state):
                print "Neato Burrito. Reached the end in %d steps." % len(states)
            if is_state_valid(new_state, states):
                new_states = states[:]
                new_states.append(new_state)
                try_move(new_states)

try_move([initial_state])

#print(initial_state["E"])
#for floor in range(0, len(initial_state["floors"])):
#    print floor, initial_state["floors"][floor]
#print get_possible_item_combos(initial_state)
#
#print(ideal_state["E"])
#for floor in range(0, len(ideal_state["floors"])):
#    print floor, ideal_state["floors"][floor]
#print is_state_identical(ideal_state, initial_state)
#print is_state_identical(initial_state, initial_state)
