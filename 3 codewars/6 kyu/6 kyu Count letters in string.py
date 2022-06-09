'''
https://www.codewars.com/kata/count-letters-in-string/train/python
n this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.
Example:
letter_count('arithmetics') #=>
{"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

'''
s ='arithmetics'
def letter_count(s):
    letter = list(s)
    ct = []
    for i in s:
        ct.append(s.count(i))
    return dict(zip(letter,ct))
print(letter_count(s))

from collections import Counter
def letter_count(s):
    return Counter(s)

from collections import Counter as letter_count

def letter_count(s):
    return {i: s.count(i) for i in s}

