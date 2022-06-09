# https://realpython.com/quizzes/python-variables/viewer/

n = 300
m = n
id(n)
#60127840
id(m)
#60127840

m = 400
id(m)
#60127872

'''
Reserved Words (Keywords)
There is one more restriction on identifier names. 
The Python language reserves a small set of keywords that designate special 
language functionality. No object can have the same name as a reserved word.
In Python 3.6, there are 33 reserved keywords:
PythonKeywords      
False def if raise
None del import return
True elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not 
class from or 
continue global pass 

In Python, a variable may be assigned a value of one type, and then later assigned 
a value of a different type:

True
Correct
False

Variables are not statically typed in Python, as they are in some other programming 
languages.
'''

#Python Variables 44%
#That's correct!
#Consider the following sequence of statements:

n = 300
m = n
#Following execution of these statements, Python has created how many objects and how many references?
#1 One object, one reference
#2 Two objects, two references
#3 Two objects, one reference
#  One object, two references

# The first statement creates an integer object with value 300, and n is a reference
# to it. The second statement creates a second reference to the already existing object.
# Python variable references to the same object (illustration)

#Python Variables 55%
#What Python built-in function returns the unique number assigned to an object:

#1 identity()
#2 ref()
# refnum()
# id()
#Correct
#If two variables have the same id(), you know they reference the same object:

n = 300
m = n

print(id(m))
#52132448
print(id(n))
#52132448

#Python Variables 66%
# Which of the following are valid Python variable names:

#1 return
#2 ver1.3
#3 Age
#4 4square
#5 home_address
#6 route66


# 4square is not valid because it begins with a digit.
# return is not valid because it is a Python reserved word (keyword).
# version1.3 is not valid because it contains a character which is not a letter, digit or underscore.

#You are reading Python code, and these statements appear scattered in different locations throughout the code:

#1 employeenumber = 4398
#2 EmployeeNumber = 4398
#3 employeeNumber = 4398

#These statements refer to different variables.
# These statements refer to the same variable.
#Case is significant in Python variable names, so these are all different variables.
# The person who did this is asking for trouble.

'''
Which of the following are Python reserved words (keywords):
以下哪些是Python保留字（关键字）

Which of the following are Python reserved words (keywords):

not: default,goto
yes: class,and,None


'''

#Which of the following styles does PEP8 recommend for multi-word variable names:

#1 distance_to_nearest_town (Snake Case)
#2 DistanceToNearestTown (Pascal Case)
#3 distanceToNearestTown (Camel Case)