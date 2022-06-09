
print(16 * 16)
y = 1
x = y
x = 3
xy = (x,y)
x = xy[0] - 1
print('x:',xy,x,y)
print('x:',xy,x,y)
# 孙悟空每走一步，分身为4个猴，最后数每个格子里有几只猴
'''
print("1st    2nd          3rd         4th")
print(4*0 + (4*4-2*4-3)*0 + (4*4-2*4-3)*0 + 4*4-2*4)
print(0*0 +        +         0 +      4*4-2*4)
print('corner:', 0  +    2*4      +    2*4    +     2*4+2*4  ) #四个角的猴
print(15/24)
#target: (112, 224, 0.5)

'''


class move:
    def __init__(self,x,y,step): # -> list[row,column,pace]
        self.x = x
        self.y = y
        self.step = step

    def next(self):
        self.step += 1
        x,y = (self.x,self.y)
        print('xy:',x,y)
        news = [
                [x,y-1,self.step],
            [x-1,y,self.step],[x+1,y,self.step],
                [x,y+1,self.step]
                ]

        for xy in news:
            if xy[0] == 3:
                xy[0] = 0

            if xy[0] == -1:
                xy[0] = 2

            if xy[1] == 3:
                xy[1] = 0

            if xy[1] == -1:
                xy[1] = 2
        return news


# p= [x,y,step] mark 4 direction
def fourLeap(p,arrs):
    corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
    x, y, pace = p[0], p[1], p[2]
    if (x,y) in corner:
        arrs[x][y] += 1

    elif pace < 3 and (x,y) not in corner:
        fourD = move(x,y,pace).next()
        print('fourD',fourD)
        return fourD

    elif pace == 3 and (x,y) not in corner:
         arrs[x][y] += 1

    #print(arrs)
    return 'final:',arrs

arrs = [[0,0,0],
        [0,1,0],
        [0,0,0]]

arrStep = [[0,0,0],            [0,0,0],            [0,0,0]]

p = [1,1,0]   #start location
corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
NotCorner = [(x,y) for x in range(len(arrs)) for y in range(len(arrs[0])) if (x,y) not in corner]
print('Not:',NotCorner)
#Python 中的 x for y in z for x in y语法详解
#print('NOT good code for NotCORNER:',[(x,y) for y in range(len(NotCorner)) for x in range(y)])
#print('all:',all([arrStep[xy[0]][xy[1]] < 4 for xy in NotCorner]))

cunt = 0
while all([arrStep[xy[0]][xy[1]] < 4 for xy in NotCorner]):
    cunt += 1
    for d in NotCorner:

        print('step:',arrStep)
        print('d',d[0],d[1],arrStep[d[0]][d[1]])

        if arrStep[d[0]][d[1]] < 4:
            p = d[0], d[1], arrStep[d[0]][d[1]]
            try:
                arrStep[d[0]][d[1]] = [n for n in fourLeap(p,arrs) if (n[0],[1]) == (d[0],d[1])][0]
            except:
                arrStep[d[0]][d[1]] = arrStep[d[0]][d[1]]
            print('so much test',[n for n in fourLeap(p,arrs) if (n[0],[1]) == (d[0],d[1])])
            fourLeap(p,arrs)

print("arrs_",arrs,cunt,arrStep)

'''
x,y,step = p
test = move(x,y,step)
test.next()
for i in test.next():
    x,y,step = i
    move(x,y,step)
    print('test:',test.next())

'''

#print(fourLeap(p,arrs))

def judgeCorner(arrsFinal):
    target = sum([i[0]+i[-1] for i in (arrs[0],arrs[-1])])
    total = sum([sum(i) for i in arrsFinal])
    return target,total,target/total
arrsFinal = fourLeap(p,arrs)
#print(arrsFinal)
print('target:',judgeCorner(arrs))


'''

# https://blog.csdn.net/sodalife/article/details/89461030
import copy
L = copy.deepcopy(move(1,1,0))
R = copy.deepcopy(move(1,1,0))
U = copy.deepcopy(move(1,1,0))
D = copy.deepcopy(move(1,1,0))
print(L.left(),R.right(),U.up(),D.down())



        news = [
                [self.x,self.y-1,self.step],
            [self.x-1,self.y,self.step],[self.x+1,self.y,self.step],
                [self.x,self.y+1,self.step]
                ]


arrs = [[0,0,0],
        [0,0,0],
        [0,0,0]]
start = arrs[1][1]
print(start)

#fourLeap = move(1,1)
centre = (1,1)
test = move(centre[0],centre[1],0)
#print(P)

for i in range(4):
    print('test:',test.left())



import copy
def fourLeap(x,y,step,arrs): #x_y mark 4 direction
    corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
    print('arrs:',x,y,step,arrs)
    if step <= 4 and (x,y) in corner:
        arrs[x][y] += 1

    elif step == 4 and (x,y) not in corner:
        arrs[x][y] += 1

    elif step < 4 and (x,y) not in corner:
        step += 1
        P = move(x,y,step)
        L = copy.deepcopy(P)
        R = copy.deepcopy(P)
        U = copy.deepcopy(P)
        D = copy.deepcopy(P)
        news = [L.left(), R.right(), U.up(), D.down()]
        print('news',news)
        for p in news:
            fourLeap(p[0], p[1], p[2], arrs)
    #print(arrs)
    return 'final:',arrs

arrs = [[0,0,0],
        [0,0,0],
        [0,0,0]]
p = (x,y,step) = 1,1,0
print('arrs:',arrs)
print(fourLeap(p,arrs))



def up(self):
    if self.y == 0:
        self.y = 2
    else:
        self.y -= 1
    self.step += 1
    return [self.x, self.y, self.step]


def down(self):
    if self.y == 2:
        self.y = 0
    else:
        self.y += 1
    self.step += 1

'''









'''

        for p in news:
            if p[2] == 4:
                arrs[p[0]][p[1]] += 1

            elif p[2] < 4:
                print('off',p,arrs,(p[0],p[1],step+1))
                #return fourLeap(p[0],p[1],step+1,arrs)
                #step += 1
                
            #continue
    
           
        XY = [i for i in news if (i[0],i[1]) in corner]
        print('xy:',XY)

        if len(XY) > 0:
            for i in XY:
                arrs[i[0]][i[1]] += 1
    for p in news:
        print('p:',p)
        if p in corner:
            arrs[p[0]][p[1]] += 1
            print('on:',p,arrs)
            continue
    
            #print(x,y)
            fourLeap(x,y,step+1)
            x, y = P.right()
            fourLeap(x, y, step+1)
            x, y = P.up()
            fourLeap(x, y, step+1)
            x, y = P.down()
            fourLeap(x, y, step+1)
            # print(x,y)
            
            #return fourLeap(x, y, step + 1)
'''