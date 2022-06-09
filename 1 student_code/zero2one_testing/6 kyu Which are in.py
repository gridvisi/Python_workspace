'''
https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

In Shell bash a1 and a2 are strings. The return is a string where words are separated by
commas.

Beware: r must be without duplicates.
Don't mutate the inputs.
REFACTORINGARRAYSSEARCHALGORITHMSLISTSDATA STRUCTURESSTRINGS
'''

def in_array(array1, array2):
    ans = []
    for w in array1:
        for ww in array2:
            if w in ww:
                ans.append(w)
    return ans

#1st
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

#3rd
def in_array(array1, array2):
    result = set()
    for a in array1:
        for b in array2:
            if a in b:
                result.add(a)
                break
    return sorted(result)

#4th
def in_array(array1, array2):
    # your code
    return sorted(set([word for word in array1 for word_2 in array2 if word in word_2]))

def in_array(array1, array2):
    return sorted(
        x for x in set(array1)
        if any(x in y for y in array2))