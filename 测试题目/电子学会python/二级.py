#一、 基本操作题
'''
以123为随机种子，随机生成10个介于1（含）到999（含）之间的随机数，每个随机数后跟随一个
逗号进行分隔，屏幕输出这个10个随机数
'''

import random as r

#r.seed(123)  # 随机种子，保证两次产生同样结果
count = 0
for i in range(10):
    count += 1
    print(r.randint(1, 1000), end=',' if count < 10 else '')

# 其中单行if else语句是为了实现，最后一个数字后不加逗号（,）
# 考察random库的randint()方法，随机生成整数

print("\n")
'''
随机选择手机品牌列表
brandlist = ['华为', '苹果', '诺基亚', 'OPPO', '小米']
中的一个手机品牌，屏幕输出
'''
brandlist = ['华为', '苹果', '诺基亚', 'OPPO', '小米']
result = r.choice(brandlist)
print(result)
import random

result = random.choice(brandlist)
print(result)

result = random.choices(brandlist)
print(result)

result = random.sample(brandlist,2)
print(result)

#用户输入一个字符串，将字符串逆序输出，同时紧接着输出该字符串所包含的字符个数
s = "life is short, i love python"
print(s[::-1],len(s),len(''.join(s.split(" "))))


print(f"{1447301400:,}")
num = f"{1447301400:,}"
print(type(num))
print(int(''.join(num.split(","))))

