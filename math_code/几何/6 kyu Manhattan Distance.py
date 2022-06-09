'''
https://www.codewars.com/kata/52998bf8caa22d98b800003a/train/python
Test.assert_equals(manhattan_distance([1,1],[1,1]), 0)
Test.assert_equals(manhattan_distance([5,4],[3,2]), 4)
Test.assert_equals(manhattan_distance([1,1],[0,3]), 3)
'''

def manhattan_distance(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

pointA, pointB = [5,4],[3,2]
print(manhattan_distance(pointA, pointB))