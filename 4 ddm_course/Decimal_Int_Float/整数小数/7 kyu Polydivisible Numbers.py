'''
https://www.codewars.com/kata/5e4217e476126b000170489b/train/python

Polydivisib... huh what?
So what are they?

A polydivisible number is divisible in an unusual way. The first digit is cleanly divisible by 1, the first two digits are cleanly divisible by 2, the first three by 3, and so on.

Examples
Let's take the number 1232 as an example.

1     / 1 = 1     // Works
12    / 2 = 6     // Works
123   / 3 = 41    // Works
1232  / 4 = 308   // Works

@test.describe("Basic tests")
def __():
    test.assert_equals(polydivisible(1232), True)
    test.assert_equals(polydivisible(123220), False)
    test.assert_equals(polydivisible(0), True)
    test.assert_equals(polydivisible(1), True)
    test.assert_equals(polydivisible(141), True)
    test.assert_equals(polydivisible(1234), False)
    test.assert_equals(polydivisible(21234), False)
    test.assert_equals(polydivisible(81352), False)
    test.assert_equals(polydivisible(987654), True)
    test.assert_equals(polydivisible(1020005), True)
    test.assert_equals(polydivisible(9876545), True)
    test.assert_equals(polydivisible(381654729), True)
    test.assert_equals(polydivisible(1073741823), False)
'''
#16th solution by ericlee
def polydivisible(x):
    return all([eval(str(x)[:i+1])%(i+1) == 0 for i,e in enumerate(str(x))])


def polydivisible(x):
    for i in range(1, len(str(x)) + 1):
        if int(str(x)[:i]) % i != 0:
            return False
    return True

def polydivisible(x):
    s = str(x)
    return all(int(s[:i]) % i == 0 for i in range(1, len(s) + 1))

