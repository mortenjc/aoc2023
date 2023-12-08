#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    dir, rest = ((fin.read().strip()).split('\n\n'))

rest = rest.split('\n')


M = {}
for l in rest:
    node, pair = l.split('=')
    node=node[:-1]
    pair = pair.split(',')
    print(pair)
    M[node] = (pair[0][2:], pair[1][1:-1])

print(M)

start='AAA'
nsteps = 0
print(M[start])
running = True
while running:
    for i in dir:
        if i == 'L':
            start = M[start][0]
        else:
            start = M[start][1]
        nsteps += 1
        print(start)
        if start == 'ZZZ':
            running = False
            break
print(nsteps)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
