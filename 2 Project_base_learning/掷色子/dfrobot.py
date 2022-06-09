
#第十课 扔骰子游戏

import turtle as t#导入turtle库并赋值为t
import time#导入time库
def screenint():#初始化屏幕设置
    global name
    t.title("骰子游戏！")#标题
    t.setup(width=570, height=350, startx=400, starty=300)#设置游戏窗口大小
    t.screensize(500, 300)#设置玩者信息输入框窗口大小
    name = t.textinput('完善信息', '输入姓名：')#设置玩者信息提示
    t.up()#抬笔
    t.goto(-100, 30)#去到指定坐标
    t.write(name + "正在掷出骰子……", align='left', font=('微软雅黑', 14, 'normal'))#在游戏窗口写下相关内容
    time.sleep(2)#设置延时2s
    t.clear() #清空画布
screenint()#调用这个函数


import turtle as t
import time
import random
def screenint():#初始化屏幕设置
    global name
    t.title("骰子游戏！")#标题
    t.setup(width=570, height=350, startx=400, starty=300)#设置游戏窗口大小
    t.screensize(500, 300)#设置玩者信息输入框窗口大小
    name = t.textinput('完善信息', '输入姓名：')#设置玩者信息提示
    t.up()#抬笔
    t.goto(-100, 30)#去到指定坐标
    t.write(name + "正在掷出骰子……", align='left', font=('微软雅黑', 14, 'normal'))#在游戏窗口写下相关内容
    time.sleep(2)#设置延时2s
    t.clear() #清空画布
def num(os):#设置每个点子对应的坐标数
    global one, two, three, four, five, six#定义全局变量
    one = (1, (50 + os, -50))#设置点数1的坐标
    two = (2, (25 + os, -50), (75 + os, -50))#设置点数2时两个点的坐标
    three = (3, (50 + os, -25), (25 + os, -75), (75 + os, -75))#设置点数3时三个点的的坐标
    four = (4, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75))#设置点数4时四个点的的坐标
    five = (5, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75), (50 + os, -50))#设置点数5时五个点的的坐标
    six = (6, (25 + os, -25), (75 + os, -25),
          (25 + os, -75), (75 + os, -75),
          (25 + os, -50), (75 + os, -50))#设置点数6时六个点的的坐标
def user_int():#玩者掷骰子数
    global user_count#设置全局变量，用来存储获得玩者的骰子数
    user_count = random.choice(('one', 'two', 'three', 'four', 'five', 'six'))#随机获得骰子数
def draw_dot(n):#绘制骰子点子
    for d in range(n[0]):#不同点子，执行不同的循环次数
        x = n[d + 1][0]#获取x的坐标值
        y = n[d + 1][1]#获取y的坐标值
        t.goto(x, y)#移动到指定坐标
        t.dot(25, 'red')#绘制一个直径为25，颜色为红色的圆
        t.up()#提笔
def frame(dot, os):#绘制骰子边框
    t.color('black')#设置颜色为黑色
    t.pensize(5)#设置尺寸为5
    t.up()#提笔
    t.goto(0 + os, 0)#移动到指定坐标
    t.down()#落笔
    t.speed(10)#设置画笔速度为10
    for i in range(4):#绘制正方形边框
        t.forward(100)#向前移动100像素
        t.right(90)#右转90度
    t.up()#提笔
    draw_dot(dot)#调用绘制骰子点子函数
    time.sleep(1)#延时1s
screenint()#调用屏幕初始化函数
user_int()#调用玩者掷骰子数
num(-150)#设置每个点子对应的坐标数
frame(eval(user_count), -150)#绘制骰子边框和点子


#4.1代码中自定义的num(os)函数的使用
def num(os):#设置每个点子对应的坐标数
    global one, two, three, four, five, six#定义全局变量
    one = (1, (50 + os, -50))#设置点数1的坐标
    two = (2, (25 + os, -50), (75 + os, -50))#设置点数2时两个点的坐标
    three = (3, (50 + os, -25), (25 + os, -75), (75 + os, -75))#设置点数3时三个点的的坐标
    four = (4, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75))#设置点数4时四个点的的坐标
    five = (5, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75), (50 + os, -50))#设置点数5时五个点的的坐标
    six = (6, (25 + os, -25), (75 + os, -25),
          (25 + os, -75), (75 + os, -75),
          (25 + os, -50), (75 + os, -50))#设置点数6时六个点的的坐标

#4
def frame(dot, os):#绘制骰子边框
    t.color('black')#设置颜色为黑色
    t.pensize(5)#设置尺寸为5
    t.up()#提笔
    t.goto(0 + os, 0)#移动到指定坐标
    t.down()#落笔
    t.speed(10)#设置画笔速度为10
    for i in range(4):#绘制正方形边框
        t.forward(100)#向前移动100像素
        t.right(90)#右转90度
    t.up()#提笔
    draw_dot(dot)#调用绘制骰子点子函数
    time.sleep(1)#延时1s