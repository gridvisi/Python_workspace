from collections import deque
d = deque('ghi')
print(d)  #deque(['g', 'h', 'i'])

for elem in d:   # deque 可迭代
    print(elem) # 不带  的是输出

d.append('j')
print(d) #deque(['g', 'h', 'i', 'j'])

d.appendleft('f')
print(d) #deque(['f', 'g', 'h', 'i', 'j'])

print(d.pop())
print(d)  #deque(['f', 'g', 'h', 'i'])

print(d.popleft()) #'f'
print(d) #deque(['g', 'h', 'i'])

print(d[0])  #'g'
print(d[-1]) #'i'

d.extend('jkl')  # 在右端一次增加多个元素
print(d)  #deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.extendleft('edf')
print(d) #deque(['f', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l'])
print('k' in d)  #True
d.clear()
print(d) #deque([])

list1 = ['a', 'b', 'c']
d = deque(list1)  # 可以把一个列表转为deque
print(d)

deque(['a', 'b', 'c'])
print(d.count('b'))  # count方法可以统计duque中某一元素的个数 1

print(deque(list1, 2)) # 只取后两个元素，可以实现打开文件时只取后面几行 deque(['b', 'c'], maxlen=2))