'''
操作符重载是指在其预定的操作意义之外赋予扩展意义。例如，操作符+被用来添加两个整数，
以及连接两个字符串和合并两个列表。这是可以实现的，因为'+'运算符被int类和str类所重载。
你可能已经注意到，同样的内置运算符或函数对不同类的对象显示出不同的行为，这被称为运算符重载。
'''

# Python program to show use of
# + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Geeks" + "For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks" * 4)

'''
如何在Python中重载运算符？
考虑到我们有两个对象，它们是一个类（用户定义的数据类型）的物理表示，
我们必须用二进制的'+'运算符添加两个对象，这时会出现错误，因为编译器不知道
如何添加两个对象。所以我们为运算符定义一个方法，这个过程被称为运算符重载。
我们可以重载所有现有的运算符，但我们不能创建一个新的运算符。为了执行操作符重载，
Python 提供了一些特殊的函数或神奇的函数，当它与那个特定的操作符相关联时，
会自动调用。例如，当我们使用+运算符时，神奇的方法__add__被自动调用，
其中定义了+运算符的操作。

在Python中重载二进制+运算符。
当我们在用户定义的数据类型上使用一个操作符时，
。改变操作符的行为就像改变方法或函数的行为一样简单。你在你的类中定义了方法，
操作符根据方法中定义的行为工作。当我们使用+运算符时，神奇的方法__add__被自动调用，
其中定义了+运算符的操作。通过改变这个神奇方法的代码，我们可以为+运算符赋予额外的意义。
 
'''

#代码1:
# Python Program illustrate how
# to overload an binary + operator

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print('ob1 + ob2:',ob1 + ob2)
print('ob3 + ob4:',ob3 + ob4)


#3

# of two complex numbers using binary
# + operator overloading.

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print('Ob3:',Ob3)


#4
# Python program to overload
# a comparison operators

class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False


ob1 = A(2)
ob2 = A(3)
if (ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")


#5
# Python program to overload equality
# and less than operators

class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)

'''
Python magic methods or special functions for operator overloading
Binary Operators:
Operator	Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
Unary Operators :
Operator	Magic Method
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
'''