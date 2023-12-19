#!/usr/local/bin/python3

import sys

def printg(G):
    for l in G:
        print(''.join(l))

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


def accept(part):
    state = 'in'
    while True:
        rule = R[state]
        for cmp in rule:
            state = cmp # default fallthrough
            if ':' in cmp:
                before, state = cmp.split(':')
                var, cond, val = before[0], before[1], int(before[2:])
                met = False
                if cond == '<':
                    met = (part[var] < val)
                else:
                    met = (part[var] > val)
                if met:
                    break

        if state == 'A':
            return True
        elif state == 'R':
            return False
        else:
            continue


for part in parts.split('\n'):
    part = {x[0]:int(x[2:]) for x in part[1:-1].split(',')}
    if accept(part):
        S1 += sum(part.values())


# S1 397643

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
