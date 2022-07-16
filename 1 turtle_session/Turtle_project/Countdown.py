import time
def countdown(t):
    t = int(t)
    while t:

        min,sec = divmod(t,60)
        #print(min,sec)
        timer = '{:02}:{:02}'.format(min,sec)
        #print(timer)
        # '{:02}:{:02}:{:02}'.format(13,4,57)
        #c = f"{min}:{sec}"
        print(timer)
        time.sleep(1)
        t -= 1
    print("time's up")

t = input("Enter the times in secs秒: ")
#countdown(t)

t = input("Enter the times in secs秒: ")
#countdown(t)

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

mainloop()
