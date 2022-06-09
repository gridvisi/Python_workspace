'''
https://blog.csdn.net/I_love_you_dandan/article/details/102901472?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.channel_param
文章目录
博客说明：
基础知识
   001.Hello,World
Python2.7能够正常输出py2、py3
Python3.7无法正常输出py2，版本不兼容
  002.CircularStatement
简单for循环之range示范
简单for循环之输出列表
简单for循环之字符串
自定义foreach循环之输出元祖
自定义foreach循环之输出字典
   003.ConditionalStatement
条件语句，以及质数筛法
Python数组类型的说明符
   004.range
range(start, stop[, step])
面试问题：一行代码求和[0,100],并输出结果
   005.lambda
lambda
map
filter
reduce
sum
   006.random
   007.time
   008.re
raw string 原生字符串
re.match(pattern, string, flags=0)
强化理解一：贪心模式与懒惰模式
强化理解二：实例补充
视野拓展：查看官方的开发文档
re.search(pattern, string, flags=0)
re.sub(pattern, repl, string, count=0, flags=0)
re.subn(pattern, repl, string, count=0, flags=0)
re.compile(pattern[, flags])
re.escape(string)
findall(pattern, string, flags=0)
强化理解之优先级问题
re.finditer(pattern, string, flags=0)
re.split(pattern, string[, maxsplit=0, flags=0])
re模式
贪婪模式与惰性匹配
group(s)
常见字符类
正则表达的常见应用（模型）
   009.(not) in
   010.is
   011.stack
   012.queue
   013.列表生成式
面试问题：FizzBuzz数列
   014.package
   015.搜索算法
find
BFS（广度优先）
DFS（深度优先）
   016.最短路径
   017.矩阵
   018.排序
   019.查找
   020.eval
eval()与str()
   021.待定
模板代码
   001.ProgrammingParadigm
范式编程（函数式编程）
   002.Object-Oriented Programming
OOP面向对象编程
Python中，类即对象；对比JavaScript；以及原始印象中的C++的类与对象
   003.待定
项目实战
   001.Python绘图
   002.文件操作
CSV文件
注意事项：py文件名不能起成“csv”
   004.数据清洗 (字符串操作）
正则表达式
字符串截取
字符串替换
字符串查找
字符串分割
字符串生成所有非空子串
   005.Beautiful Soup
实例运行结果（内嵌HTML字符串）
强化理解（处理绝对路径或同目录下的Html文件）
   006.requests爬取网页
   007.爬虫框架爬取网页
Scrapy
   008.selenuim+无界浏览器
   008.待定

'''
#001.Hello,World
print("Hello,World!")
print("Hi,Python2!")

print ("Hello,World!")
print ("Hi,Python3!")

#python2.7可以输出python3版本，但反过来不行
#002.CircularStatement
for i in range(10):
    print(i,"Hello,For Circular.")

#简单for循环之range示范
#   列表单、双引号都可以使用
cities = ['北京','上海',"广州","深圳"]
for eachCity in cities:
    print (eachCity)

#
# 直接通过迭代器遍历元素
py = "python"
for character in py:
    print(character)

print()#默认会输出空行

# 通过列表的索引遍历元素
print('通过列表的索引遍历元素')
for i in range(len(py)):
    print(i,py[i])

print("\nlen(py)=",len(py))

#通过列表的索引遍历元素


# 直接通过迭代器遍历元素
py = "python"
for character in py:
    print(character)

print()#默认会输出空行

# 通过列表的索引遍历元素
for i in range(len(py)):
    print(i,py[i])

print("\nlen(py)=",len(py))

# 简单foreach循环，需要Python3
def foreach(function, iterator):
    for item in iterator:
        function(item)
    return
def printItself(it):
    print(it,end=" ")
    return
# 在这里，试着比较直接使用print与使用printItself的效果

my_tuple = (1, 2, 3, [4, 5], 6)
my_dictionary = {"Apple": "Red",
                 "Banana": "Yellow",
                 "Pear": "Green"
             }
foreach(printItself, my_tuple)
    # 1 2 3 [4, 5] 6 #注释行为对应的输出结果，下同
print()
foreach(print, my_tuple)
    # 1
    # 2
    # 3
    # [4, 5]
    # 6
foreach(print, range(len(my_tuple)))
    # 0
    # 1
    # 2
    # 3
    # 4
print()

foreach(print, my_dictionary)
foreach(print, my_dictionary.keys())
    # 上二个语句等价，输出相同
    # Apple
    # Banana
    # Pear
foreach(print, my_dictionary.values())
    # Red
    # Yellow
    # Green
print()

print(my_dictionary)
    # {'Apple': 'Red', 'Banana': 'Yellow', 'Pear': 'Green'}
print(my_dictionary.keys())
    # dict_keys(['Apple', 'Banana', 'Pear'])
print(my_dictionary.values())
    # dict_values(['Red', 'Yellow', 'Green'])
print()

foreach(printItself, range(len(my_dictionary)))
    # 0 1 2
print()
foreach(printItself,my_dictionary.keys())
    # Apple Banana Pear
print()
foreach(printItself,my_dictionary.values())
    # Red Yellow Green
print("\n")

foreach(print,my_dictionary)
print()
foreach(print,my_dictionary.keys())
    # 上二个语句等价，输出相同
    # Apple
    # Banana
    # Pear
print()
foreach(print,my_dictionary.values())
    # Red
    # Yellow
    # Green
print()
for item in my_dictionary.items():
    print(item)
    # ('Apple', 'Red')
    # ('Banana', 'Yellow')
    # ('Pear', 'Green')
for it in my_dictionary:
    print(it,":",my_dictionary[it])
    # Apple: Red
    # Banana: Yellow
    # Pear: Green
    # 值得说明的是：dict[key]=value（讲究与之对应），当key值为数值时还可以采用以下途径
for i in range(len(my_dictionary)):
    print(i)
    # print(my_dictionary[i])#key值不是数值时，找不到对应项会报错
    # 0
    # 1
    # 2

print('-------------------Python数组类型的说明符-----------------')
#range

# range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(5,10)
# [5, 6, 7, 8, 9]
# range(0,10,3)
# [0, 3, 6, 9]
# range(1,10,3)
# [1, 4, 7]
# range(1,10,10)
# [1,]

# range(1,10,-2)
# [1,]
# range(2,-10,-1)
# [2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
# range(-2,-10,-1)
# [-2,-3,-4,-5,-6,-7,-8,-9]

# range(2,10,-1)、range(-2,10,-1)、range(2,-10,1)
#   以上三个容器都为空

# 语法 range(start, stop[, step])
# range(a,b,c)
# a不写时默认为0，从a开始；生成到b(故通常b>=a);c为步距
# range 默认生成正数方向，若a>b即b<a时将会往左生成负数，步距c也应要改为负数
# 即 不要求start和stop有什么直接的大小关系

# 测试
for i in range(10):
    print(i,end=" ")
print()
'''
range(start, stop[, step])
实例运行结果

print(sum(range(1,101)))
1
面试问题：一行代码求和[0,100],并输出结果

'''