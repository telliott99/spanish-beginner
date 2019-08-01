# -*- coding: utf-8 -*-

import os, sys
from os import walk
from string import lowercase

d = '/Users/telliott_admin/Desktop/Español/vocab'
fL = os.listdir(d)
D = {}
rD = {}

try:
    flag = sys.argv[1]
except:
    flag = None

if flag and flag == 'new':
    print 'new words only'
    fL = ['words-new.txt']

#print '\n'.join(fL)

for fn in fL:
    with open(d + '/' + fn,'r') as fh:
        data = fh.read().strip().split('\n')
        for e in data:
            if not e or not e[0] in lowercase:
                continue
            try:
                sp,en = e.strip().split('\t')
                if sp in D:
                    D[sp].append(en)
                else:
                    D[sp] = [en]
                if en in rD:
                    rD[en].append(sp)
                else:
                    rD[en] = [sp]
            except ValueError:
                pass

if flag and flag == 'rev':
    print 'English to Spanish'
    D = rD
