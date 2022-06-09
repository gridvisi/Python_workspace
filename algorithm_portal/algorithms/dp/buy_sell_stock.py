"""
Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


# O(n^2) time
def max_profit_naive(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_so_far = 0
    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_so_far = max(max_so_far, prices[j] - prices[i])
    return max_so_far


# O(n) time
def max_profit_optimized(prices):
    """
    input: [7, 1, 5, 3, 6, 4]
    diff : [X, -6, 4, -2, 3, -2]
    :type prices: List[int]
    :rtype: int
    """
    cur_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i-1])
        max_so_far = max(max_so_far, cur_max)
    return max_so_far
prices = [7, 1, 5, 3, 6, 4]
print(max_profit_optimized(prices))


def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i, e in enumerate(prices[1:]):
        if e - min_price > out:
            out = e - min_price
            sell = e
        if e < min_price:
            min_price = e
    return round(out, 2), sell - round(out, 2), sell
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

#
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，
最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

dp[i] 表示前 ii 天的最大利润，因为我们始终要使利润最大化，则：
dp[i]=max(dp[i−1],prices[i]−minprice)
————————————————

'''
class Solution:
    def maxProfit(self, prices): # list[int] -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0]*n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)#(dp初值dp[0]=0)
        return dp[-1]
