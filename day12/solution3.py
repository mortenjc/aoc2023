#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


# l line
# a char index
# b start of run of #
def f(l, exp, inrun, a, b, c, ):
    #print(f'f() - {l}, {exp}, {inrun}, {a}, {b}, {c}')
    if c >=len(exp):
        return False # too many matches
    if a == len(l): # last entry
        #print(f'last {inrun} {a} {b} {c}')
        if exp[c] == a-b:
            print('final match')
            return True
        else:
            print('final mismatch')
            return False

    if l[a] == '#':
        if inrun:
            a += 1
        else:
            b = a
            a += 1
            inrun = True
        return f(l, exp, inrun, a, b, c)

    elif l[a] == '.':
        if inrun:
            #print(f'len of run {a-b}')
            inrun = False
            if exp[c] == a-b:
                #print('Match')
                c += 1
                a += 1
                if c >=len(exp): # too many matches
                    return False
            else:
                #print('Mismatch')
                return False
        else:
            a += 1
        return f(l, exp, inrun, a, b, c)
    else:
        assert False, 'unimplemented'



assert f('##.##',    [2, 2], False, 0, 0, 0 )
assert f('..#....#', [1, 1], False, 0, 0, 0 )
assert f('##.##.',   [2, 2], False, 0, 0, 0 )
# failures below
assert not f('##.##',    [2, 1], False, 0, 0, 0 )
#assert not f('##.##.#', [2, 2], False, 0, 0, 0 )



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
