#https://blog.csdn.net/qq_32424059/article/details/88855423
'''
Given an array of integers, every element appears twice except for one. Find that single one.
即给定一个均为整数的数组，除了其中一个数字出现一次，其他均出现了两次，找到这个出现一次的数字
加入给[1,2,3,3,4,4,2]，则输出1。

首先将该数组从小到达排序，然后依次从第二个数开始，对比其是否与第1个不同且与第3个不同，
如果是，则代表该数字为我们要找的。代码如下：

'''
class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:#如果数组长度为1，则输出该数字。其实我这里考虑多了，题目的意思应该是该数组长度大于等于3
            return nums[0]
        else:
            nums.sort()# 排序
            #以下两个if判断头尾两个数字是否为single number
            if (nums[0] != nums[1]):
                return nums[0]
            if (nums[len(nums)-1] != nums[len(nums)-2]):
                return nums[len(nums)-1]
            else:
                for i in range(1,len(nums)-1):
                    if (nums[i]!=nums[i+1] and nums[i]!=nums[i-1]):
                        return nums[i]

#Approach 1: 这是一个比较讨巧的方法，直接将原数组用set()去重以后，求和并乘2再减去原数组的和，
# 得到single number

class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

#Approach 2:利用Hash表来实现，这里将数组里的数赋值为哈希表的下标，也很巧妙，且复杂度低

nums = [2,2,3,3,6,5,5,1,6,7,1]
class Solution(object):
    def singleNumber(self, nums):
        Hash_table = {}
        for i in nums:
            try:
                Hash_table.pop(i) #如果该下标存在数据，则删除.如果某数字出现两次，则会被添加一次和删除一次
            except:# 否则，将该下标的数据赋值为1
                Hash_table[i] = 1
        return Hash_table.popitem()[0]

def singleNumber(self, nums):
    Hash_table = {}
    for i in nums:
        try:
            Hash_table.pop(i) #如果该下标存在数据，则删除.如果某数字出现两次，则会被添加一次和删除一次
        except:# 否则，将该下标的数据赋值为1
            Hash_table[i] = 1
    return Hash_table.popitem()[0]
print(singleNumber(0,nums))

