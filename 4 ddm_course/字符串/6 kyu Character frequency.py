'''
https://www.codewars.com/kata/53e895e28f9e66a56900011a/train/python

Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.
The function should return a list of tuples (in Python and Haskell) or arrays (in other languages) sorted by the most frequent letters first. The Rust implementation should return an ordered BTreeMap. Letters with the same frequency are ordered alphabetically. For example:
letter_frequency('aaAabb dddDD hhcc')
will return
  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.

写一个函数，接受一段字符串形式的文本，并返回文本的字母频率计数。这个计数不包括数字、空格和所有标点符号。
字符的大写和小写版本是等价的，结果应该都是小写的。

该函数应该返回一个按照最频繁的字母排序的元组列表（在Python和Haskell中）或数组（在其他语言中）。
Rust的实现应该返回一个有序的BTreeMap。具有相同频率的字母按字母顺序排序。例如

'''

# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

from collections import Counter
import string
def letter_frequency(text):
    ans = Counter(text.lower())
    result = sorted([(v, k) for k,v in ans.items() if k in string.ascii_letters],key=lambda x:(x[1]))
    nkey = sorted(dict(result),reverse=True)
    final = dict(zip(nkey,' '*len(nkey)))
    print(final)
    for i in result:
        #if i[0] in nkey:
        final[i[0]] += i[1]
    final = [(v[1:],k) for k,v in final.items()]
    return [(x,v) for k, v in final for x in k]
# Time: 582ms Passed: 65 Failed: 0

# sorted(result,key=lambda x:(x[0],[1])),key=lambda x:(x[1])
#KEY POINT:
#sorted([(k, v) for k,v in ans.items() if k in string.ascii_letters],key=lambda x:(x[1],x[0]),reverse=True)

text = "As long as I'm learning something, I figure I'm OK - it's a decent day."
expected = [('i', 7), ('a', 5), ('e', 5), ('n', 5), ('g', 4), ('s', 4), ('m', 3),
            ('o', 3), ('t', 3), ('d', 2), ('l', 2), ('r', 2), ('c', 1), ('f', 1),
            ('h', 1), ('k', 1), ('u', 1), ('y', 1)]

#text = "Resulting array is of wrong length"

text = 'IWT LDGAS XH HIXAA P LTXGS EAPRT, STHEXIT BN TUUDGIH ID BPZT RATPG PCS ETGUTRI HTCHT DU XI.'
expe = [('t', 12), ('i', 7), ('h', 6), ('a', 5), ('g', 5), ('p', 5), ('x', 5),
        ('d', 4), ('s', 4), ('u', 4), ('e', 3), ('r', 3), ('b', 2), ('c', 2),
        ('l', 2), ('n', 1), ('w', 1), ('z', 1)]


#1st solution
#https://www.codewars.com/kata/53e895e28f9e66a56900011a/solutions/python

from collections import Counter
from operator import itemgetter

def letter_frequency(text):
    items = Counter(c for c in text.lower() if c.isalpha()).items()
    return sorted(
        sorted(items, key=itemgetter(0)),
        key=itemgetter(1),
        reverse=True
    )
print(text.lower())
print(letter_frequency(text))

#2nd solution
from collections import Counter
def letter_frequency(text):
  return sorted(Counter(filter(str.isalpha,
                        text.lower())
                        ).most_common(),
                key=lambda t:(-t[1],t[0]))

#3nd solution
# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

def letter_frequency(text):
  text = text.lower()
  freq = sorted([(l, text.count(l)) for l in set(text) if l.isalpha()], key=lambda k: k[0])
  return sorted(freq, key=lambda k: k[1], reverse=True)

#3rd solution
def letter_frequency(text):
    d = {}
    for i in text:
        if i.isalpha():
            i = i.lower()
            d[i] = d[i] + 1 if i in d else 1
#    return sorted(d.items(), key=lambda (k, v): (-v, k))

#4th solution
def letter_frequency(text):
  text = text.lower()
  freq_count = [(c, text.count(c)) for c in text if c.isalpha()]
  return sorted(list(set(freq_count)), key=lambda x: (-x[1], x[0]))


#5th solution
from collections import Counter
def letter_frequency(text):
    return sorted(Counter(''.join([c for c in text.lower() if c.isalpha()])).items(), key=lambda x: (-x[1],x[0]))


#6th solution
from collections import Counter
from re import sub
import operator


# return a sorted dictionary of letter frequency
def letter_frequency(text):
    # TODO get and sort letter frequency of text
    freq = Counter(sub('[^a-z]', '', text.lower())).iteritems()

    tmp = sorted(freq, key=operator.itemgetter(0), reverse=False)
    return sorted(tmp, key=operator.itemgetter(1), reverse=True)

#7th solution
# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically
from collections import Counter

def letter_frequency(text):
    txt = "".join([c for c in text.lower() if c.isalpha()])
    counts = sorted(Counter(txt).items(), key= lambda item: (-item[1], item[0]))
    return counts

#8th solution
# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

def letter_frequency(text):
    text = [i.lower() for i in text if i.isalpha()]
    from collections import Counter
    c = Counter(text)
    c = [(i,j) for i, j in c.items()]
    return sorted(c, key = lambda x: (-x[1], x[0]))


# 拓展numpy
import numpy as np
data = np.array([[1,2,3,4,5], [1,2,3,6,7], [2,3,4,5,7], [3,4,5,6,7], [4,5,6,7,8]])
idex=np.lexsort([-1*data[:,2], data[:,1], data[:,0]])
#先按第一列升序，再按第二列升序，再按第三列降序
#注意先按后边的关键词排序
sorted_data = data[idex, :]
print(sorted_data)


