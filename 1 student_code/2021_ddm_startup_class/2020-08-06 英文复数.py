

#输入需要处理的单词 words

words = ['zoo','bamboo','radio',
'studio','echo', 'ox',
'torpedo','baby','bus',
'box','boy','match',
'fly','paper','glue']

#规则变量初始化

vowel = set('aeiou')
es = {'s','x','sh','ch'}
words = ['own','owe','owel']

def dual_vow(w): #dual_vow
    return all(c in vowel for c in w[-2:])

def isVow_y(w): #cons+dual_vow
    it = iter(w[-2:])
    return next(it) in vowel and next(it) == 'y'

def isCon_y(w): #dual_vow
    it = iter(w[-2:])
    return next(it) not in vowel and next(it) == 'y'

def isEs(w): #{'s','x','sh','ch'}
    it = iter(w[-2:])
    return w[-1] in es or w[-2:] in es

irregular = ['bus','potato','tomato','hero',
'chief','roof','knife']

#不规则单词需要手动持续添加
#主函数
def plural(words):
    Dual_vow = list(map(lambda x:x+'s',filter(dual_vow,words)))
    IsVow_y = list(map(lambda x:x+'s',filter(isVow_y,words)))
    IsCon_y = list(map(lambda x:x+'ies',filter(isCon_y,words)))
    IsEs = list(map(lambda x:x+'es',filter(isEs,words)))
    return {'Dual_vow':Dual_vow,

        'IsVow_y':IsVow_y,

        'IsCon_y':IsCon_y,

        'IsEs':IsEs}

words = ['zoo','bamboo','radio',
'studio','echo', 'ox',
'torpedo','baby','bus',
'box','boy','match',
'fly','paper','glue']
print(plural(words))
print(words)