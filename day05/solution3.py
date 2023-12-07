#!/usr/local/bin/python3

import sys
from collections import defaultdict
from intervals import IntInterval

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    entries = ((fin.read().strip()).split('\n\n'))

seeds = list(map(int, entries[0].split(':')[1:][0].split()))
print(seeds)

SR=[] # seed ranges
for i in range(len(seeds)//2):
    start = seeds[2*i]
    length = seeds[2*i+1]
    SR.append([start, start + length])
print(SR)

maps = entries[1:]
print(maps)
MP = []
for m in maps:
    T = []
    t = m.split('\n')[1:]
    for f in t:
        dest, src, r = list(map(int,f.split()))
        T.append([dest, src, r])
    MP.append(T)

print(MP)


A = SR
for step in range(len(MP)):
    print(f'== step {step} ==')
    for r in A:
        for t in MP:
        print(f'matching {r} against {t}')



#


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
