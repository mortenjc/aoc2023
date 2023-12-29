#!/usr/local/bin/python3

from collections import defaultdict

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


BS = []

for i, l in enumerate(lines):
    A, B = l.split('~')
    be = list(map(int, A.split(',')))
    ed = list(map(int, B.split(',')))
    dir = [a-b for a,b in zip(ed,be)]
    l = max(dir)
    dir = [a//l if l != 0 else 0 for a in dir]


    B = []
    for j in range(l+1):
        pt = tuple([a + j*b for a,b in zip(be, dir)])
        B.append(pt)
    BS.append(B)


def moved(blocks):
    moved = set()
    SEEN = set()
    for B in blocks:
        for (x,y,z) in B:
            SEEN.add((x,y,z))

    i = 0
    while True:
        any = False
        for j, B in enumerate(blocks):
            for (x,y,z) in B:
                if z<2 or ((x,y,z-1) in SEEN and (x,y,z-1) not in B):
                    break
            else:
                moved.add(j)
                any = True
                for (x,y,z) in blocks[j]:
                    SEEN.remove((x,y,z))
                    SEEN.add((x,y,z-1))
                blocks[j] = [(x, y, z-1) for x,y,z in B]

        if not any:
            return i, len(moved), blocks
        i += 1


res, mv, NA = moved([b for b in BS])
if res != 0:
    print('blocks settled after', res, 'iterations')

for i, B in enumerate(NA):
    res, mv, _ = moved([b for b in NA if b != B])
    S2 += mv
    if res == 0:
        S1 += 1


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
