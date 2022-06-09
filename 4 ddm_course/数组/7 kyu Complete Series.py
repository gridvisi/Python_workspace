'''
https://www.codewars.com/kata/580a4001d6df740d61000301/train/python
给你一个非负整数的数组，你的任务是完成从0到数组中最高数字的序列。
如果提供的序列中的数字没有顺序，你应该对它们进行排序，但如果一个值重复，那么你必须返回一个只有一项的序列，而且该项的值必须是0.
像这样。
inputs        outputs
[0,1]   ->    [0,1]
[1,4,6] ->    [0,1,2,3,4,5,6]
[3,4,5] ->    [0,1,2,3,4,5]
[0,1,0] ->    [0]

'''
# Time: 626ms Passed: 105 Failed: 0

#19th solution by ericlee
def complete_series(seq):
    if len(set(seq)) < len(seq):return [0]
    return [i for i in range(max(seq)+1)]

#1st solution
def complete_series(a):
    return list(range(max(a) + 1)) if len(a) == len(set(a)) else [0]

#2nd solution
def complete_series(seq):
    from collections import Counter
    if Counter(seq).most_common()[0][1] > 1:
        return [0]
    return [i for i in range(max(seq)+1)]
