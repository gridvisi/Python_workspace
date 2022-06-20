'''
第一题 题目：编程计算表达式1＋3＋9＋27＋…＋2187的值。

s=0
i=1(3分)
while i<=2187:
    s=s+i(3分)
    i=i*3(4分)
print('表达式的值是：',s,)
print('最后一个加数的值是',i/3)
解析：累加题(第二个空)，从1(第一个空)开始到2187结束，每个数字都是前一个数字*3(第三个空)。
'''


'''
第二题 题目：判断是否为质数 用户输入2~99(包含2和99)之间的任一数字，程序判断输出这个数是否为质数。

n=eval(input('请输入2-99之间的任意整数：'))

f=True
for i in range(2,n): (3分)
    if n/i==n//i: (3分)
        print(n,'不是质数。')
        f=False
        break(4分)
if f :   
    print(n,'是质数。')

解析：质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。判断一个数n是不是质数，那用n除以2~n-1之间的数字(第一个空)，没有能整除的(第二个空)，如果2~n-1之间有能整除的，那就不是质数，跳出循环(第三个空)。
'''


'''
第三题题目：判断单词“python”是否在文章中。提示输入一个字符串；(提示为：请输入一个字符串：)根据输入的字符串，
程序会输出”Python”出现的次数。例如：如果输入的字符串为"Python是一种简单的编程语言。Python特别受欢迎。”

str = input("请输入一个字符串：")
count = 0
for i in range(len(str)-1): (3分)
if str[i:i+6] == "Python":  (3分) 
count = count + 1(4分)
print("Python出现的次数是：",count)

解析：这里用到了字符串的切片。定义一个计数器，也就是count=0，遍历整个字符串(第一个空)，
从i开始取i+6个字符str[i:i+6]，如果等于python(第二个空)，则计数器加1(第三个空).

'''


'''
第四题 ba0728af254c5ab5866ebfa432b73420.png
题目：这次作文大赛，获得一等奖的同学有：“小张，小王，小强，小李，小周，小芳，小兰”。请编程实现，
输入某个同学的名字进行查找，是否在一等奖的同学名单里。

l=['小张','小王','小强','小李','小周','小芳','小兰'] (3分)
s=input('请输入获一等奖选手姓名：') (3分)
if s in l: (4分)
    print(s,'同学获得一等奖！')
else:
    print(s,'同学没有获得一等奖！')
解析：这个题是序列的查找。首先初始化一个同学的序列，可以用List，元组，集合等(第一个空)，题目答案
用的List，List初始化用中括号，字符串用引号括起来。接着输入某个同学的名字，输入用input，input里
有一个字符串，可以友好提示。最后遍历列表，用for...in来遍历(第三个空)。
'''

'''
years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years

def isLeapYear(year):    
    return year%100 != 0 and year%4 == 0 or year%400 == 0

第五题 题目：判断闰年 用户可多次输入一个年份，每次输入年份，如果这个年份是闰年，则打印“是闰年”，
否则打印“不是闰年”。判断方法：普通年能被4 整除且不能被100 整除的为闰年。
(如2004 年就是闰年，2005 年不是闰年。)
世纪年要能被400 整除才是闰年。(如2000 年是闰年，1900 年不是闰年。)

while True:
   year =eval( input("请输入年份。结束程序请输入-1"))
   if year == -1:
      break

   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0: (3分)
            print("是闰年")
         else:
            print("不是闰年")
      else:
         print("是闰年")  #填是否闰年(3分)

   else:
      print("不是闰年")  #填是否闰年(4分)

解析：考核闰年的算法。能够被4整除但不能被100整除的年份为普通闰年(第二个空)，能被400整除的为世纪闰年(第一个空)。
不能被4整除，不是闰年。(第三个空)
'''

'''
第六题 题目：数字转扑克牌 用户输入1~13(包含1和13)之间的任一数字，程序输出对应的扑克牌。
如输入1，程序输出“A”；输入11，程序输出“J”。

a=eval(input('请输入1-13之间的任意整数：'))

s='A2345678910JQK'
if a==10:
    m=s[9:11] (3分)

elif a>10:
    m=s[a] (3分)

else:
    m=s[a-1] (4分)
print(a,'对应的扑克牌为：',m)

解析：扑克牌定义成了一个字符串，除10之外的扑克都是一个字符，10是两个字符，所以对10特殊处理，
用到了字符串的切片(第一个空)；如果小于10，因为从0开始的，返回的结果是输入的数字减1所在位置的
字符(第三个空)，如果大于10，因为10多占了一位，所以返回就是输入的数字所在位置的字符。(第二个空)
'''

