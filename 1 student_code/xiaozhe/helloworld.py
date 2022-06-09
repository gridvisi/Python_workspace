
name=input("输入人姓名:")#小哲 回车
print(name)
print(f"hello,{name}你几岁了")
age=1000

# Integer
a = 2
print(a)
# Output: 2
# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)

#10 = wangzijie
wangzijie = 10
# Output: None
#GoalKicker.com – Python® Notes for Professionals 7
#Variable assignment works from left to right. So the following will give you an syntax error.
#0 = x
#=> Output: SyntaxError: can't assign to literal
#You can not use python's keywords as a valid variable name. You can see the list of keyword by:
import keyword
print(keyword.kwlist)


a = 10
b = 10
w = 'rain'
if w == 'rain' or w == '太阳':
    print('带伞')
else:
    print('不带伞')
if a > b: # If block starts here
    print(a) # This is part of the if block
    print('if 如果')

else: # else must be at the same level as if
    print('else 那么')
    print(b) # This line is part of the else block

#zhihu
#stackoverflow

import math
c = [i for i in range(1,101)]
for i in c:
    for j in range(i+1,101,1):
        k = math.sqrt(i*i + j*j)
        if  k == int(k) and k in c:
            print(i,j,k)























































































































































































































































































































































































































































































