__author__ = 'Administrator'
'''
分形图案是在正方形中创建的，从9个相同的正方形排列成正号图案。在每个步骤中，从第一步开始，f(n-1),f(0)=0,f(1)=3
用正号图案替换在正边上以蓝色为边界的每个蓝色正方形。当这个图案无限期地继续时，大正方形的什么部分被阴影蓝色？

def fractal(n,ratio): # square为橙色部分面积，ratio正方形的缩放比例,本题为1/9,n是第n次分形,最外围的正方形数量为f(n)= 3**n
    if n == 0:
        return 1
    if n == 1:
        return 4/9               #fractal(square,0,ratio)-ratio*fractal(square,0,ratio)*4
    if n > 1:                    #
        square = fractal(n-1,ratio) - ratio * (3**n) * 4
        return fractal(n-1,ratio) + (ratio**n) * (3**n) * 4
'''
# 非递归
i = int(input('第n次分形:'))
ratio = 1/9
#global square
if i == 1:
    square = 4/9
    print(square)
if i == 2:
    square = 4/9 + 16*(ratio**2)
    print(square)            #fractal(square,0,ratio)-ratio*fractal(square,0,ratio)*4
if i > 2:
    j = 3
    temp = []
    new = 4/9 + 16*(ratio**2)
    while j < i+1:
        start = 4/9 + 16*(ratio**2)
        dt = (ratio**j * 4) * (3**(j-2)) * 4
        #print(ratio**j)
        new = new + dt
        temp.append(new)
        j += 1
        if j == i:
            print(1-new,temp)

print('++++++',7/27,'+++++++++++++++')
for i in range(5,9):
    print(i/27)