'''
https://www.geeksforgeeks.org/creat-an-alarm-clock-using-tkinter/?ref=rp

先决条件。Python GUI - tkinter, winsound, time, and datetime。

我们都知道，现在按时起床是一件非常困难的事情。解决方案就是闹钟。在这篇文章中，我们将学习，如何在Python中使用Tkinter创建一个闹钟。如果没有闹钟，一些人就会睡过头，上班迟到。闹钟对于保持正常的睡眠时间也很有用。

Tkinter。Python为开发GUI（图形用户界面）提供了多种选择。在所有的GUI策略中，Tkinter是最常使用的技术。它是与Python一起提供的Tk GUI工具包的一个习惯性Python接口。
Winsound。winsound模块提供了对Windows平台所提供的基本声音播放机制的访问。它包括函数和其他一些常量。鸣叫PC的扬声器。
时间。Python中的时间模块提供各种与时间有关的功能。该模块与Python的普通模块一起出现。
datetime。datetime的主要重点是使访问与日期、时间和时区有关的事物的属性更加简单。


'''

# Import Required Library
from tkinter import *
import datetime
import time
import winsound


def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm:
			print("Time to Wake up")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)


# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")


# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()