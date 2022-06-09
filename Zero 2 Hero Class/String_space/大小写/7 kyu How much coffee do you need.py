# https://www.codewars.com/kata/57de78848a8b8df8f10005b1/train/python
'''
test.describe("Basic Tests")
test.assert_equals(how_much_coffee([]), 0)
test.assert_equals(how_much_coffee(['cw']), 1)
test.assert_equals(how_much_coffee(['CW']), 2)
test.assert_equals(how_much_coffee(['cw','CAT']), 3)
test.assert_equals(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
test.assert_equals(how_much_coffee(['cw','CAT', 'cw=others']), 3)

'''
print("ABC".lower())
print('Abc'.islower())
print('abc'.islower())

def how_much_coffee(events):
    flag = [i.isupper()+1 for i in events]
    return sum(flag) if sum(flag) <=3 else 'You need extra sleep'

#1st
cs={'cw':1,'CW':2,'cat':1,'CAT':2,'dog':1,'DOG':2,'movie':1,'MOVIE':2}

def how_much_coffee(events):
    c=sum(cs.get(e,0) for e in events)
    return 'You need extra sleep' if c>3 else c