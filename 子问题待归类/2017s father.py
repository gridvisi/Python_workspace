__author__ = 'Administrator'
'''
The pyramid of integers above is constructed in such a way that each "father" has exactly 3 "children":
What number is the father of 2017?
上面的整数金字塔是这样构造的，每个“父亲”都有3个“孩子”：
2017个孩子的父亲是谁？
https://brilliant.org/weekly-problems/2017-11-13/intermediate/?p=1
'''
a = [2,4,8]
ai = [i for i in a if i != 4]
print(ai)
# 两个指针i，j，一个标记father，另一标记j,第3个儿子，形成数组如[i,j]

def tree_left(layer):
    #global layer
    if layer == 1:
        return 1
    elif layer > 1:
        return tree_left(layer-1)+3**(layer-1)
print(tree_left(3))

f = int(input("输入您要的数："))
layer = 1
while tree_left(layer) < f:
    layer += 1
    if tree_left(layer) >= f and layer > 2:
        left = tree_left(layer-1)+1
            #print(f,left)
        father =tree_left(layer-2)+1+int((f-left)/3)
        print('位于第:',layer,'层:','左边第一数是:',left,'，你寻找的',f,'的父亲是:',father)


'''
if f >= tree_left(layer):
            print(layer)
j = [i+1,i+2,i+3]
j = i[0]
for i in range(i,i++ 3**(layer+1)):
y = int(input("电阻Y的值："))
a = x
b = y
counter = int(input("二叉树的层数："))
Parallel(x, y, counter, a, b)
print("R =", cache)
import math
print(math.sqrt(1*2))
'''
