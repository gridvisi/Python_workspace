

#2016 cat11-12
'''
3 watoer through
水槽最大存水量问题

在下图中，第一个槽有高度3、2和1米的挡板，而第二个槽有高度3、1和2米的挡板。挡板相距1米，槽有1米宽，
所以第一个槽可容纳3立方米，第二个槽容纳4立方米。
请问如果有一个长的水槽有9个隔板，隔板高度分别是9 3 6 8 4 5 7 4 2。请问水槽最多能储存的水量？
'''
h = "9 3 6 8 4 5 7 4 2"
#锻炼字符串空格替代为","的操作
hights = [int(i) for i in h.split(" ")]
print(h)

#算法一：相邻两个隔板取最小的那个是，可惜这个算法是不对的
volum = 0
for i in range(len(hights)-1):
    volum += min(hights[i],hights[i+1]) * 1
print(volum)

#算法二：左隔板算起向右取余下隔板中最高的，并记录两个隔板之间的距离
s = len(hights)
i,volum , j = 0,0, s-1
# 滑动窗口 左右边界i,j
while i < j and j < s:
    left = hights[i]
    right = max(hights[i+1:])

    for r in range(s-1,0,-1):
        if hights[s-r] == right:
            volum += (s-r - i) * 1 * min(left,right)
            i = s-r
            j = len(hights)-1
            print(left, right, volum)
print(volum)

#2016 cat11-12
#water hole 10-12

# 递推：到达camp处恰好水喝完，倒推离开前一站至少有3升水！
# 依次往前类推，

s = [[0,0], [2,2],[6,3],[8,1],[11,3],[13,3],[16,0]]
s = s[::-1]
for i in range(len(s)-1):
    d = s[i][0] - s[i+1][0]
    v = s[i][1] - s[i+1][1]

    if d + v <= 0:
        s[i + 1][1] = 0
    else:
        s[i + 1][1] = abs(d+v)
print(s)
print(s[-1][1])

#13-15 Numbers on sticks broken
'''
棍子上1-9构成一个数字。棍子可以在一个或多个地方折断，然后重新排列成一个新的数字。例如，有一次中断，1 2 3 可以在1和2之间打破成2 3 1，或者在2和3之间分解成3 1 2。（注意 3 2 1 不可能通过折断一次就实现）
1 2 3 −→2 3 1 或3 1 2  共有两种序列实现

对于以下每个木棍和断裂次数，可以得到的最大数字的最后三位数字是多少？ 
A. 断点可以有2个，4 3 9 7 2 9 5 6 
B. 断点可以有3个，4 3 9 7 2 9 5 6 
C. 断点可以有4个，4 3 9 7 2 9 5 6


心算更容易得到
A.  972,956,43
B.  97,956,43,2
C.  9,9,72,56,43

继续探讨编程解
输入：数组，断点数
输出：最大数字
'''





'''
伪代码是表达算法的一种方式。
重复（循环）是用While . . . EndWhile。

决定是用If . . EndIf或If . 否则 . . EndIf.


​寻找两个数字中较大的一个。
函数1：
输入A和B
如果A>B,  最大是 A;  否则, 最大的数是B
结束条件判断

函数2：
数字1, . . . , 10  总数 ← 0 N ← 1
当N≤10时，将N加到总和中
将1加入到N中，
EndWhile：结束循环

执行算法由以下伪代码表示：
输入A和B
如果A > B：A赋值给C, B赋值给D
否则, B赋值给C, A赋值给D

while C>D时, 一直执行：
从C中减去1
给D加1
EndWhile：直到不满足C>D时退出循环执行
输出C

以下输入四对(A,B)是执行算法的输入。
(10,2), (9,17), (100,200), (1001,2005)
有多少个输出是偶数的？

'''

def cal(x,y):
    x,y = sorted([x,y],reverse=True)
    while x > y:
        x -= 1
        y += 1
    return x
inp = [(10,2), (9,17),(100,200), (1001,2005)]

ans = [cal(x,y) for x,y in inp]
print(ans)

'''
CAT 2016 senior 第 5 题 洗牌

你有两张桌子，标签是A和 B。从一开始，桌子上有一排纸牌 A. 每张卡片上都有一个数字，所以卡片线一起形成一个数字。
B为空。您希望将卡片移动到B中，并制作一个尽可能大的数字。

移动X：从A中取出最左边的牌，并将其放在B的最右端
移动Y：从A中取出最右边的牌，放在的最右端 B. 例如，

假设A上有三张卡构成数字123。
上图说明了移动YXX，给出了的最终数字312 
注意312不是最大组合，👆例子仅说明X,Y的移动

如果A上的牌是3 7 1 2 6 5 4 ，那么B的最大的第四位数字是多少？

'''
from collections import deque

