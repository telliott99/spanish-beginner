import time, os, random
from loader import D, args

# helper function for sorting
def f(s):
    pL = ['las','los','el','la','uno','una']
    for p in pL:
        if s.startswith(p):
            return s[len(p) + 1]
    return s[0]

#------------------

limit = 5
count = 0
total = 0

kL = D.keys()[:]
standard_args = ['rev','new']
args = [a for a in args if not a in standard_args]

n = None
for a in args:
    try:
        n = int(a)
        args.remove(a)
        break
    except:
        pass    

if len(args) > 0:
    # filter by first letter
    first_letters = list(args[0])  # should allow a-j etc.
    kL = [word for word in kL if f(word) in first_letters]

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
        
        response = raw_input(word + '\t')
        if response == 'q':
            break
        elif response == '':
            print trans
            
        elif response.strip() in trans:
        # '' is *in* anything!
            print 'Si!', trans
        else:
            print trans
            
        time.sleep(0.5)
        if count >= limit:
            os.system('clear')
            print str(total) + '/' + s + ':  '
            count = 0