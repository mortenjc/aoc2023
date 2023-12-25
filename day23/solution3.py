#!/usr/local/bin/python3

from collections import deque

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

dirs = [(1,0), (0,-1), (-1,0), (0,1)]


G= [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

r, c = (0, 1)

assert G[r][c] == '.'
assert G[R-1][C-2] == '.'


N = []

for r in range(R):
    for c in range(C):
        if G[r][c] == '#':
            continue
        print('testing', r, c)
        count = 0
        for dr, dc in dirs:
            if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc] != '#':
                print(r+dr, c+dc , 'is good')
                count +=1
        if count == 3:
            N.append((r,c))

# Build vertices
#TBD




print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
