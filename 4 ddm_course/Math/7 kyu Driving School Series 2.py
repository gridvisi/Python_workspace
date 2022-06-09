'''
https://www.codewars.com/kata/589b1c15081bcbfe6700017a/train/python

@test.describe('Basic Tests')
def fixed_tests():
    @test.it('It should works for basic tests.')
    def basic_tests():
        test.assert_equals(cost(45),30)
        test.assert_equals(cost(63),30)
        test.assert_equals(cost(84),40)
        test.assert_equals(cost(102),50)
        test.assert_equals(cost(273),100)

迅捷驾校（F&F）的收费标准如下。

时间成本
第1小时以内30美元
其后每半小时** 10美元
** 以后的费用是以四舍五入的方式计算的，以半小时为单位。
例如，学生X上课1小时20分钟，1小时30分钟的费用为40元(30+10)，如果他上课5分钟，整小时的费用为30元。
出于好心，富力还提供了5分钟的宽限期。因此，如果学生X上了65分钟或1小时35分钟的课，他只需支付1小时或1小时30分钟的费用。
对于给定的课程时间（分钟），写一个函数价格来计算课程的费用。

基础数学 MATEMATICSALGORITHMSNUMBERS(数字)
'''

#11th solution by ericlee
def solve(st):
    a,b = divmod(st-60,30)
    return 30*(st<=65) + (st>65)*(30+10*(a+(b>5)))
st = 102
print(solve(st))

#1st solution
import math
def cost(mins):
    return 30 + 10 * math.ceil(max(0, mins - 60 - 5) / 30)

def cost(mins):
    return 30 + max(0,(mins-60)//30+((mins-60)%30>5))*10

def cost(mins, cost=30):
    mins -= 60

    while mins > 5:
        cost += 10
        mins -= 30
    return cost

def cost(mins):
    return 30 + 10 * ((mins - 66) // 30 + 1) if mins > 65 else 30

def cost(mins):
    price =30
    while mins > 60:
        mins-=30
        if mins>35:
            price+=10
        else:
            return price
    else:
        return price


from math import ceil
def cost(n):
    return 30 + [ceil((n-65)/30)*10, 0][n<60]

#2nd solution
from math import ceil


def cost(n):
    n -= 5
    if n < 60: return 30
    n -= 60
    return 30 + ceil(n / 30) * 10
'''
    if st <= 65:
        a, b = divmod(st, 30)
        return (a <= 2)*30 + 10 * (b > 5)
    elif st > 65:
        a,b = divmod(st - 65,30)
'''