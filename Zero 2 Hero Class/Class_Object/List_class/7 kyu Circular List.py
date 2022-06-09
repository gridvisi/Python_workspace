'''
https://www.codewars.com/kata/5b2e60742ae7543f9d00005d/train/python

Create a Circular List

A circular list is of finite size, but can infititely be asked for its previous and
next elements. This is because it acts like it is joined at the ends and loops around.

For example, imagine a CircularList of [1, 2, 3, 4]. Five invocations of next() in
a row should return 1, 2, 3, 4 and then 1 again. At this point, five invocations of
prev() in a row should return 4, 3, 2, 1 and then 4 again.

Your CircularList is created by passing a vargargs parameter in,
e.g. new CircularList(1, 2, 3). Your list constructor/init code should throw an
Exception if nothing is passed in.
'''


class CircularList():

    def __init__(self, *args):
        if not args:
            raise Exception("missing required args")
        self.i = -1
        self.args = args

    def next(self):
        if self.i == -1:
            self.i = 0
            return self.args[self.i]

        elif self.i == len(self.args) - 1:
            self.i = 0
            return self.args[self.i]
        else:
            self.i += 1
        return self.args[self.i]

    # your code

    def prev(self):
        if self.i == -1:
            self.i = len(self.args) - 1
            return self.args[self.i]

        elif self.i == 0:
            self.i = len(self.args) - 1
            return self.args[self.i]

        else:
            self.i -= 1
        return self.args[self.i]
# your code
l = [1,2,3,4,5]
#l = "one", "two", "three"
week = ['Mon','Tue','Wed','Thr','Fri','Sat','Sun']
ls = CircularList(week)
ls.args = week
print(ls.next())
print(ls.next())
print(ls.next())
print(ls.next())
print(ls.next())
print(ls.next())
print(ls.next())
print(ls.next())

print("----------------------------")
l = [1,2,3,4,5]
for _ in range(19):
    print(ls.prev()) #,

print(ls.next())


#1st
class CircularList():
    def __init__(self, *args):
        if not args:
            raise Exception("missing required args")
        self.n = len(args)
        self.lst = args
        self.i = None

    def next(self):
        if self.i is None:
            self.i = -1
        self.i = (self.i + 1) % self.n
        return self.lst[self.i]

    def prev(self):
        if self.i is None:
            self.i = 0
        self.i = (self.i - 1) % self.n
        return self.lst[self.i]


# basic for class usage
class Human():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak_name(self):  # 自已要说出名字
        return f"Yes, I am {self.name}"

phil = Human("lihongfei", "Male")
print(phil.name)
print(phil.gender)
phil.speak_name()


# basic for class usage extend
class Human():
    def __init__(self, name, gender, course):
        self.name = name
        self.gender = gender
        self.course = course

    def report(self):  #计算平均分和总分
        total = sum(self.course)
        p = self.course
        return f"语文:{p[0]} 数学:{p[1]} 英语:{p[2]} total：{total},average:{total//len(self.course)}"

Phil = Human('phil','male',[99,100,97])
Alex = Human('alex','male',[90,96,92])

print(Phil.report())
print(Alex.report())
'''
phil.name = 'phil'
phil.gender = 'male'
phil.course = [99,100,97]
'''
