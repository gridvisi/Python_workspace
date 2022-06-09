'''
https://www.luogu.com.cn/problem/P1002
现在要求你计算出卒从 AA 点能够到达 BB 点的路径的条数，假设马的位置是固定不动的，并不是卒走一步马走一步。

输入格式
一行四个正整数，分别表示 BB 点坐标和马的坐标。

输出格式
一个整数，表示所有的路径条数。

输入输出样例
输入 #1复制
6 6 3 3
输出 #1复制
6
说明/提示
对于 100 \%100% 的数据，1 \le n, m \le 201≤n,m≤20，0 \le0≤ 马的坐标 \le 20≤20。
'''

def pawn(x,y,xh,yh):
    avoid = [[xh,yh]]
    step = []
    p,q = 0,0
    ans = [p,q]
    for i in range(0,x+1):
        for j in range(0,y+1):
            if abs(xh - i) + abs(yh - j)== 3 and xh!=i and yh!=j:
                #if i==x and j==y:
                avoid.append([i,j])
            else:
                step.append([i,j])
    while p <= x and q <= y:
        start = [p,q]
        while [p,q] in step:
            p += 1
            ans.append([p,q])
            q += 1
            ans.append([p,q])
            if [p,q] == [x,y]:
                return ans



    return avoid,total , step
x,y,xh,yh = 6, 6, 3, 3
x,y,xh,yh = 4, 8, 2, 4
print(pawn(x,y,xh,yh))

