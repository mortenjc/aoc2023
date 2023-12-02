#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
# from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
# import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

S1 = 0
S2 = 0

#only 12 red cubes, 13 green cubes, and 14 blue cubes
max = {'red':12, 'green':13, 'blue':14}

for l in lines:
    print(l)
    game = l.split(':')[0]
    gameid = int(game.split()[1])

    draws = l.split(':')[1:][0].split(';')
    failed = False
    maxc = {'red':0, 'green':0, 'blue':0}
    for draw in draws:
        colors = draw.split(',')
        for c in colors:
            counts = c.split()
            cn = int(counts[0])
            cname = counts[1]
            if cn > maxc[cname]:
                maxc[cname] = cn
            if cn > max[counts[1]]:
                failed = True
                print(f'failed on {cname} ({cn}) > {max[cname]}')

    S2 += maxc['red'] * maxc['blue'] * maxc['green']
    if not failed:
        S1 += gameid

    print()


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
