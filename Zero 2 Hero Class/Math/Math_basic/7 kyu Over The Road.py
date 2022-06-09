'''
https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python

Example
Given your house number address and length of street n, give the
house number on the opposite side of the street.
Street
1|   |6
3|   |4
5|   |2
Evens increase on the right; odds decrease on the left.
House numbers start at 1 and increase without gaps.
When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
'''

# 路左边的牌号是1-99的单数，右边是100-2的双数
# 小明的发现路正对面的小亮的门牌号是自家门牌号加1
# 请问小明和小亮的门牌号

leftside = [i for i in range(1,100,2)]
rightside = [i for i in range(100,0,-2)]

for i in leftside:
    if rightside[leftside.index(i)] + 1 == i:
        print(i)


#solution 1st
def over_the_road(address, n):
    left = [i for i in range(1,2*n+2,2)]
    right = [i for i in range(2*n,0,-2)]
    return right[left.index(address)]

address,n = 7,11
print(over_the_road(address, n))

#solution 2nd
def over_the_road(address, n):
    return 2*n+1 - address


    #Input: address (int, your house number), n (int, length of road in houses)
    #Returns: int, number of the house across from your house.

    # this is as much a math problem as a coding one
    # if your house is [even/odd], the opposite house will be [odd/even]
    # highest number on street is 2n
    # Left side houses are [1, 3, ... 2n-3, 2n-1]
    # Right side houses are [2n, 2n-2, ... 4, 2]
    # Sum of opposite house numbers will always be 2n+1

