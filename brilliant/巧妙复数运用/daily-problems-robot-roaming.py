'''
https://brilliant.org/daily-problems/robot-roaming/

Very very nice, I never thought of complex numbers

↑ = 1, ↓ = -1, ← = j, → = -j↑=1,↓=−1,←=j,→=−j are the directions of the axes
It would be very helpful if the z-1z−1 was changed to z+1jz+1j,
I was dumb and was wondering how the heck is that showing the red area until
I realised u had rotated the figure, or kept your axes in a different way

如果机器人向左为left简称为L，向右为right简称 R, 那么机器人走四步的可能性有数学中的全排列可。第一步是L，第一步是R两种☞
LLLL
LLLR  LLRL  LRLL RLLL
LLRR LRRL RRLL
LRRR RRRL
LRLR

RRRR RRRL
RRLR RLRR LRRR
RRLL RLLR  LLRR
RLLL LRLL LLRL LLLR
RLRL
#重复出现的划掉后面出现的，共计有16种路线。

​第一步：两种选择 L 和 R

第二步：两种选择 L 和 R

... ...

由排列组合可知，共有2的4次方即16种排列。

第二步：运用python全排列函数枚举左右路线最后的位置
'''

from itertools import product
black,blue,orange = 0, 0, 0
for moves in product((1, -1), repeat=4):
    #print(moves)
    pos = sum(moves)
    if pos <= 1:
        black += 1
    elif pos <= 2:
        blue += 1
    else:
        orange += 1
print(f"black: {black}, blue: {blue}, orange: {orange}")



print(1j + 1j,1j + abs(- 0 - 1j) + 1 == 1)
red, blue, orange = 0, 0, 0

print(sum([1, 1, -1, 1j]),abs(sum([1, 1, -1, -1j])),abs(sum([1, 1, -1, 1j]))<=1)
print(sum([1, 1, -1, (-0-1j)]))


for moves in product((1, -1, 1j, -1j), repeat=4):
    print(moves)
    z = sum(moves)
    if abs(z - 1) <= 1:
        red += 1
    elif abs(z) <= 2:
        blue += 1
    else:
        orange += 1

print(f"red: {red}, blue: {blue}, orange: {orange}")