__author__ = 'Administrator'
circle = int(input('input length of circle: '))
num = []
num = [300,250,200]
num = sorted(num)
x = circle / (num[2] - num[1])
y = circle / (num[1] - num[0])
z = circle / (num[2] - num[0])
print(x,y,z)
x = max(x, y, z)
while True:
    if x % y == 0 and x % z == 0:
        print(x)
        break;
    else:
        x += x

'''
#ircle = circle*12*60*60
num.append(int(input('input speed of jerry: ')))
num.append(int(input('input speed of tommy: ')))
num.append(int(input('input speed of susan: ')))
num=sorted(num)
'''