'''
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python
Jumping number is the number that All adjacent digits in it differ by 1.
Test.describe("Sample Test")
Test.it("Single Digit Number")
test.assert_equals(jumping_number(1), "Jumping!!")
test.assert_equals(jumping_number(7), "Jumping!!")
test.assert_equals(jumping_number(9), "Jumping!!")

Test.it("Two Digit Number")
test.assert_equals(jumping_number(23), "Jumping!!")
test.assert_equals(jumping_number(32), "Jumping!!")
test.assert_equals(jumping_number(79), "Not!!")
test.assert_equals(jumping_number(98), "Jumping!!")

Test.it("Larger Numbers")
test.assert_equals(jumping_number(8987)    , "Jumping!!")
test.assert_equals(jumping_number(4343456) , "Jumping!!")
test.assert_equals(jumping_number(98789876), "Jumping!!")
'''

#25th solution by ericlee
def jumping_number(number):
    return "Jumping!!" if all([abs(int(str(number)[i])-int(str(number)[i-1]))==1 for i in range(1,len(str(number)))]) else "Not!!"

#1st solution
def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

from numpy import diff
def jumping_number(number):
    return "Jumping!!" if all([abs(x) == 1 for x in diff([int(x) for x in str(number)])]) else "Not!!"