'''
二、计算机二级python
程序设计编程题

1.用户输入一个小数,获取整数部分
'''
num = 3.99
print(int(num//1))

#2.获得用户输入的一个整数N， 计算并输出N的32次方
n = 2
print(n ** 32)

#3.获得用户输入的一段文字，将这段文字进行垂直输出
c = '重庆欢迎您'
for i in c:
    print(i,end = '\n')

#4.获得用户输入的一个整数N, 计算并输入1到N相加的和
N = 10
print(sum([i for i in range(N+1)]))

#5.获取用户输入的一个整数， 输出该整数百位以上的数字
m = 2022
print(m //100)


#6.获取用户输入的一个字符串， 将字符串按照空格分割，然后逐渐打印出来
s = 'hello world'
s = s.split(" ")
print(s)

#7.程序读入一个表示星期几的数字（1 - 7），输出对应的星期几符串名称，
# 例如输入3, 返回星期三


def weeks(n):
    num2week = {1: "星期一", 2: "星期二", 3: "星期三",
                4: "星期四", 5: "星期五", 6: "星期六", 7: "星期日"}
    return num2week.get(n,"不存在")

#8. 设n是一任意自然数，如果n的各位数字反向排列所得自然数与n相等
# 则n被成为回文数， 从键盘输入一个5位数，请编写程序判断这个数字是不是回文数

num = 12321
def huiwen(num):
    return str(num)[::-1] == str(num)


#9.输入一个十进制数， 分别输出其二进制，八进制， 十六进制字符串
num = 2022
print(bin(num),oct(num),hex(num))


#10.输入一个年份， 输入是否是闰年，条件是： 能被4整除， 但不能被100整除，
# 或者能被400整除的年份， 都是闰年
year = 2022

def isRun(year):
    if not year%400:return f"{year}年是闰年"
    else:
        if not year%4 and year%100:
            return f"{year}年是闰年"
    return f"{year}年不是闰年"

print(isRun(year))

#判断闰年的第二种思路是充分运用逻辑运算符 and 和 or

def isRun_bool(year):
    print(bool(year%400))
    print(not bool(year%4) and bool(year%100))
    return not bool(year%400) or not bool(year%4) and bool(year%100)
year = 2020
print(isRun_bool(year))

#11.最大公约数计算， 获得两个整数， 求出这两个整数的最大公约数和最新公倍数。
#最大公约数的计算一般使用辗转相除法， 最小公倍数则使用两个数的乘积除以最大公约数
'''
回忆欧几里得辗转相减求最大公约数的数学证明
最大公约数 gcd = greatest common divisor
请您自行完成数学部分求证

假设：p，q的最大公约数是gcd 
那么：p = i * gcd，q = j * gcd
推出：p - q ,  q的最大公约数也是gcd
     q - p ，p的最大公约数也是gcd
'''

def gcd(p,q):
    while p!= q:
        if p > q:
            p = p - q
        else:q = q - p
    return q

p,q = 15,9
print(gcd(p,q))

def LCM(p,q):
    return p * q // gcd(p,q)
print(LCM(p,q))



#12.统计不同的字符个数， 用户从键盘输入一行字符编写一个程序，统计并输出其中给你的英文字符，数字，
# 空格和其他字符
strg = "life is short, we love python! 2022 kickoff"
c,n,b,e = 0,0,0,0
for i in strg:
    if i.isalpha():c += 1
    elif i.isdigit():n += 1
    elif i == " ":b += 1
    else:e += 1
print(c,n,b,e)

#13.养车门问题。 有扇关闭门， 一扇门后面停着汽车， 其余门后都是山羊.只有主持人知道每扇门后面是什么， 参赛者可以选择一扇门，在开启它之前
# 主持人会开启另一扇门， 露出门后的山羊。 此时允许参赛者更好自己选择.请问，参数者更换选择之后能否增加猜中的机会，？
# 一这是经典问题， 请使用random库对这个随机事件进行预测， 分别输出参数者改变选择和坚持选择获胜的概率。
'''
今天有趣的经典概率问题。蒙蒂-霍尔问题是以美国电视节目《我们来做个交易》为基础的概率难题。

在这个节目中，你会看到3扇门。一扇门后面有奖，两扇门没有奖（用山羊代表）。

选择一扇门后，主持人会打开另外两扇不含奖品的门中的一扇，问参与者是否想换到第三扇门。大多数人不会。人们会认为在被展示了一扇假门之后，你有五成的胜算，然而数学证明，通过转换，你的胜算会大大增加，从1/3增加到2/3。

好家伙，什么鬼？反人类直觉啊！

一旦遇到反直觉的问题，求助数学的严谨推理。在这个程序中，您将输入一系列的人，他们都猜从1，2，3中猜一扇门背后有一只羊。编号是1，2，3的三扇门只有一个门背后有羊。

图片


输入的数组是每个人第一次猜的编号，你作为主持人问嘉宾是否考虑放弃原来的选项，重新选则。每个人都听从了你的建议，聪明地换选择到另一扇门。

而你的任务就是通过代码证明更换选择真的能增加他们的获胜机会。程序返回所有参与者的胜率为四舍五入的int。


左右顺序依次是正确的选项，嘉宾的选项、猜中的概率

例如下面红色表达的第一次游戏。1号门后面有羊，14位嘉宾猜的结果数组，经过聪明的转变，最后猜中1号门的概率是71%；此时，请同学描述后面两次游戏的结果。



1, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 猜中得概率71%

2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 猜中得概率64%
3, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 猜中得概率64%

逻辑推理游戏的过程部分：
1, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]) 为例
第一步，嘉宾猜3，其实只有1号门背后有羊，
第二步，主持人的你选择2号门打开，1号门背后有羊你不会给嘉宾看，你只选择没有羊的。
第三步：再问嘉宾是否坚持原来的选择3，还是转换选1号门？
第四步：你说服嘉宾选择1，嘉宾同意并等到奇迹时刻

依次类推后面的选项。只有到最后4位选择正确的1号门的嘉宾会因为遵循主持人的建议改为选2或3，
至此全部人的选择都更改过一次。

结论：主持人方法显著提升猜中的概率！
因为更改选择前后的比较如下
更改前： [3,3,2,3,3,2,2,3,2,2,1,1,1,1] 
猜中1的次数是4，概率是4/14

更改后： [1,1,1,1,1,1,1,1,1,1,2,3,3,2] 
* 2，3，3，2是随机选项，关键是都不是正确选项1号门
猜中1的次数是10次，概率是10/14

依照以上思路你可以推导出来下面的概率如何算出来的
2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1], 
猜中得概率：64%

3, [3,3,2,3,3,2,2,3,2,2,1,1,1,1], 
猜中得概率：64%

c 代表 c 门背后有羊即正确选项
p 代表 每个人猜的数组成的数组
def monty_hall(c, p):

    return round((1 - (p.count(c) / len(p))) * 100)

c = 2

p = [3,3,2,3,3,2,2,3,2,2,1,1,1,1]

输出

64


这里的关键是：

1、每个人猜1，2，3的概率是平均分布，数组里出现的次数相同。猜中的概率是1/3
2、而经过更换选择，增加到64、71或其他显著高于1/3的结果！

网友get到精华 - 这个游戏假设我玩300次，大概有100次我第一次是选对的，有200次第一次是选错的，
所以如果我300次都选择不换，那么我可以赢得100辆跑车，如果300次都换，那么我可以赢得200辆跑车！

写法代码长很多，但忠实提现随机选择过程，用到了random

'''


import random

def monty_hall(c, p):

    return round([random.choices([i for i in [1,2,3] if i != c]) if i == c else c for i in p].count(c)/len(p),2)


#4. 实现Cal() 函数，参数作为一个字符串，字符串包含整数、“+-*/ //” 四则运算符号，
# 返回数学运算结果：例如 "2+3*4-1" ，返回：13
s = "2+3*4-1"
print("Cal:",eval(s))


#15.实现isPrime 函数，参数为整数，要有异常处理，如果整数是质数，返回True;否则返回False
def isPrime(n):
    if n==0 or n==1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:return False
    return True
n = 1
print('isPrime:',isPrime(n))


#16.编写一个函数，打印200以内的所有素数，以空格分割

def Primes(n):
    ans = []
    for i in range(n+1):
        if isPrime(i):
            ans.append(i)
    return ans
print(Primes(200))

#17. 编写一个函数，参数为i一个整数n,利用递归获取斐波那契数列中的第n个数并返回
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，
# 4181，6765，10946，17711，28657，46368.
def fib(n):
    a,b = 1,1
    ans = []
    while n > 1:
        a,b = b,a+b
        n -= 1
        ans.append(a)
    return a
n = 7
print(fib(n))

#18.
# 文字符频率统计， 编写一个程序，对给定义字符串中出现的a - z
# 字符频率进行分析，忽略大小写，采用降序方式输出
# 这个不仅可以对英文字符统计，可以对任何字符进行统计
'''
"The quick brown fox jumps over the lazy dog"（那只敏捷的棕毛狐狸跃过那只懒狗）
这句话的特别之处在于，它在保证尽可能短的同时，包含了全部的 26 个字母。追根溯源，该句最早
出现于 1885 年 2 月 10 日《波士顿日报》的一篇文章「Current Notes」。原文为：
A favorite copy set by writing teachers for their pupils is the following, 
because it contains every letter of the alphabet:

'A quick brown fox jumps over the lazy dog.'
'''
from collections import Counter
def alpha_rank(s):
    ans = Counter(s.lower())
    return ans
s = 'A quick brown fox jumps over the lazy dog.'
print(alpha_rank(s))
s = "那只敏捷的棕毛狐狸跃过那只懒狗"
print(alpha_rank(s))



#19. 实现isNum()函数，参数作为一个字符串，如果这个字符串属于整数，浮点数
'''
isinstance(s,int)判断是否是整数
isinstance(s,float)判断是否是浮点数
idinstance(s,complex)判断是否是复数
isinstance(s,basestring) 判断是否是字符串型
isinstance(a,dict) 判断是否是字典类型
补：
a.isalpha()判断是否是英文字符

a.isdigit()判断是否是数字

a.isspace()判断是否是空格
————————————————

'''
# 或复数的表示，则返回True ，否则返回False
# 扩展练习
#方法一: isdigit() 不可识别汉字 小数类型
str1 = '1'
str2 = '2.1'
str3 = '三'
str4 = '3.3.3.3'
print(" ******   第1种  ******")
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print(str4.isdigit())
'''
结果:

True
False
False
False
'''
#方法二: isdecimal() 没有与方法一发现区别
print(" ******   第2种  ******")
print(str1.isdecimal())
print(str2.isdecimal())
print(str3.isdecimal())
print(str4.isdecimal())
'''
结果:

True
False
False
False
'''
print(" ******   第3种  ******")
#方法三: isnumeric() 可以识别汉字
str1 = '1'
str2 = '2.1'
str3 = '三'
str4 = '3.3.3.3'

print(str1.isnumeric())
print(str2.isnumeric())
print(str3.isnumeric())
print(str4.isnumeric())
'''
结果:

True
False
True
False
'''
print(" ******   第4种 try except ******")
#没有找到可以识别小数的! 识别小数使用try 来判断
try:
    float(str2)
    print('is True')
except:
    print(' is False ')


try:
    float(str1)
    print('is True')
except:
    print(' is False ')
'''
运行结果:

is True
is True
'''
#由此可见. float对整数和小数都有效. 那么为了判断字符串到底能不能转换为数字.
# 我们加一个方法稍稍改动一下就可以了:

def is_number(target_str):
    try:
        float(target_str)
        return True
    except:
        pass
    if target_str.isnumeric():
        return True
    return False

print(is_number(str1))
print(is_number(str2))
print(is_number(str3))
print(is_number(str4))
'''
True
True
True
False
'''
print("******  复数的引入判别 *******")

'''
———————————————— start ————————————————
isinstance(s,int)判断是否是整数
isinstance(s,float)判断是否是浮点数
idinstance(s,complex)判断是否是复数
isinstance(s,basestring) 判断是否是字符串型
isinstance(a,dict) 判断是否是字典类型

a.isalpha()判断是否是英文字符
a.isdigit()判断是否是数字
a.isspace()判断是否是空格
———————————————— end ————————————————
'''

str5 = 3.14j
#print(f"{str5} {is_number(str5)}")
# AttributeError: 'complex' object has no attribute 'isnumeric'

print(f"{str5} is 复数吗？ {isinstance(str5,complex)}")
print(complex(3,14), str5)

n = complex(1,1)

print(n,str(n))
print(isinstance(str(n),complex))
print(isinstance(n,complex))

n = complex(0,1)
print(n,str(n))


n = complex(1,0)
print(n,str(n))

print("****   1 + 1j  ******")
n = (1+1j)
print(isinstance(n,complex))
n = 1+1j
print(isinstance(n,complex))

#n = "1+1j"
n = "1+1j"
#print(isinstance(eval(n),complex))
print(isinstance(n,complex))
inp = [1,1/3,"3.14","3.14j",3.14j,"-3i","1+1j","100","hi 007"
                                               "a+i"]
# 复数特征末尾是 j
# 有可能有 +或- 符号
# 不用re可否实现

real,complx = [],[]
for i in inp:
    try:
        if is_number(i):
            real.append(i)
        elif isinstance(i,complex):
            complx.append(i)
    except:
        if i[-1] == 'j':
            complx.append(i) # 不支持复数
print(real,complx)
print(" **** real , complex ******")


# for loop 改写为 列表推导式
'''


for c in inp:
    if c.isalnum():
        print(f"{c} is alnum")
    else:print(False)

print([c.isalnum() for c in inp])

'''
# 发现isalum可以分辨出字符串和字母混合的元素

# 正则表达式
import re
print(re.split(',','a,s,d,asd'))
['a', 's', 'd', 'asd'] #返回列表
#print(re.split("+","1+j"))


pat = re.compile(',')
pat.split('a,s,d,asd')
['a', 's', 'd', 'asd'] #返回列表

re.split('[, ]+','a , s ,d ,,,,,asd') #正则匹配：[, ]+，后面说明
['a', 's', 'd', 'asd']

re.split('[, ]+','a , s ,d ,,,,,asd',maxsplit=2) # maxsplit 最多分割次数
['a', 's', 'd ,,,,,asd']

pat = re.compile('[, ]+') #正则匹配：[, ]+，后面说明
pat.split('a , s ,d ,,,,,asd',maxsplit=2) # maxsplit 最多分割次数
['a', 's', 'd ,,,,,asd']


#注意一下缩进，可能上传它缩进有写问题

def isNum(a):
    try:
        if type(a) == int or type(a) == float or type(a) == complex:
            print('True')
        else:
            print('False')
    except:
        print('False')
a = 1
print(isNum(a))


#了解所有的python库表
'''
import distutils.sysconfig as sysconfig
import os
import sys

std_lib = sysconfig.get_python_lib(standard_lib=True)

for top, dirs, files in os.walk(std_lib):
    for nm in files:
        prefix = top[len(std_lib)+1:]
        if prefix[:13] == 'site-packages':
            continue
        if nm == '__init__.py':
            print (top[len(std_lib)+1:].replace(os.path.sep,'.'))
        elif nm[-3:] == '.py':
            print (os.path.join(prefix, nm)[:-3].replace(os.path.sep,'.'))
        elif nm[-3:] == '.so' and top[-11:] == 'lib-dynload':
            print (nm[0:-3])

for builtin in sys.builtin_module_names:
    print (builtin)

'''

#https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators)

print(f"{1447301400:,}")