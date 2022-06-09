'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        numstr = list(map(str,numbers)) #用str方式将int型数字转换成string
        for i in range(len(numstr)):
            for j in range(i+1,len(numstr)):
                a=int(numstr[i]+numstr[j])
                b=int(numstr[j]+numstr[i])
                if(a>b):
                    t=numstr[i]
                    numstr[i]=numstr[j]
                    numstr[j]=t
        s=""
        for i in range(len(numstr)):
            s=s+numstr[i]
        return int(s)

numbers = [3,32,321]
res = Solution()
print(res.PrintMinNumber(numbers))

print('--------# fake usage # --------')
#print(res(numbers))
#print(res.PrintMinNumber(numbers))
#re = numbers.PrintMinNumber
#print(Solution.PrintMinNumber(self, numbers))

#print(Solution.numbers)

class A(object):
    def test(self):
        print('test1')

fun = getattr(A, 'test')
print('Self:',A)
print('fun:',fun(A))   #一定要加A

