#https://www.jianshu.com/p/9c4ee8cb9b09

import random
import tkinter as tk
import time

    #方法一
def func1():

    text1.delete(1.0,tk.END)
    start = time.clock()
    amount = int(entry1.get())
    num = int(entry2.get())
    list1 = []
    for i in range(0,num-1):        # 生成 n-1 个随机节点
        a = random.randint(0,amount)
        list1.append(a)
    list1.sort()                    # 节点排序
    list1.append(amount)            # 设置第 n 个节点为amount，即总金额

    list2 = []
    for i in range(len(list1)):
        if i == 0:
            b = list1[i]            # 第一段长度为第 1 个节点 - 0
        else:
            b = list1[i] - list1[i-1]   # 其余段为第 n 个节点 - 第 n-1 个节点
        text1.insert('end',str(b) + '  ')
        list2.append(b)
    end = time.clock()
    text1.insert('end','\n耗时：%s 秒' %(end - start))
    print(list2)                    # 打印耗时

    # 方法二
def func2():
    text2.delete(1.0,tk.END)
    start = time.clock()
    amount = int(entry1.get())
    num = int(entry2.get())

    list3 = []
    num2 = num                      # 剩余红包数
    for i in range(0,num):
        if num2 != 1:                   # 除了最后一个随机数，其余随机数的生成规则
            mu = int(amount / num2)
            sigma = 5                   # 设定方差 sigma 为一个常数
            isnotpos = True
            while isnotpos:             # 循环，当生成的随机数小于0或者剩余总额小于0时重新生成随机数
                a = random.normalvariate(mu,sigma)
                if a > 0:
                    if (amount - a) > 0:
                        isnotpos = False
            a = int(a)
            text2.insert('end',str(a) + '  ')
            list3.append(a)
            amount = amount - a         # 计算剩余总额
            num2 = num2 - 1             # 剩余红包数 - 1
        else:                           # 最后一个随机数就等于最后剩余的总额
            a = amount
            text2.insert('end',str(a) + '  ')
            list3.append(a)
    end = time.clock()
    text2.insert('end','\n耗时：%s 秒' %(end - start))  # 打印耗时
    print(list3)

win = tk.Tk()                          # 用tkinter写界面
win.geometry('600x350')
win.title("红包生成器")

label = tk.Label(win, text="点击生成你的红包!",font=('黑体,40'))
label.pack(side = 'top',pady = '30')

frm = frm1 = tk.Frame(win)
frm.pack()

label1 = tk.Label(frm, text="请输入红包金额 :")
label1.pack(side = 'left')
entry1 = tk.Entry(frm, width = 5)
entry1.pack(side = 'left',padx = '20')

label2 = tk.Label(frm, text="请输入红包个数 (1-10):")
label2.pack(side = 'left')
entry2 = tk.Entry(frm, width = 5)
entry2.pack(side = 'left',padx = '20')

frm1 = tk.Frame(win)
frm1.pack(pady = '30')
frm2 = tk.Frame(win)
frm2.pack(pady = '30')

text1 = tk.Text(frm1, height=2,width=55)
text2 = tk.Text(frm2, height=2,width=55)
btn1 = tk.Button(frm1,text='方法一',command = func1)
btn2 = tk.Button(frm2,text='方法二',command = func2)

text1.pack(side = 'left',padx = '50')
btn1.pack(side = 'right', padx = '20')
text2.pack(side = 'left',padx = '50')
btn2.pack(side = 'right', padx = '20')

text1.pack()

win.mainloop()