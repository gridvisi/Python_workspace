'''
https://www.codewars.com/kata/553a2461098c64ae53000041/train/python

wordify(1) == "one"
wordify(12) == "twelve"
wordify(17) == "seventeen"
wordify(56) == "fifty six"
wordify(90) == "ninety"
wordify(326) == "three hundred twenty six"
'''

from num2words import num2words
def numtoword(x):
    return num2words(x)
x = 234
print(numtoword(x))