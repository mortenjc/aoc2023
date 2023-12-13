#!/usr/local/bin/python3

import sys

# my own ugly and slow solution

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


def match(patt, expect):
    p = patt.split('.')
    res = [len(x) for x in p if x != '']
    return res == expect


def generate(n):
    res = []
    for i in range(2**n):
        c = ''
        for bit in range(n):

            if i & 1<<bit:
                c = '#' + c
            else:
                c = '.' + c
        res.append(c)
    return res


def subs(line, wild):
    assert line.count('?') == len(wild)
    sub = 0
    nl = ''
    for i in range(len(line)):
        if line[i] == '?':
            nl += wild[sub]
            sub += 1
        else:
            nl += line[i]
    return nl

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

for i, l in enumerate(lines):
    mp, intv = l.split(' ')
    intv = list(map(int, intv.split(',')))

    unkn = mp.count('?')

    s = generate(unkn)

    for pat in s:
        if match(subs(mp, pat), intv):
            S1 += 1
        else:
            pass

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
