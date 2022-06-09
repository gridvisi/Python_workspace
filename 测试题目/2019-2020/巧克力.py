__author__ = 'Administrator'
'''
A shopkeeper has an excellent recycling policy:
He gives you 1 chocolate per every Dollar you give him.
He gives you 1 chocolate per every 3 wrappers you give him.
You have $59049 with you. What is the maximum number of chocolates that you can buy?
Extra Credit: Try to derive a generalized expression for the number of chocolates you can buy with $n.
Details and Assumptions:
You do not initially have any wrappers with you.
All the chocolates you buy come wrapped in wrappers.
There is no upper bound on the number of transactions you can do.
The shopkeeper has infinite chocolates.
'''
print(4%3)
def max_choco(x,y):

    if x == 1:
        counter = 0
        return x + y
    if x == 2:
        counter = 0
        return x + y
    if x == 3:
        y += 1
        return y + x,y
    else:
        #y += 1
        #func = max_choco(x-1,y)
        #x = func[0]
        #y = func[1]
        return max_choco(x-1,y)

print(max_choco(9,0))

rmb = 59049
wrappers = 0
eaten = 0
while rmb > 0:
    rmb -= 1
    eaten += 1
    wrappers += 1
    if wrappers == 3:
        wrappers -= 3
        eaten += 1
        wrappers += 1
print ("Answer:", eaten)

'''
一个函数中调用另一个函数返回的多个值中的一个
首先，定义了一个函数 。
代码如下：
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
1
2
3
4
第二，为了能够分开使用这个函数返回的group和labels 。

我们可以这么做使用 fun()[1] // 下标从0开始，来调取返回值

代码如下 ：

www= createDataSet()
print("group的值为")
print(www[0])
print("lables的值为")
print(www[1])
1
2
3
4
5
最后结果显示如下：
group的值为
[[ 1.   1.1]
 [ 1.   1. ]
 [ 0.   0. ]
 [ 0.   0.1]]
lables的值为
['A', 'A', 'B', 'B']
---------------------
作者：DeepRunning
来源：CSDN
原文：https://blog.csdn.net/u010801439/article/details/78458223

'''