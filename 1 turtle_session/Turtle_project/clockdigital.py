
import time
print('{:02}:{:02}:{:02}'.format(13,4,57))

#常量 和 变量

t = 1   # 整数型
print(type(t))
t = '1' # str = 字符串型
print(type(t))
print(int(t) / 1)
print(type(t))

def countdown(t):
    t = int(t) #integer

    while t:
        min,sec = divmod(t,60)  #
        #print(min,sec)
        timer = '{:02}:{:02}'.format(min,sec)
        #print(timer)
        # '{:02}:{:02}:{:02}'.format(13,4,57)
        #c = f"{min}:{sec}"
        print(timer)
        time.sleep(1)
        t -= 1
    print("time's up")

t = input("Enter the times in secs 秒: ")
countdown(t)

# skin
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Digital clock')
label = Label(root,font=('aerial',60),background='black',foreground='white')

def timer():
    strs = strftime("%H:%M:%S %p")
    label.config(text=strs)
    label.after(1000,timer)

label.pack(anchor='center')
timer()

#mainloop()


#3 countdown with skin


# skin
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Digital clock')
label = Label(root,font=('aerial',40),background='black',foreground='white')

def timer():
    strs = strftime("%H:%M:%S %p")
    label.config(text=strs)
    label.after(1000,timer)

label.pack(anchor='center')
timer()

#mainloop()

