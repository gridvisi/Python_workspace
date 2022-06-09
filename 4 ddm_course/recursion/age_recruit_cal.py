__author__ = 'Administrator'
'''
有5个人坐在一起，
问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。
请问第五个人多大？用递推算法实现。
'''

persons = [0] * 5
persons[0] = 10
older = [2,2,2,2]
for i in range(1,len(persons)):
    persons[i] = persons[i-1]+older[i-1]
print(persons[-1])


def ages(n):
    if n==1:
        return 10
    return ages(n-1)+2

n = 5
print(ages(n))

'''
题目21：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，
又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第8天早上想再吃时，见只剩下一个桃子了。
求第一天共摘了多少。

'''

x2 = 1
for day in range(7,0,-1):
    x1 = (x2 + 1) * 2
    x2 = x1
print(x1)

#recursion_slove

def recur(day):
    if day == 8:
        return 1
    return 2*(recur(day+1) + 1)

day = 1
print(recur(day))


#利用递归方法求 5!

def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
print(fact(5))


#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string:')
l = len(s)
output(s, l)

