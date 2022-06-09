#https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
'''
 Python 有一个内置的函数叫 repr，它能把一个对象用字符串的形式表达出来以便辨认，这就是“字符串表示形式”。
 repr 就是通过 repr 这个特殊方法来得到一个对象的字符串表示形式的。如果没有实现 repr，当我们在控制台里
 打印一个向量的实例时，得到的字符串可能会是 <Vector object at 0x10e100070>

 交互式控制台和调试程序（debugger）用 repr 函数来获取字符串表示形式；在老的使用% 符号的字符串格式中，
这个函数返回的结果用来代替 %r 所代表的对象；同样，str.format 函数所用到的新式字符串格式化语法
（https://docs.python.org/2/library/string.html#format-string-syntax）
也是利用了 repr，才把!r 字段变成字符串。

 repr 和 str 的区别在于，后者是在 str() 函数被使用，或是在用 print 函数打印一个对象的时候才被调用的，
并且它返回的字符串对终端用户更友好。如果你只想实现这两个特殊方法中的一个，repr 是更好的选择，因为如果一个
对象没有 str 函数，而 Python 又需要调用它的时候，解释器会用 repr 作为替代。

“Difference between str and __repr__Python”
http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-inpython）
是 Stack Overflow 上的一个问题，Python 程序员 Alex Martelli 和 MartijnPieters 的回答很精彩。
'''
print("Difference between str and __repr__Python")
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Test():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '这个类的名字是: % s' % self.name

print(Test('科学'))

'''
str(object)：将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式
repr(object)：返回指定值的字符串表示
'''
print(repr("Hello, \nWorld!"))
# 'Hello, \nWorld!'

print(str("Hello, \nWorld!"))
# Hello,
# World!

import decimal
a = decimal.Decimal(1.25)
print(str(a), repr(a))  # 1.25 Decimal('1.25')


from datetime import date
b = date.today()
print(str(b), repr(b))  # 2019-05-22 datetime.date(2019, 5, 22)
'''
这两者之间到底有什么区别呢？总结来说以下几点：

两者之间的目标不同：str()主要面向用户，其目的是可读性，返回形式为用户友好性和可读性都较强的字符串类型；
而repr()面向的是Python解释器，或者说开发人员，其目的是准确性，其返回值表示Python解释器内部的含义，
常作为编程人员debug用途。

在解释器中直接输入a时调用repr()函数，而print(a)则调用str()函数。

repr()的返回值一般可以用eval()函数来还原对象，通常来说有如下等式。

但需要提醒的是，这个等式不是所有情况下都成立。
这两个方法分别调用内建的__str__()方法和__repr__()方法，一般来说在类中都应该定义__repr__()方法，
而__str__()方法则为可选，当可读性比准确性更为重要的时候应该考虑定义__str__()方法。如果类中没有定义__str__()方法，
则默认会使用__repr__()方法的结果来返回对象的字符串表示形式。用户实现__repr__()方法的时候最好保证其返回值可以用
eval()方法使对象重新还原。


+100
Alex总结得很好，但令人惊讶的是，太过简洁。

首先，让我重申一下Alex帖子中的主要观点。

默认的实现是无用的(很难想出一个不是无用的实现，但确实如此)
_repr__目标是要明确。
__str__目标是可读性
容器的__str__使用包含对象的__repr__。
缺省执行是无用的

这主要是一个惊喜，因为 Python 的默认值往往相当有用。然而，在这种情况下，为 __repr__ 提供一个默认值，它的作用就像。

return "%s(%r)" % (self.__class__, self.__dict__)
会太危险 (例如，如果对象之间相互引用，太容易陷入无限递归)。所以 Python 拒绝了。注意有一个默认值是真：
如果定义了 __repr__，而 __str__ 没有定义，那么对象的行为就会像 __str__=__repr__。

简单地说，这意味着：几乎每一个你实现的对象都应该有一个可以用来理解对象的函数式的 __repr__。实现__str__是可选的：
如果你需要一个 "漂亮的打印 "功能(例如，被报表生成器使用)，那么就去做。

__repr__ 的目标是毫不含糊的

让我直接说出来--我不相信调试器。我真的不知道如何使用任何调试器，也从未认真使用过。此外，我相信调试器的大毛病是它
们的基本性质--我调试的大多数故障都发生在很久很久以前，在很远很远的银河系里。这意味着，我确实以宗教般的狂热相信日
志记录。日志记录是任何一个像样的 "火与忘 "的服务器系统的命脉。Python 使得日志记录变得很容易：也许有一些特定的
项目包装，你所需要的只是个

log(INFO, "我在奇怪的函数中，a是", a, "b是", b, "但我得到了一个空的C--使用default", default_c)
但你必须做最后一步--确保你实现的每一个对象都有一个有用的repr，这样的代码就可以随便用了。这就是为什么会出现 
"eval "这个东西：如果你有足够的信息，所以eval(repr(c))==c，那就意味着你知道了关于c的所有信息，如果这足够简
单，至少以模糊的方式，就去做。如果不是，无论如何要确保你有足够的关于c的信息。我通常使用类似eval的格式。

"MyClass(this=%r,that=%r)" % (self. this,self. that). 这并不意味着你真的可以构造MyClass，也不意味
着这些是正确的构造函数参数--但这是一种有用的形式，可以表达 "这是你需要知道的关于这个实例的一切"。

注意：我上面用的是%r，而不是%s。你总是希望在__repr__实现里面使用repr()[或者%r格式化字符，等价地]，否则你就
违背了repr的目标。你希望能够区分 MyClass(3) 和 MyClass("3") 。

__str__ 的目标是可读的。

具体来说，它并不是为了毫不含糊--请注意，str(3)==str("3")。同样，如果你实现了一个IP抽象，让它的str看起来像
192.168.1.1就可以了。当实现一个日期/时间抽象时，str可以是 "2010/4/12 15:35:22 "等。我们的目标是用一种用户
而不是程序员想要阅读的方式来表示。砍掉无用的数字，假装成其他类--只要它支持可读性，就是一种改进。

容器的__str__使用包含对象的__repr__。
这似乎令人吃惊，不是吗？是有一点，但如果用他们的__str__，那会有多大的可读性呢？
'''