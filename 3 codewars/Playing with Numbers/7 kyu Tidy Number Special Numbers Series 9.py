'''
https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

Explanation:
The Number's Digits {1 , 0, 2, 4} are not in non-Decreasing Order as 0 <= 1 .
'''


def tidyNumber(n):
    return list(str(n)) == sorted(list(str(n)))

#1st
def tidyNumber(n):
    s = list(str(n))
    return s == sorted(s)

