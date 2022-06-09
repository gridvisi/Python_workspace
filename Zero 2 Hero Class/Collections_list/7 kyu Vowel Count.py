#https://www.codewars.com/kata/54ff3102c1bad923760001f3/solutions/python

#ericlee
def getCount(sentence):
    return sum([sentence.count(i) for i in 'aeiou'])


#1st
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

#2nd
def getCount(s):
    return sum(c in 'aeiou' for c in s)

#3rd
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))