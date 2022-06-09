__author__ = 'Administrator'

'''
让我们使用具有两个本机函数的ELeNeLIST对象：
您可以比较列表中的任意两个值，以查看哪一个更大。
可以在列表中交换任意两个值。
下面是一个例程，它使用一些本地操作来对列表进行排序。在所有四个元素输入列表中，元素比较的最大数目是多少？
请随意修改第4行中的输入列表并重新运行代码！

#from brilliant.algorithms.lists import *

# Try changing the order of these elements and running the code!
lst = ElementList('c', 'b', 'd', 'a')

n = len(lst)
assert n==4

for i in range(n-1):
    for j in range(i+1,n):
        if lst[i] > lst[j]:
            lst.switch(i, j)

print('Sorted list: ' + str(lst))
print('Number of comparisons: '+str(lst.num_comparisons))
print('Number of switches: ' +str(lst.num_switches))


Feel free to play around in the previous problem with the number of operations it takes to calculate various
Fibonacci numbers. For example, it takes 102334154 operations to calculate the 40th Fibonacci number.

A good approximation for the number of operations it takes to calculate the th Fibonacci number is
which suggests that it would take approximately  addition operations to calculate the 1000th Fibonacci number.
Suppose you have a super-computer that can do  additions per second (which corresponds to the current state of the art).
How long would it take for your super-computer to calculate

使用递归可以自由地在前一个问题中使用计算斐波那契数的运算次数。例如，它需要102334154个运算来计算第四十个斐波那契数。

计算TH斐波那契数所需运算数的一个很好的近似
这意味着需要大约加法运算来计算第一千斐波那契数。
假设你有一台超级计算机，可以每秒做加法运算（这相当于当前的技术状态）。你的超级计算机需要多长时间计算？
'''
import math
sec_cal = 10**(-15)*0.5*((1+math.sqrt(5))/2)**1000
year_sec = 24*3600*365
print(10**(-15)*0.5*((1+math.sqrt(5))/2)**1000)
print(sec_cal/year_sec)
'''
解决方案真实世界应用
不幸的是，您发现大多数用户不愿意等待这个时间量来创建一个新帐户，因此您损失了很多业务。
然而，有人提出了一个新的实现ISI可用。此实现通过现有用户名的排序列表运行二进制搜索。如果仍然如此，
们可以每秒运行一百万个比较，并且我们有三亿个用户名，大约需要多长时间来确认未使用的用户名可用？
'''

users = ['amy', 'bob', 'charlie']

def is_available(username, users):
    if len(users) == 0:
        return True
    elif len(users) == 1:
        return username != users[0]
    else:
        i = int(len(users)/2)
        if username == users[i]:
            return False
        elif username < users[i]:
            return is_available(username, users[:i])
        else:
            return is_available(username, users[i:])