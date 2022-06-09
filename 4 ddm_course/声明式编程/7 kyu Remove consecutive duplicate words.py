'''
https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python

import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');

'''
#9th solution by ericlee
def remove_consecutive_duplicates(s):
    flag = s.split(' ')[0]
    ans = flag
    for i,w in enumerate(s.split(' '),1):
        #print(flag,w,s.split(' '))
        if w != flag:
            ans +=' ' + w
            flag = w
        elif w == flag:
            pass
    return ans
s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(remove_consecutive_duplicates(s))

#1st solution
from itertools import groupby
from operator import itemgetter

def remove_consecutive_duplicates(s):
    return ' '.join(map(itemgetter(0), groupby(s.split())))

#2nd solution
from itertools import groupby

def remove_consecutive_duplicates(s):
    return ' '.join(k for k,_ in groupby(s.split()))

#3rd solution
def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)

#4th solution
import re
def remove_consecutive_duplicates(s):
    return re.sub(r"\b(\w+)(\s(\1\b))+", r"\1", s)


#5th solution
def remove_consecutive_duplicates(s):
    words = []
    for (word1, word2) in zip(s.split(), s.split()[1:] + ['']):
        if word1 != word2:
            words.append(word1)
    return ' '.join(words)