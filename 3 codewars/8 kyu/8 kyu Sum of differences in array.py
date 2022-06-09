'''
Your task is to sum the differences between consecutive pairs in the array in descending order.

For example: sumOfDifferences([2, 1, 10]) Returns 9

Descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

price = [5,8,10,7,7,11,15,10] #even
'''

#ada买了一只股票100股，一年内多次卖出又买入，最终ada赚钱了吗？赚了多少
#购买和卖出的价格交替：5元第一次买入，8元卖出，
# 200 300 130 200 600 700 400 1000
# 100 100 100 100 100 100 100 100

price = [5,8,10,7,7,11,15,10] #even
price = [15,9,10,11,17,13,15,10] #even
n = len(price)//2
num = [int(n) for n in input().split()]
print(num)

re = 0
for i in range(1,len(price),2):
    print(num[i//2])
    re += (price[i] - price[i-1]) * num[i//2]
    print(re)
print(re)