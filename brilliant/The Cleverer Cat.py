# https://brilliant.org/problems/the-cleverer-cat/
'''
The Cleverer Cat?
Computer Science Level pending
How many slices of the list used in this problem multiply to
get a prime less than or equal to 31?

This problem is inspired by Agnishom Chattopadhyay who was
inspired by Christopher Boo, who in turn was inspired by the
Malaysia Computing Olympiad 2014.

聪明的猫？
计算机科学水平待定
这个问题中使用的列表中的多少个片断相乘可以得到一个小于或等于31的素数？

这个问题的灵感来自Agnishom Chattopadhyay，他的灵感来自Christopher Boo，
而Christopher Boo的灵感又来自2014年马来西亚计算机奥林匹克竞赛。
'''

def is_prime(a):
    return a > 1 and all(a % i for i in range(2, a))

array= [i for i in range(2,32) if is_prime(i)]
def totall(array,num):
    total=0
    for n in range(1,len(array)+1):
        for i in range(len(array)):
            cur=array[i:i+n]
            if len(cur)==n:
                prod=1
                for i in cur:
                    prod*=i
                if prod<=num and is_prime(prod): total+=1
    return total
print(totall(array,31))

#https://d18l82el6cdm1i.cloudfront.net/uploads/documents/list-GfO0iB928U.txt
# https://brilliant.org/problems/the-clever-cat/?group=sigjT0HDmvgp&amp;ref_id=713367
