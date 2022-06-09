'''
https://www.codewars.com/kata/55b080eabb080cd6f8000035/train/python
odd_one_out('Hello World')   ==  ["H", "e", " ", "W", "r", "l", "d"]
odd_one_out('Codewars')      ==  ["C", "o", "d", "e", "w", "a", "r", "s"]
odd_one_out('woowee')        ==  []
odd_one_out('wwoooowweeee')  ==  []
odd_one_out('racecar')       ==  ["e"]
odd_one_out('Mamma')         ==  ["M"]
odd_one_out('Mama')          ==  ["M", "m"]
'''
s = 'wwoooowweeee'
#s = 'Mama'
#s = 'racecar'
#s = 'Hello World'
s = '¼ x 4 = 1 and ½ x 4 = 2'
s = 'Hello World'
from collections import deque
def odd_one_out(s):
    d,re = deque(s),deque('')
    res = []
    for e in s:
        if e not in res:
            res.append(e)
        else:res.remove(e)
    return res
print(odd_one_out(s))

from collections import Counter
def odd_one_out(s):
    d = Counter(reversed(s))
    print([x for x in d])
    return [x for x in d if d[x] % 2][::-1]
print(odd_one_out(s))

from collections import Counter
def odd_one_out(s):
    return [k for k, v in Counter(s[::-1]).items() if v % 2][::-1]

def odd_one_out(s):
    d = {}
    for i in s:
        if i in d:
            del d[i]
        else:
            d[i] = None
    return list(d.keys()),d
print(odd_one_out(s))
'''
 
def odd_one_out(s):
    re,res,result = list(s),[],[]
    bench = [0] + [re.index(i) for i in re if i == ' '] + [len(s)]
    for i in range(len(bench) - 1):
        sl = re[bench[i]:bench[i + 1]]
        for e in sl:
            if sl.count(e) % 2 == 1:
                res.append(e)
    for j in res:
        if res.count(j) % 2 == 1:
            result.append(j)
    return result
'''
