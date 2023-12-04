#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
# from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
# import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

def getNumbers(y):
    b = 0
    e = 0
    s = 0
    num = ''
    nums = []
    for i in range(R):
        ch = G[y][i]
        if s == 0:
            if ch.isnumeric():
                s = 1
                b = i
                num = ch
        elif s == 1:
            if ch.isnumeric():
                num += ch
            else:
                s = 0
                if num == '':
                    continue
                e = i - 1
                nums.append((int(num), b, e))
                num = ''
    if num != '':
        nums.append((int(num), b, i))
    return nums



def touches(x, y):
    tch = []
    if y >= 0:
        nums = getNumbers(y - 1)
        for n in nums:
            l = n[1]
            r = n[2]
            if x - 1 >= l and x - 1 <= r or \
               x     >= l and x     <= r or \
               x + 1 >= l and x + 1 <= r:
                #print('above touches')
                tch.append(n)
    # always
    nums = getNumbers(y)
    for n in nums:
        l = n[1]
        r = n[2]
        if x-1 == r or x+1 == l :
            #print('side touches')
            tch.append(n)

    if y < R:
        nums = getNumbers(y + 1)
        for n in nums:
            l = n[1]
            r = n[2]
            if x - 1 >= l and x - 1 <= r or \
               x     >= l and x     <= r or \
               x + 1 >= l and x + 1 <= r:
                #print('below touches')
                tch.append(n)
    return tch


S1 = 0
S2 = 0


for y in range(R):
    for x in range(C):
        ch = G[y][x]
        if ch == '*':
            #print(f'testing {x},{y}')
            tch = touches(x, y)
            #print(tch)
            if len(tch) == 2:
                ratio = tch[0][0] * tch[1][0]
                S2 += ratio


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
