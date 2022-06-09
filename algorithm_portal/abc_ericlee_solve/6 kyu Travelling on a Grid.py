'''
https://www.codewars.com/kata/5845b080a87f768aaa00027c/train/python

You have an 8x8 grid with coordinates ranging from 1 to 8.
The origin (1, 1) is in the top left corner.
The bottom right corner is (8, 8).

You are given a string as an input which will contain the 2
coordinates in this format: "(x1 y1)(x2 y2)", where (x1 y1)
represents point A and (x2 y2) represents point B.

In the inputs provided, point A will always be up and to the
left of point B. In other words, x1 < x2 and y1 < y2 will be
true for every input.

Your goal is to find out the number of different paths you can
take to get from point A to point B by moving one cell at a time
either down or right.

Example
Given an input of "(2 3)(3 5)", the number of possible paths to
get from A to B is 3.

 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  A  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  B  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
 .  .  .  .  .  .  .  .
Possible paths, marked with x:

A .       A .       A x
x .       x x       . x
x B       . B       . B

tests = ["(1 1)(3 3)", "(2 3)(4 8)", "(1 8)(4 8)",
        "(8 1)(8 6)", "(1 2)(8 7)", "(3 6)(8 7)", "(3 1)(7 8)"]
results = [6, 21, 1, 1, 792, 6, 330]
'''
#排列组合思路：
def travel_chessboard(s):

    st,nd = [i for i in s.strip('()').split(")(")]
    st_xy = list(map(int,st.split(" ")))
    nd_xy = list(map(int,nd.split(" ")))
    # n+m
    n = nd_xy[0]-st_xy[0]
    m = nd_xy[1]-st_xy[1]
    cunt,d,div = 1,0,1
    # C(n+m,n) combination
    for i in range(n+m,m,-1):
        d += 1
        cunt *= i
        div *= d
        print(cunt,i,d,div)
    return cunt//div
s = "(1 1)(3 3)"
print('C(n,m+n):',travel_chessboard(s))

#二进制思路
# 右走一步为1，下走一步为0，那么n * m网格即为n个1，和m个0组合
# 000...111 ——> 111...000循环遍历所有含有n个1，和m个0的二进制值
def travel_chessboard(s):
    cunt,road = 0 ,[]
    st,nd = [i for i in s.strip('()').split(")(")]
    st_xy = list(map(int,st.split(" ")))
    nd_xy = list(map(int,nd.split(" ")))
    # 求n和m各是多少
    n = nd_xy[0]-st_xy[0]
    m = nd_xy[1]-st_xy[1]
    # binary combination: n*1,m*0
    minb = int('0b'+n*'1',2)
    maxb = int('0b'+n*'1'+m*'0',2)
    print(minb,maxb,n,m)
    for n in range(minb,maxb+1):
        road = bin(n)
        print(bin(n)[2:].count('1'),bin(n)[2:].count('0'))
        if bin(n)[2:].count('1')==n: # and bin(n).count('0')==m:
            cunt+=1
    return cunt
s = "(1 1)(3 3)"
print(travel_chessboard(s))




#递归思路
#f(x,y) = f(x-1,y) + 2*f(x-1,y-1) + f(x,y-1)
# x,y in range(st_xy,nd_xy)
#初始化->
# f(st_xy[0]+1,st_xy[1])=1
# f(st_xy[0],st_xy[1]+1)=1
# f(st_xy[0]+1,st_xy[1]+1)=2

#f(x,y) =

def travel_chessboard(s):
    cunt ,road = 0 ,[]
    st,nd = [i for i in s.strip('()').split(")(")]
    st_xy = list(map(int,st.split(" ")))
    nd_xy = list(map(int,nd.split(" ")))
    # 递归的边界返回条件
    #if st_xy[0]
    steps = nd_xy[0]-st_xy[0] + nd_xy[1]-st_xy[1]
    right = nd_xy[0]-st_xy[0]-1
    down = nd_xy[1]-st_xy[1]-1
    return 2**(steps-2) + right + down
s = "(1 1)(3 3)"
print(travel_chessboard(s))

#try endwith fail!
def travel_chessboard(s):
    cunt ,road = 0 ,[]
    st,nd = [i for i in s.strip('()').split(")(")]
    st_xy,nd_xy = list(map(int,st.split(" "))),list(map(int,nd.split(" ")))
    for i in range(st_xy[0],nd_xy[0]+1):
        for j in range(st_xy[1],nd_xy[1]+1):
            road.append((i,j))
            if road[-1] == tuple(nd_xy):
                cunt += 1
    return cunt,road #st_xy #,nd



# very import solution
def travel_chessboard(s):
    '''
    Classic problem
        * Classic puzzle
        * Classic combinatorial counting problem
        * Excellent Computer Based Math problem
        * Classic beginner's Dynamic Programming Problem
        * Excellent problem for exhaustive Recursive search
        * Excellent problem for understanding time/space/implementation tradeoffs
    '''
    x1, y1, x2, y2 = list(map(int, s.replace('(', ' ').replace(')', ' ').split()))
    m, n = x2 - x1 + 1, y2 - y1 + 1

    grid = [[0] * n for i in range(m)]

    for i in range(1, m): grid[i][0] = 1
    for j in range(1, n): grid[0][j] = 1
    print('grid:',grid)
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
    print('grid2:', grid)
    return grid[m - 1][n - 1]
s = "(1 1)(3 3)"
print(travel_chessboard(s))


#1st
#from math import comb
from itertools import combinations
def travel_chessboard(s):
    x1, y1, x2, y2 = (int(e) for e in s.replace(')(', ' ')[1:-1].split(' '))
    return combinations(x2-x1 + y2-y1, x2-x1)


import re
from math import factorial as fac

def travel_chessboard(s):
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', s))
    dx, dy = (x2 - x1), (y2 - y1)
    return fac(dx + dy) / (fac(dx) * fac(dy))


from math import factorial
def travelChessboard(s):
    r, c = int(s[6]) - int(s[1]), int(s[8]) - int(s[3])

    return factorial(r + c) / (factorial(r) * factorial(c))