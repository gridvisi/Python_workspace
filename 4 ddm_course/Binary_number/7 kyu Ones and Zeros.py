'''
https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

Test.describe("One's and Zero's")
Test.it("Example tests")
Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)
'''
arr = [1,1,1,1]
def binary_array_to_number(arr):
    return sum([2**i*e for i,e in enumerate(arr[::-1])])

print(binary_array_to_number(arr))

#1st solution
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)