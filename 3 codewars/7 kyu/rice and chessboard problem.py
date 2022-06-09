'''
https://www.codewars.com/kata/the-wheat-slash-rice-and-chessboard-problem/train/python
squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
'''

# suppose the number of rice between the 2**n and 2**(n+1)
# if n=0
grains = 0#17171
def squares_needed(grains):
    if grains == 0:return 0
    else:
        return len(str(bin(grains))[2:])

def squares_needed(grains):
    return grains.bit_length()

squares_needed = int.bit_length

from math import log2, ceil
def squares_needed(grains):
    return grains and ceil(log2(grains+1))

print(squares_needed(grains))