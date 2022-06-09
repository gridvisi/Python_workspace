'''
https://www.codewars.com/kata/split-strings/python
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:g
solution('abc') # shhould return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''
s = 'abcdefg'

def solution(s):
    re = []
    for i in range(0,len(s),3):
        print('tance',i)
        re.append(s[i:i+3])
    if len(re[-2]) == 2:
        re[-2] = re[-2]+'_'
    return re,len(s)

print(solution(s))


import re
def solution(s):
    return re.findall(".{2}", s + "_")

import re
def solution(s):
    return re.findall('..', s + '_')


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result