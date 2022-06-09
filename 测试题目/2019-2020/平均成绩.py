import matplotlib.pyplot as plt
import numpy as np
x, y, z = 128, 256, 1024
#fig, ax = plt.subplots()
#ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
#plt.show()

arrs = [[96, 93, 89, 160, 47],
            [102, 96, 95, 155, 39],
            [99, 82, 86, 149, 40],
            [110, 99, 91, 152, 43]]

def avg_array(arrs):
    re = []
    res = list(zip(*arrs))
    print(res)
    for i in res:
        re.append(sum(i)/len(arrs))
    return re
print(avg_array(arrs))


import random
re = []
for i in range(50):
    s = random.randint(1,120)
    re.append(s)
print(re)

score = [96, 102, 99, 110,78,59,88,72,89,94,66,100,75]
score = re
total = len(score)
print("全年级共有学生:",len(score))

score =  [51, 102, 20, 26, 92, 71, 93, 32, 87, 4, 61, 51, 1, 68, 68, 4, 76, 48, 120, 34, 27, 79, 33, 104, 35, 94, 23, 118, 86, 48, 5, 88, 69, 55, 8, 84, 49, 103, 55, 50, 111, 83, 32, 71, 34, 11, 102, 23, 68, 114]
x = len([i for i in score if i >= 90 and i < 100])
y = len([i for i in score if i >= 80 and i < 90])
z = len([i for i in score if i >= 70 and i < 80])
a = len([i for i in score if i >= 60 and i < 70])
b = len([i for i in score if i >= 100 and i < 110])
print(x,y,z,a,b)
#x,y,z,m = score
fig, ax = plt.subplots()
ax.pie((x,y,z,a,b), labels=('90-100', '80-90', '70-80','60-70','100-110'), autopct='%1.1f%%')
plt.show()

fig, ax = plt.subplots()
ax.pie((x,y,z,a,b), labels=('90-100', '80-90', '70-80','60-70','100-110'), autopct='%1.1f%%')
plt.show()

# 直方图

score =  [51, 102, 20, 26, 92, 71, 93, 32, 87, 4, 61, 51, 1, 68, 68, 4, 76, 48, 120, 34, 27, 79, 33, 104, 35, 94, 23, 118, 86, 48, 5, 88, 69, 55, 8, 84, 49, 103, 55, 50, 111, 83, 32, 71, 34, 11, 102, 23, 68, 114]
x = len([i for i in score if i >= 90 and i < 100])
y = len([i for i in score if i >= 80 and i < 90])
z = len([i for i in score if i >= 70 and i < 80])
a = len([i for i in score if i >= 60 and i < 70])
b = len([i for i in score if i >= 100 and i < 110])
#print(x,y,z,a,b)
#x,y,z,m = score

hist =  [  9,  20,  70, 146, 217, 239, 160,  86,  38,  15]
bin_edges = [-3.04614305, -2.46559324, -1.88504342, -1.3044936 , -0.72394379,
       -0.14339397,  0.43715585,  1.01770566,  1.59825548,  2.1788053 ,
        2.75935511]
np.histogram(hist)
fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()