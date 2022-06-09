

import turtle as t
t.speed(0)
def zfx(a=200):
    for i in range(4):
        t.forward(a)
        t.left(90)

#然后再写一个函数，主要是为了给正方形做颜色填充和显示文字

def zfx2(a=100,x=0,y=0,c='gray',s=''):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    zfx(a)
    t.end_fill()
    t.forward(a/2)
    t.write(str(s),align='center',font=('宋体',50,'bold'))

#画九宫格的函数，画九个格子，接收一个参数，一个字符串，把要显示的数字传进来。

def jgg(s='012345678'):
    zfx2(x=-150,y=50,c='gray',s=s[0])
    zfx2(x=-50,y=50,c='white',s=s[1])
    zfx2(x=50,y=50,c='gray',s=s[2])
    zfx2(x=-150,y=-50,c='white',s=s[3])
    zfx2(x=-50,y=-50,c='gray',s=s[4])
    zfx2(x=50,y=-50,c='white',s=s[5])
    zfx2(x=-150,y=-150,c='gray',s=s[6])
    zfx2(x=-50,y=-150,c='white',s=s[7])
    zfx2(x=50,y=-150,c='gray',s=s[8])

# 就是暴力算法，用到random的库shuffle函数，这个函数可以打乱元素。然后8个条件满足了就画图，
# all函数是列表所有元素都是True那么就返回True，这个用来这里代码写起来就比较简洁了，不要写
# 一堆逻辑运算或者条件运算了。

import random
n=[1,2,3,4,5,6,7,8,9]
w=t.Screen()
def run(x,y):
    while(1):
        random.shuffle(n)
        real=[(n[0]+n[1]+n[2])==15,
        (n[3]+n[4]+n[5])==15,
        (n[6]+n[7]+n[8])==15,
        (n[0]+n[3]+n[6])==15,
        (n[1]+n[4]+n[7])==15,
        (n[2]+n[5]+n[8])==15,
        (n[0]+n[4]+n[8])==15,
        (n[2]+n[4]+n[6])==15]
        if all(real):
            jgg(n)
        break
w.onclick(run)
t.mainloop()