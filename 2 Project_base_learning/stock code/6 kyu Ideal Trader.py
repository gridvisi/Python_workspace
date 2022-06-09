'''
https://www.codewars.com/kata/610ab162bd1be70025d72261/train/python

from solution import ideal_trader
import codewars_test as test

@test.describe("Fixed tests")
def fixed_tests():
    @test.it("can't make any profit in flat market")
    def flat():
        prices = [1.09, 1.09, 1.09, 1.09]
        test.assert_approx_equals(ideal_trader(prices), 1)

    @test.it("minimal example of profit")
    def profit():
        prices = [2, 3]
        test.assert_approx_equals(ideal_trader(prices), 1.5)

    @test.it("example from the description")
    def description():
        prices = [1.0, 1.0, 1.2, 0.8, 0.9, 1.0]
        test.assert_approx_equals(ideal_trader(prices), 1.5)

小王对他的工作感到厌倦。他认为他的老板很吝啬，给工资很低。昨天他发现了外汇交易。现在他看着图表，幻想着成为一名交易员，幻想着他能赚多少钱。

任务
编写一个函数，接受图表上的价格点列表并返回交易的最大可能利润。

例子
ideal_trader([1.0, 1.0, 1.2, 0.8, 0.9, 1.0]) -> 1.5
假设我们的理想交易员在开始交易前有x美元的存款。

以下是他的做法：
他用他所有的钱在1.0买入。
他在1.2卖出所有的东西，获得20%的利润。他的存款现在价值1.2倍
他用所有的钱在0.8价位再次买入。
他在1.0价位卖出所有东西，获得25%的利润。他的存款现在值1.5倍
因此，在这个时段，一个理想的交易者会把X美元变成1.5x美元。

输入
价格的输入列表。

总是包含至少两个价格点。
只包含正数价格。
可以包含重复的价格（如例子中的1.0，1.0）。
对交易者的补充说明
你应该假定，在比利的幻想中。

不考虑以下因素的影响：
没有经纪人的佣金。
不使用杠杆，包括做空（比利还不知道这些东西，对他来说是好事）。
他总是可以准确地以当前价格买入或卖出（没有价格滑移）。
订单是即时执行的（在价格变化之前）。


事后诸葛亮的做法，不过拿来做为编程任务还是过过瘾可以


#
'''

#1st
def ideal_trader(prices):
    res = 1
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            res *= prices[i]/prices[i-1]
    return res


print(float('-inf') < 0)

def ideal_trader(prices):

    buy,sell = float('inf'),0
    margin = 1
    for i,p in enumerate(prices):
        print(p,buy,sell,margin)
        if p < buy:
            buy = p

        elif p > sell and p > prices[i-1]:
            sell = p

        if p < prices[i-1]:
            print('break even:',round(sell/buy,2),p,prices[i-1],margin)
            #margin += round(sell - buy,2)
            margin *= round(sell/buy,2)

        #print('break even:', p, prices[i - 1], margin)
    return margin

prices = [1.0, 1.0, 1.2, 0.8, 0.9, 1.0]
prices = [2, 3]
prices = [1.09, 1.09, 1.09, 1.09]
print(ideal_trader(prices))