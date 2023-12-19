#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    rules, parts = ((fin.read().strip()).split('\n\n'))


R = {}
for rule in rules.split('\n'):
    name, logic = rule.split('{')
    R[name] = logic[:-1].split(',')


def new_range(op, n, l, h):
    if op == '>':
        l = max(n+1, l)
    elif op == '<':
        h = min(n-1, h)
    elif op == '>=':
        l = max(n, l)
    elif op == '<=':
        h = min(n, h)
    else:
        assert False
    return (l, h)


def new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh):
    if var == 'x':
        xl, xh = new_range(op, n, xl, xh)
    elif var == 'm':
        ml, mh = new_range(op, n, ml, mh)
    elif var == 'a':
        al, ah = new_range(op, n, al, ah)
    elif var == 's':
        sl, sh = new_range(op, n, sl, sh)
    else:
        assert False
    return (xl, xh, ml, mh, al, ah, sl, sh)

S2 = 0
Q = []
Q.append(('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000))
while Q:
    state, xl, xh, ml, mh, al, ah, sl, sh = Q.pop()

    if xl>xh or ml>mh or al>ah or sl>sh:
        continue

    if state == 'A':
        score = (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
        S2 += score
        continue
    elif state == 'R':
        continue
    else:
        rule = R[state]
        print(rule)
        for cmd in rule:
            applies = True
            res = cmd
            if ':' in cmd:
                cond, res = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                Q.append((res, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh)))
                xl, xh, ml, mh, al, ah, sl, sh = new_ranges(var, '<=' if op == '>' else '>=', n, xl, xh, ml, mh, al, ah, sl, sh)
            else:
                Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
