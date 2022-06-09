'''
https://www.codewars.com/kata/559f44187fa851efad000087/train/python
'''

def seven_ate9(str_):
    while True:
        if '797' in str_:
            str_ = str_.replace("797", "77")
        else: return str_

#2nd
def seven_ate9(str_):
    while "797" in str_:
        str_ = str_.replace("797", "77")
    return str_

#1st
def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_


#3rd
import re

def seven_ate9(str_):
    return re.sub(r'79(?=7)', r'7', str_)


def seven_ate9(str_):
    if '797' not in str_:
        return str_
    else:
        return seven_ate9(str_.replace('797', '77'))
str_ = '617976797779777978797'
str_ = '7979797'
print(seven_ate9(str_))