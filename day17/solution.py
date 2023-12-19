#!/usr/local/bin/python3

import sys
from collections import deque
import heapq


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


dirs = [0, 1 ,2 , 3] # left, down, right, up
dirval = [(0,-1), (1,0), (0,1), (-1,0)]


Q = []
D = {}
Q.append((0, 0, 0, 2, 1))
Q.append((0, 0, 0, 1, 1))
while Q:
    cost, r, c, dir, indir = heapq.heappop(Q)
    #print(f'{cost=}, ({r=}, {c=}), {dir=}, {indir=}')
    if (r, c, dir, indir) in D:
        continue

    D[(r, c, dir, indir)] = cost

    for nd in [dir, (dir+1)%4, (dir-1)%4]:

        dr = dirval[nd][0]
        dc = dirval[nd][1]

        nr = r + dr
        nc = c + dc
        #print(f'new potential dir: {dir}->{nd} : ({r},{c}) ->({nr},{nc})')
        if not (0<= nr < R and 0<= nc < C):
            continue

        assert nd != (dir + 2)%4
        newcost = cost + G[nr][nc]

        if nd == dir:
            if indir < 3:
                indir += 1
            else:
                continue
        else:
            indir = 1

        #print('newdir', nr, nc, nd, indir)
        heapq.heappush(Q, (newcost, nr, nc, nd, indir))


for r, c, dir, indir in D:
    if r == R-1 and c == C-1:
        print(r, c, dir, indir, D[(r, c, dir, indir)])
#print(D)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
