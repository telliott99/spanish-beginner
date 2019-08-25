# -*- coding: utf-8 -*-

irr1 = ['venir']
irr2 = ['dar','poder','poner','tener']
irr = irr1 + irr2
reg = ['hablar', 'comer', 'vivir']
trans = True   # transpose output

tenses = ['present','past','past_imp',
          'cond','future']

eD = {
# present tense
'present_ar':  ['o','as','a','amos','an'],
'present_er':  ['o','es','e','emos','en'],
'present_ir':  ['o','es','e','imos','en'],

# past perfect
'past_ar':  ['é','aste','ó', 'amos','aron'],
'past_er':  ['í','iste','ió','emos','ieron'],
'past_ir':  ['í','iste','ió','imos','ieron'],
'past_sp':  ['e','iste','o','imos','ieron'],

# past imperfect
'past_imp': ['a','as','a','amos','an'],
'cond':     ['a','as','a','amos','an'],
'future':   ['é','ás','á','emos','án'] }
    
def get_ending(verb, tense):
    if tense in tenses[2:]:
        return eD[tense]
    if tense == 'past' and verb in irr1:
        return eD['past_sp']
    # present and past p depend on -ar -er -ir
    return eD[tense + '_' + verb[-2:]]

def get_stem(verb, tense):
    stem = verb[:-2]
    if tense == 'past_imp':
        if verb[-2:] == 'ar':
            return stem + 'ab'
        else:
            return stem + 'í'
    elif tense == 'cond':
        return verb + 'í'
    elif tense == 'future':
        return verb
    # for present and past perfect
    else:
        return stem
        
special_stems = { 'dar': ['d','dar'],
           'poder': ['pud','podr'],
           'poner': ['pus','pondr'],
           'tener': ['tuv','tendr'],
           'venir': ['vin','vendr'] }
   
D = { 'dar':   ['doy','das','da','damos','dan'],
      'poder': ['puedo','puedes','puede','podemos','pueden'],
      'poner': ['pongo','pones','pone','ponemos','ponen'],
      'tener': ['tengo','tienes','tiene','tenemos','tienen'],
      'venir': ['vengo','vienes','viene','venemos','vienen'] }

def conjugate(verb):
    rL = []
    for tense in tenses:
        if verb in irr:
            if tense == 'present':
                # we just memorize all irr
                rL.append(D[verb])
                continue
            elif tense == 'past':
                # get irregular stem
                stem = special_stems[verb][0]
            elif tense == 'cond':
                # get irregular stem
                stem = special_stems[verb][1]
            elif tense == 'future':
                # get irregular stem
                stem = special_stems[verb][1]
            else:
                stem = get_stem(verb, tense)
        else:  
            stem = get_stem(verb, tense)
        eL = get_ending(verb, tense)
        sL = [stem + e for e in eL]
        rL.append(sL)
    return verb,rL
    
def transpose(L):
    return zip(*L)

def pad(w):
    wd = 14
    # if the last letter is accented
    # ljust puts one less than needed (b/c len is more)
    accents = ['\xb3','\xad','\xa9']
    if not w[-1] in accents:
        return w.ljust(wd)
    return w.ljust(wd+1)

def fmt(L):
    #print L
    if trans:
        L = transpose(L)
    pL = []
    for sL in L:
        row = ''.join([pad(w) for w in sL])
        pL.append(row)
    return '\n'.join(pL)
    
verbs = reg + irr
for verb in verbs:
    verb,L = conjugate(verb)
    s = fmt(L)
    print verb
    print s
    print
