'''
————————————————
版权声明：本文为CSDN博主「your_answer」的原创文章，遵循
CC
4.0
BY - SA
版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / your_answer / article / details / 79274789
'''

import numpy as np

weight = [2, 2, 6, 5, 4]
value = [3, 6, 5, 4, 6]
weight_most = 10


def bag_0_1(weight, value, weight_most):  # return max value
    num = len(weight)
    weight.insert(0, 0)  # 前0件要用
    value.insert(0, 0)  # 前0件要用
    bag = np.zeros((num + 1, weight_most + 1), dtype=np.int32)  # 下标从零开始
    for i in range(1, num + 1):
        for j in range(1, weight_most + 1):
            if weight[i] <= j:
                bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
            else:
                bag[i][j] = bag[i - 1][j]
    # print(bag)
    return bag[-1, -1]


result = bag_0_1(weight, value, weight_most)
print(result)

'''

[[ 0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  3  3  3  3  3  3  3  3  3]
 [ 0  0  6  6  9  9  9  9  9  9  9]
 [ 0  0  6  6  9  9  9  9 11 11 14]
 [ 0  0  6  6  9  9  9 10 11 13 14]
 [ 0  0  6  6  9  9 12 12 15 15 15]
————————————————
版权声明：本文为CSDN博主「your_answer」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/your_answer/article/details/79274789

LeetCode--416. Partition Equal Subset Sum（将数组切分为两个和相等的子数组）Python
题目：

给定一个数组nums（仅包含正整数），将这个数组切分为两个子数组，使得这两个子数组的和相等。若能完成上述切分，返回True，否则返回False

解题思路：

跟494.target sum 非常类似，该题直通车：

http://blog.csdn.net/xiaoxiaoley/article/details/78968852

本题思路，先进行数学分析，设子集为A、B，则有sum(A)+sum(B)=sum(nums),sum(A)=sum(B)，则有sum(A)=sum(nums)/2。故可以将题目转化为从nums中寻找是否有和为sum(nums)/2的子集，有则返回True，否则返回False。

寻找和为sum(nums)/2的子集，可以使用动态规划的思路。用dp[i]来存储和为i的组合个数，对nums里边的数字用n进行遍历，对于所有i>=n的i，有dp[i]=dp[i]+dp[i-n]。

代码（Python）：
————————————————
版权声明：本文为CSDN博主「诚实的小小乐」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiaoxiaoley/article/details/78980823
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]:
            return True
        if sum(nums)%2==1:
            return False
        target = sum(nums)/2
        print(target)
        dp = [0]*(target+1)
        dp[0] = 1
        for n in nums:
            i = target
            while(i>=n):
                dp[i] = dp[i]+dp[i-n]
                i = i-1
        if dp[target]>=2:
            return True
        else:
            return False
'''
题目:

给定一个数组nums，代表每家可以打劫到的钱数，连着打劫相邻的两家会自动报警。在保证不报警的前提下，找到可以打劫到的最多钱数。

解题思路：

考虑使用动态规划。dp[i]表示从0-i户可以打劫到的最大钱数。则有dp[i] = max(dp[i-1],dp[i-2]+nums[i])。

代码（Python）：
————————————————
版权声明：本文为CSDN博主「诚实的小小乐」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiaoxiaoley/article/details/78981918
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[len(nums) - 1]
