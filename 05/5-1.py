#!/usr/bin/python

import argparse, sys, md5

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-05")
parser.add_argument("input_file")
args = parser.parse_args()

with open(args.input_file, "r") as f:
    for line in f:
        digits_found = 0
        index = 0
        digits = ""
        while digits_found < 8:
            digest = md5.new(line[:-1] + str(index)).hexdigest()
            if digest.startswith("00000"):
                digits += digest[5]
                digits_found += 1
            index += 1
        print(digits)
