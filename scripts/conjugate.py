# -*- coding: utf-8 -*-

import os, sys
from os.path import expanduser

h = expanduser('~')
d = h + '/Github/Español/verbs'
fL = ['regular.txt', 'ser+3.txt', 'venir+3.txt']
L = []
D = {}

for fn in fL:
    with open(d + '/' + fn) as fh:
        data = fh.read()
        data = data.strip().split('#-----\n')
        L.extend(data)

for e in L[:1]:
    lines = e.strip().split('\n')
    verb = lines[0]
    stem, r1, r2 = lines[1].strip().split(',')
    pp =  (stem + r1.strip()).replace('-','')
    pap = (stem + r2.strip()).replace('-','')
    print stem, pp, pap
    