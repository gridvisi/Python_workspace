
import turtle as t

colors = ['red','orange','yellow','green','cyan','blue','purple']
#

print('for loop')
for i,e in enumerate(3*colors):
    print(i,e)
    t.goto(0+i*10,0+i*10)

    t.color(colors[i])
    t.color(e)
    t.left(-15)
    for j in range(3*len(colors)):
        #print(200-i*20)
        t.forward(200-j*10)
        t.left(120)

t.done()


t.penup()
import turtle as t

r = 'green'
t.color(r)
t.pensize(4)

for i in range(6):
    t.right(120)
    t.forward(150)
    t.right(60)
    t.forward(150)

#五角星
import turtle as t
r = 'red'
t.color(r)
t.pensize(8)
t.penup()
#t.pendown()
t.hideturtle()
for i in range(6):
    t.right(36)
    t.forward(150)
    t.right(108)
    t.forward(150)

t.done()