#!/usr/bin/python

import argparse, sys, re

class Bot:
    def __init__(self, num):
        self.num = num
        self.chips = []
        self.give_low_type = ""
        self.give_low_num = -1
        self.give_high_type = ""
        self.give_high_num = -1
    def __str__(self):
        return "BOT %d: chips: %s low %s %d high %s %d" % (self.num, repr(self.chips), self.give_low_type, self.give_low_num, self.give_high_type, self.give_high_num)

parser = argparse.ArgumentParser(description="Program to solve Advent of Code for 2016-12-10")
parser.add_argument("--input_file", default="input.txt")
args = parser.parse_args()


bots = {}
outputs = {}

def handle_set(value, bot):
    if bot not in bots:
        newbot = Bot(bot)
        newbot.chips.append(value)
        bots[bot] = newbot
    else:
        foundbot = bots[bot]
        if len(foundbot.chips) >= 2:
            sys.exit("Unexpected! Bot already has enough chips!", bot, foundbot.chips, value)
        foundbot.chips.append(value)

def handle_give_rule(bot, lowtype, lownum, hightype, highnum):
    if bot not in bots:
        b = Bot(bot)
        bots[bot] = b
    else:
        b = bots[bot]
    if b.give_low_type != "" or b.give_high_type != "":
        sys.exit("Unexpected! Overriding bot give rules!", bot, lowtype, lownum, hightype, highnum)
    b.give_low_type = lowtype
    b.give_low_num = lownum
    b.give_high_type = hightype
    b.give_high_num = highnum

def parse_rule(line):
    m = re.match("value (\d+) goes to bot (\d+)", line)
    if m:
        handle_set(int(m.group(1)), int(m.group(2)))
        return
    m = re.match("bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line)
    if m:
        handle_give_rule(int(m.group(1)), m.group(2), int(m.group(3)),
                         m.group(4), int(m.group(5)))
        return
    sys.exit("Unhandled line '%s' while parsing!" % line)

def give_chips(bot):
    if bot.give_low_type == "":
        # No rules given yet. Try again later.
        return False
    bot.chips = sorted(bot.chips)

    # Bodge for AOC answer!
    if bot.chips[0] == 17 and bot.chips[1] == 61:
        print(bot.num)
    # END BODGE

    # Bots don't exist yet, try again later.
    if bot.give_low_type == "bot" and bot.give_low_num not in bots:
            return False
    if bot.give_high_type == "bot" and bot.give_high_num not in bots:
            return False

    if bot.give_low_type == "bot":
        bots[bot.give_low_num].chips.append(bot.chips[0])
    elif bot.give_low_type == "output":
        if bot.give_low_num not in outputs:
            outputs[bot.give_low_num] = [bot.chips[0]]
        else:
            outputs[bot.give_low_num].append(bot.chips[0])
    else:
        sys.exit("Bot %d giving to unexpected type '%s'" % (bot.num, bot.give_low_type))

    if bot.give_high_type == "bot":
        bots[bot.give_high_num].chips.append(bot.chips[1])
    elif bot.give_high_type == "output":
        if bot.give_high_num not in outputs:
            outputs[bot.give_high_num] = [bot.chips[1]]
        else:
            outputs[bot.give_high_num].append(bot.chips[1])
    else:
        sys.exit("Bot %d giving to unexpected type '%s'" % (bot.num, bot.give_high_type))
    bot.chips = []
    return True

def process_pending():
    things_happened = False
    for bot in bots.itervalues():
        if len(bot.chips) == 2:
            things_happened = give_chips(bot)
        elif len(bot.chips) > 2:
            sys.exit("Unexpected! Bot %d has more than 2 chips!" % bot)
    return things_happened

with open(args.input_file, "r") as f:
    for line in f:
        parse_rule(line)
        while process_pending():
            True

#for bot in bots.itervalues():
#    print bot
#for num, output in outputs.iteritems():
#    print(num, output)

print(outputs[0][0] * outputs[1][0] * outputs[2][0])
