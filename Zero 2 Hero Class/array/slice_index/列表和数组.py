# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python
'''
Wolves have been reintroduced to Great Britain.
You are a sheep farmer, and are now plagued by
wolves which pretend to be sheep. Fortunately,
you are good at spotting them.

Warn the sheep in front of the wolf that it is
about to be eaten. Remember that you are standing
at the front of the queue which is at the end of
the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1
If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
Note: there will always be exactly one wolf in the array.

Tags:

FUNDAMENTALS ARRAYS LOOPS CONTROLFLOW BASIC LANGUAGE FEATURES

Examples
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
'''
sheeps = ['sheep', 'wolf', 'pig','sheep', 'sheep', 'sheep', 'sheep', 'sheep']
print(sheeps.index('wolf'))
print(f"Oi! Sheep number {sheeps.index('wolf')+1}! You are about to be eaten by a wolf!")

print(sheeps[sheeps.index('wolf') + 1])

bag = ['pen','key',10] #list
print(bag.index('pen'))

sheeps = ['羊','羊','羊','羊','羊','羊','狼','羊','羊'] #列表
print(sheeps.index('狼'))

students_age = ['12','11',14]
# 字符串
# 整数

print('12' == 12)
#print('12' - 12)

#True or False
print(2 - 1 == 1)

print('hello world' == '你好，世界')

x = [1,0,0,1,2,3,4,'',True,False]
print('True.index:',x.index(True))
# Because True == 1
print(True == 1)

print('x have several items:',len(x)) #length

for i in range(len(x)):
    if x[i] == 4:
        print('x中等于4的元素位置是：',i)

print(x.index(3))
#print(x.index(4,True,False))


x = '王君梓竹 丁丁猫  李大喵'
print(x[0:3])
i = x.index('丁')
print(x[i:i+3])






print(x[0],x[i])
print(x[0:4] + x[9:13])
print(x[1:14:2])
x = 'we are a dingdingmao coding camp'
l = len(x)
print(x[0],x[0:l:3])

for i in range(len(x)):
    if x[i] == 4:
        print('x中等于4的元素位置是：',i)