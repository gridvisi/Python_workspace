__author__ = 'Administrator'
def dfs(x,y,step):
    global min
    global tx,ty
    next = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    if x == mx and y== my:
        if min > step:
            min = step
            print(min)
        return
    for k in range(4):
        tx = x + next[k][0]
        ty = y + next[k][1]
        if tx < 0 or tx > n-1 or ty < 0 or ty > m-1:
            continue
        if a[tx][ty]==0 and book[tx][ty]==0:
            book[tx][ty]=1
            dfs(tx,ty,step+1)
            book[tx][ty]=0
    return
if __name__=='__main__':
    n=int(input('输入矩阵行数n:'))
    m=int(input('输入矩阵列数m:'))
    arrayString = input('输入一个二维数组：')
    a=eval(arrayString)
    startx = int(input('输入开始的位置startx:'))
    starty = int(input('输入开始的位置starty:'))
    mx = int(input('输入的终点位置mx:'))
    my = int(input('输入的终点位置my:'))
    book=[[0]*51]*51
    min=99999999
    book[startx][starty]=1
    dfs(startx,starty,0)
    print("最短步数：%d" % min)