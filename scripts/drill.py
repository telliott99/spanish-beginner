import time, os, random
from loader import D, other_args, phrases
from utils import f

limit = 5
count = 0
total = 0

if phrases:
    pause = 4.0
else:
    pause = 3.0

kL = D.keys()[:]

n = None
for a in other_args:
    try:
        n = int(a)
        other_args.remove(a)
        break
    except:
        pass

if len(other_args) > 0:
    # filter by first letter
    first_letters = list(other_args[0])  # should allow a-j etc.
    kL = [word for word in kL if f(word)[0] in first_letters]

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
        time.sleep(0.5)
        if (n > 0 and count >= n) \
        or (n == 0 and count >= limit) \
        or count >= 10:
            os.system('clear')
            print str(total) + '/' + s + ':  '
            count = 0