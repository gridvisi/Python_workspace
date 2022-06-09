'''
https://www.codewars.com/kata/5706be574f2c297a7b00060d/train/python

Inputs:
Starting price: start (dollars)
Use: soil (percentage)
Age: age (years)
The action pants appreciate every year depending on the level to which they are soiled
(soil input):

Barely used: 10
Seen a few high kicks: 25
Blood stained: 30
Heavily soiled: 50

@test.describe("Example Tests")
def test_group():
    @test.it("Basic tests")
    def test_case():
        test.assert_equals(price(19.95, 'Barely used', 3), '$26.55')
        test.assert_equals(price(27.76, 'Seen a few high kicks', 15), '$788.99')
        test.assert_equals(price(13.26, 'Blood stained', 25), '$9356.80')
        test.assert_equals(price(44.11, 'Heavily soiled', 7), '$753.66')
        test.assert_equals(price('pants', 6, 7), 'Chuck is bottomless!')
'''
from decimal import *
import math
print(float('%.2f' % math.pi))

def price(start, soil, age):
    if isinstance(start,float) and isinstance(soil,str) and isinstance(age,int):
        rate = {'Barely used':0.1,
            'Seen a few high kicks':0.25,
            'Blood stained': 0.30,
            'Heavily soiled':0.50,
            }
        ans = start * (1 + rate[soil])**age
        return '%.2f'%ans  #float('%.2f' % start * (1 + rate[soil])**age)
    else: return 'Chuck is bottomless!'

# round 遇到xxx.x0时，只保留1位小数， f"${round(start * (1 + rate.get(soil,1))**age,2)}"

start, soil, age = 19.95, 'Barely used', 3
start, soil, age = 27.76, 'Seen a few high kicks', 15
start, soil, age = 13.26, 'Blood stained', 25
print(price(start, soil, age))

#1st
def price(start, soil, age):
    yrate = {'Barely used':1.1, 'Seen a few high kicks':1.25,
             'Blood stained':1.3, 'Heavily soiled':1.5}
    try:
        return f"${start*(yrate.get(soil)) **age :0.2f}"
    except:
        return "Chuck is bottomless!"

print(1.15 ** 15 * 27.76)
print(1.15 * 15 * 27.76)


'''
python保留两位小数

a = 5.5461

方法一：round(a,2)
方法二：float('%.2f' % a)
方法三：‘%.2’ %a
方法四：

from decimal import Decimal
Decimal('5.026').quantize(Decimal('0.00'))



当需要输出的结果要求有两位小数的时候，字符串形式的：'%.2f' % a 方式最好，其次用Decimal。
需要注意的：
1. 可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确。
2. Decimal还可以用来限定数据的总位数。
'''