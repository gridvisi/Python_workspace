'''
https://www.codewars.com/kata/5892595f190ca40ad0000095/train/python

@test.describe('Sample Tests')
def sample():
    test.assert_equals(mispelled('versed','xersed'),True)
    test.assert_equals(mispelled('versed','applb'),False)
    test.assert_equals(mispelled('versed','v5rsed'),True)
    test.assert_equals(mispelled('1versed','versed'),True)
    test.assert_equals(mispelled('versed','versed'),True)
'''


def mispelled(word1, word2):
    if word1 == word2: return True
    if any([len(word1) == 0, len(word2) == 0]):
        return False

    if abs(len(word1) - len(word2)) == 1:
        if word2 in word1 or word1 in word2:
            return True
        return False
    elif len(word1) == len(word2):
        return ([(i == j) for i, j in zip(list(word1), list(word2))]).count(False) == 1
    else:
        return False


word1,word2 = '1versed','versed'
#word1,word2 = 'versed','v5rsed'
#word1,word2 = 'versed','versed'
word1,word2 = '','2'
#word1,word2 =  'pxRLSqcTqTXfD' and 'GR'
#word1,word2 = 'Kmp6krr' and '3'


#1st solution
import regex

def mispelled(word1, word2):
    return (word1 == '') == (word2 == '') and regex.fullmatch(r'(?:\L<word1>){1i+1d+1s<=1}', word2, word1=(word1,)) is not None
print(mispelled(word1,word2))

# Not good
def mispelled(word1,word2):
    x = len([i for i in word2 if i not in word1])
    y = len([i for i in word1 if i not in word2])
    print(x,y)
    if x == y == 0:return True
    return (x == 1 or False) or (y == 1 or False)

import difflib
def mispelled(word1,word2):
    d = difflib.Differ()
    return list(d.compare(word1,word2))

def mispelled(word1,word2):
    if any([word1=='',word2=='']):
        return False
    if word2 == word1:return True
    elif abs(len(word1) - len(word2)) == 1:
        if word1 in word2 or word2 in word1:
            return True
    else:
        return ([(i==j) for i,j in zip(list(word1),list(word2))]).count(False) == 1