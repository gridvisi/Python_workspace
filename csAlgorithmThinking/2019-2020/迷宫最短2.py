__author__ = 'Administrator'
import numpy as np
import queue
INF=1000000
que = queue.Queue()#建队列变量

maze=np.array([[1,2,1,1,1,1,1,1,0,1],#0 代表通道，1代表墙，2代表入口，3代表出口
              [0,0,0,0,0,0,1,0,0,1],
              [0,1,0,1,1,0,1,1,0,1],
              [0,1,0,0,0,0,0,0,0,0],
              [1,1,0,1,1,0,1,1,1,1],
              [0,0,0,0,1,0,0,0,0,1],
              [0,1,1,1,1,1,1,1,0,1],
              [0,0,0,0,1,0,0,0,0,0],
              [0,1,1,1,1,0,1,1,1,0],
              [0,0,0,0,1,0,0,0,3,1]])
d=maze#其实只是复制一个与maze大小的数组，后面会先全部设置为INF
N,M=maze.shape#读取maze的维数
sx,sy=0,1#设置起始点坐标
gx,gy=9,8#设置终止点坐标

dx=[1,0,-1,0]#四个方向移动向量
dy=[0,1,0,-1]#四个方向移动向量


def bfs():
    for i in range(N):
        for j in range(M):
            d[i][j]=INF#初始化为INF
    p_list=[sx,sy]#形成一个坐标，一起压入队列
    d[sx][sy]=0#将d的起始点坐标设置为0
    #print(d)
    que.put(p_list)#将坐标压入队列
    #print(que.qsize())
    #print(que.get())
    #print(que.qsize())
    while(que.qsize()):
        que_get=que.get()  #读取队列
        #print(que_get)
        if(que_get[0]==gx and que_get[1]==gy ):#如果到终点，结束搜索
            break
        #四个移动方向
        for i in range(4):
            #移动之后的位置记为nx，ny
            nx=que_get[0]+dx[i]
            ny=que_get[1]+dy[i]
            #判断是否可以移动，并且是否已经访问过（访问过d[nx][ny]!=INF）
            if(0<=nx and nx<N and 0<=ny and ny<M and maze[nx][ny]!=1 and d[nx][ny]==INF):
                p_list=[nx,ny]#如果可以移动，将该点加入队列；并且距离加一
                que.put(p_list)
                d[nx][ny]=d[que_get[0]][que_get[1]]+1
    print(d)
    return d[gx][gy]

def solve():
    res=bfs()
    print('最少次数为%d'%res)
solve()
