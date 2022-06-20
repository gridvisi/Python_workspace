import turtle
n = 23
for i in range(1,n,1):
    for j in [90,180,-90,0]:
        turtle.seth(j)
        turtle.fd(n)
        n += 5