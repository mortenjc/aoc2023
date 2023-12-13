#!/usr/local/bin/python3

import sys

# This solution required heavy inspiration from Jonathan Paulson
# kind of got the solution but kept tripping over my own feet
# on the termination and recurrence conditions.

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


DP = {}
def f(l, exp, i, bi, current):
    state = (i, bi, current)
    if state in DP:
        return DP[state]
    ans = 0
    if i == len(l):
        if bi == len(exp) and current == 0:
            return 1
        elif bi == len(exp)-1 and exp[bi] == current:
            return 1
        else:
            return 0

    for c in ['.', '#']:
        if l[i] == c or l[i] == '?':
            if c == '.' and current == 0:
                ans += f(l, exp, i+1, bi, 0)
            elif c =='.' and current > 0 and bi < len(exp) and exp[bi] == current:
                ans += f(l, exp, i+1, bi+1, 0)
            elif c == '#':
                ans += f(l, exp, i+1, bi, current + 1)

    DP[state] = ans
    return ans


for part2 in [False,True]:
  for line in lines:
    l, exp = line.split()

    if part2:
      l = '?'.join([l, l, l, l, l])
      exp = ','.join([exp, exp, exp, exp, exp])
    exp = [int(x) for x in exp.split(',')]

    DP.clear()
    score = f(l, exp, 0, 0, 0)
    if part2:
        S2 += score
    else:
        S1 += score


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
