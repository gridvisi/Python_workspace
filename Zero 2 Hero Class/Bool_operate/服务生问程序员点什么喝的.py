'''
服务生问程序员点什么喝的？

​程序员答，按照python的and与or用法，已经替我选好了!
​
- 咖啡和茶，您点哪个？
- 茶-

- 咖啡或者茶，您点哪个？
- 咖啡

童鞋们，为什么说服务生已经选好？


'''
print('coffee' and 'tea')
print('coffee' or 'tea')

disk = []
fold = disk.append([])

while disk:
     disk.pop()
print(disk)


f = lambda x,y: 'greater' if x > y else 'less' if y > x else 'equal'

array = [(0,0),(0,1),(1,0),(1,1)]

for a in array:
  x, y = a[0], a[1]
  print(f(x,y))

# Output is:
#   equal,
#   less,
#   greater,
#   equal

pegen = "🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧"
for i in range(0,len(pegen),int(len(pegen)**0.5)):
    print(pegen[i:i+int(len(pegen)**0.5)]+"\n")
print(len(pegen))

'''
Q2:趣味编程小问题

无论你如何定义，成为一名更好的教育工作者的挑战之一，都是对不了解某些事情的恐惧和羞愧。
我们需要变得更有知识，塑造一个学习的姿态并成长。


One of the challenges of becoming a better educator, however you define this, 
is the fear and shame that can come from not knowing something. 
If we call ourselves in and feel safe to say that we need to become more informed, 
we model a learning stance and grow.

请试试python编程所有含ing的单词挑出来
​
'''
s = "One of the challenges of becoming a better educator, however you define this,/
is the fear and shame that can come from not knowing something. \n
If we call ourselves in and feel safe to say that we need to become more informed,
we model a learning stance and grow."