'''
https://www.codewars.com/kata/568dc69683322417eb00002c/train/python

Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

tripleX("abraxxxas") → true
tripleX("xoxotrololololololoxxx") → false
tripleX("softX kitty, warm kitty, xxxxx") → true
tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
FUNDAMENTALSSTRINGSLOOPSCONTROL FLOWBASIC LANGUAGE FEATURESREGULAR EXPRESSIONSDECLARATIVE
PROGRAMMINGADVANCED LANGUAGE FEATURES
'''
s = "softX kitty, warm kitty, xxxxx"
print(s.find('x'))

#19th solution by ericlee
def triple_x(s):
    for i,e in enumerate(s):
        if e=='x':
            return s[i+1:i+3] == 'xx'

print(triple_x(s))


#1st solution
def triple_x(s: str) -> bool:
    return 0 <= s.find("x") == s.find("xxx")


import re

def triple_x(s):
    return re.match('[^x]*xxx', s) is not None
'''
def triple_x(s):
    cnt = ''
    i,j = 0, 1
    while i < j < len(s)-1:

        if s[i] != s[j] or s[i] != s[i].lower() or s[i] != 'x':
            i += 1
            j += 1
        else:
            if s[i] == s[j] == 'x':

                cnt += s[j]
                start,end = i,j
                j += 1

            if len(cnt) >= 3:
                return True
            else:
                i = j
                j += 1
        return False

'''