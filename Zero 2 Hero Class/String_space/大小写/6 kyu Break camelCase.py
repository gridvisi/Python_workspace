'''
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
FUNDAMENTALSSTRINGSFORMATTINGALGORITHMS
'''

print(ord('a'))

def solution(s):
    return ''.join([' '+i if ord(i)<97 else i for i in s])
s = "camelCasing"
print(solution(s))


#1st
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


#2nd
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

#3rd
def solution(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string