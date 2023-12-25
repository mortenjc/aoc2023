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

skipped = set()
#opt = set()
while Q:
    r, c, steps, seen = Q.popleft()
    # prune
    # if (r, c, steps) in opt:
    #     continue
    if not (0<=r<R and 0<=c<C):
        continue
    if (r,c) in seen or G[r][c] == '#':
        continue

    # goal
    if (r,c) == (R-1, C-2):
        S1 = max(S1, steps)
        print('##', r,c, steps, 'max', S1)
        continue

    # search

    #opt.add((r, c, steps))
    new_seen = seen | set([(r, c)])
    for dr, dc in dirs:
        s = ''
        #print('r,c', r, c,'testing dir', dr, dc)
        nr = r
        nc = c
        t = 0
        s += f'({nr},{nc}) '
        while 0<=nr+dr<R and 0<=nc+dc<C:
            if G[nr+dr][nc+dc] == '#':
                break
            nr += dr
            nc += dc
            t += 1
            s += f'({nr},{nc}) '
        if t!= 0:
            print(f'compressed ({r},{c}) to ({nr},{nc}) in {t} steps')
            print(s)
            Q.append((nr, nc, steps+t, new_seen))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
