#!/usr/local/bin/python3

from collections import deque

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

lo = 200000000000000
hi = 400000000000000
# lo = 7
# hi = 27

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


def intersect(l1, l2,lo, hi):
    x1, y1, z1, vx1, vy1, vz1 = l1
    x2, y2, z2, vx2, vy2, vz2 = l2

    a = x1
    b = vx1
    c = x2
    d = vx2
    e = y1
    f = vy1
    g = y2
    h = vy2

    denum = (b*h - f*d)

    if denum == 0: # assume parallel
        if x1==x2 and y1 == y2:
            return True
        else:
            return False

    s = (b*(e-g) + f*(c-a))/denum
    t = (c + d*s -a)/b
    if s<0 or t < 0:
        return False
    print('s,t', s, t)
    print('x', x1 + vx1*t, x2 + vx2*s)
    print('y', y1 + vy1*t, y2 + vy2*s)

    xi = x1 + vx1*t
    yi = y1 + vy1*t
    return (lo<= xi <=hi) and (lo<=yi<=hi)
    #print('xi, yi', x1 + vx1*t, y1 + vy1*t)



L = []
for l in lines:
    a, b = l.split('@')
    x, y, z = list(map(int, a.split(',')))
    vx, vy, vz = list(map(int, b.split(',')))

    L.append((x, y, x, vx, vy, vz))

for l1 in range(len(L)-1):
    for l2 in range(l1+1, len(L)):
        if intersect(L[l1], L[l2], lo, hi):
            print('intersects:',L[l1], L[l2])
            S1 += 1


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
