#https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''
word, words = 'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']
word, words = 'abba', ['aabb', 'abcd', 'bbaa', 'dada','ababaab']
def anagrams(word, words):
    return [w for w in words if set(w) == set(word) and len(w) == len(word)]

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
print(anagrams(word, words))

def anagrams(word, words):
    return [w for w in words if sorted(list(w)) == sorted(list(word))]
print(anagrams(word, words))