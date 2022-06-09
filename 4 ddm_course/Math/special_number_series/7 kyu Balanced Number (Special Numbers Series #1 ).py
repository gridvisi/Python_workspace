'''
https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

Definition
Balanced number is the number that * The sum of all digits to the left of the
middle digit(s) and the sum of all digits to the right of the middle digit(s)
are equal*.

Test.describe("Sample Tests")
Test.it("Check Balanced Number")
test.assert_equals(balanced_num(7)  , "Balanced");
test.assert_equals(balanced_num(959), "Balanced");
test.assert_equals(balanced_num(13) , "Balanced");
test.assert_equals(balanced_num(432), "Not Balanced");
test.assert_equals(balanced_num(424), "Balanced");

Test.it("Check Large Number")
test.assert_equals(balanced_num(1024)    , "Not Balanced")
test.assert_equals(balanced_num(66545)   , "Not Balanced")
test.assert_equals(balanced_num(295591)  , "Not Balanced")
test.assert_equals(balanced_num(1230987) , "Not Balanced")
test.assert_equals(balanced_num(56239814), "Balanced")
'''

def balanced_num(number):
    mid = len(str(number))//2
    left,right = str(number)[:mid],str(number)[-mid:]
    return  "Balanced" if sum([int(i) for i in left]) == sum([int(i) for i in right]) else "Not Balanced"
number = 56239814
#number = 295591
print(balanced_num(number))