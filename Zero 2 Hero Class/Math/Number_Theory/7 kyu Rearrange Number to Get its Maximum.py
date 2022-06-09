'''
https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python
'''

def max_redigit(num):
    # your code here
    return int(''.join(sorted(list(str(num)),reverse=True)))
num = 123
print(max_redigit(num))