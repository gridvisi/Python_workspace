'''
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

Test.assert_equals(beeramid(9, 2),  1)
Test.assert_equals(beeramid(21, 1.5),  3)
Test.assert_equals(beeramid(-1, 4), 0)
'''

def beeramid(bonus, price):
    level = s = 0
    if bonus < 0:return 0
    while s <= bonus/price:
        s += level*level
        level += 1
    return level-2
bonus,price = 1500, 2
bonus,price = 5000, 3
bonus,price = 21, 1.5
print(beeramid(bonus,price))


def beeramid(bonus, price):
    beers = bonus // price
    levels = 0
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers -= levels ** 2

    return levels

print(sum([i*i for i in range(14)]))

nums = 100
def pyramid(nums):
    levels = 0
    while nums >= (levels + 1) ** 2:
        levels += 1
        nums -= levels ** 2
    return levels,nums
print(pyramid(nums))