'''
第七题 题目：快递的计费规则如下：5千克以内(含)，20元；以后每增加一千克，计费增加5元；
总价超过200元，打85折。请编程输入重量，输出费用。

t=eval(input('请输入快递物品的重量：'))
if t<=5:
    p=20(3分)
else:
    p=(t-5)*5+20(3分)
if p>200:
    p=p*0.85(4分)
print('本快递需要付费',p,'元')

解析：5千克以内(含)，20元，也就是<=5，p=20(第一个空)；每增加1千克，增加5元，t-5是增加的千克数量，
(t-5)*5是每增加1千克，增加5元。所以，p=(t-5)*5+20(第二个空)。超过200，打85折。如果p>200，85折
是乘以0.85,p=p*0.85(第三个空)。
'''

'''
第八题 题目：猜数游戏 小明的实际年龄是11岁，让用户来猜，猜错时，会提示猜的年龄是大了还是小了，直到用户猜对为止。

m=11      
f=True
while f:
    n=eval(input('请猜小明的年龄：'))
    if n>m: (3分)
        print('猜大了！')

    elif n: (3分)
        print('猜小了！')

    else:
        print('恭喜！猜中了！')
        f=False(4分)

解析：m=11表示实际年龄，f=True，表示一直循环，当猜对的时候，跳出循环，此时要设置f=False(第三个空)。
如果输入的年龄比实际年龄大，说猜大了(第一个空)；如果输入的年龄比实际年龄小，说猜小了(第二个空)。
'''

'''
第九题 题目：输入任意一段字符串，找出重复次数最多的字符，并统计这个字符的重复次数。

n=input('请输入任意字符串：')
x=1
for i in range(0,len(n)):
    t=n.count(n[i]) (3分)
    if t>x:
        x=t(3分)
        k=i(4分)

print('重复次数最多的是：',n[k],'重复了',x,'次')
解析：count是计算某个子串的个数。遍历整个字符串，计算每一个字符的个数，x存储的是重复次数
最多的字符的重复次数，先初始化为1，如果遍历过程中，字符的重复次数大于这个数，则把重复次数
和字符的位置记录下来，k记录的是字符的位置。
'''

'''
第十题 题目：设有6位评委的打分是10,8,9,9,8,6，运用Python语言编程实现：
去掉一个最高分，去掉一个最低分，计算平均分，并打印出来。

l=[10,8,9,9,8,6]
mx=max(l)
mn=min(l)
l.remove(mx) (3分)
l.remove(mn) (3分)
s=sum(l)/len(l) (4分)
print(s)

解析：先用max取出最高分，用min取出最低分，去掉列表中的元素用remove，所以用remove(mx),remove(mn)
去掉最高分和最低分，最后计算平均分，平均分是用总分除以个数，sum来计算总分，len来计算个数。

电子学会Python二级知识点，主要是复杂的数据结构：列表、元组、字符串、字典。以及三种控制结构：顺序、
条件(if/else/elif)、循环(for/while/break/continue)的使用。
'''



#36 日期转换
'''
写一个程序，实现用户输入一个日期，格式为"月/日/年"，
如输入       '05/21/2021'，
程序输出日期为'May 21,2021'
1至12月的英文名称如下：
January，February，March，April，May，June，July，
August，September，October，November，December

题型：编程题
答案：
'''
month = "January，February，March，April，May，June，July，" \
        "August，September，October，November，December"
month = month.split("，")
print(month)
num = ['0'+str(i) if i < 10 else str(i) for i in range(1,13)]
num2month = dict(zip(num,month))
print(num2month)

def convert(inp): #->str
    month = "January，February，March，April，May，June，July，" \
            "August，September，October，November，December"
    month = month.split("，")
    print(month)
    num = ['0' + str(i) if i < 10 else str(i) for i in range(1, 13)]
    num2month = dict(zip(num, month))
    inps = inp.split("/")
    print('inps:',inps)
    return num2month[inps[0]] +" "+ ','.join(inps[1:])
inp = '05/21/2021' #'May 21,2021'
print(convert(inp))