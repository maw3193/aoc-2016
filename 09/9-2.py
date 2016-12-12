#!/usr/bin/python

import argparse, sys, re

def get_decrypted_length(text):
    pos = 0
    length = 0
    # Find any decryption texts
    # Iterate over every match
    while pos < len(text):
        if text[pos] != "(":
            pos += 1
            length += 1
        else:
            match = re.match("\((\d+)x(\d+)\)", text[pos:])
            if not match:
                sys.exit("A '(' exists that isn't encryption in '%s'" % text[pos:])
            covered_chars = int(match.group(1))
            repeat = int(match.group(2))
            start = pos + len(match.group(0))
            end = start + covered_chars
            length += repeat * get_decrypted_length(text[start:end])
            pos += len(match.group(0)) + covered_chars
    return length

while True:
    line = sys.stdin.readline()
    if line:
        print get_decrypted_length(line.strip())
    else:
        break
