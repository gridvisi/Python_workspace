'''
https://www.codewars.com/kata/5c745b30f6216a301dc4dda5/train/python

test.describe("Basic Tests")
test .assert_equals(moving_average([40, 30, 50, 46, 39, 44],3),[40.0, 42.0, 45.0, 43.0])
test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],2),[35.0, 40.0, 48.0, 42.5, 41.5])
test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],4),[41.5, 41.25, 44.75])
test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],0),None)
'''

#10th solution by ericlee
def moving_average(values,n):
    if not n or not values: return None
    ans = []
    for i in range(len(values)-n+1):
        ans.append(sum(values[i:i+n])/n)
    return ans if ans else False
values,n = [40, 30, 50, 46, 39, 44],0

def moving_average(a, n):
    if 0 < n <= len(a): return [sum(a[i:i+n]) / n for i in range(len(a) - n + 1)]

def moving_average(arr, n):
    return n and [sum(arr[i:i + n]) / n for i in range(len(arr) - n + 1)] or None
print(moving_average(values,n))