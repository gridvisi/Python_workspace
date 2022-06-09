'''
https://www.codewars.com/kata/equal-sides-of-an-array/train/python
Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(range(1,100)),-1)
Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
“如果更多情况有效，则应选择第一个索引”）
Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
Test.assert_equals(find_even_index(range(-100,-1)),-1)
'''

def find_even_index(arr):
    for i,e in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
arr = [20,10,30,10,10,15,35]

arr = range(-100,-1)
arr = [1,2,3,4,5,6]
arr = range(1,100)
arr = [20,10,-80,10,10,15,35]
arr = [0,0,0,0,0]
arr = [1,2,3,4,3,2,1]
print(find_even_index(arr))


#Q2 若干同学体重为数组w，有跷跷板要求左右重量一样，给出左右各同学的体重，如果无法平衡输出-1

w = [20,10,30,10,10,15,35]

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        # 特判
        if size == 0:
            return False

        # 特判，如果整个数组的和都不是偶数，就无法平分
        s = sum(nums)
        if s & 1 == 1:
            return False

        # 二维 dp 问题：背包的容量
        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]

        # 先写第 1 行：看看第 1 个数是不是能够刚好填满容量为 target
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        # i 表示物品索引
        for i in range(1, size):
            # j 表示容量
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

