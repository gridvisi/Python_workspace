'''
# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings

try:
    alternateCase = alternate_case
except:
    pass

Test.describe("Basic Tests")

test.assert_equals(alternateCase("ABC"),"abc")
test.assert_equals(alternateCase(""),"")
test.assert_equals(alternateCase(" ")," ")
test.assert_equals(alternateCase("Hello World"),"hELLO wORLD")
test.assert_equals(alternateCase("cODEwARS"),"CodeWars")
test.assert_equals(alternateCase("i LIKE MAKING KATAS VERY MUCH"),"I like making katas very much")
'''

def alternateCase(s):
    # your code here
    return ''.join([i.upper() if i == i.lower() else i.lower() for i in s])
s = "hELLO wORLD"
print(alternateCase(s))

def alternateCase(s):
    return s.swapcase()