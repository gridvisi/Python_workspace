
color = ['red','cyan','blue','white','purple']
import turtle as t
t.penup()
t.goto(-100,-100)
t.pendown()
for i in range(3):
    t.forward(300)
    t.left(120)
    t.color("red")
t.penup()
t.goto(-100,100)
t.pendown()



for i in range(3):
    t.forward(300)
    t.right(120)
    t.color("purple")
t.done()

# coding=utf-8
import turtle
import time

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))

turtle.mainloop()


#7 kyu Dot Calculator
# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python
'''
Dot Calculator
You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the oparator. The dots and the operator will be separated by one space.

Here are the following valid operators :

+ Addition
- Subtraction
* Multiplication
// Integer Division
Your Work (Task)
You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.

Examples
calculator("..... + ...............") => "...................."
calculator("..... - ...") => ".."
calculator("..... - .") => "...."
calculator("..... * ...") => "..............."
calculator("..... * ..") => ".........."
calculator("..... // ..") => ".."
calculator("..... // .") => "....."
calculator(". // ..") => ""
calculator(".. - ..") => ""
'''


def calculator(txt):
    # This is the place to code!
    for op in ("+","-","*","//"):
        if op in txt:
            head,tail = txt.split(op)
            s = op
            break
    return '.'* eval(str(head.count(".")) + s + str(tail.count('.')))

# Be carefull fellow code is len not count
#eval(str(len(head))+ op+ str(len(tail)))

txt = "..... - ..."
print(calculator(txt))


#1st
def calculator(txt):
    a, op, b = txt.split()
    a, b = len(a), len(b)
    return '.' * eval(f'{a} {op} {b}')

