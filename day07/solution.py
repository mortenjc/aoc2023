#!/usr/local/bin/python3

import sys
from collections import defaultdict
import functools


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

cval = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}





def makemap(hand):
    hmap = defaultdict(int)
    hset = set()
    for c in hand:
        hset.add(c)
        hmap[c] += 1
    return hmap, hset


# 7 6 5 4 3 2 1
def htype(hand):
    hmap, hset = makemap(hand)
    maxcount = max(hmap.values())
    different = len(hset)
    js = hand.count('J')


    if different == 1: # fiveofakind
        return 6
    elif different == 2:
        if maxcount == 4:
            return 5 #fourofakind
        else:
            return 4 #fullhouse
    elif different == 3:
        if maxcount == 3:
            return 3 # three of a kind
        else:
            return 2 #twopair
    elif different == 4:
        return 1
    else:
        return 0

assert htype('T55J5') == 3




def higher(h1, h2):
    for i in range(len(h1)):
        h1val = cval[h1[i]]
        h2val = cval[h2[i]]
        if h1val > h2val:
            return -1
        elif h2val > h1val:
            return 1
        else:
            continue
    return 0


assert higher('A3322', 'K3322') == -1
assert higher('33332', '2AAAA') == -1

def compare(h1, h2):
    if htype(h1) > htype(h2):
        return -1
    if htype(h2) > htype(h1):
        return 1
    else:
        return higher(h1, h2)


assert htype('33332') == htype('2AAAA')
assert compare('33332', '2AAAA') == -1

rank = [[] for i in range(7)] # 7 different types

bets = {}
for l in lines:
    hmap = defaultdict(int)
    hand, bet  = l.split()
    bet = int(bet)
    bets[hand] = bet
    hm, hs = makemap(hand)
    #print(list(hs))
    #print(hand, hm, max(hm), hm[max(hm)])
    rank[htype(hand)].append(hand)

assert len(bets) == len(lines)
currank = 1
for i in range(7):
    print(i)
    lst = rank[i]
    if lst != []:
        sorted_l = sorted(lst, key=functools.cmp_to_key(compare))
        sorted_l.reverse()
        print(sorted_l)
        for j in sorted_l:
            print(bets[j], currank)
            S1 += currank * bets[j]
            currank +=1



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
