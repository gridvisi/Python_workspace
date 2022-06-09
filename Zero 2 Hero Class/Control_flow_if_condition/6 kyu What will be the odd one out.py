'''
https://www.codewars.com/kata/55b080eabb080cd6f8000035/train/python

Test.assert_equals(odd_one_out('Hello World'), ["H", "e", " ", "W", "r", "l", "d"])
Test.assert_equals(odd_one_out('Codewars'), ["C", "o", "d", "e", "w", "a", "r", "s"])
Test.assert_equals(odd_one_out('woowee'), [])
Test.assert_equals(odd_one_out('wwoooowweeee'), [])
Test.assert_equals(odd_one_out('racecar'), ["e"])
Test.assert_equals(odd_one_out('Mamma'), ["M"])
Test.assert_equals(odd_one_out('Mama'), ["M", "m"])
Test.assert_equals(odd_one_out('¼ x 4 = 1'), ["¼", "x", "4", "=", "1"])
Test.assert_equals(odd_one_out('¼ x 4 = 1 and ½ x 4 = 2'), ["¼", "1", "a", "n", "d", "½", "2"])
'''

#10th solve by ericlee
from collections import Counter
def odd_one_out(s):
    sdict = dict((k,v) for k,v in Counter(s[::-1]).items() if v%2==1)
    return list(sdict.keys())[::-1]
s = '¼ x 4 = 1 and ½ x 4 = 2'
print(odd_one_out(s))


#1st
from collections import Counter
def odd_one_out(s):
    d = Counter(reversed(s))
    return [x for x in d if d[x] % 2][::-1]

#2nd
def odd_one_out(s):
    d = {}
    for i in s:
        if i in d:
            del d[i]
        else:
            d[i] = None
    return list(d.keys())

#3rd
from collections import Counter

def odd_one_out(s):
    return [k for k, v in Counter(s[::-1]).items() if v % 2][::-1]