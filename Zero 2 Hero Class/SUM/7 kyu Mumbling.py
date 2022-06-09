'''
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
'''


s = "abcd"
def accum(s):
    word = ''
    for i,e in enumerate(s,1):
        word += e.title() + (i-1)*e.lower() +'-'
    return word[:-1]

#1st
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))