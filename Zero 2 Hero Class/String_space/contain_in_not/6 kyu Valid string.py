'''
https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/train/python
'''
# 互斥的if

#1st solution
def valid_word(seq, word):
    return not word or any(valid_word(seq,word[len(x):]) for x in seq if word.startswith(x))

#re
import re
def valid_word(seq, word):
    regex = '^(' + '|'.join(seq) + ')+$'
    if re.match(regex, word):
        return True
    return False

#
from typing import List

def valid_word(seq: List[str], word: str) -> bool:
    return not word or any(word.startswith(w) and valid_word(seq, word[len(w):]) for w in seq)


# ericlee draft
def valid_word(seq, word):
    keys = seq
    wd = word
    for w in seq:
        print(w,wd)
        wd = wd.split(w)
    return wd

seq,word = ['code', 'star', 'wars'], 'starwars'
print(valid_word(seq,word))




def valid_word(seq, word):
    # your code here
    if all([w in word for w in seq]):

        return True
    elif any([w in word for w in seq]):
        return   #''.join(seq) == word

def valid_word(seq, word):
    def rec(word):
        if not word: return True
        for prefix in seq:
            if word.startswith(prefix):
                test = rec(word[len(prefix):])
                if test: return True
        return False
    return rec(word)