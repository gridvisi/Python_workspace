# https://dbader.org/blog/python-dunder-methods

'''
这里是指 "双下划线（下划线）"。这些都是常用的运算符重载。一些神奇方法的例子有
__init__, __add__, __len__, __repr__等等。

当一个类的实例被创建时，用于初始化的__init__方法不需要任何调用，就像某些其他
编程语言如C++, Java, C#, PHP等中的构造函数一样。这些方法是我们可以用'+'运算符
添加两个字符串而不需要任何明确的类型转换的原因。

下面是一个简单的实现。

'''
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)

#declare our own string


class String:

        # magic method to initiate object
        def __init__(self, string):
            self.string = string

        # print our string object
        def __repr__(self):
            return 'Object: {}'.format(self.string)


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    #print(string1 + ' world')
# TypeError: unsupported operand type(s) for +: 'String' and 'str'
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

        # print our string object

    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' Geeks')



# Case_2nd bank Account!
'''
对象表示：__str__,__repr__
Python 中的常见做法是为类的使用者提供对象的字符串表示形式（有点像 API 文档。）使用 dunder 方法有两种方法可以做到这一点：
__repr__：对象的“官方”字符串表示。这就是你将如何制作类的对象。的目标__repr__是明确的。
__str__：对象的“非正式”或可很好打印的字符串表示形式。这是针对最终用户的。
让我们在类上实现这两个方法Account：
'''

"""一个简单的帐户类"""
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []


"""        这是让我们从这个类        """
acc = Account('bob')  # 默认金额 = 0
acc = Account('bob', 10)
acc4 = Account('sue', 10)

#我还定义了一个属性来计算帐户余额，这样我就可以方便地使用account.balance. 
# 此方法采用起始金额并添加所有交易的总和：
@property
def balance (self):
    return self.amount + sum(self._transactions)

# 让我们在帐户上进行一些存款和取款：
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)


print('\nBalance start: {}'.format(acc4.balance))
validate_transaction(acc4, 20)
print('\nBalance end: {}'.format(acc4.balance))




# 3rd Case_study!
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)



class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age


if __name__=="__main__":
    print("\t".join([str(item) for item in sorted([People("abc", 18),
        People("abe", 19), People("abe", 12), People("abc", 17)])]))
    # 补充直观比较
    print(People("abe", 19)<People("abe", 12))


'''
https://www.geeksforgeeks.org/dunder-magic-methods-python/?ref=gcse
'''

