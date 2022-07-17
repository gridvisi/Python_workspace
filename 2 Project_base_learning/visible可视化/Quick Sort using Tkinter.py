'''
https://www.geeksforgeeks.org/visualizing-quick-sort-using-tkinter-in-python/?ref=rp

先决条件。快速排序（QuickSort

Tkinter是一个非常容易使用且对初学者友好的GUI库，可用于将排序算法可视化。这里的快速排序算法是可视化的，它是一种分而治之的算法。它首先考虑一个支点元素，然后创建两个子数组来保存小于支点值的元素和大于支点值的元素，然后递归排序子数组。该算法有两个基本操作，即原地交换项目和分割数组的一个部分。这个过程通过递归重复进行，直到子数组小到可以轻松排序。最终，较小的子数组可以一个一个地放在另一个上面，产生一个完全排序的元素集。

在这篇文章中，我们将使用Python GUI库Tkinter来展示QuickSort算法的可视化。

算法。

选择任何元素作为支点
小于支点的元素被放在它的前面，大于支点的元素被放在它的后面。在支点的两侧创建两个子数组。
同样的过程被递归地应用于左右两个子数组，以对它们进行排序。
时间复杂度:

最好的情况。最好的情况是，支点总是将数组分成两个相等的部分。在最好的情况下，结果将是对数(N)级的分区，最上一级有一个大小为N的数组，下一级有一个大小为N/2的数组，以此类推。快速排序算法的最佳情况下的复杂度是O(log N)
最坏的情况。最坏的情况将发生在枢轴对数组的分解工作做得不好的时候，也就是说，当一个分区中没有元素，而另一个分区中有N-1个元素的时候。快速排序的最坏情况下的时间复杂度将是O(N^2)。
快速排序的扩展代码:

这是快速排序算法的扩展代码，它被导入Tkinter可视化软件的主代码中，以实现快速排序算法并返回排序结果。

# 扩展快速排序代码
'''

# Extension Quick Sort Code
# importing time module
import time


# to implement divide and conquer
def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head,
                                 tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head,
                                     tail, border, j))
        time.sleep(timeTick)

    # swapping pivot with border value
    drawData(data, getColorArray(len(data), head,
                                 tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border


# head  --> Starting index,
# tail  --> Ending index
def quick_sort(data, head, tail,
               drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head,
                                 tail, drawData,
                                 timeTick)

        # left partition
        quick_sort(data, head, partitionIdx - 1,
                   drawData, timeTick)

        # right partition
        quick_sort(data, partitionIdx + 1,
                   tail, drawData, timeTick)


# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - after all elements are sorted

# assign color representation to elements


def getColorArray(dataLen, head, tail, border,
                  currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('Grey')
        else:
            colorArray.append('White')

        if i == tail:
            colorArray[i] = 'Blue'
        elif i == border:
            colorArray[i] = 'Red'
        elif i == currIdx:
            colorArray[i] = 'Yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'Green'

    return colorArray


# code for Quick Sort Visualizer
# using Python and Tkinter
# import modules
from tkinter import *
from tkinter import ttk
import random

# initialising root class for Tkinter
root = Tk()
root.title("Quick Sort Visualizer")

# maximum window size
root.maxsize(900, 600)
root.config(bg="Black")

select_alg = StringVar()
data = []


# function to generate the data values
# by accepting a given range
def generate():
    global data

    # minval : minimum value of the range
    minval = int(minEntry.get())

    # maxval : maximum value of the range
    maxval = int(maxEntry.get())

    # sizeval : number of data
    # values/bars to be generated
    sizeval = int(sizeEntry.get())

    # creating a blank data list which will
    # be further filled with random data values
    # within the entered range
    data = []
    for _ in range(sizeval):
        data.append(random.randrange(minval, maxval + 1))

    drawData(data, ['Red' for x in range(len(data))])


# function to create the data bars
# by creating a canvas in Tkinter
def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width / (len(data) + 1)
    offset = 30
    spacing = 10
    # normalizing data for rescaling real-valued
    # numeric data within the
    # given range
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        # top left corner
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340

        # bottom right corner
        x1 = ((i + 1) * x_width) + offset
        y1 = can_height

        # data bars are generated as Red
        # colored vertical rectangles
        canvas.create_rectangle(x0, y0, x1, y1,
                                fill=colorlist[i])
        canvas.create_text(x0 + 2, y0, anchor=SE,
                           text=str(data[i]))
    root.update_idletasks()


# function to initiate the sorting
# process by calling the extension code
def start_algorithm():
    global data

    if not data:
        return

    if (algmenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data) - 1, drawData, speedbar.get())
        drawData(data, ['Green' for x in range(len(data))])


# creating main user interface frame
# and basic layout by creating a frame
Mainframe = Frame(root, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

# creating user interface area in grid manner
# first row components
Label(Mainframe, text="ALGORITHM",
      bg='Grey').grid(row=0, column=0,
                      padx=5, pady=5,
                      sticky=W)

# algorithm menu for showing the
# name of the sorting algorithm
algmenu = ttk.Combobox(Mainframe,
                       textvariable=select_alg,
                       values=["Quick Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)

# creating Start Button to start
# the sorting visualization process
Button(Mainframe, text="START",
       bg="Blue",
       command=start_algorithm).grid(row=1,
                                     column=3,
                                     padx=5,
                                     pady=5)

# creating Speed Bar using scale in Tkinter
speedbar = Scale(Mainframe, from_=0.10,
                 to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL,
                 label="Select Speed")
speedbar.grid(row=0, column=2,
              padx=5, pady=5)

# second row components
# sizeEntry : scale to select
# the size/number of data bars
sizeEntry = Scale(Mainframe, from_=3,
                  to=60, resolution=1,
                  orient=HORIZONTAL,
                  label="Size")
sizeEntry.grid(row=1, column=0,
               padx=5, pady=5)

# minEntry : scale to select the
# minimum value of data bars
minEntry = Scale(Mainframe, from_=0,
                 to=10, resolution=1,
                 orient=HORIZONTAL,
                 label="Minimum Value")
minEntry.grid(row=1, column=1,
              padx=5, pady=5)

# maxEntry : scale to select the
# maximum value of data bars
maxEntry = Scale(Mainframe, from_=10,
                 to=100, resolution=1,
                 orient=HORIZONTAL,
                 label="Maximum Value")
maxEntry.grid(row=1, column=2,
              padx=5, pady=5)

# creating generate button
Button(Mainframe, text="Generate",
       bg="Red",
       command=generate).grid(row=0,
                              column=3,
                              padx=5,
                              pady=5)

# to stop automatic window termination
root.mainloop()
