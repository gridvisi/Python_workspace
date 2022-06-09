
import turtle as t

colors = ['red','orange','yellow','green','blue','purple','pink']
#print('for loop')
for i,e in enumerate(3 * colors):
    print(i,e)
    #t.goto(0 + i*10,0+i*10)
    #t.color(colors[i])
    t.color(e)
    t.left(-30)
    for j in range(4):
        print(200-i*20)
        t.forward(200-i*20)
        t.left(90)
t.done()