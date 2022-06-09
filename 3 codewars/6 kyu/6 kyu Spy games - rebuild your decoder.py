# https://www.codewars.com/kata/586988b82e8d9cdc520003ac/train/python
'''
sum of integers in "x20*6<xY" --> 2 + 0 + 6 = 8
sum of integers in "y_r9L" --> 9
'''
import string
print(string.ascii_letters)
s = ' ' + string.ascii_letters
code = 'x20*6<xY y875_r97L'
#code = '8S6 K00= 3Ob28W4'
def decrypt(code):
    code_sum = [sum([int(i) for i in e if i.isnumeric()]) for e in code.split(' ')]
    return ''.join([s[i] for i in code_sum])
print(decrypt(code))