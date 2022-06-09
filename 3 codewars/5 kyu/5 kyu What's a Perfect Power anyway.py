# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

import math
from decimal import *

print(math.log(125,5), int(math.log(125,5)))
print(math.log(16,4) == int(math.log(16,4)))

print(Decimal(math.log(125,5)), int(Decimal(math.log(125,5))))
print(math.log(16,4) == int(math.log(16,4)))

def isPP(n):
    re = []
    for i in range(2,int(math.sqrt(n))):
        if math.log(n,i) == int(math.log(n,i)):
            re.append(i)
    return re
n = 125
print(isPP(n))

'''
一、数字类型
1、整数
0，-1234，5678，9223372036854775808
十六进制：0x9a，0XFF
八进制：0o73，0O35
二进制：0b100100，0B101100
2、浮点数
1.23，1.，3.45e-10，4E100
3、复数
complex(real,imag), 3+5j，4J
4、其他
分数：Fraction(4,5), Fraction(7,8)
无穷大/小：float(‘inf’), float(‘-inf’)
非数字NaN：float(‘nan’)
二、数字类型的应用
1、整数
在Python 2.x版本中整数分为一般整数和长整数，但是在Python 3.x就没有这种区分，整数只有一个类型，
在Python里整数可以输入或输出成二进制，八进制或者十六进制数。
二进制数表示方式为0b或者0B开头。例如：0b10110010，0B11001001
八进制数表述方式为0o或者0O开头。例如：0o632765，0O223174
十六进制数表述方式为0x或者0X开头。例如：0xff，0X3A，0xAC，0Xb7

需要把整数输出成非十进制数的时候，需要使用一下函数：bin(i), oct(i), hex(i) ，在这里i是十进制数字，
输出的是文本形式。
'''

#2、浮点数 在Python里浮点数是用64bit来存储的，精度大约能达到17位。

print(1.0/7.0)
#0.14285714285714285

'''
三、运算符
1、各类运算符
算数运算符：+,-,,/,%,//,**
比较运算符：==,!=,>,<,>=,<=
赋值运算符：=,+=,-=,=,/=,%=,//=,**=
位运算符：&,|,^,~,<<,>>
逻辑运算符：and,or,not
成员运算符：in, not in
身份运算符：is, is not

2、运算符优先级

 ~,+,- #这里的加和减是一元运算符
 ,/,%,//
 +,- <<,>>
&
 ^,|
 <=,>=,<,>
 ==,!=
 =,+=,-=,=,/=,%=,//=,=
 is, is not
 in, not in
not,and,or

四、运算符应用
1、类型升级
>>> Dora=153
>>> Emon=1.53
>>> Da=1+3j
>>> Xiong=Fraction(1,3)
>>> print(type(Dora),type(Emon),type(Da),type(Xiong))
<class 'int'> <class 'float'> <class 'complex'> <class 'fractions.Fraction'>
>>> print(type(Dora+Emon),type(Dora+Da),type(Dora+Xiong),type(Da+Xiong))
<class 'float'> <class 'complex'> <class 'fractions.Fraction'> <class 'complex'>
'''

'''
注：type()函数可以用来查看字符类型。

2、只能用于整数的运算符
位运算符：&、|、^、~、<<、>>

3、结果可能不是预期的运算符
逻辑运算符：and,or
'''
print(1 and 3)
#3
print(3 and 1)
#1
print(1 or 3)
#1
print(3 or 1)
#3

print(1<3>5)
#False
print(1<3 and 3>5)
#False

'''
五、基本数学函数
1、pow：幂函数
2、abs：绝对值
3、fabs：绝对值（与abs稍微有区别）(math)
4、round：四舍五入
5、ceil，floor：取整(math)
6、int,bin,oct,hex,float等：格式转换
7、random：随机函数(random)
8、log：算出自然对数(math)
9、log10：算出底数为10的对数(math)
10、max，min：选出最大，最小值
11、modf：对浮点数分成小数部分和整数部分（math）
12、sqrt：算出平方根

六、数学函数的应用
1、pow：幂函数，功能与运算符**一样

'''
#1、pow：幂函数，功能与运算符**一样

print(pow(5,3))
#125

#abs：取绝对值

print(abs(-153)) #153

#3、fabs：取绝对值，fabs函数取出来的是浮点数，而abs可以保持原有的数字类型

import math
math.fabs(-153)
#153.0

#4、round：四舍五入？
print(round(13.5))
#14
print(round(2.5))
#2
print(round(1/3,5))
#0.33333

#5、ceil：取最小的大于该值的最大整数, floor：取最大的小于该值的最小整数

print(math.ceil(13.5))
#14
print(math.floor(13.5))
#13

#7、random，是Python 里很好的随机函数使用的模块，其使用方法如下：
#a、取0-1之间的随机小数：

import random
random.random()
#0.41430515476488494

#b、取自定义数里的随机数(多个元素）：
print(random.choice((1,2,3,4,5,6,7)))
#6
print(random.choice((1,2,3,4,5,6,7)))
#2
print(random.sample((1,2,3,4,5,6,7),3))
#[4, 5, 3]

#c、随机打乱顺序：

a=[1,2,3,4,5,6,7]
print(random.shuffle(a))
print(a)
#[6, 2, 5, 1, 7, 4, 3]

#d、获取N位随机数（二进制）：

print(random.getrandbits(200))
#771596897424695624466272211269661342068063847000212188678258
#注：random.getrandbits(n)，返回的是0-2^n之间的数

#8、log：指数函数，默认e为底数，结果为浮点数，可以自定义底数。

math.log(8)
#2.0794415416798357

print(math.log(8,2))
#3.0

#9、log10：以10为底数的指数函数。

print(math.log10(1000))
#3.0

#10、max，min：选出最大，最小值

max(1,3,5,2,4) #5
min(1,3,5,2,4) #1

#11、modf：将浮点数的整数位和小数位单独取出来

math.modf(13.5)
#(0.5, 13.0)

#12、sqrt：算出当前数的平方根

math.sqrt(49) #7.0

'''
七、其他数字相关内容
1、round与格式化输出
当输出以一定的格式来输出的时候，比如：a的值是2.5和2.335，2.345的时候，我们只需要小数点之后两位，
这个时候不会使用round函数来进行所谓的“四舍五入”，两者也会有点区别。
'''

round(2.5)
#2

print(format(2.5,'0.0f'))
#'2'

print(round(2.335,2))
#2.33

print(format(2.335,'0.2f'))
'2.33'

print(round(2.345,2))
#2.35

print(format(2.345,'0.2f'))
#'2.35'

#2、Decimal模块
#在使用浮点数的时候，因为计算机里是使用二进制来表示，所以会出现精度问题，当金融行业等不许出现一丝问题的时候，
# 我们会使用Decimal模块来解决精度问题。

a=2.1
b=4.2
print(a+b)
#6.300000000000001

from decimal import *
a= Decimal('2.1')
b= Decimal('4.2')
print(a+b)
Decimal('6.3')

'''
3、format格式化输出
使用bin(),oct(),hex()的时候会发现前面会加0b，0o，0x。我们不想要前缀的时候可以使用format函数来解决。

'''
a=153
print(bin(a),oct(a),hex(a))
#0b10011001 0o231 0x99

print(format(a,'b'),format(a,'o'),format(a,'x'))
#10011001 231 99

