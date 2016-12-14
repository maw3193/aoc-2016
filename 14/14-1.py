#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, md5
from collections import OrderedDict

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-14")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

salt = 0

keys = set()
triples = OrderedDict() # dict of index to character tripled

with open(args.input, "r") as f:
    salt = f.read().strip()

def get_repeat_chars(text, repeats):
    for i in range(len(text) - repeats + 1):
        c = text[i]
        is_match = True
        for j in range(i+1, i+repeats):
            if text[j] != c:
                is_match = False
                break
        if is_match:
            return c
    return False

index = 0
while len(keys) < 64:
    test_hash = md5.new(salt+str(index)).hexdigest()
    tri = get_repeat_chars(test_hash, 3)
    if tri:
        triples[index] = tri
    quint = get_repeat_chars(test_hash, 5)
    if quint:
        remove_keys = []
        for key, char in triples.iteritems():
            if key < index - 1000:
                remove_keys.append(key)
            elif char == quint and key != index:
                print "Quintuple at %d validates key at %d" % (index, key)
                keys.add(key)
#                if len(keys) == 64:
#                    print "The 64th key is at %d" % key
                remove_keys.append(key)
        for r in remove_keys:
            del triples[r]

    index += 1
