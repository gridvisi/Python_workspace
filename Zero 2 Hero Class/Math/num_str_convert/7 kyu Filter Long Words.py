'''
https://www.codewars.com/kata/5697fb83f41965761f000052/train/python
'''

def filter_long_words(sentence, n):
    return [w for w in sentence.split(' ') if len(w) > n]

import re
def filter_long_words(sentence, n):
    return re.findall('[A-Za-z_\(\)]{%s,}' % str(n+1), sentence)

def filter_long_words(sentence, n):
    returnlist = []
    split = str.split(sentence)
    for word in split:
        if len(word) > n:
            returnlist.append(word)
    return returnlist
