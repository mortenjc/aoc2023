#!/usr/local/bin/python3

import sys

from unionfind import unionfind

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


nodes = {}
v = []
for l in lines:
    parent, chlds = l.split(': ')
    chlds = chlds.split(' ')

    elts = list((parent, *chlds))
    for n in elts:
        if not n in nodes:
            nodes[n] = len(nodes)
    for n in chlds:
        v.append((nodes[parent], nodes[n]))

print(nodes)
print(v)

cc = [i for i in range(len(nodes))]
print(cc)



def test(v1, v2):
    skip = set()
    skip.add((v1[0], v1[1]))
    skip.add((v2[0], v2[1]))
    u = unionfind(len(cc))

    for l in lines:
        parent, chlds = l.split(': ')
        chlds = chlds.split(' ')

        pi = nodes[parent]
        for c in chlds:
            ci = nodes[c]
            if (pi, ci) in skip or (ci, pi) in skip:
                pass
                #print('skip', pi, ci)
            else:
                #print(f'union of {parent}({pi}) and {c}({ci})')
                u.unite(pi, ci)
    if len(u.groups()) == 2:
        print(u.groups())
    return u.groups()

for p in range(len(v)):
    for q in range(p+1, len(v)):
        #print('skipping', v[p], v[q])
        res = test(v[p], v[q])






print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
