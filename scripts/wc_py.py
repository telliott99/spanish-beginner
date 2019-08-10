import sys
try:
    fn = sys.argv[1]
except:
    sys.exit()

with open(fn) as fh:
    data = fh.read()

L = data.strip().split('\n')
L = [e for e in L if not e.strip() == '']
lines = len(L)

L = data.split()
words = len(L)
chars = len(''.join(L))

iL = [lines, words, chars]
print iL
n = max([len(str(i)) for i in iL])
n += 5

for e in iL:
    print str(e).rjust(n),

print