__author__ = 'Administrator'
'''
Amy is a cashier at a convenience store and has run out of all dollar bills. But she has plenty of coins--pennies (1 cent), nickels (5 cents), dimes (10 cents), quarters (25 cents)--in the cash drawer, and is well trained for an emergency situation like this: give the change with the fewest possible coins!
艾米是一家便利店的出纳，所有的美元钞票都用完了。但是她在现金抽屉里有很多硬币——一美分（1美分）、五美分（5美分）、一角硬币（10美分）、四分之一硬币（25美分），并且受过良好的紧急情况下的训练：用最少的硬币兑换！

She just gave a change with 20 coins. What is the minimum possible value of the change, in cents?
她刚换了20个硬币。变化的最小可能值是多少（美分）？

Clarification: For example, if you think the change she just gave her customer is 2 dollars and 37 cents, write 237.
澄清：例如，如果你认为她给客户的零钱是2美元37美分，写237。
'''
#https://blog.csdn.net/churximi/article/details/51648388

x = [1,5,10,25]   #coin denominations
how_many_coins  =  20
sum_ = 0
count = 0
for key, i in enumerate(x):
    if key < len(x)-1:
        for j in range(x[key],x[key+1]+1,i):
            if sum_+x[key]< x[key+1]:
                sum_ += x[key]
                count += 1
min_tot_chg =  ((how_many_coins - count) * x[-1]) + sum_
print (min_tot_chg)

# staff solution bingo!1！
denominations = sorted([25,10,5,1], reverse = True)
print(denominations)
def min_change(n):
    s = 0
    while n > 0:
        for coin in denominations:
            if n > 0:
                s += int(n/coin)
                n -= coin*int(n/coin)
    return s

found = False
n = 1
while found == False:
    if min_change(n) == 20:
        print(n)
        found = True
    else:
        n += 1

import math
print(1/((2/3) - 0.5*(math.sqrt(3)/math.pi)))