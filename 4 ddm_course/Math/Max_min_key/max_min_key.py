# 6 kyu
# Character with longest consecutive repetition
# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

s = [{'name': 'li', 'age': 24},{'name': 'he', 'age': 45} ]
b = max(s, key=lambda x: x['age'])
print(b)

d1 = {'name': 'egon', 'price': 100}
d2 = {'name': 'rdw', 'price': 666}
d3 = {'name': 'zat', 'price': 1}
l1 = [d1, d2, d3]
a = max(l1, key=lambda x: x['name'])
print(a)
b = max(l1, key=lambda x: x['price'])
print(b)


import math
a = [1,3,5,7,9,11,13,15,17]
min(a, key=math.sin)
#11
math.sin(11) # 元素11的正弦值最小
#-0.9999902065507035


a = [8,5,2,4,3,6,5,5,1,4,5]
print(max(set(a), key=a.count))
#5
print(a.count(5))

chars = "bbbaaabaaaa"
print(max(set(list(chars)),key=chars.count))