#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-04")
parser.add_argument("input_file")
args = parser.parse_args()

def cmp(a, b):
    # Sort left is numbers are bigger
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0
    else:
        sys.exit("Unexpected case in comparison between % and %" % (a, b))

def generate_checksum(room):
    lettersums = {}
    for c in room["letters"]:
        if not c in lettersums:
            lettersums[c] = 1
        else:
            lettersums[c] += 1
    s = sorted(lettersums.iteritems(), cmp)
    checksum = ""
    for n in range(0, 5):
        checksum += s[n][0]
    return checksum

def parse_room(line):
    split = line.split("-")
    letters = "".join(split[:-1])
    split2 = split[-1].split("[")
    number = split2[0]
    checksum = split2[1][:-2]
    return {"letters":letters, "number":number, "checksum":checksum}

room_sum = 0
with open(args.input_file, "r") as f:
    for line in f:
        room = parse_room(line)
        if generate_checksum(room) == room["checksum"]:
            room_sum += int(room["number"])

print(room_sum)
