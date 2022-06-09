'''
https://www.codewars.com/kata/5d49c93d089c6e000ff8428c/train/python

Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.

Input:
Array of file sizes (0 <= s <= 100)
Capacity of the HD (0 <= c <= 500)
Output:
Number of files that can be fully saved in the HD.
Examples:
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12
save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, but 4+4+4 > 11
Do not expect any negative or invalid inputs.


test.it("Calculate number of files")
test.assert_equals(save([4,4,4,3,3], 12), 3)
test.assert_equals(save([4,4,4,3,3], 11), 2)
test.assert_equals(save([4,8,15,16,23,42], 108), 6)
test.assert_equals(save([13], 13), 1)
test.assert_equals(save([1,2,3,4], 250), 4)
test.assert_equals(save([100], 500), 1)
test.assert_equals(save([11,13,15,17,19], 8), 0)
test.assert_equals(save([45], 12), 0)
'''

#23rd solution by ericlee
def save(sizes, hd):
    cap = 0
    for i,c in enumerate(sizes):
        cap += c
        if cap == hd:
            return i+1
        elif cap > hd:
            return i
    if cap < hd:
        return len(sizes)


#1st solution
def save(sizes, hd):
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)

#2nd solution
from bisect import bisect
from itertools import accumulate

def save(sizes, hd):
    return bisect(list(accumulate(sizes)), hd)


#3rd solution
def save(sizes, hd):
    return save(sizes[:-1], hd) if sum(sizes) > hd else len(sizes)