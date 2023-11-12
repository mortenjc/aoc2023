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


S1 = ''
S2 = ''


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
