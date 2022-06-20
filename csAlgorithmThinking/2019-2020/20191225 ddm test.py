'''
丁丁猫2019年期末小测验

'''
#https://www.codewars.com/kata/57eae65a4321032ce000002d
#139 = 001
'''
def fake_bin(x):
    re = []
    for i in str(x):
        if x < 0
'''


#热身题

# 庆庆 打一地名。用函数def caimi()实现：
# 输入: 庆庆
# 输出：谜底
x =['庆庆','复复']
#print(x.count('庆'))

def caimi(x):
    for i in list(x):
        print(i)
        if x.count(i) == 2:
            return '重'+i

print(caimi(x))


# 输入：庆庆庆庆祝
# 输出：庆祝

#1 老师将lucas和alex的岁数记混淆了，见下面描述。现在你要修改正确，难度8kyue
# 考察理解变量，掌握python语言的变量赋值

lucas = 9
alex = 12
print(abs(lucas - alex))

#请在下面写下你的代码：


#2 现在判断lucas和alex的谁的年龄大，大几岁。请补全代码
'''
if   :
    print('  比  年龄大',大' ')
else:
    print('  比  年龄大',大' ')
'''
#请在上面基础上，补齐代码：
lucas = 10
alex = 9
if lucas > alex:
    print("lucas比alex年龄大:",lucas - alex)
else:print("lucas比alex年龄小:",alex - lucas)
print(f"{alex}")

#3 你接下一个任务为水果店的老板设计一个程序，顾客提出要买的水果后，程序能够给出
# 判断顾客想买的水果有没有库存，初级班的同学完成此步即可
# 高级班的同学完成更进一步：如果有就将库存减去顾客买的数量，
# 如果没有，就显示'None'

fruit = {'apple':'30','orange':'20','banana':'10'} #水果库
fruit = {'apple':30,'orange':20,'banana':10}
fruit["apple"] -= 3
print(fruit)

# lyn score = 15, hy = 6, zhq = 4

#  这是小明同学的写的代码，先看结果对不对？再看有没有办法简化？
'''
fruit = {'apple':'30','orange':'20','banana':'10'}
小明先将字典更改为数组后，再开始判断：
fruit = ['apple','orange','banana']
if fruit == "apple" or fruit == "orange" or fruit == "banan":
    print('yes,i have',f"{fruit}")  #如果有就显示库存有该水果的名称
'''
#请在上面基础上，补齐代码：

fruit = ['apple', 'orange', 'banana']
for i in fruit:
    if i == 'pear':
        print('in stock')
    else:
        print('not in stock')

if 'pear' in fruit:
    print('youhuo')
else:
    print("meihuole")
print('pear' not in fruit)

s = 'apple'



'''
for i in fruit:
    if s == i:print('yes')
    else:print("No")
'''
s = 'pear'
re = [i==s for i in fruit if i == s]
print(re)

#高级班

fruit = {'apple':'30','orange':'20','banana':'10'} #水果库存
summer = {'apple':'3'}  # summer买个苹果
steve = {'orange':'5'}  # steve买的水果
alan = {'banana':'9'}   # alan买的水果

for i in (summer, steve, alan):
    print('store', i)



#4 仔仔为新年买了一大袋苹果，仔仔说见面就分一半。回学校的路上，仔仔前后遇到了6个同学争着要去帮他提，
#  等仔仔到了学校后，苹果只剩一个了，请问仔仔最初买了多少苹果？
#  用数学直接算，但还要用编程实现：如果遇到n个同学，如何迅速得到结果
#  考察二进制的理解
#  请在下面写下你的代码：
#

# 二进制的 1111
print('1111,2',int('0b1000000',2))

#5 为了缓解交通压力，假设重庆推出汽车限号，就是说单号是车牌尾数为单数的上路，双号尾号为双数的车牌
# 可以上路现在你要为警察叔叔设计一个程序，帮助警察叔叔找出下面的车牌哪些是违规上路的？

# 高级班的同学请搜索网上的知识运用time函数取出电脑系统时间，初级班不必
# 考察4个点 条件判断 数组切片，逻辑判断符，取余数算符

import datetime
now_time = datetime.datetime.now()
print(f"{now_time}"[:10])

name = "周宏宇"
print(name[-1])

num_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']
day_time = '20191227' #初级班直接运用day变量

import time

#day = how_to_time.how_to_time.now()
#day2 = how_to_time.date.today()

#print("当前年月日时分秒:", day)
#print("只查看年月日:", day2)
#输出的格式： ['渝C5072','渝A2966'] 是不可以上路的

#1 取出每一个车牌
#2 判断车牌号尾数是不是奇数
#3 如果是奇数，那么就不同意上路
#4 如果是偶数，那么就同意上路
