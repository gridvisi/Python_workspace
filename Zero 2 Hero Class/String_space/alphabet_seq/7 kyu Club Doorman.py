'''
https://www.codewars.com/kata/5c563cb78dac1951c2d60f01/train/python

import codewars_test as test
from solution import pass_the_door_man

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals( pass_the_door_man("lettuce") , 60)
        test.assert_equals( pass_the_door_man("hill"), 36)
        test.assert_equals( pass_the_door_man("apple"), 48)
'''

import string
def pass_the_door_man(word):
    #dup = [i for i in word if word.count(i) == 2]
    dup = [e for i,e in enumerate(word[:-1]) if word[i]==word[i+1]]
    print(dup,string.ascii_lowercase.index(dup[0]))
    return 3*sum(string.ascii_lowercase.index(i)+1 for i in set(dup))

word = "lettuce"
word = 'hill'
word = "apple"
print(pass_the_door_man(word))


#1st
def pass_the_door_man(word):
    for i in word:
        if i*2 in word:
            return (ord(i)-96) * 3

#2nd
import re

def pass_the_door_man(word):
    return (ord(re.findall(r'(.)\1', word)[0]) - 96) * 3


