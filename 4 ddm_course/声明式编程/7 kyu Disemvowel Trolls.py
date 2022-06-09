# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

'''
test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")
'''

def disemvowel(string):
    return ''.join([i for i in string if i not in 'aeiouAEIOU'])

string = "This website is for losers LOL!"
print(disemvowel(string))

#1st solution
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)