'''
groupby()
将key函数作用于原循环器的各个元素。根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。
每个新的循环器以函数返回结果为标签。
这就好像一群人的身高作为循环器。我们可以使 用这样一个key函数: 如果身高大于180，返回"tall"；
如果身高底于160，返回"short";中间的返回"middle"。最终，所有身高将分为三个循环器，
即"tall", "short", "middle"。

'''

from itertools import *
def height_class(h):
    if h > 180:
        return 'tall'
    elif h < 160:
        return 'short'
    else:
        return 'middle'

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
friends = sorted(friends,key = height_class)
for m,n in groupby(friends,key = height_class):
    print(m,':',list(n))
    print(list(n))  #why was it empty for list(n)



# codewars 6kyu
s = 'You CAN YOU UPUUPPP'

from itertools import groupby
def reverse(s):
    res = ''
    for c, group in groupby(s):
        print(c,list(group))
        w = ''.join(group)
        print('w:',w)
        if len(w) > 1:
            w = w.swapcase()
            print('ww:',w)
        res += w
    return res

print(reverse(s))

import re
def reverse(s):
    return re.sub(r'(.)\1+', lambda m: m.group().swapcase(), s)

