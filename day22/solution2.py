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


nxy = 10
nzz = 14

G = [[[-1 for k in range(nxy)] for j in range(nxy)] for i in range(nzz)]


def printg():
    for z in range(nzz-1, 0, -1):
        for x in range(nxy):
            for y in range(nxy):
                if G[x][y][nzz - 1 - z] != -1:
                    print(x, y, z, G[x][y][nzz - 1, z])


def canadd(i, x,y,z, dx,dy,dz):
    res = True
    l = max(dx, dy, dz)
    dx = dx//l
    dy = dy//l
    dz = dz//l
    for i in range(l):
        x += dx
        y += dy
        z += dz
        if G[x][y][z] != -1 and G[nx][ny][nz] != i:
            print(f'G[{x}][{y}][{nzz-1-z}] occupied by {G[x][y][nzz-1-z]}')
            res = False
            break
    return res


def doadd(i, x,y,z,dx,dy,dz):
    print('doadd d*', dx, dy, dz)
    l = max(dx, dy, dz)
    dx = dx//l
    dy = dy//l
    dz = dz//l
    for i in range(l):
        nx = x + i
        ny = y + i
        nz = z + i
        assert G[nx][ny][nz] == -1 or G[nx][ny][nz] == i
        G[x][y][z] = -1
        G[nx][ny][nz] = i


blk = []
for i, l in enumerate(lines):
    st, ed = l.split('~')
    sx, sy, sz = list(map(int, st.split(',')))
    ex, ey, ez = list(map(int, ed.split(',')))

    print(ex-sx, ey-sy, ez-sz, '-', sx, sy, sz, ex, ey, ez)
    blk.append((sx, sy, sz, ex, ey, ez))


# lowest first
sorted(blk,  key=lambda x: x[2])
i = -1
while blk:
    i+=1
    # get next block, sorted by z low to high
    sx, sy, sz, ex, ey, ez = blk.pop(0)
    print('='*80)
    print('pop', sx, sy, sz, ex, ey, ez)
    last = sz
    for z in range(sz, 0, -1):
        if canadd(i, sx, sy, z, ex-sx, ey-sy, ez-sz):
            #print(z, 'can add', sx, sy, z, ex, ey, z + ez-sz+1)
            last = z
        else:
            break
            #print(z, 'cant add')
    if last == sz:
        print('block stays put')
    else:
        print(f'move block {i} from {sz} to {last}')
        doadd(i, sx, sy, last, ex-sx, ey-sy, ez-sz)

printg()

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
