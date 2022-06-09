'''
https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python

Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
should return false:

isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")
'''

#ericlee
def isDigit(string):
    return all([i in '0123456789.-' and i.isdigit for i in string])

#1st
def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False

#1st check point: Not pass
def isDigit(string):
    try:
        if float(string):
            return True
    except: return False

#2nd
def isDigit(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False