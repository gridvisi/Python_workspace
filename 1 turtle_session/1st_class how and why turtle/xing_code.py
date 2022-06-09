

import turtle as t
t.speed (10)
t.pensize(2)
colors = ('red','brown','purple','black')
for i in range(400):
    angle = i * 0.1
    t.color(colors[i%4])
    t.forward(8*1)
    t.left(5.1415) #90 + angle


import turtle as t
colors = ['red','orange','yellow','green','blue','purple','pink']
for i in range(7):
    t.forward(90)
    t.left(90)
    t.color(colors[i])
t.done()