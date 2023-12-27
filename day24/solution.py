#!/usr/local/bin/python3

import sys
from sympy import symbols, Eq, solve


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'test.txt':
    lo = 7
    hi = 27
else:
    lo = 200000000000000
    hi = 400000000000000


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


L = []
for l in lines:
    a, b = l.split('@')
    x, y, z = list(map(int, a.split(',')))
    vx, vy, vz = list(map(int, b.split(',')))

    L.append((x, y, z, vx, vy, vz))


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

    xi = x1 + vx1*t
    yi = y1 + vy1*t
    return (lo<= xi <=hi) and (lo<=yi<=hi)


def part1():
    ans = 0
    for l1 in range(len(L)-1):
        for l2 in range(l1+1, len(L)):
            if intersect(L[l1], L[l2], lo, hi):
                #print('intersects:',L[l1], L[l2])
                ans += 1
    return ans


def part2():
    x, y, z, vx, vy, vz = symbols('x y z vx vy vz')

    x1, y1, z1, vx1, vy1, vz1 = L[0]
    e1 = Eq((y-y1)*(vx1-vx) + (vy-vy1)*(x-x1), 0)
    e2 = Eq((z-z1)*(vx1-vx) + (vz-vz1)*(x-x1), 0)

    x2, y2, z2, vx2, vy2, vz2 = L[1]
    e3 = Eq((y-y2)*(vx2-vx) + (vy-vy2)*(x-x2), 0)
    e4 = Eq((z-z2)*(vx2-vx) + (vz-vz2)*(x-x2), 0)

    x3, y3, z3, vx3, vy3, vz3 = L[2]
    e5 = Eq((y-y3)*(vx3-vx) + (vy-vy3)*(x-x3), 0)
    e6 = Eq((z-z3)*(vx3-vx) + (vz-vz3)*(x-x3), 0)


    res = solve([e1, e2, e3, e4, e5, e6], [x, y, z, vx, vy, vz])
    for x0, y0, z0, vx0, vy0, vz0 in res:
        if x0+y0+z0 == int(x0+y0+z0):
            return x0+y0+z0


S1 = part1()
S2 = part2()

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
