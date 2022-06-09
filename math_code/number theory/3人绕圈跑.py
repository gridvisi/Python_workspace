'''
input length of circle: 400
input speed of jerry: 300
input speed of tommy: 250
input speed of susan: 200

circle = int(input('input length of circle: '))
speed = []
speed.append(int(input('input speed of jerry: ')))
speed.append(int(input('input speed of tommy: ')))
speed.append(int(input('input speed of susan: ')))
'''

speed = [120,100,80]  # metre/min
circle = 800         # meter
speed = sorted(speed)
mx = max(speed)
counter = 0
for time in range(330): # 300分钟内再次相遇的时间minute以分钟计算
    if int((mx * time) - time * speed[1]) % circle == 0 and int((mx * time) - int(time * speed[0])) % circle == 0:
        counter += 1
        print(time,counter,time*mx,time*speed[1],time*speed[0])

'''
circle = int(input('input length of circle: '))
speed.append(int(input('input speed of jerry: ')))
speed.append(int(input('input speed of tommy: ')))
speed.append(int(input('input speed of susan: ')))

speed = sorted(speed)
mx = max(speed)

for time in range(18000): # 1800秒内再次相遇的时间second以秒计算

    if int((time * mx/60 - time * speed[1]/60) % circle) == 1.00 and int((mx * time/60 - time % speed[0]/60) % circle) == 1.00:
        print('按秒计算结果：')
        print(time,time*mx/60,time*speed[1]/60,time*speed[0]/60)



num = speed
x = circle / (num[2] - num[1])
y = circle / (num[1] - num[0])
z = circle / (num[2] - num[0])
while True:
    if x % y == 0 and x % z == 0:
        print(x)
        break;
    else:
        x += x
print(x)
'''


