'''
https://www.codewars.com/kata/515f51d438015969f7000013/train/python

Test.assert_equals(pyramid(0), [])
Test.assert_equals(pyramid(1), [[1]])
Test.assert_equals(pyramid(2), [[1], [1, 1]])
Test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])
'''

def pyramid(n):
    ans = []
    if n == 0:
        return ans
    for i in range(1,n+1):
        ans.append([1] * i)
    return ans
n = 3
print(pyramid(n))

#1st solution
def pyramid(n):
    return [[1]*x for x in range(1, n+1)]

