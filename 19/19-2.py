#!/usr/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import argparse, sys, math

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

def take_presents(elves, num_elves):
    remaining_elves = num_elves
    current_elf = elves.head.next
    # opposite elf also exists, half-way across
    opposite_elf = elves.head.next
    for n in range(int(math.floor(num_elves / 2))):
        opposite_elf = opposite_elf.next

    # When the number of elves left is odd, skip on in the next iteration.
    while remaining_elves > 1:
        print "%d elves left" % remaining_elves
        # Give opposite elf's presents to current elf
        current_elf.data[1] += opposite_elf.data[1]

        # Eliminate opposite elf
        elves.remove(opposite_elf)
        # Move opposite elf 1 or 2 elves along
        skip_steps = 1
        if remaining_elves % 2 == 1:
            skip_steps += 1
        for s in range(skip_steps):
            if opposite_elf.next == elves.head:
                opposite_elf = opposite_elf.next.next
            else:
                opposite_elf = opposite_elf.next

        # Move current elf
        if current_elf.next == elves.head:
            current_elf = current_elf.next.next
        else:
            current_elf = current_elf.next

        # Decrement elf counter
        remaining_elves -= 1

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

take_presents(elves, num_elves)
# Print what each elf has
print_elves(elves)
#inspect_linked_list(elves)
