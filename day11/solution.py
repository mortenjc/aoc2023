#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[c for c in l] for l in lines]

def columns(m, i):
    return [x[i] for x in m]


for part in [1,2]:
    R = len(G)
    C = len(G[0])
    gal = {}
    n = 0
    rr = 0
    if part == 1:
        offset = 1
    else:
        offset =999999

    for r in range(R):
        # adjust r
        if G[r].count('.') == R:
            rr += offset
        cc = 0
        for c in range(C):
            if G[r][c] == '#':
                gal[n] = (r+rr, c+cc)
                n += 1
            # adjust c
            if columns(G,c).count('.') == R:
                cc += offset


    # distances
    for g1 in range(len(gal)-1):
        for g2 in range(g1 + 1, len(gal)):
            dist = abs(gal[g1][0]- gal[g2][0]) + abs(gal[g1][1]- gal[g2][1])
            if part == 1:
                S1 += int(dist)
            else:
                S2 += int(dist)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
