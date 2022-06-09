'''


完成你的选择后，建议拷贝代码测试运行一下，验证你的选择！

如果代码不熟悉，可以讲述自己的思路！

一、一个整数n, 如何知道n是几位数？

例如：100，999都是3位数；10，90都是2位数
下面的选项哪些是可以正确完成任务？

1）  len(n)
2)  len(str(n))
3)  小明运用数学课的知识，想出用while循环实现如下：n是需要判断的整数
'''

print('2的幂函数：',2**4)


n = 1999 #-> '1999'
strn = str(n)
print(type(n),type(strn)) #type命令测试变量的类型
#int 整数； 字符串

name = "lizhenjie" #name 'lizhenjie' is not defined
print([name,10,name * 2])

lzj = [name,10,name * 2]
lzj.append('3年级')
print('输出第2个：',lzj[3])

print(len(lzj))

print(2 ** 4)
nane = "lizhengjie"
print([nane,10,nane * 2])
print('lzj:',len(nane))

n = 199
print('判断几位数：',len(str(n)))
#1 n转换为字符串
#2 判断字符串长度

#print(len(n)) #object of type 'int' has no len()

# 1999 // 10 = 199
# 199 // 10 = 19
# 19// 10 = 1
# 1// 10 = 0

def cuntDigit(n):
    cunt = 0
    while n > 0:
        #n //= 10
        n = n // 10
        cunt +=1
    return cunt

'''

二、你是丁丁猫的学员，你定义一个函数，
   输入同学的名字***，输出："***同学是python学员"
'''
print(f"{n} 同学是python学员")

def ddm(name):
    return f"{name} 同学是python学员"




'''

三、某人的名字是"张三丰”，请你运用切片操作，输出：姓，名
输出格式是："姓：张，名：三丰"
函数的格式：

'''
def xingmin(name,age):

    return f"姓：{name[0]}, 名：{name[1:]}, 年龄:{age}"  #"此处补齐代码"

name,age = "刘致远",10
print(xingmin(name,age))


#都说人生第一行代码是:hello,world
# 丁丁猫的大喵说，平时见面招呼是这样的:
# Hi There are 4 coders code in Python.
# 有四个编程人写的代码，哪个是对的？
# Which is right?
# 1)Print("Hi")
# 2)print(Hi)
# 3)print ("Hi")
# 4)print("Hi")


my_name = input('name:')
x = int(input("年龄 的值是多少:"))
y = int(input("3 years after:"))
age = x + y
print(x + y,age)
# 括号内有一个字符串，作用是提示你输入的值将赋给等号左边的变量

name,age = "lzj",10
# lzj is 10 years old #
# lzj 是 10 岁