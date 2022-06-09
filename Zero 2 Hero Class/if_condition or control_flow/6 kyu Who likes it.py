'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
'''

def likes(names):
    persons = len(names)
    if persons == 0:
        return "no one likes this"
    elif persons == 1:
        return f"{names} likes this"
    elif persons == 2:
        return f"{names[0]} and {names[1]} like this"
    elif persons == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif persons > 3:
        return f"{names[0]}, {names[1]} and {persons-2} others like this"


#1st
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)