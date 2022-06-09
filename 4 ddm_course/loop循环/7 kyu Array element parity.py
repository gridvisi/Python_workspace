'''
https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python

In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.
Examples:
[1, -1, 2, -2, 3] => 3
3 has no matching negative appearance
[-3, 1, 2, 3, -1, -4, -2] => -4
-4 has no matching positive appearance
[1, -1, 2, -2, 3, 3] => 3
(the only-positive or only-negative integer may appear more than once)
Good luck!
'''

arr = [-3,1,2,3,-1,-4,-2]
def solve(arr): return sum(set(arr))

def solve(arr):
    res = []
    for i in arr:
        if -i not in arr and -i not in res:
            res.append(i)

    return res[0]
print(solve(arr))
