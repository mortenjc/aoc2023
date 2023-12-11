#!/usr/local/bin/python3

import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    entries = ((fin.read().strip()).split('\n\n'))

seeds = list(map(int, entries[0].split(':')[1:][0].split()))
print(seeds)



SR=[] # seed ranges
for i in range(len(seeds)//2):
    start = seeds[2*i]
    length = seeds[2*i+1]
    SR.append([start, start + length])
#print(SR)

maps = entries[1:]
#print(maps)
MP = []
for m in maps:
    T = []
    t = m.split('\n')[1:]
    for f in t:
        dest, src, r = list(map(int,f.split()))
        T.append([dest, src, r])
    MP.append(T)

#print(MP)


def ints(A, B):
    AB, AE = A
    BB, BE = B
    ovl = [max(AB,BB), min(AE, BE)]
    a = []
    b = []
    if ovl[0] >= ovl[1]: # no overlap
        return [AB, AE], [], []
    if AB < BB:
        b = [AB, ovl[0]]
    if AE > BE:
        a = [ovl[1], AE]
    #print(b, ovl, a)
    return b, ovl, a

#              A        B
assert ints([10, 20],[20, 40]) == ([10, 20],       [],       []), '1 ok'
assert ints([10, 20],[10, 20]) == (      [], [10, 20],       []), '2 ok'
assert ints([10, 25],[10, 20]) == (      [], [10, 20], [20, 25]), '3 ok'
assert ints([ 5, 20],[10, 20]) == ([ 5, 10], [10, 20],       []), '4 ok'

# assert False, 'all good'
# sys.exit(0)

print(SR)




def f(R, transforms):
    A = []
    for dst, src, sz in transforms:
        #print(f'transform [{src},{src+sz}] -> [{dst},{dst+sz}]')
        NR = []
        while R:
            st, ed = R.pop()
            #print(f' range [{st},{ed}]')
            b, c, a = ints([st, ed], [src, src + sz])
            #print(b, c, a)
            if b != []:
                NR.append(b)
            if a != []:
                NR.append(a)
            if c != []:
                c2 = [c[0] + dst - src, c[1] + dst - src]
                A.append(c2)
        R = NR
    return A + R

R = SR
for i, tr in enumerate(MP):
    print(f'Step {i}')
    print(f'R: {R}')
    R = f(R, tr)
    print(f'R: {R}')


S2 = min([x[0] for x in R])


#


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
