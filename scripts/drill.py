import time, os, random
from loader import D, flag

limit = 5
count = 0

L = D.keys()[:]
random.shuffle(L)
for word in L:
    count += 1
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
        count = 0