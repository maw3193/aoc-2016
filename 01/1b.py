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

def check_been_here_before(positions, newpos):
    print(newpos['x'], newpos['y'])
    for pos in positions:
        if (pos['x'] == newpos['x']) and (pos['y'] == newpos['y']):
            print("I've been here before!")
            print(pos)
            distance = abs(pos['x']) + abs(pos['y'])
            print("distance: %d" % distance)
            sys.exit(0)


def fill_positions(positions, oldpos, newpos):
    # No diagonals, so iterating over the range in X and range in Y
    # will cover all possible movement.

    # X-axis
    if newpos['x'] > oldpos['x']:
        for xpos in range(oldpos['x'], newpos['x'])[1:]:
            interpos = {'x':xpos, 'y':oldpos['y']}
            check_been_here_before(positions, interpos)
            positions.append(interpos)
    elif newpos['x'] < oldpos['x']:
        for xpos in range(oldpos['x'], newpos['x'], -1)[1:]:
            interpos = {'x':xpos, 'y':oldpos['y']}
            check_been_here_before(positions, interpos)
            positions.append(interpos)

    # Y-axis
    if newpos['y'] > oldpos['y']:
        for ypos in range(oldpos['y'], newpos['y'])[1:]:
            interpos = {'x':newpos['x'], 'y':ypos}
            check_been_here_before(positions, interpos)
            positions.append(interpos)
    elif newpos['y'] < oldpos['y']:
        for ypos in range(oldpos['y'], newpos['y'], -1)[1:]:
            interpos = {'x':newpos['x'], 'y':ypos}
            check_been_here_before(positions, interpos)
            positions.append(interpos)

# facing is numerically coded for 0=N, 1=E, 2=S, 3=W
position = {'x': 0, 'y': 0, 'facing': 0}
positions = []
positions.append({'x':position['x'], 'y':position['y']})
with open(args.input_file, 'r') as f:
    # The file is one big line, and isn't huge. Don't bother splitting.
    data = f.read()
    for direction in data.split(', '):
        newpos = walk(position, direction)
        fill_positions(positions, position, newpos)
        position = newpos
