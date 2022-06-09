import numpy as np
import matplotlib as plt

def fibo(n):
    if n == 0:
        fibo_list = np.array([0])
    elif n == 1:
        fibo_list = np.array([0,1])
    else:
        f_0, f_1 = 0, 1
        fibo_list = np.array([f_0,f_1])
        for i in np.arange(n-2):
            fibo_num = f_0 + f_1
            fibo_list = np.append(fibo_list,fibo_num)
            f_0, f_1 = f_1, fibo_num
    return fibo_list

import numpy as np
def find_o_xy(f_list):
    #起始圆心坐标
    x_n, y_n = 0, 0
    o_x_array, o_y_array = np.array([x_n]), np.array([y_n])
    for n in np.arange(1,len(f_list)):
        #需要注意pyhton中计数是从0开始
        #第一项作为起始点已经给出
        y_n=y_n+np.mod(n+1,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        x_n=x_n+np.mod(n,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        #横纵坐标(x,y)
        o_x_array = np.append(o_x_array, x_n)
        o_y_array = np.append(o_y_array, y_n)
    return o_x_array, o_y_array

'''3.绘制菲波那切数列曲线
已知圆心位置，圆的半径变化符合数列规律。因此，可以绘制曲线。
以n=5为例'''
# 以下绘图以n=7为例
count = 7
f_list = fibo(count)
x0_array, y0_array = find_o_xy(f_list)

# 各个正方形对应的边长,如例图半径从1,2...开始
f_list_r = fibo(count + 2)[2::]

# 画出各个正方形内的1/4圆
start_angle, end_angle = np.pi, 1.5 * np.pi
for n in np.arange(len(f_list)):
    t = np.arange(start_angle, end_angle, 0.001)
    circle_x = (f_list_r[n]) * (np.sin(t)) + x0_array[n]
    circle_y = (f_list_r[n]) * (np.cos(t)) + y0_array[n]

    start_angle += 0.5 * np.pi
    end_angle += 0.5 * np.pi

    plt.plot(circle_x, circle_y, color='b')

'''4.为仿照例图，画出正方形
确定方形顶点思路是先找到圆心对角的顶点，再写出另外两点。'''
count = 7
f_list = fibo(count)
x0_array, y0_array = find_o_xy(f_list)

f_list_r = fibo(count + 2)[2::]  # 各个正方形对应的边长
square_list = np.zeros([1, 2, 5])
start_angle, end_angle = np.pi, 1.5 * np.pi
for n in np.arange(len(f_list_r)):
    # 圆心坐标
    x0 = x0_array[n]
    y0 = y0_array[n]

    # 得到对角顶点坐标
    x2 = x0 + f_list_r[n] * (-1) ** ((np.mod(n + 1, 2) + n + 1) / 2)
    if n == 0:
        y2 = -1  # 起始点特殊目前只想到这么整了
    else:
        y2 = y0 + f_list_r[n] * (-1) ** (1 + (np.mod(n, 2) + n) / 2)

    # 其余两点坐标
    x1, x3 = x0, x2
    y1, y3 = y2, y0

    # 整合一下,画正方形需要回到原点，因此5个点
    pp = np.array([[[x0, x1, x2, x3, x0], [y0, y1, y2, y3, y0]]])

    # 画出圆弧
    t = np.arange(start_angle, end_angle, 0.001)
    circle_x = (f_list_r[n]) * (np.sin(t)) + x0_array[n]
    circle_y = (f_list_r[n]) * (np.cos(t)) + y0_array[n]
    start_angle += 0.5 * np.pi
    end_angle += 0.5 * np.pi

    plt.plot(pp[0][0][::], pp[0][1][::], color='b')
    plt.plot(circle_x, circle_y, color='b')


import numpy as np
import pylab as plt

# 产生菲波那切数列
def fibo(n):
    f_0 = 0
    f_1 = 1
    fibo_list = np.array([f_0,f_1])
    for i in np.arange(n-2):
        fibo_num = f_0 + f_1
        fibo_list = np.append(fibo_list,fibo_num)
        f_0, f_1 = f_1, fibo_num
    return fibo_list

#找出各个圆心
def find_o_xy(f_list):
    import pylab as plt
    x_n, y_n = 0, 0         #起始圆心坐标
    o_x_array, o_y_array = np.array([x_n]), np.array([y_n])
    for n in np.arange(1,len(f_list)):
        #需要注意pyhton中数组计数是从0开始
        #第一项作为起始点已经给出
        y_n=y_n+np.mod(n+1,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        x_n=x_n+np.mod(n,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        o_x_array = np.append(o_x_array, x_n)
        o_y_array = np.append(o_y_array, y_n)
    return o_x_array, o_y_array

count = 5
f_list = fibo(count)
x0_array,y0_array = find_o_xy(f_list)
#------------------------头像4----------------------------
f_list_r = fibo(count+2)[2::]
start_angle, end_angle = np.pi, 1.5*np.pi
fig = plt.figure(num=1,facecolor='k',figsize=(10,10))

#增加坐标轴对象，显示box
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True,aspect=1)

x_min, x_max, y_min, y_max = 0, 0, 0, 0
for n in np.arange(len(f_list_r)):
    #圆心坐标
    x0 = x0_array[n]
    y0 = y0_array[n]
    #得到对角顶点坐标
    x2 = x0+f_list_r[n]*(-1)**((np.mod(n+1,2)+n+1)/2)
    if n == 0:
        y2 = -1         #起始点特殊目前只想到这么整了
    else:
        y2 = y0+f_list_r[n]*(-1)**(1+(np.mod(n,2)+n)/2)
    #画出圆弧
    t=np.arange(start_angle,end_angle,0.001)
    circle_x = (f_list_r[n])*(np.sin(t))+x0_array[n]
    circle_y = (f_list_r[n])*(np.cos(t))+y0_array[n]
    start_angle += 0.5*np.pi
    end_angle += 0.5*np.pi
    #画图，在坐标轴上画图
    ax.plot(np.append(x0_array[n],np.append(circle_x,x0_array[n])),
            np.append(y0_array[n],np.append(circle_y,y0_array[n])),
            color='k',linewidth=5)

    ax.fill(np.append(circle_x,x0_array[n]),
            np.append(circle_y,y0_array[n]),
            facecolor='gold',
            alpha = 1)#f5bf03

#设置axes内的填充颜色
ax.patch.set_facecolor('k')

#调节坐标范围
x_min,x_max=8.5,-11.5
y_min,y_max=10,-10
mul_times = 1.5
ax.set_xlim(x_min*mul_times, x_max*mul_times)
ax.set_ylim(y_min*mul_times, y_max*mul_times)

#不显示坐标轴刻度以及刻度线
ax.tick_params(axis='both',labelsize=0,length=0)

#设置spine,即图形边框
ax.spines['top'].set_color('none')    #设置颜色
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')

#设置图片保存为png格式，有背景
plt.savefig('sdf.png',format = 'png',transparent=False,dpi=300)


'''
————————————————
版权声明：本文为CSDN博主「CD_Don」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/CD_Don/article/details/87212314
'''