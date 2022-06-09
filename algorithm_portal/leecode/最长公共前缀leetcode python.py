'''
最长公共前缀-----leetcode刷题（python解题）

14. 最长公共前缀-----leetcode刷题（python解题）
 pythonleetcode算法
发布于 2019-06-29
[TOC]

题目
**编写一个函数来查找字符串数组中的最长公共前缀。**
如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/probl...
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解答
'''

class Solution(object):
    def __init__(self, strs):
        self.strs = strs
        #self.age = age

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = 0
        num = []
        len_strs = len(strs)
        for i in strs:
            num.append(len(i))
        if num == []:
            return ""
        min_num = min(num)
        for i in range(min_num):
            for j in range(len_strs - 1):

                if strs[j][i] != strs[j + 1][i]:
                    break
            else:
                a += 1
                continue
            break
        return strs[0][:a]

s = ["flower","flow","flight"]
myQuestion = Solution(s)
#myQuestion = longestCommonPrefix(s)
s = ["flower","flow","flight","fluence"]
print(myQuestion.longestCommonPrefix(s))

# 定义一个Person类
class Person(object):
    """人类"""
    def __init__(self, name , age):
        self.name = name
        self.age = age

p = Person('小黑',18)
print(p)

print('\n\n\n\n\n')

# 定义一个Person类
class Person(object):
    """人类"""
    def __init__(self, name , age):
        self.name = name
        self.age = age

    # __str__（）这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果  （print函数）
    def __str__(self):
        print(Person)
        return 'Person [name=%s , age=%d]'%(self.name,self.age)

p = Person('小黑',18)
print(p)