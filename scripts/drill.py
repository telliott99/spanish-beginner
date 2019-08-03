import time, os, random
from loader import D, other_args
from utils import f

limit = 5
count = 0
total = 0
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

random.shuffle(kL)

# now filter by number of words desired
if n:
    kL = kL[:n]
    
s = str(len(kL))

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
        if count >= limit:
            os.system('clear')
            print str(total) + '/' + s + ':  '
            count = 0