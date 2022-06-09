import turtle as t
t.pensize(3)
t.pencolor("blue")
t.fillcolor("black")
t.color('blue')
t.up()
t.goto(0,-100)
t.down()
t.circle(100)
t.up()
t.forward(100)
t.down()
for i in range(5):
    t.left(90)
    t.forward(200)

#t.end_fill()     #填充完成
t.done()


# sequar inner and cirle outer
#for i in range(5):
    #t.left(90)
    #t.forward(200)

t.end_fill()     #填充完成
t.done()
