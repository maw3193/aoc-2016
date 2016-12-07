#!/usr/bin/python

import argparse, sys, re

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-07")
parser.add_argument("input_file")
args = parser.parse_args()

def find_abas(s):
    abas = []
    for i in range(0, len(s) - 2):
        if s[i] != s[i+1] and s [i] == s[i+2]:
            abas.append(s[i:i+3])

    if len(abas) > 0:
        return abas
    else:
        return False

def get_bab(aba):
    return aba[1]+aba[0]+aba[1]

def address_is_valid(address):
    all_abas = []
    for unbracketed in address["unbracketed"]:
        abas = find_abas(unbracketed)
        if abas:
            all_abas += abas

    if len(all_abas) == 0:
        return False

    for bracketed in address["bracketed"]:
        for aba in all_abas:
            if get_bab(aba) in bracketed:
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
