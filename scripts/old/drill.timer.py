import time, os, random
from loader import D, flag

limit = 5
count = 0

while True:
    L = D.keys()[:]
    random.shuffle(L)
    for word in L:
        count += 1
        try:
            sp = word
            en = ', '.join(D[sp])
            if flag and flag == 'rev':
                en,sp = sp,en
        except:
            print 'problem with', item
            continue
        
        print sp
        time.sleep(2)
        print en
        time.sleep(2)
        if count >= limit:
            os.system('clear')
            count = 0