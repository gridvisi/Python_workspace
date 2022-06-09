import random
s = []
for i in range(999):
    s.append(random.randint(1,1000))
print(len([i for i in s if i%2 ==1]),len([i for i in s if i%2 ==0]))


#long list duplicate find


def dup(ls):
    re = []
    ls = sorted(ls)
    print(ls[1:])
    for i,e in enumerate(ls[1:]):
        if ls[i-1] == ls[i]:
            re.append(ls[i])
        if len(set(re)) == 2:
            return set(re)

nums = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(dup(nums))

class Solution:
    def singleNumbers(self, nums):
        re = []
        sel = set(sorted(ls))
        for i in sel:  # print(ls[1:])
            if i not in nums[:nums.index(i)]:
                if i not in nums[nums.index(i)+1:]:
                    re.append(i)
                    if len(re) == 2:
                        return re

class Solution:
    def singleNumbers(self, nums):
        re = []
        sel = set(sorted(nums))
        for i in sel:
            if nums.count(i) == 1:
                re.append(i)
                if len(re) == 2:
                    return re
ls = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(Solution.singleNumbers(0, ls))


class Solution:
    def singleNumbers(self, nums):
        re,s = [],len(set(nums))
        key = set(sorted(nums))
        for i,e in enumerate(nums):
            l = nums[:i]+nums[i+1:]
            if s - len(set(l)) == 1:
                re.append(e)
                if len(re) == 2:
                    return re
ls = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(Solution.singleNumbers(0, ls))


class Solution:
    def singleNumbers(self, nums):
        re,s = [],len(set(nums))
        key = set(sorted(nums))
        for i,e in enumerate(key):
            if nums.count(e) == 1:
                re.append(e)
                if len(re) == 2:
                    return re
ls = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(Solution.singleNumbers(0, ls))

from collections import Counter
class Solution:
    def singleNumbers(self, nums):
        d = Counter(nums)
        re = []
        key = set(sorted(nums))
        for e in key:
            if d[e] == 1:
                re.append(e)
                if len(re) == 2:
                    return re
ls = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(Solution.singleNumbers(0, ls))
#执行结果：通过显示详情执行用时 :88 ms, 在所有 Python3 提交中击败了26.35%的用户内存消耗 :15.6 MB, 在所有 Python3 提交中击败了100.00%的用户

from collections import Counter
class Solution:
    def singleNumbers(self, nums):
        d = Counter(nums)
        re = []
        #key = set(sorted(nums))
        for k,v in d.items():
            if d[k] == 1:
                re.append(k)
                if len(re) == 2:
                    return re
ls = [2,3,1,2,6,7,8,8,9,5,11,2,7,7,5]
print(Solution.singleNumbers(0, ls))

'''
几秒前	超出时间限制	N/A	N/A	Python3
23 分钟前	通过	4496 ms	15.4 MB	Python3
28 分钟前	通过	6952 ms	15.4 MB	Python3

'''