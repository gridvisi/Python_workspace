'''
https://www.codewars.com/kata/523a86aa4230ebb5420001e1/solutions/python

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
ALGORITHMSSTRINGS
'''
# solve by ericlee
def anagrams(word, words):
    ans = []
    for w in words:
        if set(word) == set(w) and len(word) == len(w):
            ans.append(w)
    return ans

#1st
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]

#2nd
def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)

#3rd
from collections import Counter

def anagrams(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]

