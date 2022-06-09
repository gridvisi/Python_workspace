'''
AMC 10: 红 绿 蓝 组成3*3的九宫格

上下左右相邻的方块颜色都不相同
问共有多少种不同的摆放？

参数：n 种颜色
返回：f(n)种摆放方法
'''

#1st 暴力枚举
'''

AMC 10: 红 绿 蓝 组成3*3的九宫格

上下左右相邻的方块颜色都不相同
问共有多少种不同的摆放？
参数：n 种颜色
返回：f(n)种摆放方法

step 1 所有左右相邻不重复的所有组合

'''
colors = ['r','b','g']
pattn = []

#暴力枚举并条件判断过滤
for i in colors:
    for j in colors:
        for l in colors:
            s = i+j+l
            if len(set(list(s))) >= 2 and all([dd not in s for dd in ('rr','bb','gg')]):
                pattn.append(s)
N = len(pattn)

#Step 2 暴力枚举并判断过滤出pattn列表中C(3, N)满足上下相邻不重复


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

'''

36
 [
['rbr', 
'bgb',
 'grg'], 

['rbr', 
'grg', 
'bgb'], 

['rbg', 
'bgr', 
'rbg'], 

['rbg', 
'bgr', 
'grb'], 

['rbg',
 'grb', 
'rbg'], 

['rbg', 
'grb', 
'bgr'], 

['rgr', 'brb', 'gbg'], ['rgr', 'gbg', 'brb'], ['rgb', 'brg', 'rgb'], ['rgb', 'brg', 'gbr'],
 ['rgb', 'gbr', 'rgb'], ['rgb', 'gbr', 'brg'], ['brb', 'rgr', 'gbg'], ['brb', 'gbg', 'rgr'], 
['brg', 'rgb', 'brg'], ['brg', 'rgb', 'gbr'], ['brg', 'gbr', 'rgb'], ['brg', 'gbr', 'brg'], 
['bgr', 'rbg', 'bgr'], ['bgr', 'rbg', 'grb'], ['bgr', 'grb', 'rbg'], ['bgr', 'grb', 'bgr'],
 ['bgb', 'rbr', 'grg'], ['bgb', 'grg', 'rbr'], ['grb', 'rbg', 'bgr'], ['grb', 'rbg', 'grb'], 
['grb', 'bgr', 'rbg'], ['grb', 'bgr', 'grb'], ['grg', 'rbr', 'bgb'], ['grg', 'bgb', 'rbr'], 
['gbr', 'rgb', 'brg'], ['gbr', 'rgb', 'gbr'], ['gbr', 'brg', 'rgb'], ['gbr', 'brg', 'gbr'], 
['gbg', 'rgr', 'brb'], ['gbg', 'brb', 'rgr']]

'''

'''

     
    def up(self):
        if self.y == 0:
            self.y = 2
        else:
            self.y -= 1
        self.step += 1
        return [self.x,self.y,self.step]

    def down(self):
        if self.y == 2:
            self.y = 0
        else:
            self.y += 1
        self.step += 1
        return [self.x,self.y,self.step]
'''



class Jigsaw:
    def __init__(self,r,b,y,rby): # -> list[ row,column]
        self.r = r
        self.b = b
        self.y = y
        self.rby = rby

    def red(self):
        if self.r <= self.rby and self.r > 0:
            self.r -= 1
            return ['red', self.r]
        else:
            return [0,self.r]

    def blue(self):
        if self.b <= self.rby and self.b > 0:
            self.b -= 1
            return ['blue', self.b]
        else:
            return [0,self.b]


class move:
    colors = ['r', 'b', 'y']
    def __init__(self,x,y,arrs,colors): # -> list[ row,column]
        self.x = x
        self.y = y
        self.arrs = arrs
        self.colors = colors

    def pickCorl(self):  #取当前位置颜色
        if self.x == 0 and self.y == 0:
            self.color = self.colors
            return self.color

        elif self.x == 0 and 0 < self.y < 2:
            self.colors = self.arrs[self.x+2,self.y-1]

        elif self.x == 0 and 0 < self.y < 2:
            self.colors = self.arrs[self.x+2,self.y-1]
        else:
            self.color = [i for i in self.colors]



    def next(self):  #取完颜色，右方移动一格
        if self.x == 2:
            self.x = 0
            self.y += 1
        else:
            self.x += 1

        return [self.x, self.y]
