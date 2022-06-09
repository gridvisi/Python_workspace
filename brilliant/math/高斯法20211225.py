
student = 114
bus_a = [18,160]
bus_b = [12,120]

print(114//12)

num = 0
for i in range(1, 4): #
    num += i
    print(num)

def triangle_ball(n):
    num = 0
    for i in range(n):
        num += i
    return num
n = 3
print('木头有多少根：',triangle_ball(n))
