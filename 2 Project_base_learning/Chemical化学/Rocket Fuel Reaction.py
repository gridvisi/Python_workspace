'''
https://brilliant.org/daily-problems/rocket-combustion/
10Al + 6NH4ClO4 -->4Al2O3 + 2AlCl3 + 3N2 + 12H2O

原文链接：https://blog.csdn.net/qq_44723623/article/details/89052848
x-y-z=2
2x-y-3z=1
3x+2y-5z=0
求x,y,z值,程序代码如下：
'''
import numpy as np
A=np.mat("1 -1 -1;2 -1 -3;3 2 -5")
B=np.array([2,1,0])
result=np.linalg.solve(A,B)
print("x={},y={},z={}".format(result[0],result[1],result[2]))

# x*'Al'+ y*('N'+'H'*4+'Cl'+'O'*4) -->Al2O3 + AlCl3 + N2 + H2O
# z*'Al'*2+z*'O'*3 + i*'Al'+i*'Cl'*3 + j*'N'*2 + k*'H'*2+k*'O'
'''
x = 2*z + i 
y = 2*j 
4*y = 2*k
y = 3*i
4*y = 3*z + k

j = 1.5*i
k = 3*z
y = 1.5*z 
k = 2*y

'''

'''
1*x + 0*y - 2*z - 1*i + 0*j + 0*k = 0  # al balance act
0*x + 1*y + 0*z + 0*i - 2*j + 0*k = 0
0*x + 4*y + 0*z + 0*i + 0*j - 2*k = 0
0*x + 1*y + 0*z - 3*i + 0*j - 0*k = 0
0*x + 4*y - 3*z + 0*i + 0*j - 1*k = 0

等式右边只有一项包含N，N的系数j = 2*y 成功消除1个元变量 满足5个等式5个变量

1*x + 0*y - 2*z - 1*i + 0*k = 0  # al balance act
0*x - 3*y + 0*z + 0*i + 0*k = 0
0*x + 4*y + 0*z + 0*i - 2*k = 0
0*x + 1*y + 0*z - 3*i - 0*k = 0
0*x + 4*y - 3*z + 0*i - 1*k = 0

'''
A = np.mat("1 0 -2 -1 0;0 -3 0 0 0;0 4 0 0 -2;0 1 0 -3 0;0 4 -3 0 -1")
B = np.array([0,0,0,0,0])
result=np.linalg.solve(A,B)
print("x={},y={},z={},i={},k={}".format(result[0],result[1],result[2],result[3],result[4]))