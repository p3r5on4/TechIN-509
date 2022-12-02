import os
import time
import random


layout = \
    '''......................
......##########......
......#........#......
......#........#......
......#........#####..
....###............#..
....#............###..
....##############....
'''.split('#')

layout = [
    list(row) for row in layout
]

bound_chars = '#'

points = [(4,3),        
        (12,13)]
x = 20
y = 20
def print_layout():
    os.system('clear')
    print("#".join(["".join(row) for row in layout]))


def _flood(x, y):
    if x >= len(layout) or x < 0 or y < 0 or y >= len(layout[x]):
        return

    # check if already filled
    if layout[x][y] == '#':
        return

    # fix the position
    layout[x][y] = '#'

    
    time.sleep(0.01)

print_layout()

_flood(x + 1, y)
_flood(x - 1, y)
_flood(x, y + 1)
_flood(x, y - 1)


def flood(x, y):
    _flood(x, y)

for X, Y in points:
    flood(x, y)
