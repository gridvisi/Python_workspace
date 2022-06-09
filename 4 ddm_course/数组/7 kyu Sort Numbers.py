'''
https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python

python官方文bai档在说明type函数的用法时，明文推荐用duisinstance测试对象类zhi型。
isinstance似乎不是这么用的。 我通dao常的做法是用
typex=int(5)
if type(x)==int:
    print " x is interger.
else: print "false."isinstance
可以用来判断一个变量是否属于一个类。 在python里应该是正确的。
if type(x)==list:passif type(x)==dict:pass
'''

def solution(nums):
    if type(nums) == list:return sorted(nums)
    elif type(nums) != list:return []

nums = []
nums = 'abc'

#1st solution
def solution(nums):
    return sorted(nums) if nums else []
print(solution(nums))
