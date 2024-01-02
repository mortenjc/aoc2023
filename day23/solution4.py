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


SEEN = set()
V = []
start = (0,0)
end = (0,0)
for c in range(C):
    if G[R-1][c] == '.':
        end = (R-1,c)
        V.append(end)
    if G[0][c] == '.':
        start = (0,c)
        V.append(start)

for r in range(R):
    for c in range(C):
        if G[r][c] == '#':
            continue
        f = 0
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
                f +=1
        if f > 2:
            V.append((r,c))


E = {}
for rv, cv in V:
    E[(rv,cv)] = []
    Q = deque()
    Q.append((rv, cv, 0))
    SEEN = set()
    while Q:
        r, c, d = Q.popleft()
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        if (r,c) in V and (r,c) != (rv, cv):
            E[(rv,cv)].append((r,c,d))
            continue
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
                Q.append((rr,cc, d+1))

print(V)
print(E)


# Now to DFS
ans = 0
SEEN = [[False for _ in range(C)] for _ in range(R)]

def dfs(v, d):
    #print('dfs', v, d)
    global ans
    r, c = v
    if SEEN[r][c]:
        return

    SEEN[r][c] = True

    if r == R-1 and c == C-2:
        #print('end', ans, d)
        ans = max(ans, d)

    for nr, nc, cost in E[v]:
        #print(f'new path ({r},{c}) -> ({nr},{nc}) cost {d+cost}')
        dfs((nr,nc), d+cost)
    SEEN[r][c] = False



dfs((0,1), 0)

S2 = ans



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
