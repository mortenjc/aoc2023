#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])


def newdir(r, c, dr, dc):
    ch = G[r][c]
    if ch == '/':
        if dr == 0: # left right
            if dc == 1:
                return (r-1, c, -1 , 0)
            else:
                return (r+1, c, 1, 0)
        if dc == 0: # up down
            if dr == 1:
                return (r, c-1, 0, -1)
            else:
                return (r, c+1, 0, 1)
    elif ch == '\\':
        if dr == 0: # left right
            if dc == 1:
                return (r+1, c, 1 , 0)
            else:
                return (r-1, c, -1, 0)
        if dc == 0: # up down
            if dr == 1:
                return (r, c+1, 0, 1)
            else:
                return (r, c-1, 0, -1)
    else:
        assert False, 'bad reflection'


def printg(G,E):
    for r in range(len(G)):
        s = ''
        for c in range(len(G[0])):
            if E[r][c] == 1:
                s += 'O'
            elif E[r][c] > 1:
                s += '#'
            else:
                s += '.'
        print(s)


def isvalid(r,c):
    return r >=0 and r < R and c >=0 and c < C


def getnewpos(G, BMS):
    NB = []
    for r, c, dr, dc in BMS:
        assert c != -1 and c != C and r != -1 and r != R

        ch = G[r][c]
        if ch == '.' or (ch == '|' and dr != 0) or (ch == '-' and dc != 0):
            if isvalid(r+dr, c+dc):
                NB.append((r+dr, c+dc, dr, dc))
        elif ch == '|':
                nb1 = (r-1, c, -1, 0)
                nb2 = (r+1, c, 1, 0)
                if isvalid(r-1, c):
                    NB.append(nb1)
                if isvalid(r+1, c):
                    NB.append(nb2)
        elif ch == '-':
                nb1 = (r, c-1, 0, -1)
                nb2 = (r, c+1, 0, 1)
                if isvalid(r, c-1):
                    NB.append(nb1)
                if isvalid(r, c+1):
                    NB.append(nb2)
        elif ch == '/' or ch == '\\':
            r, c, dr, dc = newdir(r, c, dr, dc, ch)
            if isvalid(r,c):
                NB.append((r,c,dr,dc))
        else:
            printg(G,E)
            assert False, 'uncaught'
    return NB


def tiles(start):
    seen = set()
    seen2 = set()
    BMS = set()

    BMS.add(start)
    while True:
        if BMS == []:
            break

        for r, c, dr, dc in BMS:
            seen.add((r, c, dr, dc))
            if (r, c, dr, dc) in seen2:
                continue

        NP = getnewpos(G, BMS)
        for np in NP:
            if np in seen:
                seen2.add(np)
            BMS.add(np)

    return len(seen2)



best = 0
for c in range(C):
    start = (0, c, 1, 0)
    best = max(best, tiles(start))
    print(start, best)
    start = (R-1, c, -1, 0)
    best = max(best, tiles(start))
    print(start, best)

for r in range(R):
    start = (r, 0, 0, 1)
    best = max(best, tiles(start))
    print(start, best)
    start = (r, C-1, 0, -1)
    best = max(best, tiles(start))
    print(start, best)

S1 = tiles((0,0,0,1))
S2 = best

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
