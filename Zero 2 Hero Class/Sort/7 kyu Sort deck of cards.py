'''
https://www.codewars.com/kata/56f399b59821793533000683/train/python

Write a function sort_cards() that sorts a shuffled list of cards, so that any
given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards
looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
'''


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    """
    template = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    return sorted(cards,key=lambda x:template.index(x))

cards = ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']
print(sort_cards(cards))

#1st
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)