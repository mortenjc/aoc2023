#!/usr/local/bin/python3

import sys
from collections import defaultdict
from intervals import IntInterval

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


mp = defaultdict(lambda:-1)

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n\n'))


seeds = map(int, lines[0].split(':')[1].split())
maps = lines[1:]

C = []
for i, m in enumerate(maps):
    D = []
    ranges = m.split('\n')[1:]
    for r in ranges:
        d, s, l = map(int, r.split())
        itv = IntInterval.closed(s, s+l -1)
        D.append([itv, d-s])
    C.append(D)
    print(i, C[i])
    print('...')



def getfinal(n):
    src = n
    for i in range(len(C)):
        res = src
        found = False
        for j in range(len(C[i])):
            itv, diff = C[i][j]
            if src in itv:
                found = True
                src = src + diff
                break
        if not found:
            src = src
    return src

res = []
for n in seeds:
    res.append(getfinal(n))
print(min(res))



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
