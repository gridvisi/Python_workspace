'''
https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python
'''

# two testing fail
def isDigit(string):
    return all([i in '0123456789.-' and i.isdigit for i in string])


#1st
def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False


#2
def isDigit(string):
    return string.lstrip('-').replace('.','').isdigit()

def isDigit(string):
    try:
        return isinstance(float(string), float)
    except:
        return False

    
from re import match

def isDigit(string):
    return bool(match(r"^[-+]?\d+\.?\d*?$", string))