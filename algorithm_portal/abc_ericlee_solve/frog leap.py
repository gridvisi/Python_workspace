__author__ = 'Administrator'

def frog(n):
    """

    :rtype : object
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return frog(n-1) + frog(n-2)
print(frog(11))

'''
How many ways can we arrange 10 identical black balls and 10 identical red balls in a line,
such that no more than 2 balls of the same color ever appear in a row?
有多少种方式可以将10个相同的黑球和10个相同的红球排成一行，使得同一颜色的球不会连续出现超过2个？
00     10, 11,
0       2,  3

01     00, 01, 10, 11
1       0,  1,   2,    3

10     01, 10,11
2       1,   2,  3

11     00, 01, 10, 11
3       0,   1,   2,  3
print('------------------------------')

ball = {0:[2,3],1:[0,1,2,3],2:[1,2,3],3:[0,1,2,3]}
for key in ball:
    print ('key is %s,value is %s'%(key,ball[key]))

for key in range(4):
    path = [key]
    for value in ball[key]:  #print(value)
        for i in range(len(ball[key])):
            path.append(ball[key][i])
            for j in range(ball[ball[key][i]]):
                path.append(j)
print(path)
'''
'''
ball = {
1 : [7, 13, 19], 2 : [12, 18, 20], 3 : [16, 17, 19], 4 : [11, 14, 18],
5 : [13, 15, 18], 6 : [9, 14, 16], 7 : [1, 15, 17], 8 : [10, 16, 20],
9 : [6, 11, 19], 10 : [8, 12, 17], 11 : [4, 9, 13], 12 : [2, 10, 15],
13 : [1, 5, 11], 14 : [4, 6, 20], 15 : [5, 7, 12], 16 : [3, 6, 8],
17 : [3, 7, 10], 18 : [2, 4, 5], 19 : [1, 3, 9], 20 : [2, 8, 14]
}


我要取出字典中的键
可以使用keys()方法取出字典中的键，不取对应的值

#创建一个人和对应喜欢水果的字典
people={'lifei':'apple','fanming':'peach','gaolan':'banana','hanmeimie':'peach'}
for name in people.keys():
    print(name)

输出：（顺序是随机的）
hanmeimie
gaolan
fanming
lifei
---------------------
全文地址请点击：https://blog.csdn.net/a411178010/article/details/78548168?utm_source=copy


        for num in ball.keys():
            print (num)

'''
ball = {0:[2,3],1:[0,1,2,3],2:[1,2,3],3:[0,1,2,3]}
def find_all_paths(graph, i, count, path=[]):
    """
https://blog.csdn.net/a411178010/article/details/78548168/
    :rtype : object
    """

    path = path + [i]
    paths = []
    if count > 0:
        j = len(graph[i])

        for j in range(j-1):
            node = graph[i][j-1]
            newpaths = find_all_paths(graph, node, count,path)
            count -= 1
            paths.append(newpaths)
                   #if node not in path:
    return paths

set=[]
#for i in ball[0]:
set.append(find_all_paths(ball, 0, 20))

print(set)
print('total:', len([j for i in set for j in i]))

'''
for i in range(4):
    x = len(ball[i])
    print(x)

def transfer(x):
    if x == 0:
        return 1
    if x == 1:
        return 0
print(transfer(0))

queu = [0 for i in range(20)]
print(queu)

i = 0
while i < 18:
    if queu[i] == queu[i + 1]:
        queu[i + 2] = transfer(i+1)
    queu[i + 2] = transfer(i+1)
    i += 1
print(queu)

def rwball(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    #if x == 3:

    return rwball(x - 2) + rwball(x - 1) +1
print('ball rw:',rwball(20))
'''
def S(t,x):
    if x < 0 or x > t:
        return 0
    if t == 0:
        return 1
    if t == 1:
        return x
    return S(t-1,t-x) + S(t-2,t-x)

print (2*S(20,10))
'''
CS: RECURSION
The following code shell partially implements the binary search algorithm,
with the base case implemented. Can you fill in the recursive step?
'''
# Returns True if A contains item and False otherwise
def binary_search(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
       # your code goes here
        #A[:middle] is a copy of the elements of A to the left of middle
            return binary_search(A[:middle], item)
        else:
        #A[middle+1:] is a copy of the elements of A to the right of middle
            return binary_search(A[middle + 1:], item)
list = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103,4]
print(binary_search(list, 4))
print(binary_search(list, 42))