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

G = [[int(x) for x in l] for l in lines]
R = len(G)
C = len(G[0])


dirs = [0, 1 ,2 , 3] # left, down, right, up
dirval = [(0,-1), (1,0), (0,1), (-1,0)]


def solve(part2):
    Q = []
    D = {}
    best = 1e9
    Q.append((0, 0, 0, 2, 1))
    Q.append((0, 0, 0, 1, 1))
    while Q:
        cost, r, c, dir, indir = heapq.heappop(Q)

        if (r, c, dir, indir) in D:
            continue

        if r == R-1 and c == C-1:
            best = min(cost, best)

        if part2:
            if r == R-1 and c == C-1:
                if indir < 4:
                    continue

        D[(r, c, dir, indir)] = cost

        for nd in [dir, (dir+1)%4, (dir-1)%4]:
            dr = dirval[nd][0]
            dc = dirval[nd][1]

            nr = r + dr
            nc = c + dc
            if not (0<= nr < R and 0<= nc < C):
                continue

            newcost = cost + G[nr][nc]
            new_indir = (1 if nd != dir else indir+1)

            isvalid1 = (new_indir <= 3)
            isvalid2 = ((new_indir <= 10 and dir == nd) or (indir >= 4 and dir != nd ))

            isvalid = (isvalid2 if part2 else isvalid1)

            if isvalid:
                heapq.heappush(Q, (newcost, nr, nc, nd, new_indir))

    return best

S1 = solve(False)
S2 = solve(True)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
