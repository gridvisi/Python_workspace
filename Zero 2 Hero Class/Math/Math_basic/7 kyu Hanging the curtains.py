'''
https://www.codewars.com/kata/5d532b1893309000125cc43d/train/python

介绍一下。
想象一下，你接到一个任务，要用窗帘钩在窗户上挂上一个已知长度(long)的窗帘。要求每个钩子之间的间距（距离）
在整个窗帘上是一致的，并且小于或等于提供的距离（max_hook_dist）。但您不允许使用任何测量设备或方法。
您应该如何测量？您需要多少个窗帘钩？

速记。
给定窗帘长度和窗帘钩之间的最大均匀距离 max_hook_dist 写一个函数，返回窗帘钩的数量，以便按照描述的方式悬挂窗帘。

定义
length - 窗帘的长度。始终为正值。

max_hook_dist - 窗帘钩之间的最大均匀距离[1,100]（假设窗帘钩没有厚度，可以固定在整个窗帘的任何位置）。可
以高于窗帘的长度。

测量设备/方法--不允许使用任何可用于测量挂钩之间距离的测量方法或仪表类型（尺子、手指等）。用数学来代替。

P.S.希望这个卡塔能改变你自己挂窗帘时使用窗帘钩的数量:)
test.assert_equals(number_of_hooks(200,70), 5)
test.assert_equals(number_of_hooks(200,10), 33)
'''
#9th slove by ericlee
def number_of_hooks(length,max_hook_dist):
    n = 0
    while length/2**n > max_hook_dist:
        n += 1
    return 2**n + 1
length,max_hook_dist = 200,10
#length,max_hook_dist = 200,70
length,max_hook_dist = 200,202
print(number_of_hooks(length,max_hook_dist))

#1st
from math import *

def number_of_hooks(length, maxHook):
    return length and 2**ceil(max(0,log2(length/maxHook) )) + 1

