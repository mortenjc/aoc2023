#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict

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

Q = deque()
V = defaultdict(set)
#         d  r  c  vr  vc
Q.append((0, 0, 1, 0, 1))
SEEN = set()
while Q:
    d, r, c, vr, vc = Q.popleft()
    if (r,c) in SEEN:
        continue

    if r == R-1 and c == C-2:
        V[(r,c)].add((vr, vc, d))
        V[(vr,vc)].add((r, c, d))

    SEEN.add((r, c))

    f = 0
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        rr = r + dr
        cc = c + dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
            f +=1
    if f == 3:
        V[(vr,vc)].add((r,c,d))
        V[(r,c)].add((vr,vc,d))
        print(f'added vertex', vr, vc, '->r', r,c, 'dist', d)
        vr = r
        vc = c
        d = -1
    else:
        pass
        #print('move forward to', rr, cc, d)

    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        rr = r + dr
        cc = c + dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
            Q.append((d+1, rr, cc, vr, vc))


print(V)
# Now to DFS

Q = deque()
# edge   r  c  d
Q.push((0, 1, 0, []))
while Q:
    r, c, d, seen = Q.popleft()
    print(f'pop ({r},{c}, cost {d}, {seen})')

    if r == R-1 and c == C-2:
        print('goal', r, c, d)
        continue

    A = [s for s in seen]
    A.append((r,c))
    A = list(set(A))

    for nr, nc, cost in V[(r,c)]:
        if (nr, nc) in A:
            continue
        Q.append((nr, nc, d + cost, A))






print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
