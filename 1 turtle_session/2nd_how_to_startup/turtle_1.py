import turtle as t
t.color('red')
t.goto(0,0)

for n in range(10):
    t.fd(200)
    t.left(108)

t.goto(-200,-200)
for n in range(10):
    t.fd(200)
    t.left(108)

t.goto(-200,100)
for n in range(10):
    t.fd(200)
    t.left(108)

t.goto(100,-200)
for n in range(10):
    t.fd(200)
    t.left(108)

t.end_fill()     #填充完成
t.done()