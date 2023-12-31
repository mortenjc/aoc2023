#!/usr/local/bin/python3

from collections import defaultdict

import sys

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

print(MODS)
print(DST)
print(IN)
print(TYPE)

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


Q = []
pc = defaultdict(int)

for i in range(1000):
    Q.append(('button', 'broadcaster', 0))
    while Q:
        src, dest, val = Q.pop(0)
        print(f'{src} -{vals[val]}-> {dest}')
        pc[val] += 1

        dtype = TYPE[dest]
        if dtype == '%':
            if val == 1:
                continue
            STATE[dest] = (STATE[dest] + 1)%2
            newval = STATE[dest]
            #print(f'update ff, newval {newval}')

        elif dtype == '&':
            MEM[dest][src] = val
            ret = remember(dest)
            if ret:
                newval = 0
            else:
                newval = 1
            print(f'   update conj, new val {newval}')
        else:
            newval = val
            #print(f'broadcast, newval {newval}')

        for t in DST[dest]:
            Q.append((dest, t, newval))

print(pc[0], pc[1])
S1 = pc[0] * pc[1]


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
