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
V = set()
ni = {}
for l in lines:
    par, chls = l.split(': ')
    chls = chls.split(' ')
    V.add(par)
    if not par in ni:
        ni[par] = len(ni)
    for ch in chls:
        if not ch in ni:
            ni[ch] = len(ni)
        E[par].add(ch)
        E[ch].add(par)
        G.add_edge(par, ch, capacity=1.0)

        V.add(ch)

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
            se1 = e1
            se2 = e2
            print(se1, se2)
            run = False
            break


from graphe.graph import graph
from graphe.graph import bfs
from graphe import draw

MG = graph.Graph(len(V))
SEEN = set()
for adj in E:
    for other in E[adj]:
        a = ni[adj]
        b = ni[other]
        if (a,b) in SEEN:
            continue
        SEEN.add((a,b))
        SEEN.add((b,a))
        MG.add_edge(a, b)


fig = draw.Draw()
fig.node_attr(label='')
fig.draw(MG)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
