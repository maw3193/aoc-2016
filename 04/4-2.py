#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-04")
parser.add_argument("input_file")
args = parser.parse_args()



def decrypt_name(room):
    shifts = int(room["number"]) % 26
    newwords = []
    for word in room["letters"].split("-"):
        newword = ""
        for letter in word:
            oldval = ord(letter)
            newval = oldval + shifts
            if newval > ord("z"):
                newval -= 26
            newword += chr(newval)
        newwords.append(newword)
    print(" ".join(newwords), room["number"])

def parse_room(line):
    split = line.split("-")
    letters = "-".join(split[:-1])
    split2 = split[-1].split("[")
    number = split2[0]
    checksum = split2[1][:-2]
    return {"letters":letters, "number":number, "checksum":checksum}

room_sum = 0
with open(args.input_file, "r") as f:
    for line in f:
        room = parse_room(line)
        decrypt_name(room)
