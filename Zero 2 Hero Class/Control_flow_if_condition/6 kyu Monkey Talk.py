'''
https://www.codewars.com/kata/59f897ecc374cb9ed90000c2/train/python

import codewars_test as test
from solution import monkey_talk

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(monkey_talk('Hello'), 'Ook.')
        test.assert_equals(monkey_talk('Everyone'), 'Eek.')
        test.assert_equals(monkey_talk('Hello Everyone'), 'Ook eek.')
        test.assert_equals(monkey_talk('Everyone Hello'), 'Eek ook.')
'''

def monkey_talk(phrase):
    return ' '.join([f"{w[-1]}{w[-1]}{'k'}" for i,w in enumerate(phrase.split(" "))]).capitalize()
#[f"{w[-(i==0)]}{w[-1]}{'k'}" for i,w in enumerate(phrase.split(" "))]
phrase = 'Hello Everyone'
phrase = 'Everyone Hello'
print(monkey_talk(phrase))