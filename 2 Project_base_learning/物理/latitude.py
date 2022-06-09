__author__ = 'Administrator'
'''
北半球的游牧部落每年沿着下面的路线移动：
春天，部落向东移动100公里。
夏天，部落向北移动100公里。
秋天，部落向西移动98公里。
冬天，部落向南移动100公里。
部落从春天到达了它的确切起点，并在那里建立了它的冬季住所。
冬季的纬度是多少度？注意：地球的半径是6371公里
'''
import math
R = 6371
a = math.pi*100/6371

#math.sin(x)*R / math.sin(x-a)*R = 100 / 98
variance = []
v = {}
for i in range(1,90):
    rate = math.sin((i/90*math.pi - a))/ math.sin(i*math.pi/90)
    variance.append(rate)
    print(rate,i)
#print(variance)

for j in range(1,90):
    print(variance[j])
    #v = {j:(variance[j] - 0.98)}




