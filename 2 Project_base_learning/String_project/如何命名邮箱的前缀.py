'''

任务课题：
注册邮箱的项目任务学习完整过程

任务说明：
注册电子邮件地址，需要哪些信息？
回忆李老师帮助同学注册邮箱的时，
为了每个同学容易记住邮箱地址，采用了哪些策略：

1、邮箱的命名以同学的汉语拼音的首字母为主
2、有重名的可能时，怎么解决？例如姓名的全拼作为邮箱地址前缀；

解释名词：
前缀就是@之前的部分如：
"李铮杰"同学的地址是 lzj@gridvisi.com
李铮杰同学的姓名全拼为：lizhengjie
注意思考再深入一些，上面的拼写的字符串无法区分开姓和名
你就需要考虑字符串的格式加入空格：li  zheng  jie，这样运用
python的字符串操作顺利分割开，现在你运用学过的split命令
顺利将分割为3个字符串："li" , "zhen”，“gjie", 并且取三个字符串
的首字母：lzj，作为电子邮箱的前缀。


接着思考并找到下列问题中，你认为有效的思路和方法：

Q1st: 同学思考采用lizhengjie还是lzj，各有什么优缺点？

Q2nd: 校长委托你帮助他，顺利完成全校同学的邮箱注册，
你需要写一个行动计划完成任务。提示你需要考虑：
A、需要学校提供哪些信息才能顺利完成？如姓名
B、需要如何处理给你的信息？中文可以直接注册吗等
C、如何判断你正确完成了任务？邮箱可以用吗？

Q3rd：现在你已经拿到了若干同学的姓名
试着完成自己的邮箱前缀，并且编写循环算法，批量完成所有同学的邮箱前缀的命名！

任务总结：
你会发现一个任务从理解需求开始，接着理顺思路，最后才是依据思路写出代码切分字符串，
并且比较几种方案找到高效的做法实现姓和名的首字母拼接为电子邮件的前缀。

到此为止，恭喜你已经掌握邮箱注册命名的常见思路，甚至运用python批量处理的注册！
未来继续该任务的学习，讨论如何生成安全性高的密码！

课外作业：
现在尝试提交题库链接见👇
你会发现题库的任务是从Q3rd，第三步开始的
但真实的任务需要你首先独立完成前面两步Q1st和Q2nd

7 kyuReturn String of First Characters
https://www.codewars.com/kata/5639bdcef2f9b06ce800005b/train/python

```
代码块
``
'''
#1st first : name = "李铮杰"@qq.com
#2nd second: "lizhengjie" 字符串
#print("lizhengjie".split("")) #输出打印
# split 分开
#
print("li zheng jie".split(" "))
# split bill AA制
# 17 rmb

print(round(17/2,2))

def prefix(name): #name str格式的字符串
    # 首先姓名切分为若干个字符串，三个字的名字，复姓，
    # 或者四字姓名
    # 提前要求按照录入汉语拼音的时候需要姓和名用空格  分开
    # surname，family name都是指姓
    # first name，given name都是指名
    sur,given,given_2 = name.split(" ")
    return sur[0] + given[0] + given_2[0]
name = "li sheng jie"
# not enough values to unpack (expected 3, got 2)

print('1st step:',prefix(name))

name = "li zheng jie"
print(prefix(name))


# 写法二 进阶
def prefix(name): #name str格式的字符串
    # 首先姓名切分为若干个字符串，三个字的名字，复姓，或者四字姓名
    # 提前要求按照录入汉语拼音的时候需要姓和名用空格  分开
    # prefixshort变量存储首字母,
    # prefixlong变量存储姓名全拼,
    prefixshort,prefixlong = "",""
    for c in name.split(" "):
        print('c:',c)
        prefixshort += c[0]
        prefixlong += c
    return prefixlong,prefixshort
name = "li zheng jie"
print('upgrade:',prefix(name))

name = "li zheng jie"
print(prefix(name))

# 7 * 40 - 40
print(7 * 40 - 50)

def prices(d):  #define d=day:tian
    # 3 days

    if 1 < d < 3:
        return d * 40  #return 交作业
    if 3 <= d <= 7:
        return d * 40 - 20

# https://www.codewars.com/kata/5639bdcef2f9b06ce800005b/train/python

def rental_car_cost(d):
    # your code
    return result
d = 17
print(rental_car_cost(d))