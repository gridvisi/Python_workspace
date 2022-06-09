'''
https://www.codewars.com/kata/59126cd3379de6ca5f00019c/train/python
'''
#chr(x) num -> letter
# upper(65->90)  lower(97->122)

#21st by ericlee
def case_unification(x):
    b = len([i for i in x if ord(i) <= 90]) > len(x)//2
    return x.upper() if b else x.lower()

x = 'z'
print(case_unification(x))


import re

def case_unification(s):
    return s.lower() if len(re.findall("[a-z]", s)) > len(s)/2 else s.upper()


def case_unification(s):
    len_s = len(s)
    low = sum(letter.islower() for letter in s)
    upp = len_s - low
    return s.lower() if low > upp else s.upper()

def case_unification(s):
    l = sum(1 if i.isupper() else -1 for i in s)
    return s.lower() if l < 0 else s.upper()