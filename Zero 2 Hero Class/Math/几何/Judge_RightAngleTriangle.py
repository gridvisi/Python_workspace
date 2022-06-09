# 判断三条直线的长度能否构成直角三角形？

a,b,c = 5,4,3
a,b,c = 15,24,23
a,b,c = 35,48,36
sides = sorted([a,b,c])
print(sides[0]**2+sides[1]**2 == sides[2]**2)

first = 1
ans = []
for first in range(1,101):
    for second in range(first,101):
        for third in range(second,101):
            if first**2 + second**2 == third**2:
                ans.append([first,second,third])
print(ans,len(ans))
