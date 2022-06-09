__author__ = 'Administrator'

import math
import sys		#用于将浮点数与0比较
import cmath		#import cmath是用于计算复数的平方根函数
def get_float(msg,allow_zero):  #获取用户输入函数，并判断是否为浮点值和能否为0，allow_zero是布尔值，指定是否可以输入0
    x=None
    while x is None:
        try :					#这里的try可使得当用户输入的不是数值是提示出错，但循环继续，如果没有try，函数就会中断
            x=float(input(msg))
            if not allow_zero and x<sys.float_info.epsilon:  #sys.float_info.epsilon 是两个浮点数比较的最小差值，这一句是判断输入是否为0
                print("zero is not allowed")
                x=None
        except ValueError as err:
            print(err)
    return x

print("ax\N{SUPERSCRIPT TWO}+bx+c=0") 		#\{ASCII码} 可以输出指定的ASCII码的符号，这里是２的平方的ASCII码（开始一直看不懂...）
a=get_float("enter a:",False)
b=get_float("enter b:",True)
c=get_float("enter c:",True)
x1=None
x2=None
discriminant=(b ** 2)-(4 * a * c)
if discriminant==0:
    x1=-(b/(2*a))
else:
    if discriminant>0:
        root=math.sqrt(discriminant)
    else:
        root=cmath.sqrt(discriminant)		#cmath
    x1=(-b+root)/(2*a)
    x2=(-b-root)/(2*a)
equation=("{0}x\N{SUPERSCRIPT TWO}+{1}x+{2}=0"
          "\N{RIGHTWARDS ARROW} x={3}").format(a,b,c,x1)
if x2 is not None:
    equation += " or x={0}".format(x2)

print(equation)