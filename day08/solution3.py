#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools
import math


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    dirs, rest = ((fin.read().strip()).split('\n\n'))

GO = {}
GO['L'] = {}
GO['R'] = {}
S = []
for l in rest.split('\n'):
    key, d  = l.split('=')
    key = key[:-1]
    if key[-1] == 'A':
        S.append(key)
    L = d.split(',')[0][2:]
    R = d.split(',')[1][1:-1]

    GO['L'][key] = L
    GO['R'][key] = R

print(S)


N = []
for s in S:
    n = 0
    start = s
    while True:
        c = dirs[n%len(dirs)]
        n += 1

        start = GO[c][start]
        if start[-1] == 'Z':
            N.append(n)
            break

S2 = math.lcm(*N)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
