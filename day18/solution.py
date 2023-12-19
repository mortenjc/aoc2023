#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

todir = {'R':0, 'L':2, 'D':1, 'U':3}
dirs = {0:(0,1), 2:(0,-1), 3:(-1,0), 1:(1,0)}



def solve(part2):
    r, c = [0,0]
    path = [(r,c)]
    ans = 0
    for l in lines:
        dirc, n, col = l.split()

        dir = todir[dirc]
        n = int(n)

        if part2:
            dir = int(col[-2])
            n = int(col[2:-2], 16)

        ans += abs((n) * dirs[dir][0])
        ans += abs((n) * dirs[dir][1])
        nr = r + (n) * dirs[dir][0]
        nc = c + (n) * dirs[dir][1]
        path.append((nr, nc))
        r = nr
        c = nc

    for i in range(len(path)-1):
        p1r = path[i][0]
        p1c = path[i][1]
        p2r = path[i+1][0]
        p2c = path[i+1][1]
        ans += (p1c*p2r - p2c*p1r)

    ans = ans // 2 + 1

    return ans

S1 = solve(False)
S2 = solve(True)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
