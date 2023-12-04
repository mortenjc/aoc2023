#!/usr/local/bin/python3

import sys
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

# for l in lines:
#     print(l)

copies = defaultdict(int)

for i, l in enumerate(lines):
    card = i + 1
    copies[card] += 1
    _, rest = l.split(':')
    wins, my = rest.split('|')
    wins = wins.split()
    my = my.split()

    hits = len(set(my) & set(wins))

    if hits == 0:
        continue

    score = 2**(hits-1)
    S1 += score
    for h in range(card + 1, card + 1 + hits):
        copies[h] += copies[card]

for e in copies:
    S2 += copies[e]



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
