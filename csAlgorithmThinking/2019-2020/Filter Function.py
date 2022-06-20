#24. The Filter() Function
#The filter() function is to filter a sequence using the specified function or lambda function.
# This function returns a filter object, which is an iterator. Overall, its usage is very similar
# to the map() function.
'''
实例所有集合 x 中没有项目存在于集合 y 中，则返回 True：
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook",'aeiou',"banana"}
z = x.isdisjoint(y)
vow = {'aeiou'}
ls = vow.isdisjoint(y)
print(z,ls,set('aeiou'))

def good_word(x: str):
    has_vowels = not set('aeiou').isdisjoint(x.lower())
    long_enough = len(x) > 7
    good_start = x.lower().startswith('pre')
    return has_vowels & long_enough & good_start,has_vowels
words = ['Good', 'Presentation', 'preschool', 'prefix','prccccc']
print(list(filter(good_word, words)))



#w = 'earful,earth early ,earn ,earache ,eardrum ,earl ,earnings earphones ,earpiece ,earplug ,earring, earthly, earth,earlaps,earthy'

words = ['ear','earful', 'Earth','early', 'era', 'earn',
'earache', 'hear', 'earl', 'earnings','earphones',
'swear', 'earplug', 'earring', 'Gear', 'earth',
'earlaps', 'earthy','Bear','tear','wear','heard']

s = set(words)
#word_st = s.startwith('ear')
#print('ww',word_st)

def root_word(w,words):
    #has_vowels = not set('aeiou').isdisjoint(x.lower())
    #long_enough = len(x) > 7
    left_ear = [x for x in words if x.lower().startswith(w)]
    right_ear = [x for x in words if x.lower().endswith(w)]
    return left_ear, right_ear
w = 'ear'
print(root_word(w,words))
#print(list(filter(root_word, words)))

'''
es与s的变化规则
1、代表有生命的（动植物）的单词后加es，例如:potato(土豆),tomato（西红柿）,hero（英雄）,Negro（黑人）。

2、而无生命的单词加s，比如photo(照片)，piano（钢琴），radio（收音机），zoo（动物园），kilo（公斤）。
3、这样,凡外来词则加s。如solos，pianos，kilos，tohaccos，凡词尾以两个元音结尾的词则加s，如：zoos，bamboos，coos，radios，studios。

除此而外,其他的都加es，如echoes（回声），torpedoes（鱼雷）。

2可数名词复数的规则变化
1.直接在名词末尾加s。如：desk-desks

2.以s,x,sh,ch结尾的加es，如：box-boxes,brush-brushes,match-matches

3.以y结尾，前为辅音字母，要变y为i+es。如：baby-babies。但前为元音字母时，直接加s，如：boy-boys

4.以o结尾的名词，有些加词尾-s，有些加-es，有些加-s或-es均可。如：piano/pianos 钢琴tomato/tomatoes 西红柿

5.以f或fe结尾的名词，也有两种可能：即有些直接加词尾-s，有些则把f/fe改为ves：chief/chiefs首领 roof/roofs屋顶
'''

vowel = set('aeiou')
es = {'s','x','sh','ch'}
words = ['own','owe','owel']

w = 'zoo'  #plural_vow(w)
def dual_vow(w): #dual_vow
    return all(c in vowel for c in w[-2:])
print(dual_vow(w))

w = 'boy'
def isVow_y(w): #dual_vow
    it = iter(w[-2:])
    return next(it) in vowel and next(it) == 'y'
print(isVow_y(w))

def isCon_y(w): #dual_vow
    it = iter(w[-2:])
    return next(it) not in vowel and next(it) == 'y'
w = 'baby'
print(isCon_y(w))

def isEs(w): #{'s','x','sh','ch'}
    it = iter(w[-2:])
    return w[-1] in es or w[-2:] in es
w = ['box','brush','match'] # boxes-brushes-matches
print([isEs(w) for w in w])
print(isEs(w[0]))

irregular = ['bus','potato','tomato','hero','chief','roof','knife']

words = ['zoo','bamboo','radio',
         'studio','echo', 'ox',
         'torpedo','baby','bus',
         'box','boy','match',
         'fly','paper','glue']

def plural(words):
    Dual_vow = list(map(lambda x:x+'s',filter(dual_vow,words)))
    IsVow_y = list(map(lambda x:x+'s',filter(isVow_y,words)))
    IsCon_y = list(map(lambda x:x+'ies',filter(isCon_y,words)))
    IsEs = list(map(lambda x:x+'es',filter(isEs,words)))
    return {'Dual_vow':Dual_vow,
            'IsVow_y':IsVow_y,
            'IsCon_y':IsCon_y,
            'IsEs':IsEs}

print(plural(words))

'''
如有其他字符串拼接方法 欢迎留言提出哦
1. 加号
2. 逗号
3. 直接连接
4. 格式化
5. join
6. 多行字符串拼接（）
'''

