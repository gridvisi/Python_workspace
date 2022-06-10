
'''
全班同学挑选运动服，校运动会规定每位同学的衣服颜色和数字必须有一样是不同的才行。例如，
衣服上的编号相同，颜色不同是容许的，或者颜色不同，数字相同也是容许的。请问，以上图的4种颜
色和6个数字组合，最多能满足多少同学的衣服符合要求？

(2) 升级任务：全班同学排出一列长队出场开幕式。要求队伍中每个人与前后的同学颜色和
数字都不同，请问共有多少种不同的排列方式？

(3) 升级任务：全班同学排出 m *  n 的方阵出场开幕式。要求每个同学前后左右的同学
颜色和数字都不同，请问共有多少种不同的排列方式？

通过以上找到一种算法。
team = [c + str(n) for c,n in zip(color,num)]
'''

color = ['r','y','g','b']
num = [1,2,3,4,5,6]
t = []
def teams(color,num):
    for c in color:
        for n in num:
            t.append(c+str(n))
    return t
print(teams(color,num))

def line(color,num):

    i = 0
    cdict = {k:v for k,v in zip(color,[num]*len(color))}
    team,n = ['r1'],1


    return cdict
print(line(color,num))


import random
import turtle as t
def bit_16(n):
    ans = []
    for i in range(n):
        c = '#'+"".join([random.choice("0123456789ABCDEF") for i in range(6)])
        ans.append(c)
    return ans

def square(l,c): #
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(l)
        t.right(90)
    t.end_fill()
    return       #t.done()

def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    colors = bit_16(n)
    print(colors)
    for i,c in enumerate(colors):
        t.penup()
        t.goto(x + (i % 3)*l, y-(i//3)*l)
        #算法怎么实现9个正方形的起笔位置准确入位？
        t.pendown()
        t.left(90)
        square(l, c)

    return t.done()
n,l = 9,100
x,y = -200,100
print(main_square(n,l,x,y))