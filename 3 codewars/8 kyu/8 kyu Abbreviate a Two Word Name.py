'''
https://www.codewars.com/kata/abbreviate-a-two-word-name/train/javascript
'''

def abbrevName(name):
    return '.'.join([e[0].upper() for e in name.split(' ')])

name = "Patrick Feenan"

print(abbrevName(name))