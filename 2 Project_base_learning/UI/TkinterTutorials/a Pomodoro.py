'''
https://www.geeksforgeeks.org/create-a-pomodoro-using-python-tkinter/?ref=rp


在这篇文章中，我们将看到如何使用Python Tkinter创建Pomodoro。

为什么是 "点点通"？
专注于学习或工作是时间管理的最重要部分。当涉及到专注于工作时，我们总是把时间管理搞得一团糟。
幸运的是，你可以通过专注于你的工作来管理你的时间，然后进行短暂的休息来放松。庞多罗技术是更
受欢迎的技术，可以在特定时间内专注于工作，不受任何干扰。庞多罗在创建有效的时间管理系统方面
发挥了重要作用。

首先，你需要接受一项任务，并在没有任何分心的情况下连续工作25分钟。一旦完成了25分钟的时间，
就进行5分钟的短暂休息。在这5分钟里，你可以通过听音乐或简短的播客来放松你的大脑。每天重复
这个过程4到5次，你会看到一个巨大的变化。

使用Python Tkinter创建Pomodoro计时器
Pomodoro从25分钟的工作开始，你需要专注于25分钟。一旦25分钟，时间段完成，使用Tkinter的
消息框，你可以提示信息。休息时间也是如此。

现在，一旦我们导入了所需的库，接下来的事情就是创建一个GUI干扰。Pomodoro在意大利语中是
"番茄 "的意思。为了使这个GUI看起来很真实，我们将使用一个番茄图片作为背景图片。你可以使
用Canvas widget将背景图片添加到Tkinter应用程序中。最后讲到项目的最后一部分是对倒计时
器进行编程。

我们将使用时间模块来处理倒计时的问题。由于你现在已经熟悉了Pomodoro技术，首先创建一个25
分钟工作的命令函数。初始化分、秒变量，并将工作和休息时间的总秒数存储在一个变量中。递减计
数器并每秒更新GUI窗口。一旦计数达到零，你应该从工作切换到休息，或者反过来。当你专注于工
作时，你将如何知道计数为零？你可以在这里使用Tkinter的消息框。此外，你甚至可以实现一个
playingsound模块，在计数为0时播放小音乐。

下面是在Tkinter中编写Timer语法的技巧。

因为初始时间是25分钟，所以首先要把分钟转换为秒。
'''

# timer = minutes*60
timer = 25*60 #for work
timer = 5*60 #for break

# divmod syntax: divmod(x,y) => returns tuple (x//y,x%y)
minute, second = divmod(1366, 60)
print(minute)
print(second)

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time


class Pomodoro:
    def __init__(self, root):
        self.root = root

    def work_break(self, timer):

        # common block to display minutes
        # and seconds on GUI
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)

    def work(self):
        timer = 25 * 60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:
                # once work is done play
                # a sound and switch for break
                playsound("sound.ogg")
                messagebox.showinfo(
                    "Good Job", "Take A Break, \
                    nClick Break Button")
            timer -= 1

    def break_(self):
        timer = 5 * 60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:
                # once break is done,
                # switch back to work
                playsound("sound.ogg")
                messagebox.showinfo(
                    "Times Up", "Get Back To Work, \
                    nClick Work Button")
            timer -= 1

    def main(self):

        # GUI window configuration
        self.root.geometry("450x455")
        self.root.resizable(False, False)
        self.root.title("Pomodoro Timer")

        # label
        self.min = tk.StringVar(self.root)
        self.min.set("25")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root,
                                  textvariable=self.min, font=(
                "arial", 22, "bold"), bg='#37B0B4', fg= '#53616A')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root,
                                  textvariable=self.sec, font=(
                "arial", 22, "bold"), bg= '#53616A', fg='white')
        self.sec_label.pack()
        '''
        ['#4A01A0', '#B66AAA', '#37B0B4', '#814208', 
        '#72C47D', '#B0F71C', '#C478E5', '#BB38F4', '#FF0AB1']
        
        ['#6C7B3C', '#0418F8', '#935C19', '#7131B9', '#4150F3', 
        '#3E8EB3', '#682C0D', '#684DA7', '#53616A']
        '''

        # add background image for GUI using Canvas widget
        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill="both")
        img = Image.open('pomodoro.jpg')
        bg = ImageTk.PhotoImage(img)
        canvas.create_image(90, 10, image=bg, anchor="nw")

        # create three buttons with countdown function command
        btn_work = tk.Button(self.root, text="Start",
                             bd=5, command=self.work,
                             bg='#6DC2CE', font=(
                "arial", 15, "bold")).place(x=140, y=380)
        btn_break = tk.Button(self.root, text="Break",
                              bd=5, command=self.break_,
                              bg='#6DC2CE', font=(
                "Calibri", 15, "bold")).place(x=240, y=380)

        '''
        ['#59CFD0', '#743460', '#AC570A', '#2A8595', '#EC4B8C', 
        '#3540EB', '#8AD183', '#E87BB7', '#D90367']
        '''

        self.root.mainloop()


if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()