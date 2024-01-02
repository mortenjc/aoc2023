#!/usr/local/bin/python3

from collections import defaultdict

import sys

from math import lcm

def printg(G):
    for l in G:
        print(''.join(l))

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))



MODS = set()
DST = defaultdict(list)
TYPE = {}
STATE = {}

IN = defaultdict(list)
MEM = defaultdict(dict)

for l in lines:
    src, dstlist = l.split('->')
    src = src.strip()
    dstlist = dstlist.strip()

    if src[0] in ['&', '%']:
        module = src[1:]
        type = src[0]
    else:
        module = src
        type = '-'

    MODS.add(module)
    TYPE[module] = type

    for dst in dstlist.split(','):
        dst = dst.strip()
        if dst not in MODS:
            MODS.add(dst)
            TYPE[dst] = '-'
        DST[module].append(dst)
        IN[dst].append(module)



for module in MODS:
    for src in IN[module]:
        MEM[module][src] = 0

for m in MODS:
    STATE[m] = 0 # all starts in off

# print(MODS)
# print(DST)
# print(IN)
# print(TYPE)

vals = {0:'low', 1:'high'}

def remember(module):
    assert TYPE[module] == '&'
    hi = 0
    lo = 0
    for m in IN[module]:
        if MEM[module][m] == 0:
            lo += 1
        else:
            hi += 1
    assert lo+hi == len(IN[module])
    if hi == len(IN[module]):
        return True
    else:
        return False

watch = {'sh':0, 'mz':0, 'bh':0, 'jf':0}

Q = []
PREV = {}
COUNT = defaultdict(int)
pc = defaultdict(int)
RES = []
for i in range(1, 10**9):
    Q.append(('button', 'broadcaster', 0))
    while Q:
        src, dest, val = Q.pop(0)
        pc[val] += 1

        if val == 0:
            if dest in watch and COUNT[dest] == 2 and dest in PREV:
                print(i, dest, val, PREV[dest], i - PREV[dest])
                RES.append(i - PREV[dest])
            PREV[dest] = i
            COUNT[dest] += 1
        if len(RES) == 4:
            print(lcm(*RES))
            sys.exit(0)


        dtype = TYPE[dest]
        # flipflop
        if dtype == '%':
            if val == 1:
                continue
            STATE[dest] = (STATE[dest] + 1)%2
            newval = STATE[dest]
        # conjunction
        elif dtype == '&':
            MEM[dest][src] = val
            ret = remember(dest)
            if ret:
                newval = 0
            else:
                newval = 1
        # default
        else:
            newval = val

        for t in DST[dest]:
            Q.append((dest, t, newval))

    if i == 1000:
        S1 = pc[0] * pc[1]
        print(pc[0] * pc[1])

    if i % 1000 == 0:
        print(watch)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
