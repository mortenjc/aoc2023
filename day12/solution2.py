#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


gens = {}
seen = set()

def match(patt, expect):
    #print(f'match() - expect {expect}')
    p = patt.split('.')
    #print(f'match() - p {p}')
    res = [len(x) for x in p if x != '']
    #print(f'match() - res {res}')
    return res == expect

# assert match('.#...#....###.', [1, 1, 3])
# assert not match('.#...#..#..###.', [1, 1, 3])
#
# assert match('#.#.###', [1, 1, 3])

def generate(n):
    if n in seen:
        return gens[n]

    res = []
    for i in range(2**n):
        c = ''
        for bit in range(n):

            if i & 1<<bit:
                c = '#' + c
            else:
                c = '.' + c
        res.append(c)
    seen.add(n)
    gens[n] = res
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

# assert subs('????', '#.#.') == '#.#.'

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

print(infile)

for i, l in enumerate(lines):
    mp, intv = l.split(' ')
    mp = (mp+'?')*5
    mp = mp[:-1]
    intv = list(map(int, intv.split(','))) * 5


    unkn = mp.count('?')

    s = generate(unkn)
    print(mp)
    print(i, unkn, intv)
    for pat in s:
        print(f'pat {pat}')
        print(f'subs |{subs(mp, pat)}|')
        if match(subs(mp, pat), intv):
            #print('match')
            S1 += 1
        else:
            pass
            #print('no match')
    #print(i, count)








print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
