#!/usr/local/bin/python3

# Not genuine my solution but inspired by Jonathan Paulson
# (https://www.youtube.com/watch?v=22IrAlrWqu4)

import sys
from collections import defaultdict
import functools
from collections import Counter


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

def hprint(hand):
    hand = hand.replace(chr(ord('9')+5), 'A')
    hand = hand.replace(chr(ord('9')+4), 'K')
    hand = hand.replace(chr(ord('9')+3), 'Q')
    hand = hand.replace(chr(ord('9')+2), 'J')
    hand = hand.replace(chr(ord('9')+1), 'T')
    print(hand)

def score(hand, part):
    hand = hand.replace('A', chr(ord('9')+5))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('J', chr(ord('9')+2) if part ==1 else chr(ord('2')-1))
    hand = hand.replace('T', chr(ord('9')+1))

    C = Counter(hand)
    C2 = Counter(hand)

    if part == 2:
        target = 0
        for k in C:
            if k != '1':
                target = max(target, C[k])

        if '1' in C:
            print('score', hand, C, target)
            for k in C:
                if C[k] == target and k != '1':
                    C2[k] += C['1']
                    del C2['1']
                    break
    C = C2
    print(C)
    C = sorted(list(C.values()))

    if C == [5]:
        return (7, hand)
    elif C == [1, 4]:
        return (6, hand)
    elif C == [2,3]:
        return (5, hand)
    elif C == [1,1,3]:
        return (4, hand)
    elif C == [1, 2, 2]:
        return (3, hand)
    elif C == [1, 1, 1, 2]:
        return (2, hand)
    elif C == [1, 1, 1, 1, 1]:
        return (1, hand)
    else:
        assert True == False, C



with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for part in [1,2]:
    print(f'part {part}')
    H = []
    B = {}
    for i, l in enumerate(lines):
        hand = l.split()[0]
        bid = l.split()[1]

        sc = score(hand, part)
        print(sc)
        H.append(sc)
        B[sc[1]] = int(bid)
    #print(H)
    HS = sorted(H)
    #print(HS)
    #print(B)

    for i in range(len(H)):
        #hprint(HS[i][1])
        #print(B[HS[i][1]], i+1)
        if part == 1:
            S1 += B[HS[i][1]] * (i+1)
        if part == 2:
            S2 += B[HS[i][1]] * (i+1)




print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
