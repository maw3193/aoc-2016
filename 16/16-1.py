#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-16")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()


def generate_data(text, length):
    append_s = ""
    for c in text:
        if c == "0":
            append_s = "1" + append_s
        else:
            append_s = "0" + append_s
    new_data = text + "0" + append_s
    if len(new_data) == length:
        return new_data
    elif len(new_data) > length:
        return new_data[:length]
    else:
        return generate_data(new_data, length)

def checksum(data):
    sum_str = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i+1]:
            sum_str += "1"
        else:
            sum_str += "0"
    if len(sum_str) % 2 != 0:
        return sum_str
    else:
        return checksum(sum_str)

disk_length = 272
#disk_length = 20
with open(args.input, "r") as f:
    for line in f:
        data = generate_data(line.strip(), disk_length)
        s = checksum(data)
        print data, s
