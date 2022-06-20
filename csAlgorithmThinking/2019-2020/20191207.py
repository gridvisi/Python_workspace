'''

    import turtle
    t = turtle.Pen()  #获得画笔
    t.hideturtle()  #隐藏海龟
    t.fillcolor("blue")
    t.penup()
    t.goto(-130,-130)
    t.pendown()
    t.forward(300)
    for _ in range(5):
        t.left(120)
        t.forward(300)
    #t.goto(10,10)
    turtle.done()


'''

print(10 % 6)
print(12 / 6)
print(13 // 6)

#0 - 100 even 偶数
print()
x = 17
for i in range(2,x):
    if x % i == 0:print(False)
    if x % i != 0:
        print('alan:',i)