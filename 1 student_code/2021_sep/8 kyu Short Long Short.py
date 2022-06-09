'''
https://www.codewars.com/kata/50654ddff44f800200000007/train/python
'''

def solution(a, b):
    s,l = sorted([a,b],key=len)
    return s+l+s

#1st
def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b

