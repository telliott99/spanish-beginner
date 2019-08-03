import sys
from utils import f, clean

fn = sys.argv[1]

with open(fn) as fh:
    data = fh.read().strip().split('\n')
            
data.sort(key = f)
data = clean(data)

ofn = '.'.join(fn.split('.')[:-1]) + '.sorted.txt'
with open(ofn, 'w') as fh:
    fh.write('\n'.join(data))