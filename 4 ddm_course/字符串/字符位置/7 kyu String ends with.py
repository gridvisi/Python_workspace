'''
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns fals
'''

def solution(string, ending):
    return string[::-1].find(ending[::-1]) == 0
string, ending = 'abc', 'bc'
print(solution(string, ending))

def solution(string, ending):
    return string.endswith(ending)

from re import search, escape

def solution(string, ending):
    return bool(search(escape(ending)+'\Z',string))

def solution(string, ending):
    return string[-len(ending):] == ending if len(ending) else True