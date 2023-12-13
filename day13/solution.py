#!/usr/local/bin/python3

import sys
import copy


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    groups = ((fin.read().strip()).split('\n\n'))


def col(G, i):
    return [x[i] for x in G]

def draw(G, refl, horiz):
    for j, r in enumerate(G):
        s = ''
        for i, c in enumerate(r):
            if c=='#':
                s += '\u25a0'
                #s += '#'
            else:
                s += ' '
            if not horiz:
                if i in refl:
                    s+= '|'
        print(s)
        if horiz:
            if j in refl:
                print('-'*len(G[0]))


def reflect(G):
    RL = []
    R = len(G)
    refl = 0
    for i in range(R-1):
        r1 = G[i]
        r2 = G[i+1]
        if r1 == r2:
            for j in range(min(R-i-1, i+1)):
                if G[i-j] != G[i+j+1]:
                    break
            else:
                RL.append(i)
                refl += (i+1)
    return refl, RL



def refl(G):
    G1 = [[c for c in l] for l in G.split('\n')]
    G1T = [col(G1, i)[::-1] for i in range(len(G1[0]))]

    countl, RL = reflect(G1T)
    #draw(G1, RL, False)
    counta, RA = reflect(G1)
    #draw(G1, RA, True)
    return countl, counta, RL, RA


for ng, G in enumerate(groups):
    RR = len(G.split('\n'))
    CC = len(G.split('\n')[0])

    cl, ca, rl, ra = refl(G)
    S1 += cl + 100*ca

    done = False
    for r in range(RR):
        if done:
            continue
        for c in range(CC):
            C = [[ch for ch in l] for l in G.split('\n')]
            if C[r][c] == '.':
                C[r][c] = '#'
            else:
                C[r][c] ='.'
            NEWC = []
            for l in C:
                NEWC.append(''.join(l))
            C = '\n'.join(NEWC)

            cl2, ca2, rl2, ra2 = refl(C)
            ncl2 = 0
            nca2 = 0
            if (rl2 != rl and rl2 != []) or (ra2 != ra and ra2 != []):
                for q in rl2:
                    if q not in rl:
                        ncl2 += q + 1
                for p in ra2:
                    if p not in ra:
                        nca2 += p + 1
                done = True
                break
    S2 += ncl2
    S2 += nca2 * 100


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
