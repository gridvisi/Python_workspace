'''
https://blog.csdn.net/yywan1314520/article/details/50818471
'''

import matplotlib.pyplot as plt
import random
import numpy as np

score = []
for i in range(100):
   s = random.randint(1,120)
   score.append(s)
print(score)

score = [101, 56, 99, 42, 24, 35, 84, 51, 112, 84, 9, 69, 64, 49, 8, 81, 117, 96, 94, 14, 17, 78, 12, 54, 34, 68, 29, 114, 91, 4, 110, 6, 52, 57, 116, 17, 5, 24, 38, 36, 108, 55, 117, 63, 111, 96, 25, 41, 9, 106, 101, 98, 64, 5, 116, 98, 42, 58, 108, 45, 112, 82, 21, 42, 63, 5, 107, 6, 67, 49, 19, 33, 7, 56, 4, 47, 103, 54, 46, 74, 9, 13, 109, 27, 101, 59, 31, 91, 44, 97, 2, 105, 71, 2, 10, 71, 53, 73, 21, 102]

head = [i for i in score if i >= 100 and i < 120]
print([i for i in score if i >= 100 and i < 120])

x = len([i for i in score if i >= 90 and i < 100])
print([i for i in score if i >= 90 and i < 100])

y = len([i for i in score if i >= 80 and i < 90])
print([i for i in score if i >= 90 and i < 100])

z = len([i for i in score if i >= 70 and i < 80])
print([i for i in score if i >= 70 and i < 80])

a = len([i for i in score if i >= 60 and i < 70])
print([i for i in score if i >= 60 and i < 70])

b = len([i for i in score if i >= 0 and i < 60])
print([i for i in score if i >= 0 and i < 60])

# pie chart

fig, ax = plt.subplots()
ax.pie((head,x,y,z,a,b), labels=('100-110','90-100', '80-90', '70-80','60-70','< 60',), autopct='%1.1f%%')
plt.show()

group = [b,a,z,y,x,head]
print('group:',group,sum(group))
score_by_segment = ['< 60','60-70','70-80','80-90', '90-100', '100-110']

name_list = score_by_segment  #['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
num_list = [i*(100/100) for i in group]#[23,8, 19.1, 23.8, 14.3, 19.0]
print(num_list)

rects = plt.bar(range(len(num_list)), num_list, color='rgby',align="center")
# X轴标题 rects =plt.bar(left = (0.2,1),height = (1,0.5),width = 0.2,align="center",yerr=0.000001)
index = [0, 1, 2, 3, 4 ,5]
index = [float(c) + 0.5 for c in index]
plt.ylim(ymax=80, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("比例 percentage(%)")  # X轴标签
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height) + '%', ha='center', va='bottom')
plt.show()


