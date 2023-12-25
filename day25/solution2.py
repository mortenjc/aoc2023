#!/usr/local/bin/python3

import sys
from collections import defaultdict
import networkx as nx

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

E = defaultdict(set)
G = nx.Graph()
for l in lines:
    par, chls = l.split(': ')
    chls = chls.split(' ')
    for ch in chls:
        E[par].add(ch)
        E[ch].add(par)
        G.add_edge(par, ch, capacity=1.0)

run = True
for e1 in E:
    if run == False:
        break
    for e2 in E:
        if e1 == e2:
            continue
        v, p = nx.minimum_cut(G, e1, e2)
        if v == 3:
            S1 = len(p[0]) * len(p[1])
            run = False
            break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
