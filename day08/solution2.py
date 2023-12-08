#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    dirs, rest = ((fin.read().strip()).split('\n\n'))

rest = rest.split('\n')


M = {}
nodes = []
for l in rest:
    node, pair = l.split('=')
    node=node[:-1]
    nodes.append(node)
    pair = pair.split(',')
    print(pair)
    M[node] = (pair[0][2:], pair[1][1:-1])

print(M)
print(nodes)
print("==============")

start=[]

for n in nodes:
    print(n)
    if n[-1] == 'A':
        start.append(n)

print(start)
print('==============')

S2 = 1
n = 0
lc = defaultdict(int)
running = True
q = len(start)
seen = set()
while running:
    for dir in dirs:
        NewS=[]
        print(n, start)
        assert q == len(start)

        for idx, S in enumerate(start):
            key = str(idx)+dir+S
            if ((key in seen) or S[-1] == 'Z')  and lc[idx] == 0:
                print(f'loop at {n}: {key}')
                lc[idx] = n-1
                if len(lc) == q:
                    print('done')
                    print(lc)
                    for v in lc.values():
                        S2*=v
                    S2 = S2//2
                    running = False
            else: # key not seen
                seen.add(key)
            if dir == 'L':
                T = M[S][0]
            else:
                T = M[S][1]
            NewS.append(T)
        start = NewS
        n += 1


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
