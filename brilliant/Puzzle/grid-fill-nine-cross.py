'''
https://brilliant.org/daily-problems/grid-fill-nine-cross/
'''

flip,target = [1,2,3,4,5],9

def Nine(flip,target):
    total,select = 0,[]
    for i in flip:
        select.append(i)
        total += i
        if total == target:
            return select
    else:
        return total,select
print(Nine(flip,target))


import copy
def Nine(flip,target):
    total,select,dp = 0,[],copy.deepcopy(flip)
    two,three,c,t = [],[],[],target
    for i in flip:
        if t - i in flip and i in flip:
            two.append([i,t-i])
        else:
            t = t - i

            three.append([t,i])
    return two,three
flip,target = [1,2,3,4,5],9
print('Nine-2:',Nine(flip,target))


def Sum2Nine(flip, target):
    total,select = 0,[]
    for i in flip:
        select.append(i)
        total += i
        if total == target:
            return select
    else:
        return total,select
print(Sum2Nine(flip,target))



#1st solution
dp = [0] * len(flip)


class Puzzle:
    def combinationSum9(self, nums, target):
        size = len(nums)
        if size == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target + 1)]

        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这一步要加深体会

        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(size):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp,dp[-1]

puzzle = Puzzle()
nums,target = [2,3,4,5],6
print(puzzle.combinationSum9(nums, target))


#https: // blog.csdn.net / weixin_39029194 / article / details / 104761070


#2nd solution
def comb(arr):
    ans = []
    for i in range(len(arr)-1):
        for j in arr[i+1:]:
            ans.append([arr[i],j])
    return ans
x = [1,2,4,5]
print(comb(x))

for i in flip:
    if i + sum(flip) == 9+9:
        x = [n for n in flip if n != i]
        ans = [k+[i] for k in comb(x) if sum(k)+i == 9]
print(ans)

#3rd solution

def lists_combination(lists, code=''):
    '''输入多个列表组成的列表, 输出其中每个列表所有元素可能的所有排列组合
    code用于分隔每个元素'''
    try:
        import reduce
    except:
        from functools import reduce

    def myfunc(list1, list2):
        return [str(i) + code + str(j) for i in list1 for j in list2]

    return reduce(myfunc, lists)

'''


init()方法有两个方面的重大意义：1. 在对象生命周期中初始化；每个对象必须正确初始化后才能正常工作。2. init()参数值可以有多种形式。

__init__有点像C#中的构造函数，在类实例创建后立即调用。

class Student:
    def __init__(self,number):
        self.number=number 
    def student_number(self):
        print('number:',self.number)
        
student=Student(34)
student.student_number()
1
2
3
4
5
6
7
8
在这里，我们把__init__方法定义为有一个参数number和self，它创建一个新域number，self为指向类本身。这个过程中，通过self.number=number将数据封装在类中，调用时直接时直接通过类Student进行调用。

那么，如果不用__init__()方法定义类会怎么样呢？ geerniya在他的博客对这块内容作了如下解释：

不用__init__()方法定义类
class Student:
    def student_info(self,name,number):
        print('name: {}, number: {}'.format(name,number))
                
student=Student()
student.student_info('zhang',34)
print(student.__dict__)
7
输出结果为

name: zhang, number: 34
{}

虽然不用__init__()方法也能正常实现要求，但查看这个实例的属性竟然是空的。在实例化对象的时候，student=Student()的参数是空的，只有在调用函数的时候才指定，并且类中定义的方法都有参数，明显不是很便捷。

用__init__()方法定义类
class Student:
    def __init__(self,name,number):
        self.name=name
        self.number=number
        
    def student_info(self):
        print('name: {}, number: {}'.format(self.name,self.number))
        
student=Student('zhang',34)
student.student_info()
print(student.__dict__)

输出

name: zhang, number: 34
{‘name’: ‘zhang’, ‘number’: 34}

定义完后，每个实例都有自己的属性（name,number），可以直接调用类中的函数。

init(self,参数）和__init__(self)区别
定义
两种类型的init定义方式如下
class Person:
#     def __init__(self):
#         self.name=None
#         self.gender=None
#         self.age=None
    
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
         
    def print_info(self):
        if str.lower(self.gender)=='female':
            print('Her name is {}, she is {} years old'.format(self.name,self.age))
        elif str.lower(self.gender)=='male':
            print('His name is {}, he is {} years old'.format(self.name,self.age))
        else:
            print('ERROR')
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
前者__init__()方法中只有self，但在方法的类部包含三个属性。而后者在定义方法的时候，直接给定两个参数。
2. 实例化
两者的实例化方法如下：

#person=Person()
#person.name='lisa'
#person.gender='female'
#person.age=18
#person.print_info()

person2=Person('lisi','male',20)
person2.print_info()
1
2
3
4
5
6
7
8
两者的主要区别：
前者定义类可以是一个空结构，当有输入进来的时候再添加相应的数据
后者则必须传值，不予许为空值，例如

person2=Person()
person2.print_info()
1
2
输出将会报错

TypeError: init() missing 3 required positional arguments: ‘name’, ‘gender’, and ‘age’

相关博客和学习网站
[1] 廖雪峰官网https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408
[2]详细解读Python中的__init__()方法https://www.cnblogs.com/insane-Mr-Li/p/9758776.html
[3] python学习——类中为什么要定义__init__()方法.https://blog.csdn.net/geerniya/article/details/77487941
[4]python def init(self, name等多参数), def init(self)https://blog.csdn.net/m0_37693335/article/details/82972925
'''