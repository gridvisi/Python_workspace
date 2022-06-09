'''
https://www.codewars.com/kata/542f0c36d002f8cd8a0005e5/train/python

There's a waiting room with N chairs set in single row.
Chairs are consecutively numbered from 1 to N.
First is closest to the entrance (which is exit as well).

For some reason people choose a chair in the following way

Find a place as far from other people as possible
Find a place as close to exit as possible
All chairs must be occupied before the first person will be served

So it looks like this for 10 chairs and 10 patients

Chairs	    1	2	3	4	5	6	7	8	9	10
Patients	1	7	5	8	3	9	4	6	10	2
Your task is to find last patient's chair's number.

Input - N - integer greater than 2 - number of chairs.
Output should positive integer too - last patient's chair's number

Have fun :)

ALGORITHMSSORTINGPUZZLESGAMES

有一个候诊室，里面有N把椅子摆成一排。椅子的编号从1到N连续排列。
出于某种原因，人们以下列方式选择椅子
找到一个尽可能远离其他人的地方
找一个尽可能靠近出口的地方
在为第一个人服务之前，所有的椅子都必须被占用。

因此，对于10把椅子和10个病人来说，情况是这样的

椅子 1 2 3 4 5 6 7 8 9 10
病人 1 7 5 8 3 9 4 6 10 2
你的任务是找出最后一个病人的椅子号码。

输入 - N - 大于2的整数 - 椅子的数量。输出也应该是正整数 - 最后一个病人的椅子号码

祝你玩得开心 :)

算法分类拼图游戏
'''



# Timeout solution
def last_chair(n):
    chairs,start,end = [0] * n,0,n-1
    chairs[start],chairs[end] = 1,2
    for i in range(3,n):
        mid = (start + end)//2
        chairs[mid] = i
        take = [i for i,e in enumerate(chairs) if e != 0]
        gap = [(y-x,x,y) for x,y in list(zip(take[:-1],take[1:]))]
        start,end = max(gap,key=lambda x:x[0])[1:]
    return end

n = 10
print(last_chair(n))


#1st
def last_chair(n):
    # Propn:
    #   Given there are n seats, n >= 2. The (n-1)th seat is always the
    #   last to be taken (taken in iteration n).
    # Proof:
    #   Suppose that, for some n >= 2, the (n-1)th seat is taken on
    #   iteration i > 2. The nth seat is already taken, since the 2nd
    #   iteration will always claim it. Therefore i must sit beside
    #   at least one person (the occupant of seat n).
    #   Additionally, the (n-2)th seat must also already be taken.
    #   If it were not taken, (n-2) would have a free seat at (n-1)
    #   and would be closer to the exit, and so would rank higher
    #   than (n-1) in the choice algorithm.
    #   Therefore (n-1) will only be chosen when (n-2) and (n) are
    #   both taken.
    #   Also, all other seats must also be taken, since
    #   otherwise i would taken them, having at most as many people
    #   around as seat (n-1) and being closer to the exit.
    #   Therefore (n-1) is the last seat to be taken.
    return n - 1

'''
   # 预言。
    # 鉴于有n个座位，n>=2。第(n-1)个座位总是
    # 最后一个被占用的座位（在迭代n中被占用）。
    # 证明。
    # 假设，对于某些n >= 2，第(n-1)个座位是在
    # 迭代i>2。第n个座位已经被占用了，因为第2个
    # 迭代总是会占用它。因此，我必须坐到
    # 至少有一个人（第n个座位的占用者）。
    #此外，第(n-2)个座位也必须已经被占用。
    # 如果它没有被占用，(n-2)就会在(n-1)有一个空闲的座位
    # 而且离出口更近，所以排名会更高
    # 在选择算法中比(n-1)高。
    # 因此，只有当(n-2)和(n)都被占用时，(n-1)才会被选中。
    # 都被选中。
    # 同时，所有其他的席位也必须被占用，因为
    # 否则我就会选择它们，因为最多只有这么多人
    #周围的人和座位（n-1）一样多，而且离出口更近。
    # 因此(n-1)是最后一个被占用的座位。
    返回 n - 1
'''