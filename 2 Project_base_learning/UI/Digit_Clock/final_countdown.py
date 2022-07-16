t = 1000
min, sec = divmod(t, 365)  # 模运算

print(1000 % 365, 1000 // 365, 1000 / 365)
print(min, sec)

n = 16
m = 16
print(id(m), id(n))

print(f"{n} 八进制是", oct(16))
print(bin(n))
print(hex(n))

'''
pip install cx_Freeze
cxfreeze -c YOUR_PROGRAM.py -–target-dir dist -–target-name NAME_OF_EXE

https://www.geeksforgeeks.org/convert-python-script-to-exe-file/

pyinstaller --onefile -w 'filename.py'
'''
import time

print('{:02}:{:02}:{:02}'.format(13, 4, 57))


def countdown(t):  # 函数
    # 错误提示输入的类型有错 pi，-1000
    t = abs(int(t))  # 取整 绝对值
    while t:  # t=20，t -= 1
        min, sec = divmod(t, 60)
        # print(min,sec)
        timer = '{:02}:{:02}'.format(min, sec)
        # print(timer)
        # '{:02}:{:02}:{:02}'.format(13,4,57)
        # c = f"{min}:{sec}"
        print(timer)
        time.sleep(1)
        t -= 1
    print("time's up")


t = int(input("Enter the times in secs秒: "))
# countdown(t)


# tk
# http://c.biancheng.net/tkinter/what-is-tkinter.html
# 为什么很多IDE都使用Courier New作为默认字体？
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('倒计时开始 Final Countdown')
root.geometry('350x150')
label = Label(root, font=('YouYuan', 100), background='#66A5BB', foreground='white')
# label = Label(root,font=('Microsoft YaHei',40),background='dark grey',foreground='white')
# font option https://zhuanlan.zhihu.com/p/491101710
# Courier New
# Console
# 仿宋体
'''
https://mp.weixin.qq.com/s?__biz=MzI4NjAyNTMxMQ==&mid=2649458178&idx=2&sn=71ea9a85919e30fafda150a34826c10a&chksm=f3fc1532c48b9c242ec86c2f6d46fd4c66164a64449e32ad4e24042f583f14ce76c343b0d36d&scene=21#wechat_redirect

turtle色彩：调色板九宫格之二

['#F97693', '#C5564C', '#F17F38', '#713F91', '#91958C',
 '#2DEEF0', '#11CA40', '#B19080', '#A568A0']


['#59CFD0', '#743460', '#AC570A', '#2A8595', '#EC4B8C', 
'#3540EB', '#8AD183', '#E87BB7', '#D90367']

['#B2B70A', '#6678F6', '#EFB5AB', '#11182B', '#F76ADB', 
'#EA7F64', '#6EB1EC', '#0D942D', '#226F46']

['#82943C', '#46FE86', '#4A6157', '#1B125F', '#0354A7', 
'#C0C95C', '#87C3DE', '#07C890', '#66A5BB']

# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=root.Button(root,text="关闭",command=root.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
root.mainloop()
'''


def st(t):
    while t >= 0:
        min, sec = divmod(int(t), 60)
        # print(min,sec)
        strs = '{:02}:{:02}'.format(min, sec)
        time.sleep(1)
        t -= 1
        return strs


it = iter([i for i in range(t)][::-1])


def timer():
    # strs = strftime("%H:%M:%S %p")
    t = next(it)
    if t:
        time.sleep(0.1)
        label.config(text=st(t))
        label.after(1000, timer)


label.pack(anchor='center')
timer()
mainloop()

'''
字体名称    英文名称    Unicode 编码
宋体  SimSun  \5B8B\4F53
新宋体 NSimSun \65B0\5B8B\4F53
黑体  SimHei  \9ED1\4F53
微软雅黑    Microsoft YaHei \5FAE\8F6F\96C5\9ED1
楷体_GB2312   KaiTi_GB2312    \6977\4F53_GB2312
隶书  LiSu    \96B6\4E66
幼园  YouYuan \5E7C\5706
华文细黑    STXihei \534E\6587\7EC6\9ED1
细明体 MingLiU \7EC6\660E\4F53
新细明体    PMingLiU    \65B0\7EC6\660E\4F53


颜色选择：

['#F97693', '#C5564C', '#F17F38', '#713F91', '#91958C',
 '#2DEEF0', '#11CA40', '#B19080', '#A568A0']
'''
