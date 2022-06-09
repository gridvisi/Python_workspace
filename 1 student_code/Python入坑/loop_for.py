num_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']
#今天的作业是7月15日（明天）按单双号出行，哪些车牌可以上路？

print(5/2, 5//2 ,5%2 , float(1/3))
print(len('0.3333333333333333')) #18位

import math
print(math.pi)

for plate in num_plate:
    if eval(plate[-1])%2 == 1: # plate[5]
        print(plate)

# str -> int  int(), eval()


import keyword

print(keyword.kwlist)
print(keyword.iskeyword('is'))

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']


my_fruit = ['watemelon','apple','mango','banana','peach']
for i in my_fruit:
    if i == 'banan':
        print(i)
else:
    print(None)

your_fruit = ['pear','strawberry','pear','mango']
print(my_fruit[::1]) #slice

print('slice-even:',list(range(1,100))[::2])
print([i for i in range(100) if i%2==0])

print(set(my_fruit) & set(your_fruit))

# 最大公约数
# 15 = {3，5，15}
# 9 = {3，9}
factor_15 = {3,5,15}
factor_9 = {3,9}
print(factor_15 & factor_9)

#10 stone, 3 in group
print(10%3)