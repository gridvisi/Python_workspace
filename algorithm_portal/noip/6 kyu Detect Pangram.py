'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
pangram是一个包含字母表中每个字母至少一次的句子。例如，“快速的棕色狐狸跳过懒惰的狗”这个句子是一个pangram，因为它至少使用了一次字母a-Z（case是不相关的）。
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
给定一个字符串，检测它是否为pangram。如果是，则返回True；如果不是，则返回False。忽略数字和标点符号。

string = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+', "",line)
'''
import re
line = pangram = "The quick, brown fox jumps over the lazy dog!"

st = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",line)
print(st)
import string
def is_pangram(s):
    sl = string.ascii_letters
    s = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",s)
    #it = iter(s)
    #print(list(it))
    return all(x in s for x in sl)
s = 'The quick brown fox jumps over the lazy dog!'
s = 'The quick brown fox jumps over the lazy dog!'
s = 'How quickly daft jumping zebras vex.'

s = 'abcdefghijklmopqrstuvwxyz '
import string
def is_pangram(s):
    sl = string.ascii_letters
    #s = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+
    for x in sl[:26]:
        print(x)
        if x not in s.lower():return (False,x)
    return True
print(is_pangram(s))

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())


def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.lowercase)
'''
Test Results:
False should equal True
Cwm fjord bank glyphs vext quiz is a pangram: False should equal True
Pack my box with five dozen liquor jugs. is a pangram: False should equal True
How quickly daft jumping zebras vex. is a pangram: False should equal True
ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ is a pangram: False should equal True
Test Passed
abcdefghijklmopqrstuvwxyz is not a pangram.: True should equal False

reg = [(&nbsp;)|(" ")|(r'，')|(\\-)|(\\、)|(\\。)|(\\：)|(\\？)|(\\（）)|(&nbsp;)|(<img.*?>)|(<br>)|(</br>)|(<br/>)|(<span.*?>)|(</span>)|(<p.*?>)|(</p >)|(<u.*?>)|(</u>)|(<sup.*?>)|(</sup>)|(<sub.*?>)|(</sub>)|(<font.*?>)|(</font>)|(<strong.*?>)|(</strong>)|(</underpoint>)|(<b>)|(</b>)|(\s+)|(,)|(:)|(\\·)|(\\“)|(\\；)|(\\《)|(\\》)|(\\__)|(\\”)]
res['choice']=res['choice'].apply(lambda x:re.sub(reg,'',x))

'''