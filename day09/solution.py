#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for l in lines:
    W = []
    r = list(map(int, l.split()))
    W.append(r)
    while True:
        tmp = []
        for i in range(len(r)-1):
            tmp.append(r[i+1]-r[i])
        W.append(tmp)
        r = tmp
        if all([x == 0 for x in tmp]):
            p = 0
            p2a = 0
            for l2 in W[::-1]:
                p += l2[-1]
                p2b = l2[0]
                p2a = p2b - p2a
            S1 += p
            S2 += p2a
            break



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
