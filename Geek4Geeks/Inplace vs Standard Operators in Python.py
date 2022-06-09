# https://www.geeksforgeeks.org/inplace-vs-standard-operators-python/
'''
普通操作符做的是简单的分配工作。另一方面，Inplace操作符的行为与普通操作符类似，只是在可变和不可变目标的情况下，它们以不同的方式行事。


_add_方法，做简单的加法，接受两个参数，返回总和，并将其存储在另一个变量中，不修改任何参数。
另一方面，_iadd_方法也需要两个参数，但是它通过存储总和对传递的第一个参数进行了就地修改。由于在这个过程中需要对对象进行变异，所以不可变的目标，如数字、字符串和图元，不应该有_iadd_方法。
普通运算符的 "add() "方法，实现了 "a+b"，并将结果存储在所述变量中。
Inplace运算符的 "iadd() "方法，如果它存在，就实现 "a+=b"（即在不可变目标的情况下，它不存在），并改变所传递参数的值。但如果不存在，就会实现 "a+b"。
案例1：不可变的目标。
在不可变的目标中，如数字、字符串和图元。Inplace操作符的行为与普通操作符相同，即只进行赋值，不对传递的参数进行修改。
'''

# Python code to demonstrate difference between
# Inplace and Normal operators in Immutable Targets

# importing operator to handle operator operations
import operator

# Initializing values
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
z = operator.add(a, b)

# using iadd() to add the arguments passed
p = operator.iadd(x, y)

# printing the modified value
print("Value after adding using normal operator : ", end="")
print(z)

# printing the modified value
print("Value after adding using Inplace operator : ", end="")
print(p)

# printing value of first argument
# value is unchanged
print("Value of first argument using normal operator : ", end="")
print(a)

# printing value of first argument
# value is unchanged
print("Value of first argument using Inplace operator : ", end="")
print(x)


#2

# Python code to demonstrate difference between
# Inplace and Normal operators in mutable Targets

# importing operator to handle operator operations
import operator

# Initializing list
a = [1, 2, 4, 5]

# using add() to add the arguments passed
z = operator.add(a, [1, 2, 3])

# printing the modified value
print("Value after adding using normal operator : ", end="")
print(z)

# printing value of first argument
# value is unchanged
print("Value of first argument using normal operator : ", end="")
print(a)

# using iadd() to add the arguments passed
# performs a+=[1, 2, 3]
p = operator.iadd(a, [1, 2, 3])

# printing the modified value
print("Value after adding using Inplace operator : ", end="")
print(p)

# printing value of first argument
# value is changed
print("Value of first argument using Inplace operator : ", end="")
print(a)