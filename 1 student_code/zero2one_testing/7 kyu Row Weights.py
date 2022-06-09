'''
https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

Test.describe("Basic tests")
Test.assert_equals(row_weights([80]), (80,0))
Test.assert_equals(row_weights([100,50]), (100,50))
Test.assert_equals(row_weights([50,60,70,80]), (120,140))
Test.assert_equals(row_weights([13,27,49]), (62,27))
Test.assert_equals(row_weights([70,58,75,34,91]), (236,92))
Test.assert_equals(row_weights([29,83,67,53,19,28,96]), (211,164))
Test.assert_equals(row_weights([0]), (0,0))
Test.assert_equals(row_weights([100,51,50,100]), (150,151))
Test.assert_equals(row_weights([39,84,74,18,59,72,35,61]), (207,235))
Test.assert_equals(row_weights([0,1,0]), (0,1))
'''
array = [39,84,74,18,59,72,35,61]
def row_weights(array):
    left = sum([e for i,e in enumerate(array) if i%2 == 0])
    return [left,sum(array)-left]
print(row_weights(array))


#1st solution
def row_weights(array):
    return sum(array[::2]), sum(array[1::2])