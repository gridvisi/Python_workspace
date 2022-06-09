#  [18,12] #最大公约数 == 12,18%12 == 12,6


import turtle as t
colors =['#e2d8e2', '#a8996c', '#2d281f',
    '#9facb1', '#e9daa9', '#684a24',
    '#5c6051', '#bb783b',  '#86a086',]

def square(l,c): #子函数输出小正方形
    t.color(c)
    t.begin_fill()
    for i in range(4): #浪费时间，4不能做到九宫格，5
        t.forward(l)
        t.right(90)
    t.end_fill()
    return #'output'   #t.done()

#主函数：

def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i,c in enumerate(colors): #len(colors)=9
        #enumerate for循环加地址坐标
        print(i,c)
        t.penup()
        t.goto(x + (i % 3)*l, y - (i//3)*l)  #取余，取整
        # for
        t.pendown()
        t.left(90)
        square(l, c)  #

    return t.done()
n,l = 9,100
x,y = -200,100
print(main_square(n,l,x,y))