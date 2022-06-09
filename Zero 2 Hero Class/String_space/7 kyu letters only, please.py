'''
https://www.codewars.com/kata/59be6bdc4f98a8a9c700007d/train/python


'''

import string
def remove_chars(s):
    return ''.join([i for i in s if i in string.ascii_letters + ' '])
s = 'john.dope@dopington.com'
print(remove_chars(s))

#1st
import re
def remove_chars(s):
    return re.sub(r'[^a-zA-Z ]', '', s)