'''
https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

Make a program that takes a value (x) and returns "Bang" if the
number is divisible by 3, "Boom" if it is divisible by 5,
"BangBoom" if it divisible by 3 and 5, and "Miss"

if it isn't divisible by any of them. Note:
Your program should only return one value

Ex: Input: 105 --> Output: "BangBoom"
Ex: Input: 9 --> Output: "Bang"
Ex:Input: 25 --> Output: "Boom"

FUNDAMENTALS

test.assert_equals(multiple(30), "BangBoom")
test.assert_equals(multiple(3), "Bang")
test.assert_equals(multiple(98),"Miss")
test.assert_equals(multiple(65),"Boom")
test.assert_equals(multiple(23),"Miss")
test.assert_equals(multiple(15),"BangBoom")
'''


def multiple(x):
    if x % 3 == 0 and x % 5 != 0:
        return "Bang"

    elif x % 3 != 0 and x % 5 == 0:
        return "Boom"

    elif x % 3 == 0 and x % 5 == 0:
        return "BangBoom"
    else:
        return "Miss"
#1st
def multiple(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'

#2nd
def multiple(x):
    if x % 15 == 0: return "BangBoom"
    if x % 5 == 0: return "Boom"
    if x % 3 == 0: return "Bang"
    return "Miss"

def multiple(x):
    val = ''
    if x % 3 == 0:
        val += 'Bang'
    if x % 5 == 0:
        val += 'Boom'
    if val == '':
        val = 'Miss'
    return val

#3rd
def multiple(x):
    return"BangBoom" if not x % 15 else ("Boom" if not x % 5 else ("Bang" if not x % 3 else "Miss"))


#4th
def multiple(x):
    #Good Luck
    return ['Miss', 'Bang', 'Boom', 'BangBoom'][(x%3 == 0) + (x%5 == 0)*2]