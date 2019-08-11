import time, os, random
from loader import D, args, phrases
from utils import f

limit = 5
count = 0
total = 0

if phrases:
    pause = 5.0
else:
    pause = 2.5

kL = D.keys()[:]

n = None
for a in args:
    try:
        n = int(a)
        args.remove(a)
        break
    except:
        pass

# doesn't work any more with 'phrases', etc.
'''
if len(args) > 0:
    # filter by first letter
    first_letters = list(args[0])  # should allow a-j etc.
    kL = [word for word in kL if f(word)[0] in first_letters]
'''

# now filter by number of words desired
random.shuffle(kL)
if n:
    kL = kL[:n]

s = str(len(kL))
print len(kL), 'items'

while True:
    random.shuffle(kL)
    for word in kL:
        count += 1
        total += 1
        try:
            trans = ', '.join(D[word])
        except:
            print 'problem with', word
            continue
            
        print word
        time.sleep(pause)
        print trans
        if phrases:
            time.sleep(2.0)
        else:
            time.sleep(0.5)
        if (n > 0 and count >= n) \
        or (n == 0 and count >= limit) \
        or count >= 10:
            os.system('clear')
            print str(total) + '/' + s + ':  '
            count = 0