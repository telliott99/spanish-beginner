# -*- coding: utf-8 -*-

import os, sys
from os import walk
from string import letters
from os.path import expanduser

h = expanduser('~')
d = h + '/Github/Español/vocab'

all_files = os.listdir(d)
all_files.remove('.DS_Store')

D = {}
rD = {}

args = sys.argv[1:]

rev = 'rev' in args
if rev:
    args.remove('rev')
    
new = 'new' in args
if new:
    args.remove('new')

std_args = ['nouns','verbs','adverbs',
            'phrases','phrases-verbs']
args = [a for a  in args if a in std_args]

phrases = False
for a in args:
    if a.startswith('phrases'):
        phrases = True
        break

v = False
if v:
    print 'args:', ' '.join(args)
    print 'phrases', phrases
    print 'new:     ', new
    print 'rev:     ', rev

#--------------------------------

fL = []

if not args:
    fL = all_files
else:
    for fn in all_files:
        for a in args:
            if fn.startswith(a) or a in fn.split('-'):
                fL.append(fn)
                break
                        
if new:
    fL = [fn for fn in fL if 'new' in fn]
    
pL = [a.replace('.txt', '') for a in fL]
pL.sort()
print 'loading:  ', ', '.join(pL)

for fn in fL:
    with open(d + '/' + fn,'r') as fh:
        data = fh.read().strip().split('\n')
        for e in data:
            if not e or e[0] in ['-']:
                continue
            #print 'trying:', e
            try:
                sp,en = e.strip().split('\t')
                if sp in D:
                    if en in D[sp]:
                        continue
                    D[sp].append(en)
                else:
                    D[sp] = [en]
                #print 'after:', sp, D[sp]
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
