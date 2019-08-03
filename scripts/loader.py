# -*- coding: utf-8 -*-

import os, sys
from os import walk
from string import lowercase
from os.path import expanduser

h = expanduser('~')
d = h + '/Github/Español/vocab'

all_files = os.listdir(d)
all_files.remove('.DS_Store')

D = {}
rD = {}

args = sys.argv[1:]
std_args = [a for a in args if a in ['new','words','verbs','phrases']]
rev = 'rev' in args
if rev:
    args.remove('rev')

other_args = [a for a in args if not a in std_args]

print 'std_args:', ' '.join(std_args)
print 'other:   ', ' '.join(other_args)
print 'rev:     ', rev

fL = all_files
for a in std_args:
    fL = [fn for fn in fL if a in fn]
    
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
                sL = en.strip().split(',')
                sL = [e.strip() for e in sL]
                for e in sL:
                    if e in rD:
                        rD[e].append(sp)
                    else:
                        rD[e] = [sp]
            except ValueError:
                pass

if rev:
    print 'English to Spanish'
    D = rD
