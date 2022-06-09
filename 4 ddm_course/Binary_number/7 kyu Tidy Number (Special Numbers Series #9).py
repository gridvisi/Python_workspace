'''
https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

test.describe("Basic Tests")

test.it("Sample Tests")

test.assert_equals(tidyNumber(12), True)
test.assert_equals(tidyNumber(102), False)
test.assert_equals(tidyNumber(9672), False)
test.assert_equals(tidyNumber(2789), True)
'''
def tidyNumber(n):
    return list(str(n)) == sorted(list(str(n)))

def tidyNumber(n):
    s = list(str(n))
    return s == sorted(s)


def binNumber(n):
    return bin(n)[2:].count('1')==1