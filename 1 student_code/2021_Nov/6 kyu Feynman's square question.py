'''
https://www.codewars.com/kata/551186edce486caa61000f5c/train/python

Feynman
理查德-菲利普斯-费曼是美国著名的物理学家，也是诺贝尔物理学奖的获得者。
他从事理论物理学研究，并开创了量子计算领域。

最近，一位老农发现了一些据说是属于费曼的论文和笔记。在关于介子和电磁学的笔记中，
有一张餐巾纸，他在上面写了一个简单的谜题："在NxN个方格中，有多少个不同的方格？"。

例如，当N=2时，答案是5：2x2的正方形本身，加上其角落里的四个1x1的正方形。


任务
你必须写一个函数

def count_squares(n):
来解决Feynman的问题。你的函数的输入将始终是一个正整数。

#Examples

count_squares(1) = 1
count_squares(2) = 5
count_squares(3) = 14

(改编自Diego Satoba的Sphere Online Judge问题SAMER08F)

test.assert_equals(count_squares(1),  1,    "count_squares(1)" )
test.assert_equals(count_squares(2),  5,    "count_squares(2)" )
test.assert_equals(count_squares(3),  14,   "count_squares(3)" )
test.assert_equals(count_squares(5),  55,   "count_squares(5)" )
test.assert_equals(count_squares(8),  204,  "count_squares(8)" )
test.assert_equals(count_squares(15), 1240, "count_squares(15)")
'''

def count_squares(n):
    #对角线共有n-1个正方形
    #横纵f(x，x)*2 + 2*(x+1)-1 -> f(x+1,x+1)
    #网格上的点x,y：range(0,n)有min(n-i,n-j)种正方形
    cunt = 0
    for i in range(n):
        for j in range(n):
            cunt += min(n-i,n-j)
    return cunt
n = 15
print(count_squares(n))
