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


TO = defaultdict(list)
FROM = defaultdict(list)
MEM = defaultdict(dict)
TYPE = {}
STATE = {}

for l in lines:
    src, dstlist = l.split('->')
    src = src.strip()
    dstlist = dstlist.strip()

    src2 = src if not src[0] in ['&', '%'] else src[1:]
    if src != 'broadcaster':
        TYPE[src2] = src[0]
    for dst in dstlist.split(','):
        dst = dst.strip()
        TO[src2].append(dst)
        FROM[dst].append(src2)


def dprint(name):
    print(name, 'to', TO[name], 'from', FROM[name])

print(FROM)
for block in FROM:
    print(block)
    if TYPE[block] != '&':
        continue
    for src in FROM[block]:
        MEM[block][src] = 0


for b in FROM:
    STATE[b] = 0

print(MEM)

Q = []
Q.append(('button', 'broadcaster', 0))
while Q:
    src, dest, val = Q.pop(0)
    print(f'pop - {src=} {val=} -> {dest=}')
    print(f'state {STATE}')

    for newdst in TO[dest]:
        #print(dest, val, '->', newdst)
        old_state = STATE[newdst]
        type = TYPE[newdst]
        if type == '%': #ff
            if val == 0:
                new_state = (STATE[newdst] + 1)%2
                STATE[newdst] = new_state
                print(old_state, new_state)
                for tgt in TO[newdst]:
                    #print('Q', newdst, new_state, '->', tgt)
                    Q.append((newdst, tgt, STATE[newdst]))
            else:
                pass
                #print(dst, 'ignore', val)

        elif type == '&': #conj
            #print(f'{src=} {dest=} {val=} {type=} {newdst=}')
            mem = MEM[newdst] # our memory
            print(mem)
            mem['c'] = val
            print(mem)

            print([x==1 for x in mem.values()])
            if all(x == 1 for x in mem.values() ):
                #print('condition met')
                STATE[newdst] = 0
            else:
                #print('condition NOT met')
                STATE[newdst] = 1
            for tgt in TO[newdst]:
                #print('Q', dst, STATE[newdst], '->', tgt)
                Q.append((newdst, tgt, STATE[newdst]))
        else:
            assert False, TYPE[newdst]

print(STATE)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
