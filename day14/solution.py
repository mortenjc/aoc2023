#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[x for x in line] for line in lines]


def rotate(G):
    R = len(G)
    C = len(G[0])
    NG = [['?' for x in range(R) ] for l in range(C)]
    assert R == len(NG[0])
    assert C == len(G)
    for r in range(R):
        for c in range(C):
            NG[c][R-r-1] = G[r][c]
    return NG



def sliden(G):
    R = len(G)
    C = len(G[0])
    dir = (-1,0)  # n, w, s, e
    rocks = []
    for r in range(C):
        for c in range(C):
            if G[r][c] == 'O':
                rocks.append((r,c))
    rocks = sorted(rocks, reverse=True)

    while rocks:
        rock = rocks.pop()
        #print(rock)
        rr, cc = dir
        r, c = rock
        nr = r + rr
        nc = c + cc
        #print(f'testing rock {r},{c}')
        while nr >= 0 and nr < R and nc >= 0 and nc < C:
            if G[nr][nc] != '.':
                break
            #print(f'move rock from {r},{c} to {nr},{nc}')
            G[nr][nc] = 'O'
            G[r][c] = '.'
            r += rr
            c += cc
            nr = r + rr
            nc = c + cc
    return G


def score(G):
    s = 0
    R = len(G)
    for i in range(R):
        s += G[i].count('O') * (R-i)
    return s


def printg(G):
    for r in G:
        print(''.join(r))


for part in [1,2]:
    if part == 1:
            G = [[x for x in line] for line in lines]
            S1 = score(sliden(G))

def gstr(G):
    str = ''
    for r in G:
        str += ''.join(r)
    return str

t = 0
DG = {}
scores = []
rep = 0
tgt = 1000000000
first = True
while t < tgt:
    key = gstr(G)
    for r in range(4):
        G = sliden(G)
        G = rotate(G)

    t += 1
    sc = score(G)
    if t > 100:
        if key in DG and first:
            first = False
            rep = len(scores)
            #print('t',t, 'scores', scores, 'rep', rep)
            #print('advance by', tgt - t - rep)
            #t += ((tgt - t) - rep)
            #t += (tgt - rep)%rep
            n = (tgt - t)//rep
            t += n*rep
            # while t < tgt - rep:
            #      t += rep
        else:
            scores.append(sc)
            DG[key] = sc

        print('t',t,'score',sc)
S2 = sc



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
