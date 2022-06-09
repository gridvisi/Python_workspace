'''

upper()：所有字母大写

lower()：所有字母小写

capitalize()：首字母大写，其他字母小写

title()：每个单词首字母大写，其他小写


# try-except
while True:
    try:
        print(1/0)
    except ZeroDivisionError:
        print("恁除错了！")
'''


students = ['phil','jack','luigi','hongyu','dingdingmao']
students_age = ['9','10','11','12','8']
students_ages = ['9','10','11','12','8']
students_age = [int(i) for i in students_ages] #integer
print('字符串转整数：',students_age)
print('string:',students_ages)
print('average:',sum(students_age)//len(students_age))
print(5/4, 5//4)
#
#string
#str()
#print([students[-i] for i in range(len(students),0,1)])

students.append('waixingren')
students = []
students.append('teacher li')
for i in students:
    print('forloop:','Good afternoon ' + i)


#1st slice:

# 函数
def huiwen(guest):
    return [guest[-1]+ guest[total - 2],total-3]

def greet(person):  #
    return "Good afternoon " + person
teacher = 'eric'
print(greet(teacher))



def daxieCap(c):
    #c = list(c)
    #c[0].uppercase()
    return c.capitalize()
c = 'hongyu'
print('daxie',daxieCap(c))

for person in students:
    print(greet(person.upper()))
    print(greet(person.capitalize()))


Phil = input("Rock")
Jack = input("Paper")
def caiquan(Phil,Jack="Paper"):
    rules = {'win':()}
    if Phil == "Rock" and Jack == "Paper":
        return 'Jack win Jack'

    return 'Phil win Jack'





s = ""  #string  object
a = 123
print(str(a)[0])
print(list(str(a)))



def appleNum(x):
    return x

total = 0
for day in range(11):
    print(total)
    total += appleNum(day)
print('10',total)

def appleNum(x):  # 10th days
    return x + 1
x = 1
print(appleNum(x))


#focus on


'''
今天思考任务：

体育课面向老师，有17个同学从左到右按身高低到高顺序站一排。
老师命令身高从高到低排，并且每个同学记住，
左数第一个同学是编号1，开始数到自己的位置的编号数字​。
phil发现自己的位置编号数字没有变化，

1、请问phil同学站的位置？

2、展开讨论，是否总是存在同学，编号不变？

先用数学解法：从略见课堂讨论

再用编程解法：

有奇数个元素的数组，当数组倒序，是否总存在某个元素，数组位置不变？

'''


