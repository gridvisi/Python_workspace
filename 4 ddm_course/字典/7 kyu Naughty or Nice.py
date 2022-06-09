'''
https://www.codewars.com/kata/52a6b34e43c2484ac10000cd/train/python

get_nice_names( [
    { 'name': 'Warrior reading this kata', 'was_nice': True },
    { 'name': 'xDranik', 'was_nice': False },
    { 'name': 'Santa', 'was_nice': True }
] )
# => returns [ 'Warrior reading this kata', 'Santa' ]
'''

people = [
    { 'name': 'Warrior reading this kata', 'was_nice': True },
    { 'name': 'xDranik', 'was_nice': False },
    { 'name': 'Santa', 'was_nice': True }
]
#1st solution by ericlee
def get_nice_names(people):
    return [p['name'] for p in people if p['was_nice']]

def get_naughty_names(people):
    return [p['name'] for p in people if not p['was_nice']]