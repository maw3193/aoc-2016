#!/usr/bin/python

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-07")
parser.add_argument("input_file")
args = parser.parse_args()

def find_abba(s):
    for i in range(0, len(s) - 3):
        if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
            return True
    return False

def address_is_valid(address):
    for bracketed in address["bracketed"]:
        if find_abba(bracketed):
            return False
    for unbracketed in address["unbracketed"]:
        if find_abba(unbracketed):
            return True
    return False

addresses = []

def parse_address(s):
    address = {"bracketed": [], "unbracketed": []}
    bracketed_pattern = r"\[(\w+)\]"
    unbracketed_start = r"^(\w+)\["
    unbracketed_mid = r"\](\w+)\["
    unbracketed_end = r"\](\w+)$"
    address["bracketed"] += re.findall(bracketed_pattern, s)
    address["unbracketed"] += re.findall(unbracketed_start, s)
    address["unbracketed"] += re.findall(unbracketed_mid, s)
    address["unbracketed"] += re.findall(unbracketed_end, s)
    print(address)
    return address

with open(args.input_file, "r") as f:
    pattern = r"(\w+)\[(\w+)\](\w+)"
    for line in f:
        addresses.append(parse_address(line))


valid_addresses = 0
for address in addresses:
    if address_is_valid(address):
        valid_addresses += 1
print(valid_addresses)
