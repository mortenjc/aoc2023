#!/usr/local/bin/python3

import sys
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


mp = defaultdict(lambda:-1)

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n\n'))


seeds = lines[0].split(':')[1].split()
maps = lines[1:]

C = []
for i, m in enumerate(maps):
    C.append(defaultdict(lambda:-1))
    ranges = m.split('\n')[1:]
    for r in ranges:
        d, s, l = map(int, r.split())
        #print(s, d, l)
        for j in range(l):
            n = s + j
            n2 = d + j
            C[i][n] = n2
    print(i, C[i])
    #print('...')



src = 79
def getfinal(C, n):
    src = n
    for i in range(len(C)):
        if C[i][src] == -1:
            src = src
        else:
            src = C[i][src]
    return src

min = 10000000000
for sds in seeds:
    sds = int(sds)
    r = getfinal(C, sds)
    if r < min:
        min = r
print(min)




print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
