'''
你已经解锁了一项新的特权!
你的主宰之路还在继续。你已经证明了自己是一个非常值得尊敬的战士。当把一个测试版卡塔标记为 "准备好了 "时，你的票数现在价值3倍！

不要让这么多的力量白白浪费了! 前往测试区，帮助我们找到下一个伟大的卡塔。
You have unlocked a new privilege!
Your path to mastery continues. You have proven yourself to be a highly honorable warrior. When marking a beta kata as "ready", your vote is now worth 3 times as much!

Don't let this much power go to waste! Head over to the beta section and help us find the next great kata.




选择题，部分有答案提示

1、在Python中，一个变量必须在被赋值之前被声明？

不正确
正确

*在Python中，变量不需要事先声明或定义。要创建一个变量，你只需给它一个值。

2、在Python中，以下哪条语句为变量x赋值为100
x = 100
x ← 100
let x = 100
x := 100
x << 100



3、Python中变量被分配一个类型的值，然后可以再分配一个不同类型的值。
不正确
正确

*注释：在Python中，变量不是静态类型的，就像其他一些编程语言中一样。

4、考虑下面的语句序列
n = 300
m = n

执行这些语句后，Python创建了多少个对象和多少个引用？
一个对象，一个引用
两个对象，两个引用
一个对象，两个引用
两个对象，一个引用

*第一个语句创建了一个值为300的整数对象，n是它的一个引用。第二条语句为已经存在的对象创建第二个引用。

5、哪个Python内置函数返回分配给一个对象的唯一数字？
refnum()
ref()
identity()
id()

知识点：*如果两个变量的id()相同，你就知道它们引用的是同一个对象。

>>> n = 300

>>> m = n

>>> id(m)

52132448

>>> id(n)

52132448


6、下面哪些是有效的Python变量名？
4square
route66
return
ver1.3
Age
Correct
home_address

知识点：
4square是无效的，因为它以数字开头。
return是无效的，因为它是一个Python保留字（关键字）。
version1.3是无效的，因为它包含一个不是字母、数字或下划线的字符。

7、你正在阅读Python代码，这些语句散布在代码的不同位置。
employeenumber = 4398
EmployeeNumber = 4398
employeeNumber = 4398

这些语句指的是不同的变量。
在Python变量名中，大小写是很重要的，所以这些都是不同的变量。这样做的人是在自找麻烦。


8、PEP8为多字变量名推荐了以下哪种风格？
distance_to_nearest_town (Snake Case)
distanceToNearestTown (Pascal Case)
distanceToNearestTown (Camel Case)


9、下面哪些是Python的保留词(关键词)？

default
None
goto
and
class

 完成测验并检查你的结果

'''


#10、找出下列同学成绩最高的同学，请补齐代码？
score = {'ada' : 97, 'ben': 90, 'cindy': 99, 'dios': 93}
print([k for k,v in score.items() if v == max(score.values())])


#编程任务：

#10、找出下列同学成绩最高的同学，请补齐代码？
score = [97,90,99,93]
#请运用函数或其他办法找到分数最高是多少分？

#10-2 以上分数对应的同学分别用字典表达如下：
scores = {'ada' : 97, 'ben': 90, 'cindy': 99, 'dios': 93}
#如何实现输出分数最高和最低的同学名字？


#10-3 按照分数高到低排列，输出结果
#如何运用python内置的函数实现？


#11、小明每3天买一杯饮料，饮料每杯5元。一年按365天计算，小明总共要买多少钱的饮料？
#提示：除法、循环、切片三种方法实现，比较结果


#12、Phil帮助数学老师计算同学的python测验成绩的平均分数，分别用sum函数，和自己定义求总和函数两种方法试试看可以吗？
scores = [98, 89,93,99,90,93]
#方法一：sum()
#请写出求和并且算平均的代码
print('sum:',sum(scores))

#方法二：不使用sum，自己定义函数和算法
#第1步：先定义加法函数

def add(x,y):
    return x + y

#第二步：将前n个同学的分数的总数，再加上第n+1个同学的分数

sub = 0
for c in scores:
    #sub = sub + add(sub,c)
    #sub = add(sub, c)
    #x,sub = c,sub+c
print('add:',sub)


#13、python turtle绘制一面五星红旗