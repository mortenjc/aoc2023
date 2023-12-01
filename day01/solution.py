#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
# from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
# import re

words={"zero":0,  "one":1,   "two":2,  "three":3, "four":4, "five":5, "six":6,
       "seven":7, "eight":8, "nine":9, "sixteen" :16}

def getNum(str):
    for w in words:
        if str.startswith(w):
            return words[w]
    return -1




infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

S1 = 0
S2 = 0
for l in lines:
    digs = []
    wdigs = []
    for i in range(len(l)):
        c = l[i]
        s = l[i:]
        if c.isdigit():
            digs.append(c)
            wdigs.append(c)
            continue

        if getNum(s) != -1:
            wdigs.append(getNum(s))

    if len(wdigs) >=1:
        S1 += 10*(int(digs[0])) + int(digs[-1])
        S2 += 10*(int(wdigs[0])) + int(wdigs[-1])


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
