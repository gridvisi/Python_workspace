# 6 kyu
# Pair of gloves
# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python

'''
Pair of gloves
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

Examples:
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)

'''
from collections import Counter
def number_of_pairs(gloves):
    g = Counter(gloves)
    pair = 0
    for k,v in g.items():
        #if not v%2:
        pair += v//2
    return pair

def number_of_pairs(gloves):
    unique = set(gloves)
    return sum(gloves.count(i)//2 for i in unique)

from collections import Counter
def number_of_pairs(gloves):
    return sum(c // 2 for c in Counter(gloves).values())