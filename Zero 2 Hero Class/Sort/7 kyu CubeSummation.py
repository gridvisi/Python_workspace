'''
https://www.codewars.com/kata/550e9fd127c656709400024d/train/python

Write a function cubeSum(n, m) that will calculate a sum of cubes of numbers in a given range, starting from the smaller (but not including it) to the larger (including). The first argument is not necessarily the larger number.

If both numbers are the same, then the range is empty and the result should be 0.

Examples:

cube_sum(2,3); # => 3^3 = 27
cube_sum(3,2); # => 3^3 = 27
cube_sum(0,4); # => 1^3+2^3+3^3+4^3 = 100
cube_sum(17, 14); # => 15^3+16^3+17^3 = 12384
cube_sum(9, 9); # => 0
'''

#4th solve by ericlee
def cube_sum(n, m):
    return sum([(i+1) ** 3 for i in range(min(n, m), max(n, m))])

n,m = (5, 0)  # 225
print(cube_sum(n,m))
print(range(sorted([n,m])))


#1st
def cube_sum(n, m):
    n, m = sorted([n, m])
    return sum(i ** 3 for i in range(n + 1, m + 1))

def cube_sum(n, m):
    return sum([(i + 1) ** 3 for i in range(sorted((n, m)))])
n,m = (5, 0)  # 225
print(cube_sum(n,m))