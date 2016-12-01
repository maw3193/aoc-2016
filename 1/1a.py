#!/usr/bin/python

import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="The file containing input data for this challenge")
args = parser.parse_args()

def walk(position, direction):
    newpos = {}
    turn = direction[0]
    steps = int(direction[1:])
    if turn == 'L':
        newpos['facing'] = (position['facing'] - 1) % 4
    elif turn == 'R':
        newpos['facing'] = (position['facing'] + 1) % 4
    else:
        sys.exit("Unexpected facing argument")

    if newpos['facing'] == 0:
        newpos['x'] = position['x']
        newpos['y'] = position['y'] - steps
    elif newpos['facing'] == 1:
        newpos['x'] = position['x'] + steps
        newpos['y'] = position['y']
    elif newpos['facing'] == 2:
        newpos['x'] = position['x']
        newpos['y'] = position['y'] + steps
    elif newpos['facing'] == 3:
        newpos['x'] = position['x'] - steps
        newpos['y'] = position['y']
    else:
        sys.exit('Unexpected facing value %d' % newpos['facing'])

    return newpos


# facing is numerically coded for 0=N, 1=E, 2=S, 3=W
position = {'x': 0, 'y': 0, 'facing': 0}
with open(args.input_file, 'r') as f:
    # The file is one big line, and isn't huge. Don't bother splitting.
    data = f.read()
    for direction in data.split(', '):
        position = walk(position, direction)

    print(position)
    distance = abs(position['x']) + abs(position['y'])
    print(distance)

