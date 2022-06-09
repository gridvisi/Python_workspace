

a = 10
b = 0
c = a / b
#print("done")
'''
Traceback (most recent call last):
  File "<input>", line 3, in <module>
ZeroDivisionError: division by zero

我们发现程序因为ZeroDivisionError而中断了，语句print "done" 没有运行。为了处理异常，
我们使用try...except,更改代码：
'''

a = 10
b = 0
try:
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)
    print("done")