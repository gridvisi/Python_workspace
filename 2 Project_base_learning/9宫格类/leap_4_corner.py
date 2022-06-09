
class move:
    def __init__(self,x,y,step): # -> list[ row,column]
        self.x = x
        self.y = y
        self.step = step

    def left(self):
        if self.x == 0:
            self.x = 2
        else:
            self.x -= 1
        self.step += 1
        return [self.x,self.y,self.step]

    def right(self):
        if self.x == 2:
            self.x = 0
        else:
            self.x += 1
        self.step += 1
        return [self.x,self.y,self.step]

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
def fourLeap(p,arrs):       # p= [x,y,step] mark 4 direction
    corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
    print('arrs:',p,arrs)
    if p[2] <= 4 and (p[0],p[1]) in corner:
        x,y = p[0],p[1]
        arrs[x][y] += 1

    elif p[2] == 4 and (p[0],p[1]) not in corner:
        x, y = p[0], p[1]
        arrs[x][y] += 1

    elif p[2] < 4 and (p[0],p[1]) not in corner:
        #p[2] += 1
        P = move(p[0],p[1],p[2])
        #L = R = U = D = copy.deepcopy(P) NOT RIGHT!!
        L = copy.deepcopy(P)
        R = copy.deepcopy(P)
        U = copy.deepcopy(P)
        D = copy.deepcopy(P)
        news = [L.left(), R.right(), U.up(), D.down()]
        print('news',news)
        for i in news:
            print('p:',i)
            fourLeap(i, arrs)

    #print(arrs)
    return 'final:',arrs

arrs = [[0,0,0],
        [0,0,0],
        [0,0,0]]
p = [1,1,0] #[x,y,step] =
print('arrs:',arrs)
print(fourLeap(p,arrs))

def judgeCorner(arrsFinal):
    target = sum([i[0]+i[-1] for i in (arrs[0],arrs[-1])])
    total = sum([sum(i) for i in arrsFinal])
    return target,total,target/total
arrsFinal = fourLeap(p,arrs)
print(arrsFinal)
print('target:',judgeCorner(arrs))

# https://blog.csdn.net/sodalife/article/details/89461030
import copy
L = copy.deepcopy(move(1,1,0))
R = copy.deepcopy(move(1,1,0))
U = copy.deepcopy(move(1,1,0))
D = copy.deepcopy(move(1,1,0))
print(L.left(),R.right(),U.up(),D.down())


'''

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