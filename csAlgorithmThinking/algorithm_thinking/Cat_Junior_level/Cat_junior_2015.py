
'''
挑战 5：最长子序列
子序列是一个列表中的一个或多个相邻元素的集合。例如，153是415368的一个子序列。
子序列153的和为9。以下列表中任何子序列的最大和是多少？
-6 1 6 0 -3 -3 5 7 -9 3 -9 4 7 -5 1 6 -2 1 -5 7
'''

# 不用递归算法的思路. 效率低！
# 每个数在数组中的位置坐标 i , sub = sum(s[i:])数组形式追加到 element
# 从左到右，找到两个sub的值相差最大的 2 个element的坐标

s = '-6 1 6 0 -3 -3 5 7 -9 3 -9 4 7 -5 1 6 -2 1 -5 7'
s = [int(i) for i in s.split(' ')]
print(s)
def Maxseq(s):
    seq = [sum(s[:i+1]) for i,e in enumerate(s)]
    mx,inx = 0,[]
    for i,e in enumerate(seq[:-1]):

        if max(seq[i+1:]) - e > mx:
            inx.append((i))
            mx = max(seq[i+1:]) - e
    return mx
print(Maxseq(s))

# 优化上述思路
# 遍历输入数组 s , sub = sum(s[:i])
# sub < 0时，s[:i]一定不在最大子序列中，舍弃这一段,重新i+1开始遍历
# s[i+1:]序列的最大值更替到 mx 变量
# 循环执行1，2步骤，直至数组结束

def Maxseq(s):  #只输出最大序列的值
    sub = mx = s[0]
    for i in (s):
        if sub < 0:
            sub = i
        else:
            sub += i
        #print('sub,mx = ',sub,mx)
        mx = max([sub, mx])
    return mx
print('solveOptimiz = ', Maxseq(s))


def Maxseq(s):
    sub,mx = [0] * len(s),s[0]
    sub[0] = s[0]
    for i in range(len(s)):
        if sub[i] < 0:
            sub[i] = s[i] #sub[i-1] - s[i]
            #pass
        else:
            sub[i] += s[i]
        mx = max([sub[i],mx])
    return mx,sub
print('solveOptimiz,indx = ',Maxseq(s))
# [ 0, 1, 7, 0,  0,  0, 5, 12,  0, 3,  0, 4, 11,  0, 1, 7,  0, 1,  0, 7]
# [-6, -5, 1, 0, -3, -3, 2, 9, -9, -6, -9, -5, 2, -5, -4, 2, -2, -1, -5, 2]
# [-6, 1, 6, 0, -3, -3, 5,  7, -9, 3, -9, 4,  7, -5, 1, 6, -2, 1, -5, 7]


sub,mx = [0,3],[3,5]
print(max([sub,mx],key=lambda x:x[1]))

def Maxseq(s):
    sub,mx = [0,s[0]],[0,s[0]]
    for i,e in enumerate(s):
        #print(sub,mx)
        if sub[1] < 0:
            sub[1] = e
        else:
            sub[0],sub[1] = i,sub[1] + e

        mx[0],mx[1] = i,max([sub,mx],key=lambda x:x[1])[1]
    return mx
print('solveOptimiz = ',Maxseq(s))



# 分治法
def divide_and_conquer(lst, left, right):
    if left == right:
        if lst[left] > 0:
            return lst[left]
        else:
            return 0

    center = (left + right) // 2
    # 左边界最大子序列和右边界最大子序列
    max_left_sum = divide_and_conquer(lst, left, center)
    max_right_sum = divide_and_conquer(lst, center + 1, right)

    max_left_border_sum = left_border_sum = 0
    for i in range(center, left - 1, -1):
        left_border_sum += lst[i]
        if left_border_sum > max_left_border_sum:
            max_left_border_sum = left_border_sum

    max_right_border_sum = right_border_sum = 0
    for i in range(center + 1, right + 1):
        right_border_sum += lst[i]
        if right_border_sum > max_right_border_sum:
            max_right_border_sum = right_border_sum

    # 左、右与跨越边界的子序列
    return max(max_left_sum, max_right_sum, max_left_border_sum + max_right_border_sum)


if __name__ == '__main__':
    lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(divide_and_conquer(s, 0, len(s)-1))


#3 动态规划
'''
当前的最大子序列和一定是由之前的最大子序列和加上（或不考虑）当前元素构成的。
那么我们从第一个元素开始，假设第一个元素为目前的最大子序列和，下一个最大子
序列一定是这个子序列加上第二个元素或者丢掉第一个元素。那么何时加上第二个元
素呢？

只要第一个元素不为负数（因为负数只会越加越小，根本不会构成最大子序列和），那
么就是第一个子序列和加上这个元素。如果是负数，那么目前最大的子序列的起始位置
只能是这个元素。这样每次循环都得到目前最优的子序列，直到循环结束。
回归到第一种方法，每次循环都是起始位置的确定的，结束位置也是在循环不断变化中。
此方法是在每次循环中起始位置（可能）和结束位置都在变化。

'''

def getMaxSubSeqSum(arr):
    max_sum = arr[0]
    cur_sum = arr[0]
    for i in range(1, len(arr)):
        if cur_sum < 0:
            cur_sum = arr[i]
        else:
            cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


if __name__ == '__main__':
    arr = s
    res = getMaxSubSeqSum(arr)
    print(f"最大子序列 {res}, arr = {s} ")

from collections import Counter

def count_deaf_rats(town):
    # Your code here
    p = town.index('P')
    l, r = town[:p], town[p:]
    print(Counter(l),Counter(r))
    ll = sum([v for k,v in Counter(l).items() if k=='O~'])
    rr = sum([v for k,v in Counter(r).items() if k=='~O'])
    return ll + rr

town = "P O~ O~ ~O O~"
print(count_deaf_rats(town))



def count_deaf_rats(town):
    # Your code here
    p = town.index('P')
    l, r = town[:p], town[p:]
    print(Counter(l),Counter(r))
    ll = l.count('O~')
    rr = r.count('~O')
    return ll + rr

town = "P O~ O~ ~O O~"
print(town.split('P'))
town = "~O~O~O~OP~O~OO~"
print(town.split('P'))
print(count_deaf_rats(town))


def count_deaf_rats(town):
    # Your code here
    lft,rgt ='O~','~O'
    l,r = [''.join(i.split(' ')) for i in town.split('P')]
    ll = sum([1 for i in range(0,len(l)-1,2) if l[i:i+2]==lft])
    rr = sum([1 for i in range(0,len(r)-1,2) if r[i:i+2]==rgt])
    return ll + rr

town = "P O~ O~ ~O O~"
#town = "~O~O~O~OP~O~OO~"
print(count_deaf_rats(town))

#Top 1st solve
def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')