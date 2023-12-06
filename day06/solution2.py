#!/usr/local/bin/python3

import sys
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 1
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

print(lines[0].split())
dur = int(''.join(lines[0].split(':')[1].split()))
dis = int(''.join(lines[1].split(':')[1].split()))

print(dur, dis)


R = dur
D = dis
n = 0
for d in range(R):
    hold = d
    rem = R - d
    dist = hold * rem
    if dist > D:
        n+=1
S1 *= n





print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
