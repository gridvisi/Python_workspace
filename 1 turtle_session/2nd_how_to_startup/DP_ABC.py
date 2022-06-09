
# 楼梯

def get_count(n):
    if n == 1:return 1
    elif n == 2 :return 2
    else:
        l = [1,2]
        for i in range(3,n):
            l[0],l[1] = l[1],l[0]+l[1]
        return l[0]+l[1]

#问题一：连续子数组最大和
'''
定义M[j]M[j]M[j]：以jjj结尾的字串中，和最大值
状态转移：M[j]M[j]M[j]=max {M[j−1]+A[j]，A[j]M[j-1]+A[j]，A[j]M[j−1]+A[j]，A[j]}
————————————————
'''
# stock exchange best buy and sell time
nums = [-2,-9,-3,4,-1,2,1,-5,4]
#[4,-1,2,1] is max = 6

def max_subarry(nums):
    m = nums[0]
    temp = nums[0]
    for i in range(1,len(nums)):
        if temp <= 0:
            temp = nums[i]
        else:
            temp += nums[i]
        if temp > m:
            m = temp
    return m

print( max_subarry(nums))

# 股票买入和卖出的时机
# 核心子程序解决最大差值
prices = [440.01, 389.0, 374.7, 438.2, 433.6,
477.3, 545.25, 547.39, 505.0, 510.26,
501.25, 504.0, 481.03, 509.5, 511.2,
545.0, 554.2, 562.09, 590.16, 698.97,
742.0]

def max_profit(prices):
    '''
    :param prices: list prices
    :return:
    '''
    out = prices[1] - prices[0]
    min_price = prices[0]
    #print(out,min_price)
    for i, e in enumerate(prices[1:]):
        if e - min_price > out:
            out = e - min_price
            sell = e
            #print(round(out, 2), sell - round(out, 2), sell)
        if e < min_price:
            min_price = e
    return round(out, 2), sell - round(out, 2), sell
print(max_profit(prices))

'''
问题二：数字和为sum的方案数，dp问题，节省空间用一维数组解：
dp长度为m+1的数组，表示和为下标所具备的方案
n, m = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]

给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。
当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。

输入描述:输入为两行:
第一行为两个正整数n(1 ≤ n ≤ 1000)，sum(1 ≤ sum ≤ 1000)
第二行为n个正整数Ai，以空格隔开。

输出描述:输出所求的方案数示例1
输入
第一行：5 15   #下列数列中找到数之和等于15的所有组合
第二行：5 5 10 2 3
输出
4
'''
n,m = 4,1 #
value = [1,2,5,10]

n,m = 5,15
value = [5, 5, 10, 2, 3]
def change(m,value):
    dp = [0 for i in range(m+1)]
    n,dp[0] = len(value),1
    for i in range(n):
        j = m
        while j >= value[i]:
            dp[j] += dp[j-value[i]]
            print(dp) #dp[j],dp[j-value[i]]
            j -= 1
    return dp[m]
print(change(m,value))

'''
零钱兑换II给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
示例 1:输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:5=5,5=2+2+1,5=2+1+1+1,5=1+1+1+1+1

示例 2:输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:输入: amount = 10, coins = [10]
输出: 1
'''
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for value in coins:
            for i in range(amount + 1):
                if i - value >= 0:
                    dp[i] += dp[i - value]
        return dp[amount]
'''
res = []
for i in range(101):
    if change(m,value):
        print("The amounts can be combined")
    else:
        if change(m,value) == 0:
            res.append(i)
print("The amounts" + f"{res}" "can not be combined")
'''

#问题三：最长上升子数列
List = [23,52,2,5,35,32,17]
class Solution:
    def lengthOfLIS(self, nums):  #List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        opt = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    opt[i] = max(opt[i],opt[j]+1)
        return max(opt)
res = Solution()
print(res.lengthOfLIS(nums))

#问题四：零钱兑换,amount == as less as possible in {i for i in coins}

coins,amount = [1,2,5],111
#output:3  since sum([1,5,5]) = 11

class Solution:
    def coinChange(self, coins, amount): #List[int],int,int:
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] > amount:
            return -1

        m = [-1]*(amount+1)
        m[0] = 0
        for i in range(1,amount+1):
            cur_min = amount+1
            for c in coins:
                if c <= i:
                    cur_min = m[i-c] if m[i-c] < cur_min else cur_min
            m[i] = cur_min+1 if cur_min < amount+1 else amount+1
        if m[-1] == amount+1:
            return -1
        else:
            return m[-1]

res = Solution
print(res.coinChange(0,coins, amount))

from typing import List

# 最少coins的第二种解法
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            if coins[i] < amount + 1:
                dp[coins[i]] = 1

        for i in range(1, amount + 1):
            temp = []
            for v in coins:
                if i - v >= 0 and dp[i - v] != -1:
                    temp.append(dp[i - v] + 1)
            dp[i] = min(temp) if temp != [] else -1
        return dp[amount]

if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3
    r = s.coinChange(coins, amount)
    print(r)

#5 背包问题https://www.jianshu.com/p/30fd581dd098

weight = [4, 3, 2, 6, 5]
value = [3, 4, 6, 7, 9]
maxweight = 8

# 只输出最大价值
def CompletePack_Simple(W, V, MW):#完全背包
    #存储最大价值的一维数组
    valuelist = [0] * (MW + 1)
    #开始计算
    for ii in range(len(W)):#从第一个物品
        for jj in range(MW + 1):#从重量0
            if jj >= W[ii]:#如果重量大于物品重量
                valuelist[jj] = max(valuelist[jj - W[ii]] + V[ii], valuelist[jj])#选中第ii个物品和不选中，取大的
    return '最大价值：', valuelist[-1]

#  也输出选择物品的编号以及个数
def CompletePack(W, V, MW):#完全背包
    #存储最大价值的一维数组
    valuelist = [0] * (MW + 1)
    #存储物品编号的字典
    codedict = {i: [] for i in range(0, MW + 1)}
    #开始计算
    for ii in range(len(W)):#从第一个物品
        copyvalue = valuelist.copy()
        copydict = codedict.copy()
        for jj in range(MW + 1):#从重量0
            if jj >= W[ii]:#如果重量大于物品重量
                cc = copyvalue[jj]
                copyvalue[jj] = max(copyvalue[jj - W[ii]] + V[ii], copyvalue[jj])#选中第ii个物品和不选中，取大的
                #输出被选中的物品编号
                if copyvalue[jj] > cc:
                    copydict[jj] = [ii]
                    for hh in copydict[jj - W[ii]]:
                        copydict[jj].append(hh)
        codedict = copydict.copy()#更新
        valuelist = copyvalue.copy()#更新
    result = ''
    for hcode in sorted(list(set(copydict[MW]))):
        result += '物品：%d :%d个' % (hcode + 1, copydict[MW].count(hcode))
    print(result)
    return '最大价值：', valuelist[-1]

print(CompletePack_Simple(weight, value, maxweight))