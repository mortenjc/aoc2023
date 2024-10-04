#!/usr/local/bin/python3

from collections import defaultdict

import sys

def printg(G):
    for l in G:
        print(''.join(l))

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

# Solution for part 1

G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

start = (0,0)
sq = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r, c)
        if G[r][c] != '#':
            sq += 1

print(start, sq)




n = 64

def printg(seen):
    for r in range(R):
        str = ''
        for c in range(C):
            if (r,c, n) in seen:
                str += 'O'
            else:
                str += G[r][c]
        print(str)

MV = [(0,-1), (1,0), (0,1), (-1, 0)]

SEEN = set()
Q = []
Q.append([start[0], start[1], 0])
while Q:
    r, c, steps = Q.pop(0)
    #print('pop', r, c, steps)
    if steps > n:
        continue
    if (r, c, steps) in SEEN:
        continue
    SEEN.add((r,c,steps))

    for d in [0, 1, 2, 3]:
        dr, dc = MV[d]
        if 0<=r+dr<R and 0<=c + dc<C:
            nr = r + dr
            nc = c + dc
            if G[nr][nc] != '#':
                Q.append([nr, nc, steps+1])

print('xxx')

printg(SEEN)

for r,c, st in SEEN:
    #print(r, c, st)
    if st == n:
        #print(r,c)
        S1 +=1

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
