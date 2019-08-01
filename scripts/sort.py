import sys
fn = sys.argv[1]

with open(fn) as fh:
    data = fh.read().strip().split('\n')
    
def f(s):
    if s.startswith('las'):  return s[4:]
    if s.startswith('los'):  return s[4:]
    if s.startswith('el'):  return s[3:]
    if s.startswith('la'):  return s[3:]
    return s
        
data.sort(key = f)

with open(fn + '.sorted', 'w') as fh:
    fh.write('\n'.join(data))