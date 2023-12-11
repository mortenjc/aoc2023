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

    while True:
        W.append(r)
        tmp = [r[i+1] - r[i] for i in range(len(r)-1)]
        r = tmp
        if all([x == 0 for x in tmp]):
            pa = 0
            for l2 in W[::-1]:
                S1 += l2[-1]
                pb = l2[0]
                pa = pb - pa
            S2 += pa
            break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
