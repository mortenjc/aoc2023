#!/usr/local/bin/python3

from collections import deque

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


uni = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
dirs = [(1,0), (0,-1), (-1,0), (0,1)]


G= [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

r, c = (0, 1)

assert G[r][c] == '.'
assert G[R-1][C-2] == '.'

Q = deque()
Q.append((r,c, 0, set()))


opt = set()
while Q:
    r, c, steps, seen = Q.popleft()
    if (r, c, steps) in opt:
        continue
    if not (0<=r<R and 0<=c<C):
        continue
    if (r,c) in seen or G[r][c] == '#':
        continue

    if (r,c) == (R-1, C-2):
        S1 = max(S1, steps)
        print('##', r,c, steps, 'max', S1)
        continue

    if G[r][c] in ['>', '<', 'v', '^']:
        dr, dc = uni[G[r][c]]
        nr = r + dr
        nc = c + dc
        new_seen = seen | set([(r,c)])
        opt.add((r, c, steps))
        Q.append((nr, nc, steps+1, new_seen))
    else:
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            opt.add((r, c, steps))
            new_seen = seen | set([(r, c)])
            Q.append((nr, nc, steps+1, new_seen))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
