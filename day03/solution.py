#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
# from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
# import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

def findNumber(x, y):
    ch = G[y][x]
    if not ch.isnumeric():
        return -1
    b = 0
    e = 0
    while G[y][x + e].isnumeric():
        e += 1
    while G[y][x - b].isnumeric():
        b += 1
    l = e + b
    return getNumber(x-b-1, y, l)


def getNumber(x, y, l):
    n = 0
    p = 0
    ns = ""
    for i in range(l):
        ch = G[y][x+i]
        ns += ch
    return int(ns)


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= C or y >= R:
        return False
    return True

def isAdjTo(px, py):
    for dx, dy  in [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (1,1), (1,-1), (-1, 1)]:
        x = px + dx
        y = py + dy
        if isValidPos(x, y):
            if G[y][x].isnumeric():
                findNumber(x, y)


def hasAdjacent(x, y, l):
    if  (x-1) >= 0 and G[y][x-1] != '.':
        return True
    if  (x+l) < len(G[0]) and G[y][x+l] != '.':
        return True

    for i in range(l + 2):
        if  (y+1) < R and (x+i-1) >= 0 and (x+i-1) < C and G[y+1][x+i-1] != '.':
            return True
        if  (y-1) >= 0 and (x+i-1) < C and G[y-1][x+i-1] != '.':
            return True
    return False

S1 = 0
S2 = 0


for r in range(R):
    s = 0
    y = r
    for c in range(C):
        ch = G[r][c]
        if s == 0 and ch.isnumeric():
            s = 1
            x = c
            l = 1
            continue
        if s == 0 and not ch.isnumeric():
            continue
        if s == 1 and  ch.isnumeric():
            l += 1
            if c == len(G[0])-1:
                if hasAdjacent(x, y, l):
                    n = getNumber(x,y,l)
                    S1 += n
            continue

        if s == 1 and not ch.isnumeric():
            if hasAdjacent(x, y, l):
                n = getNumber(x,y,l)
                S1 += n
            s = 0
            continue


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
