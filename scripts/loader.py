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
std_args = [a for a in args if a in ['nouns','verbs','adverbs','phrases']]

phrases = False
for a in std_args:
    if a == 'phrases':
        phrases = True

rev = 'rev' in args
if rev:
    args.remove('rev')
new = 'new' in args
if new:
    args.remove('new')
old = 'old' in args
if old:
    args.remove('old')

other_args = [a for a in args if not a in std_args]

print 'std_args:', ' '.join(std_args)
print 'other:   ', ' '.join(other_args)
print 'new:     ', new
print 'rev:     ', rev

#--------------------------------

fL = all_files
for a in std_args:
    fL = [fn for fn in fL if fn.startswith(a)]
    
if new and not old:
    fL = [fn for fn in fL if 'new' in fn]
if old and not new:
    fL = [fn for fn in fL if 'new' not in fn]

for fn in fL:
    with open(d + '/' + fn,'r') as fh:
        data = fh.read().strip().split('\n')
        for e in data:
            if not e or not e[0] in lowercase:
                continue
            try:
                sp,en = e.strip().split('\t')
                if sp in D:
                    if en in D[sp]:
                        continue
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
