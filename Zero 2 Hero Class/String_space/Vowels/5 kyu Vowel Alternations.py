'''
https://blog.csdn.net/qq_34500270/article/details/82899057?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

https://www.codewars.com/kata/54221c16dda52609b1000ffb/train/python
This list above is a valid solution instance since the vowels 'a', 'e', 'i', 'o', and 'u' occur
in the same positions between the consonant clusters 'l' and 'st'.

Your program should return a list of all solutions (like the list above) given a list of words
to search through.

Note that order matters. If you prefer to use sets for book-keeping purposes, that is fine, but
you will need to sort your list of solutions, and each solution set itself.

This is easy in Python:

solutions = [set(['last', 'lest', 'list', 'lost', 'lust']),
             set(['bill', 'bull', 'bell', 'ball', 'boll'])]

sorted_soultions = sorted(sorted(solution) for solution in solutions)
sorted_solutions == [['ball', 'bell', 'bill', 'boll', 'bull'],
                     ['last', 'lest', 'list', 'lost', 'lust']]
'''

# Exclude 'y' from vowels since it can't make up its mind if it's a vowel
vowels = 'aeiou'
words = ['aa','blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder']
#print([ord(i) for i in "aeiou"])

def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    step,re,it = 0,{},iter(words)
    for w in words:
        re[w] = sum([ord(i) for i in w])
    return sorted(re),re
#print(find_solutions(words))

from collections import defaultdict
import re

def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    solutions = defaultdict(list)
    for word in words:
        category = re.sub("[aeiou]", "*", word)
        solutions[category].append(word)
    return sorted(sorted(sol) for sol in solutions.itervalues() if len(sol) == 5)


import re
from collections import defaultdict
VOWELS = 'aeiou'
PATTERN = re.compile(r'[' + VOWELS + ']')
def find_solutions(words):
    transDct = defaultdict(set)
    for w in words:
        transDct[PATTERN.sub('_', w)].add(w)
        print('2:',transDct)
    return sorted(sorted(v) for v in transDct.values() if len(v) >= 5 )
print(find_solutions(words))

vowels = 'aeiou'
def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    return [s for s in ([w.replace('a', v) for v in 'aeiou'] for w in words if 'a' in w) if all(w in words for w in s)]

'''
tests = [
    ['last', 'lest', 'list', 'lost', 'lust'],
    ['beryl', 'jigsawed', 'oospheres', 'troweller', 'volcanizes'],
    ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder'],
'''