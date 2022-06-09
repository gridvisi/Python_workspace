def mutipy(x,y):
    return x * y 

# 通过while循环计算预算可以买多少咖啡
# FUNDAMENTALS  LOOPS  CONTROL FLOWBASIC LANGUAGE FEATURES
m = 100  #money is amount that I pay for coffee bill

def coffee(m):
    c = 0  #cup
    price = 20  # a cup of coffee
    while m >= 20: # how many rmb surplus
        m = m - price  #educe a cup of coffee subtract
        c = c + 1
    return c
print(coffee(m))


numbers = [12,37,5,42,8,3]
even_item = []
odd_item = []
while len(numbers) > 0:    #length
    number = numbers.pop()
    print('test:',number)
    if number % 2 == 0:
        even_item.append(number)
    else:
        odd_item.append(number)
print(even_item,odd_item)

numbers = [12,37,5,42,8,3]
# 列表推导式
print([n for n in numbers if n % 2 == 0],[n for n in numbers if n % 2 == 1])


#8 kyu Lario and Muigi Pipe Problem
# https://www.codewars.com/kata/56b29582461215098d00000f/train/python

def pipe_fix(nums):
    return [i for i in range(nums[0],nums[-1]+1,1)]
nums = [-1, 4]
print(pipe_fix(nums))

#1st solution
def pipe_fix(arr):
  return range(min(arr), max(arr)+1)

'''
Rankings 1-10 are.

1: Spider-Man.
2. Captain America.
3. Wolverine.
4、Nightmare.
5. Thor.
6. Hulk.
7. Dr.Doom.
8. Iron Man.
9、Laser Eye
10. Magneto.

https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python
'''

Marvel_Comics = {'Spider-Man':'蜘蛛侠'}
print(Marvel_Comics['Spider-Man'])

Spider_Man = '蜘蛛侠'
Marvel_Comics = ['']

ranking = {1:'Spider-Man'}

# zip()
# 通过字典表达漫威角色的排行

num = [i for i in range(1,11)]
print(num)



name = "1 Spider-Man.2. Captain America.3. Wolverine.4、Nightmare.5. Thor.6. Hulk." \
       "7. Dr.Doom.8. Iron Man.9、Laser Eye10. Magneto"

#print(name.split('.'))
n = name.split('.')





#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# python字典 dict() list


name = ['Spider-Man', ' Captain America', ' Wolverine', 'Nightmare', ' Thor',
        ' Hulk', ' Dr.Doom', ' Iron Man', 'Laser Eye10', ' Magneto']


num_str = [str(i) for i in range(1,11)]

print(dict(zip(name,num_str)))

rank = dict(zip(num_str,name))

print('排行榜：',rank)
print('No.7',rank['7'])

#name = "1 Spider-Man.2. Captain America.3. Wolverine.4、Nightmare.5. Thor.6. Hulk." \
#       "7. Dr.Doom.8. Iron Man.9、Laser Eye10. Magneto"


print(num_str)  # ['1234567890']

# num_str != '1234567890' 所以，if i not in num_str 是不同于 if i not in '1234567890'

num_str = '1234567890'
num_s = [str(i) for i in range(11)]
print(num_str,num_s)

#filter()
import re

print([i for i in n if i not in num_str])

#print(name.split(' '))

#print([i for i in name if i not in ' ,.'])

print(int('1') == 1)
