#!/usr/local/bin/python3

import sys
from collections import defaultdict
from intervals import IntInterval

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n\n'))


seeds = list(map(int, lines[0].split(':')[1].split()))

SR=[]
for i in range(len(seeds)//2):
    start = seeds[2*i]
    length = seeds[2*i+1]
    SR.append([IntInterval.closed(start, start+length-1), 0])

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
    #print(i, C[i])
    #print('...')


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


# start
#I = [[IntInterval.closed(2, 12), 0], [IntInterval.closed(2, 12), 0]]
# transforms
#T = [[IntInterval.closed(0, 10), 10], [IntInterval.closed(11, 15), -1], [IntInterval.closed(16, 20), 1]]

def prop(S, T):
    i2 = []
    seen = set()
    for iint in S:
        I = iint[0]
        for i, t in enumerate(T):
            #print(i, I, t[0])
            try:
                newint = I & t[0]
                #print(newint)
                if not (newint, t[1]) in seen:
                    seen.add((newint, t[1]))
                    i2.append([newint, t[1]])
            except:
                #print([I, 0])
                if not (I,0) in seen:
                    seen.add((I, 0))
                    i2.append([I, 0])

    return i2

#print(prop(I,T))

start = SR
for i, T in enumerate(C):
    print(i)
    newstart = prop(start, T)
    print(newstart)
    start = newstart
    print('--')
print()
print(start)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
