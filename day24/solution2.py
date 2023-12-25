#!/usr/local/bin/python3

import sys
from sympy import symbols, Eq, solve


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


# solve
# x + vx * t = nx + nvx * t
# x - nx = (nvx - vx) * t
x, y, z, vx, vy, vz, t1, t2, t3 = symbols('x y z vx vy vz, t1, t2, t3')

nx, ny, nz, nvx, nvy, nvz = L[0]
e1 = Eq(x + vx*t1 - nx - nvx*t1,0)
e2 = Eq(y + vy*t1 - ny - nvy*t1,0)
e3 = Eq(z + vz*t1 - nz - nvz*t1,0)

nx2, ny2, nz2, nvx2, nvy2, nvz2 = L[1]
e4 = Eq(x + vx*t2 - nx2 - nvx2*t2,0)
e5 = Eq(y + vy*t2 - ny2 - nvy2*t2,0)
e6 = Eq(z + vz*t2 - nz2 - nvz2*t2,0)

nx3, ny3, nz3, nvx3, nvy3, nvz3 = L[2]
e7 = Eq(x + vx*t3 - nx3 - nvx3*t3,0)
e8 = Eq(y + vy*t3 - ny3 - nvy3*t3,0)
e9 = Eq(z + vz*t3 - nz3 - nvz3*t3,0)

res = solve((e1, e2, e3, e4, e5, e6, e7, e8, e9), (x, y, z, vx, vy, vz, t1, t2, t3))
print(int(res[0][0] + res[0][1] + res[0][2]))

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
