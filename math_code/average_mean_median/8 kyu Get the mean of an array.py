'''
https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

est.describe("get_average")

Test.it("works for some examples")
Test.assert_equals(get_average([2, 2, 2, 2]), 2, "didn't work for [2, 2, 2, 2]")
Test.assert_equals(get_average([1, 5, 87, 45, 8, 8]), 25, "didn't work for [1, 5, 87, 45, 8, 8]")
Test.assert_equals(get_average([2,5,13,20,16,16,10]), 11, "didn't work for [2,5,13,20,16,16,10]")
Test.assert_equals(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]), 11, "didn't work for [1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]")

'''

def get_average(marks):
    return sum(marks) // len(marks)

