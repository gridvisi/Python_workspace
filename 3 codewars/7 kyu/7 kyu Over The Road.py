'''
Python
TRAINNEXT KATA
Details
Solutions
Discourse (52)
Collect|
Task
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:

Street
1|   |6
3|   |4
5|   |2
任务
你刚搬进一条笔直的街道，路两边有n栋完全相同的房子。自然，你想知道街道另一边的人的房号。这条街道看起来像这样。

街道
1| |6
3| |4
5| |2
偶数在右边增加，赔率在左边减少。宅号从1开始增加，不留空隙。当n=3时，1对6，3对4，5对2。
Example
Given your house number address and length of street n, give the house number on the opposite side of the street.
例子
给出你的房号地址和街道的长度n，给出街道对面的房号。

1| |10
3| |8
5| |6
7| |4
9| |2
'''
#7 = 2*3 + 1
#odd = odd // 2 + 1

def over_the_road(address, n):
    left = [2*i+1 for i in range(n)]
    right = [2*i for i in range(1,n+1)][::-1]
    if address % 2 == 0:
        s = right.index(address)
        return left[s]
    else:
        s = left.index(address)
        return right[s]          #left,right[::-1]
address,n = 1,10
address,n = 7, 11
print(over_the_road(address, n))