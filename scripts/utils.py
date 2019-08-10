# helper function for sort or filter
def f(s):
    if not s or s == '':
        return s
    pL = ['a', 'las','los','el','la',
          'uno','una','unos','unas']
    for p in pL:
        if s.startswith(p + ' '):
            return s[len(p) + 1:]
    return s

# already sorted
def clean(L):
    rL = []
    for s in L:
        if s == '':
            continue
        if len(rL) == 0:
            rL.append(s)
            continue
        if f(rL[-1])[0] != f(s)[0]:
            rL.append('')
        rL.append(s)
    return rL
