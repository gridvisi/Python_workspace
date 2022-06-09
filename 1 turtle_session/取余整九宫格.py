#返回结果
#


#数学  取整 取余

import turtle as t
def square(l,c): #
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(l)
        t.right(90)
        t.end_fill()

    return t.done()
l,c = 100,'#e946b9'
#print(square(l,c))

import turtle as t
colors =['#e2d8e2', '#a8996c', '#2d281f',
    '#9facb1', '#e9daa9', '#684a24',
    '#5c6051', '#bb783b',  '#86b086']
import string
c = string.ascii_lowercase
colors = ['#'+str(c[3:][i])*6 for i in range(16)]


#from random import *
import random
#bit_16 = []
def bit_16(n):
    ans = []
    for i in range(n):
        c = '#'+"".join([random.choice("0123456789ABCDEF") for i in range(6)])
        ans.append(c)
    return ans
n = 9
#print('bit16:',bit_16(n))
print("".join([random.choice("0123456789ABCDEF") for i in range(12)]))
print("".join([random.choice("0123456789ABCDEF") for i in range(30)]))
a = "".join([random.choice("0123456789ABCDEF") for i in range(12)])
#print(bytes.fromhex("a"))  # 转为bytes



def square(l,c): #
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(l)
        t.right(90)
    t.end_fill()
    return #t.done()
l,c = 100,'#e9daa9'
#print(square(l,c))

def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    colors = bit_16(n)
    print(colors)
    for i,c in enumerate(colors):

        t.penup()
        t.goto(x + (i % 3)*l, y-(i//3)*l) #算法怎么实现9个正方形的起笔位置准确入位？
        t.pendown()
        t.left(90)
        square(l, c)

    return t.done()
n,l = 9,100
x,y = -200,100
print(main_square(n,l,x,y))



# 3rd
def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i,c in enumerate(colors):

        t.penup()
        t.goto(x + (i%3)*l,y-(i//3)*l)
        t.pendown()
        t.left(90)
        square(l, c)

    return t.done()
n,l = 9,100
x,y = -200,100
#print(main_square(n,l,x,y))



# 2nd try!!
def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i,c in enumerate(colors):

        t.penup()
        t.goto(x + (i%3)*l,y-(i//3)*l)
        t.pendown()

        square(l, c)
        '''
        if not i%3 and i>0:
            t.penup()
            t.goto(x,y-l)
            t.pendown()
        '''
    return t.done()
n,l = 9,100
x,y = -200,200
#print(main_square(n,l,x,y))





# Try first time
def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i,c in enumerate(colors):
        square(l,c)
        t.goto(x+i*l,y)
        if not i%3:
            t.goto(x-l,y-l)
    return t.done()
n,l = 9,100
x,y = -200,200
#print(main_square(n,l,x,y))


#case 2nd
c = [
'lightcoral',
'coral',
'darkorange',
'gold',
'palegreen',
'paleturquoise',
'skyblue',
'plum',
'hotpink',
'pink']

sl = [1,2,3,4,5,6,7]

a = 's'




def add(x,y):
    return x * y

def fabnacci(x):
    return x

def ttm(name):  #define ： 定义
    return "牛人" #name[0] # #常量


name = "张瀚文"
print('return 返回结果：',ttm(name))


name = "lijunlin"
print('hello!',name)

print("hello,world")

names = ['zhangsan',"jack","henryparrot","mcree","thomas"]

for name in names:
    print("hello " + f"{name}")


print(1+1)



'''

colors = ['red','orange','yellow','green','blue','purple','pink']
colors = ['r','o']



print('for enumerate loop:')
for i,e in enumerate(3*colors):
    print(i,e)

print('for loop :')

for i in colors:
    print(i)


'''