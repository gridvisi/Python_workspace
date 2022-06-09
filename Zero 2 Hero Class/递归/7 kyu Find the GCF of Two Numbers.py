'''
https://www.codewars.com/kata/579e3476cf1fa55592000045/train/python

Your task here is the find the GCF (Greatest Common Factor) of any two numbers passed into a method, which will return one integer answer as an output.

Examples:

find_GCF(4, 6) # Should return 2
find_GCF(93, 186) # Should return 93
find_GCF(20, 5) # Should return 5
Here, inputs will always be natural numbers so there's no need to worry about negative
values or zero.

test.assert_equals(find_GCF(2, 4), 2)
test.assert_equals(find_GCF(8,20), 4);
test.assert_equals(find_GCF(5,13), 1);
test.assert_equals(find_GCF(100,100), 100);

ALGORITHMSNUMBERSMATHEMATICS
'''

def find_GCF(a, b):
    a,b = max(a,b),min(a,b)
    a,b = sorted([a,b])
    while b%a != 0:
        a,b = b%a,a
    return a
a,b = 12,18
print(find_GCF(a,b))


#1st
#最大公约数
# GCF(6，3) = 3
# GCF(9,6) = 3
# GCF(Great Common divisor)
def find_GCF(a, b):
    if b == 0: return a
    return find_GCF(b,a%b)

print(find_GCF(100,50))

'''
学习数学组合
自助餐有四种菜，老板喜欢数学，于是推出100元的优惠套餐计划。
每种菜只能点一盘，每次可以点两种菜，但每次来点的菜都不能和
之前来点的组合相同，问一共可以来吃多少回？并列出所有组合。
menu = [chicken，pork，beef，vegetable]

anwser：6

[['chicken', 'pork'], ['chicken', 'beef'], 
['chicken', 'vegetable'], ['pork', 'beef'], 
['pork', 'vegetable'], ['beef', 'vegetable']]

math and coding solve it
'''
menu = ['chicken','pork','beef','vegetable']
dish = []
for first in range(len(menu)-1):
    for second in menu[first+1:]:
        #if second != first:
        dish.append([menu[first],second])
print(len(dish),dish)

'''
16 
[['chicken', 'chicken'], ['chicken', 'pork'], 
['chicken', 'beef'], ['chicken', 'vegetable'], 
['pork', 'chicken'], ['pork', 'pork'], ['pork', 'beef'], 
['pork', 'vegetable'], ['beef', 'chicken'], ['beef', 'pork'], 
['beef', 'beef'], ['beef', 'vegetable'], 
['vegetable', 'chicken'], ['vegetable', 'pork'], 
['vegetable', 'beef'], ['vegetable', 'vegetable']]

'''