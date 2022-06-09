'''
https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

'''
def array(string):
    #your code here
    return (" ".join(string[1:-1].split(","))).strip(" ")

#1st
def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None