#Suppose that we have the following two lists.
names = ["John", "Mike", "Sandra", "Jennifer","eric","tom","cathy","mike"]
customer = [1,2,3,4,5,6,7,8]

person,order = iter(names),iter([i for i in range(len(names))])
for call_pair in zip(order,person):
    print(call_pair)
'''
print(next(g),names[g])
print(next(g))
print(next(g))
print(next(g))
'''
def line_up_call(n,names):
    i = 0
    while i <= n:
        yield i,names[i]

        i += 1
n = len(names)         # 注意n不是列表，是整数
print("line_UP_CALL:")
line = line_up_call(n,names)
print(next(line))
print(next(line))
print(next(line))
print(next(line))

def line_up_call(names):
    i = 0
    while i <= len(names):
        yield names[i]
        i += 1

line = line_up_call(names)
print('names[]:',next(line))
print('names[]:',next(line))
print('names[]:',next(line))
print('names[]:',next(line))

names = ["John", "Mike", "Sandra", "Jennifer"]
ids = [1, 3, 2, 4]
#Using the zip() function, we can conveniently use the information from both lists. Again, as before, you can always directly access the tuple’s items if you assign variable names to them, like for name, id in zip(names, ids).
for student in zip(names, ids):
    print(student)
'''
('John', 1)
('Mike', 3)
('Sandra', 2)
('Jennifer', 4)
Conclusions
'''


def generator():
    while True:
        for char in lines:
            yield char
string = "hello"
lines = ["John", "Mike", "Sandra", "Jennifer","eric","tom","cathy","mike"]
print(next(generator()))
print(next(generator()))
print(next(generator()))

lines = ["John", "Mike", "Sandra", "Jennifer","eric","tom","cathy","mike"]
def make_looper(lines):
    def generator():
        while True:
            for char in lines:
                yield char
    return next(generator())   #.next

p = make_looper(lines)
print(p)
print(p)

