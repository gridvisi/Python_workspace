'''
AMC 10: 红 绿 蓝 组成3*3的九宫格

上下左右相邻的方块颜色都不相同

问共有多少种不同的摆放？
参数：n 种颜色
返回：f(n)种摆放方法
'''

# bruce

colors = ['r','b','g']
pattn = []
for i in colors:
    for j in colors:
        for l in colors:
            s = i+j+l
            if len(set(list(s))) >= 2 and all([dd not in s for dd in ('rr','bb','gg')]):
                pattn.append(s)
print(pattn)

ans = []
for x in pattn:
    for y in pattn:
        for z in pattn:
            arrs = [x[i]+y[i]+z[i] for i in range(len(x))]
            #for arr in arrs:
            if all([dd not in arr for arr in arrs for dd in ('rr','bb','gg')]):
                if (x+y+z).count('r') == (x+y+z).count('b') == (x+y+z).count('g') == 3:
                    ans.append([x,y,z])
print(len(ans),ans)


#all([x[i] != y[i] and y[i] != z[i]  for i in  #and x[1] != y[1] and y[1] != z[1] and x[2]


#