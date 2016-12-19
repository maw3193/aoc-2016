#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys

class Link:
    def __init__(self, data, n, p):
        self.data = data
        self.next = n
        self.prev = p

class CircularLinkedList:
    def __init__(self):
        self.head = Link(None, None, None)
        self.head.prev = self.head
        self.head.next = self.head
    def add_at(self, data, at):
        new_link = Link(data, at.next, at)
        at.next.prev = new_link
        at.next = new_link
    def add(self, data):
        self.add_at(data, self.head)
    def remove(self, link):
        link.prev.next = link.next
        link.next.prev = link.prev
    def __contains__(self, data):
        current = self.head.next
        while current != self.head:
            if current_data == data:
                return True
        return False

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-19")
parser.add_argument("--input", default="input.txt")
args = parser.parse_args()

num_elves = 0

# Get Data
with open(args.input, "r") as f:
    num_elves = int(f.read().strip())

# Create a circular, doubly-linked list of elves
elves = CircularLinkedList()
for n in range(num_elves):
    elves.add_at([n+1, 1], elves.head.prev)

def print_elves(elves):
    ptr = elves.head.next
    while ptr != elves.head:
        print ptr.data
        ptr = ptr.next

def inspect_linked_list(elves):
    print "head=", elves.head
    print "head.prev=", elves.head.prev
    print "head.next=", elves.head.next
    ptr = elves.head.next
    while ptr != elves.head:
        print "link=", ptr
        print "link.prev=", ptr.prev
        print "link.next=", ptr.next
        print "link.data=", ptr.data
        ptr = ptr.next

def take_presents(elves):
    current_elf = elves.head.next
    while elves.head.next != elves.head.prev:
        if current_elf == elves.head:
            current_elf = current_elf.next
            continue
        if current_elf.data[1] == 0:
            print "Removing loser elf %d" % current_elf.data[0]
            elves.remove(current_elf)
            current_elf = current_elf.next
            continue
        if current_elf.next == elves.head:
            next_elf = current_elf.next.next
        else:
            next_elf = current_elf.next
        #print_elves(elves)
        current_elf.data[1] += next_elf.data[1]
        #print "Elf %d took %d presents from elf %d" % (current_elf.data[0], next_elf.data[1], next_elf.data[0])
        next_elf.data[1] = 0
        current_elf = next_elf

take_presents(elves)
# Print what each elf has
print_elves(elves)
#inspect_linked_list(elves)
