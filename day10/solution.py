#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

subst = {'|':'\u2503', '-':'\u2501',
         'F':'\u250f', '7':'\u2513',
         'L':'\u2517', 'J':'\u251b'
         }


def printg(G, path, inside = []):
    for r in range(len(G)):
        s = ''
        for c in range(len(G[0])):
            if (r,c) in path:
                ch = G[r][c]
                if ch == 'S':
                    s += 'S'
                else:
                    s += subst[ch]
            else:
                if (r,c) in inside:
                    s += '\u25aa'
                else:
                    s += ' '
        print(s)


D = { '|': [( 1, 0), (-1 , 0)],
      '-': [( 0, 1), ( 0, -1)],
      'L': [(-1, 0), ( 0,  1)],
      'J': [(-1, 0), ( 0, -1)],
      '7': [( 1, 0), ( 0, -1)],
      'F': [( 1, 0), ( 0,  1)],
    }


G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start=(r, c)


print(f'start position {start}')
seen = set()
points = []
seen.add(start)
points.append(start)
pos = start


if infile == 'puzzle.txt':
    move = (0, -1) # for puzzle.txt
elif infile == 'test3.txt':
    move = (1, 0)
else:
    move = (0, 1) # for test.txt and test2.txt


n = 0
wn = 0
while True:
    pos = (pos[0] + move[0], pos[1] + move[1])
    if pos == start:
        break

    seen.add(pos)
    points.append(pos)

    p = G[pos[0]][pos[1]]
    #print(n, pos, p)
    assert p in '|-LJ7F'

    for m in D[p]:
        np =(pos[0] + m[0], pos[1] + m[1])
        if not np in seen or np == start:
            move = m
            break
    else:
        assert False, 'no valid move'

    n += 1
S1 = (n+1)//2

#print(start)
printg(G, seen)
#sys.exit()]
points.append(start)



# part 2
def inpath(path, pos):
    assert pos not in path, 'undefined'
    wn = 0
    for i in range(len(path)-1):
        p1 = points[i]
        p2 = points[i+1]
        #print(f'p1 {p1}, p2 {p2}')

        if p2[0] == pos[0] and p1[0] > pos[0] and p1[1] > pos[1]:
            #print(f'+1/2 enter line up - {pos}, {p1}, {p2}')
            wn += 0.5
        elif p2[0] < pos[0] and p1[0] == pos[0] and p1[1] > pos[1]:
            #print(f'+1/2 leave line up - {pos}, {p1}, {p2}')
            wn += 0.5
        elif p2[0] == pos[0] and p1[0] < pos[0] and p1[1] > pos[1]:
            #print(f'-1/2 enter line down - {pos}, {p1}, {p2}')
            wn -= 0.5
        elif p2[0] > pos[0] and p1[0] == pos[0] and p1[1] > pos[1]:
            #print(f'-1/2 leave line down - {pos}, {p1}, {p2}')
            wn -= 0.5
    #if wn != 0:
        #print(f'winding number {wn}')

    if wn > 0 or wn < 0:
        return True
    else:
        return False


inside = []
for r in range(R):
    for c in range(C):
        if not (r, c) in seen and inpath(points, (r, c)):
            inside.append((r,c))
            S2 += 1


printg(G, seen, inside)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
