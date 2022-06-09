'''
https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python
For example:

grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
Should return ["sport", "ports"].
'''
word, possible_words = "ortsp", ["sport", "parrot", "ports", "matey"]
def grabscrab(word, possible_words):

    return [w for w in possible_words if sorted(w) == sorted(word)]
print(grabscrab(word, possible_words))