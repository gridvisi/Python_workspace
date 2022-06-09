'''
In this Kata, you will be given a multi-dimensional array containing 2 or more sub-arrays of integers. Your task is to find the maximum product that can be formed by taking any one element from each sub-array.

Examples:
solve( [[1, 2],[3, 4]] ) = 8. The max product is given by 2 * 4
solve( [[10,-15],[-1,-3]] ) = 45, given by (-15) * (-3)
solve( [[1,-1],[2,3],[10,-100]] ) = 300, given by (-1) * 3 * (-100)
More examples in test cases. Good luck!

FUNDAMENTALS
'''


def solve(arr):
    p, q = 1, 1

    for k in arr:
        x, y = max(k), min(k)

        a = p * x
        b = q * x
        c = p * y
        d = q * y

        p = max(a, b, c, d)
        q = min(a, b, c, d)

    return max(p, q)

def solve(arr, cur = [1]):
  return solve(arr[1:], [x*y for x in cur for y in arr[0]]) if arr else max(cur)