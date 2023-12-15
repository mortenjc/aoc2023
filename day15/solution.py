#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split(','))


def hash(s, h):
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h


hval = 0
l = [[] for i in range(256)]
for s in lines:
    S1 += hash(s, hval)

    if s[-1] == '-': # remove
        box = hash(s[:-1], 0)
        l[box] = [x for x in l[box] if x[0] != s[:-1]]
    elif s[-2] == '=':
        box = hash(s[:-2], 0)
        fl = int(s[-1])
        for i, v in enumerate(l[box]):
            if v[0] == s[:-2]:
                l[box][i] = (s[:-2], fl) # replace
                break
        else:
            l[box].append((s[:-2], fl)) # add

for box in range(len(l)):
    for i, entry in enumerate(l[box]):
        S2 += (box+1) * (i+1) * entry[1]

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