#cards = [3, 7, 1 ,2 ,6, 5 ,4]
cards = '3712654'
def shuffle(cards):
    d = deque(cards)
    ans = ''
    while d:
        if d[0] > d[-1]:
            ans += d.popleft()
        else:
            ans += d.pop()
        print(ans)
    return ans[3]
print(shuffle(cards))


# CAT 2016 senior 第 7 题 Rock Hopping 跳岩
'''
当跳岩石时，丛林步行者走到下一块岩石或跳过一块岩石。跳岩石会很累，所以他们会尽量减少踩上或跳上的岩石之间的高度差。
如果走到较低或相同水平岩石高度差，耗费的能量是0；
如果跳到更高的岩石，耗费能量等于高度
如果跳过岩石到更高的岩石，落到较低或相同水平岩石，耗费能量等于+高度差。

例如，考虑一条只有两块岩石的小溪，高度分别是3和1。跳上第1块岩石高度是3后，再踏上第2块岩石高度是
1，最后踏上岸，一共消耗3+0+0=3单位的能量。见图中的上图
跳到第1块岩石上，再跳过第2块岩石直接落在岸上，将花费3+1=4个单位的能量。见图示的中图
直接跳过第1块岩石，落在第2块岩石，最后走到河岸上，将花费2+0=2单位的能量。2=3-1 见图示的下图
3 1 2

穿过下面的每条小溪所消耗的最少的能量是多少？这些数字顺序显示了岩石的高度：
A.  2 4 1 3 
B.  3 1 2 2 4 
C.  3 1 2 2 4 1 4 3

分析：
A.  2 4 1 3 
1、如果跳到2，耗费2；跳过4落在1，耗费4-2-1=1；跳上3耗费3-1，走下到岸边耗费是0，这样共耗费 2+1+2+0=5
2、如果跳到2耗费2；跳到4耗费4-2，走到1耗费0；跳上3耗费3-1，走下到岸边耗费是0，这样共耗费 2+2+2+0=6
注意，第3和4块岩石还有一种跳法，1 跳跃过3后，落在对岸，耗费是2；这样就多出两种跳法：

3、如果跳到2，耗费2；跳过4落在1，耗费4-2-1=1；跳过3后到岸边耗费是2，这样共耗费 2+1+2=5
4、如果跳到2耗费2；跳到4耗费4-2，走到1耗费0；跳过3后到岸边耗费是2，这样共耗费 2+2+2=6

有没有耗能更少的跳法呢？
由第2块高度是4的岩石直接跳到第4块，耗能是0，总共耗能是4

算法优化结论
相邻3块岩石 高度 x,y,z
相邻3个岩石如两边高，中间低，呈现凹形时，应该直接越过谷底，而不是踏进谷底；否则将会增加一段向上跳的耗能​。
x ,y, z 满足 x > y and y < z , 
比较两种跳法： z - x 和  z - y 的大小，显然 z - x 更小
相邻3个岩石若呈现两边低，中间高，凸形时，比较两种跳法​：
x ,y, z 满足 x < y and y > z , 

A.  y - x + 0
B.  y - x - z
比较两种跳法，显然B <= A
代码实现

'''

# https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/train/python
'''
场景设置如时间序列的股票价格波动，可以参考上面的5种分类：
1、无序，有增有减
2、严格递增，一直升高
3、没有递减，存在价格不变的情况
4、严格递减，一直减少
5、保持不变
'''
def sequence_classifier(arr):
    if all(arr[i] == arr[i+1] for i in range(len(arr)-1)): return 5
    if all(arr[i] <  arr[i+1] for i in range(len(arr)-1)): return 1
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): return 2
    if all(arr[i] >  arr[i+1] for i in range(len(arr)-1)): return 3
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)): return 4
    return 0

#solution 2nd
TYPE_SEQ = {(1,): 1, (0,1): 2, (-1,):3, (-1,0): 4, (0,): 5}

def sequence_classifier(arr):
    countSet = { (a<b) - (a>b) for a,b in zip(arr, arr[1:]) }
    return TYPE_SEQ.get(tuple(sorted(countSet)), 0)