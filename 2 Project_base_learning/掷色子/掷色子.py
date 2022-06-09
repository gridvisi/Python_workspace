
import turtle as t#导入turtle库并赋值为t
import time#导入time库
import random#导入随机函数
import sys#导入sys库
def screenint():#初始化屏幕设置
    global name
    t.title("骰子游戏！")#标题
    t.setup(width=570, height=350, startx=400, starty=300)#设置游戏窗口大小
    t.screensize(500, 300)#设置玩者信息输入框窗口大小
    name = t.textinput('完善信息', '输入姓名：')#设置玩者信息提示
    t.up()#抬笔
    t.goto(-100, 30)#去到指定坐标
    t.write(name + "正在掷扔出骰子……", align='left', font=('微软雅黑', 14, 'normal'))#在游戏窗口写下相关内容
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
def ai_int():#电脑掷骰子数
    global  ai_count#设置全局变量，用来存储获得电脑的骰子数
    ai_count = random.choice(('one', 'two', 'three', 'four', 'five', 'six'))#随机获得骰子数
    t.up()#抬笔
    t.goto(100, 30)#移动到指定坐标点
    t.write("电脑正在扔出骰子……", align='right', font=('微软雅黑', 14, 'normal'))#在游戏窗口写下相关内容
    time.sleep(2)#设置延时2s
    t.undo()#撤销上一个动作
def beauty():#设置彩蛋功能
    beauty_c = 0#设置变量初始值为0
    t.setx(-200)#设置初始x的坐标
    t.pensize(2)#落笔尺寸设置为2
    t.down()#落笔
    t.color('red', 'yellow')#设置边框和填充颜色
    t.speed(8)#设置绘画的速度为8
    t.begin_fill()#开始填充
    while True:
        beauty_c += 1#每次变量加1
        t.fd(200)#向前移动200的像素
        t.lt(170)#逆时针旋转170度
        if beauty_c == 36:#判断如果变量等于36
            break#结束循环
    t.end_fill()#填充完毕
    t.done()#停止当前动作，保持当前画布
def pk():#设置比大小功能
    u_count = int(eval(user_count)[0])#将获取到的玩者掷骰子点数转换成整形
    a_count = int(eval(ai_count)[0])#将获取到的电脑掷骰子点数转换成整形
    if u_count == a_count:#点数如果相等
        t.write('打成平局！', align='right', font=('微软雅黑', 30, 'normal'))#在画布写下相应的内容
    elif u_count > a_count:#如果玩者点数大
        t.write('恭喜' + name + '胜利！', align='right', font=('微软雅黑', 30, 'normal'))#在画布写下相应的内容
        beauty()#调用彩蛋功能
    else:#否则玩者点数小
        t.write('好可惜！电脑赢了！', align='right', font=('微软雅黑', 30, 'normal'))#在画布写下相应的内容
    time.sleep(2)#延时2s
    t.bye()#关闭海龟绘图窗口
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
ai_int()#调用电脑掷骰子数
num(100)#设置每个点子对应的坐标数
frame(eval(ai_count),100)#绘制骰子边框和点子
pk()#调用比大小函数