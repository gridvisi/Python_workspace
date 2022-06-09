'''
https://www.codewars.com/kata/57cff961eca260b71900008f/train/python
Given an array of numbers, check if any of the numbers are the
character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.
def is_vow(inp):
    pass
'''
def is_vow(inp): # num -> str if ord
    return [ord(i) if i in ('a', 'e', 'i', 'o', 'u') else i for i in inp]
inp = [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
print(is_vow(inp))

#1st
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]

#2nd
def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp

#3rd cool!
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]

#4th
def is_vow(inp):
    for n in range(0,len(inp)):
        if inp[n] == 97: inp[n] = 'a'
        if inp[n] == 101: inp[n] = 'e'
        if inp[n] == 105: inp[n] = 'i'
        if inp[n] == 111: inp[n] = 'o'
        if inp[n] == 117: inp[n] = 'u'
    return inp