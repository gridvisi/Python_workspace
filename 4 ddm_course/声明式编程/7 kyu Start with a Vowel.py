'''
https://www.codewars.com/kata/5a02e9c19f8e2dbd50000167/train/python

import codewars_test as test
from solution import vowel_start

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(vowel_start('It is beautiful weather today!'), 'it isb e a ut if ulw e ath ert od ay',)
        test.assert_equals(vowel_start('Coding is great'),'c od ing isgr e at',)
        test.assert_equals(vowel_start('my number is 0208-533-2325'),'myn umb er is02085332325' ,)
        test.assert_equals(vowel_start('oranges, apples, melon, pineapple'), 'or ang es appl esm el onp in e appl e', )
        test.assert_equals(vowel_start('under_score'), 'und ersc or e')

创建一个函数，接受任何句子，并重新分配空格（如果需要的话，还可以添加额外的空格），使每个单词都以元音开头。字母的顺序应该是
一样的，但是句子中的每个元音应该是一个新单词的开始。新句子中的第一个单词可以不以元音开头。它应该返回一个全小写的字符串，
没有标点符号（只有字母数字字符）。

例子 'It is beautiful weather today!' 变成'it isb e a ut if ulw e ath ert od ay' 'Coding is great'
变成'c od ing isgr e at' 'my number is 0208-533-2325' 变成'myn umb er is02085332325' 。
'''

st = 'my number is 0208-533-2325'  # 'myn umb er is02085332325'

#11th solution by ericlee
def vowel_start(st):
    sl = [i.lower() for i in st if i.isalnum()]
    return ''.join([" " + e if e.lower() in 'aeiou' else e for e in sl]).strip()
print(vowel_start(st))

#1st solution
from re import sub
def vowel_start(st):
    return sub(r'(?<=.)([aeiou])', r' \1', sub(r'[^a-z0-9]', '', st.lower()))

#2nd solution
from re import sub

def vowel_start(st):
    return sub(r"\B([aeiou])", r" \1", ''.join(filter(str.isalnum, st)).lower())

#3rd solution
def vowel_start(s):
    r = ''
    for letter in s:
        if letter in 'aeiouAEIOU':
            r+=' '+letter.lower()
        elif letter.isalnum():
            r+=letter.lower()
    return r.lstrip(' ')

#4th solution
from string import ascii_lowercase, digits

def vowel_start(st):
    return ''.join([
        (' ' + c) if c in 'aeiou' else c
        for c in st.lower()
        if c in ascii_lowercase + digits
    ]).lstrip()

#5 solution
def vowel_start(stg):
    return "".join(f"{' ' if c in 'aeiou' else ''}{c}" for c in stg.lower() if c.isalnum()).lstrip()

def vowel_start(st):
    return ''.join(' ' * (i in 'aeiou') + i for i in st.lower() if i.isalnum()).strip()

def vowel_start(st):
    sl = [i.lower() for i in st if i.isalnum()]
    return ''.join([" " + e if e.lower() in 'aeiou' else e for e in sl]).strip()
