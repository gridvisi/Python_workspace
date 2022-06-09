'''
The Python programming language provides input() function to take input into a program from console.
input()
The simplest way to take input is using the input() function
which first takes the input from the user, then evaluates the
expression and finally converts the entered value into the
string format (irrespective of format or type of entered value).
The input() method accepts a string message which is an optional
and meant to be displayed on the output console to ask a user to
enter input value. Let’s have a look at the syntax

Python编程语言提供了input()函数，用于从控制台获取输入到程序中。
输入()
最简单的接受输入的方法是使用input()函数，它首先接受用户的输入，
然后对表达式进行评估，最后将输入的值转换成字符串格式（不论输入值的格式和类型）。
input()方法接受一个字符串消息，这个消息是一个可选的，旨在显示在输出控制台，
以要求用户输入值。让我们来看看其语法吧
'''

num = input ("Enter number :")
print('number entered is : ', num)

# printing two numbers at a time
a=7
b=9
print(a, b)

print("Integer : % 2d, Float : % 5.2f" %(1, 05.333))

print('Male', 'Female', sep='/') #will print both Male and Female separated by ‘/’

#for formatting a date
print('09','12','2018', sep='-')

# ends the output with a <space>
print("Welcome to" , end = ' ')
print("Python Progamming Course", end = ' ')

# Code for printing to a filed
welcomeFile = open("d:/welcome.txt", 'w')
print('python course', file=welcomeFile)
welcomeFile.close()



# print integer and float value
print("Integer : % 2d, Float : % 5.2f" %(1, 05.333))

'''
Use “%d” for integer value and “%f” for float value. In the above example “%2d” is 
used for the integer 1. The prefix ‘2” signifies that the number will be printed 
with 1 leading blank character as integer value 1 consists only of one digit. 
The second one “%5.2f” is a format description for a float number. 
the number following the “.” in our placeholder signifies the 
decimal part of the number or the precision, character “f” of our placeholder stands for “float”
'''

# using format() method and referring a position of the object
print("{1} {0} {1}".format("hello", "world"))# 输出结果为“'world hello world”。

print('{0} {1} {2}'.format('Python', 'Programming', 'Course'))
mobile_phone = '13701183019'
#print('{0}-{1}-{2}'.format(mobile_phone))

# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)


print('Male', 'Female', sep='/') #will print both Male and Female separated by ‘/’

print('09','12','2018', sep='-')
print("Welcome to" , end = ' ')
print("Python Progamming Course", end = ' ')
