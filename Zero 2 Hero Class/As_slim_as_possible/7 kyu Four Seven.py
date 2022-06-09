'''
https://www.codewars.com/kata/5ff50f64c0afc50008861bf0/solutions/python

今天的任务

简单的规则。你的函数输入4和7。如果输入了4，函数应该返回7。如果输入了7，函数应该返回4。其他任何输入
都应该返回一个false值，比如False、0、[]、""。
边界限制条件：函数不能包含if语句或者eval函数，由于使用它可以绕过if要求！有一些非常简单的方法来回答
这个问题，但我鼓励你尽可能地尝试和创新。

​非常简单的任务，但是做到极简就需要深入且灵活地掌握python的逻辑特性。
显然以上写法无法满足4，7之外的情况,而且还用到了if语句那么，该如何破冰​开脑洞呢？
布尔运算，往往是一条路，当上帝关上if这扇门，还好会留给

我们另外一扇门 logic operate
'''

def solution(n):
    return 4 if n == 7 else 7

def solution(n):
    return {4:7, 7:4}.get(n)