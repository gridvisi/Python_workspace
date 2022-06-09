#Python3中类Class和对象object的理解（代码示例）代码块
#https://blog.csdn.net/qq_32424059/article/details/88855423
class Person:  # 这样我们就将eating封装到了Person这个类里面
    # 只要是Person这一类别的都可以进行下面的行为（eating）
    def eating(name):
        print(name, "吃饭")

class Person:
    def eating(self):
        print(self,"吃饭")
zhangsan = Person()  # 这里就不能像以前一样用eating去调用了，因为只有Person这一类的才能就行eating这个行为
# 所以我们就要先将zhansan定义为Person这一类
zhangsan.eating()  # 然后才能让张三进行吃草这种行为

'''
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
nums = [4,3,2,7,8,2,3,1]
class Solution(object):
    def findDisappearedNumbers(self, nums):
        length = len(nums) # 求数组长度
        nums.sort() # 排序数组
        num_set = set(nums) # 去重
        list_allset = set(list(range(1,length+1))) #定义一个从1到n开始的set
        return list(list_allset - num_set) #两个set相减便得到最终结果
ans = Solution()
print(ans.findDisappearedNumbers(nums))
