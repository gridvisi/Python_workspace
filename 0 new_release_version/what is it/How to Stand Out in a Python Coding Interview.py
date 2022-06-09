'''
本教程有一个由Real Python团队制作的相关视频课程。请结合书面教程一起观看，加深理解。Python 编码面试。技巧和最佳实践。
你已经通过了与招聘人员的电话，现在是时候展示你知道如何用实际代码解决问题了。无论是HackerRank练习、带回家的作业，
还是现场白板面试，这都是你证明自己编码面试技能的时刻。

但面试不仅仅是为了解决问题：它们也是为了证明你能写出干净的生产代码。这意味着你对Python的内置功能和库有很深的了解。
这些知识向公司展示了你可以快速移动，不会因为你不知道它的存在而重复语言中自带的功能。

在Real Python，我们已经把我们的头放在一起，并讨论了我们总是在编码面试中看到什么工具，我们印象深刻。
本文将带领你了解这些功能中最好的功能，从Python的内置功能开始，然后是Python对数据结构的原生支持，
最后是Python强大的(经常被低估的)标准库。

在本文中，您将学习如何。
使用 enumerate() 遍历指数和值。
使用断点()调试有问题的代码。
使用f-字符串有效地格式化字符串
使用自定义参数对列表进行排序
使用生成器代替列表理解来节省内存。
定义查询字典键时的默认值。
使用collection.Counter类对可哈希对象进行计数。
使用标准库来获取排列组合的列表

Python Mastery上的5个想法，这是一门针对Python开发人员的免费课程，它向你展示了将你的Python技能提升到一个新的
水平所需要的路线图和心态。

为工作选择正确的内置功能
Python有一个庞大的标准库，但只有一个小的内置函数库，这些函数一直可用，不需要导入。值得逐一去了解，但在你有
机会这样做之前，这里有几个值得了解如何使用的内置函数，以及在其中一些函数的情况下，使用什么替代品来代替。

用enumerate()代替range()进行迭代。
这个场景在编码面试中可能出现的次数比其他任何场景都要多：你有一个元素列表，你需要对列表进行迭代，同时访问索引和值。


有一道经典的编码面试题叫FizzBuzz，可以通过迭代索引和值来解决。在FizzBuzz中，你会得到一个整数列表。你的任务是
做以下事情。

用 "buzz "代替所有被5整除的整数。
用 "fizzbuzz "代替所有被3和5整除的整数。
通常，开发者会用range()来解决这个问题。

'''
numbers = [45, 22, 14, 65, 97, 72]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'fizzbuzz'

    elif numbers[i] % 3 == 0:
         numbers[i] = 'fizz'

    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)
# ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
'''
对于每个元素，enumerate()返回一个计数器和元素值。计数器默认为0，这也是元素的索引。不想从0开始计数？
只需使用可选的startparameter来设置一个偏移量。
'''
num = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
    print(i, num)
'''
通过使用start参数，我们访问所有相同的元素，从第一个索引开始，但现在我们的计数从指定的整数值开始。

使用List Comprehensions代替map()和filter()

"我认为放弃filter()和map()是非常没有争议的[.]"
- Guido van Rossum，Python的创造者。

他可能错在没有争议，但Guido有充分的理由想从Python中删除map()和filter()。其中一个原因是 Python 支持列表理解，它通常更容易阅读，并且支持与 map() 和 filter() 相同的功能。

让我们先来看看我们如何结构化调用 map() 和等价的 list 解析。
'''
# 可读性是否更好
numbers = [4, 2, 1, 6, 9, 7]

def square(x):
    return x*x

print(list(map(square, numbers)))
#[16, 4, 1, 36, 81, 49]
print([square(x) for x in numbers])
#[16, 4, 1, 36, 81, 49]

#这两种方法，使用map()和list comprehension，返回的值都是一样的，但list comprehension更容易阅读和理解。
#现在我们可以对filter()和它的等价列表理解做同样的事情。
def is_odd(x):
   return bool(x % 2)
print(list(filter(is_odd, numbers)))
#[1, 9, 7]

print([x for x in numbers if is_odd(x)])
#[1, 9, 7]
sorted([6,5,3,7,2,4,1])
#[1, 2, 3, 4, 5, 6, 7]
sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
#['rhino', 'dog', 'cheetah', 'cat', 'bear]

'''
就像我们在map()上看到的一样，filter()和list comprehension方法返回的值是一样的，
但是list comprehension更容易理解。

来自其他语言的开发人员可能不同意列表理解比map()和filter()更容易读懂，但根据我的经验，
初学者能够更直观地掌握列表理解。

无论哪种方式，你在编码面试中使用列表理解很少会出错，因为它会传达你知道Python中最常见的东西。

用breakpoint()代替print()进行调试

你可能已经通过在代码中添加print()来调试一个小问题，并看到打印出来的内容。这种方法一开始很有效，
但很快就变得很麻烦。另外，在编码面试的环境中，你几乎不想让print()调用遍布你的代码。

相反，你应该使用调试器。对于非平凡的bug，它几乎总是比使用print()更快，而且考虑到调试是编写软件的一个重要部分，
这表明你知道如何使用工具，让你在工作中快速开发。

如果你使用的是Python 3.7，你不需要导入任何东西，只需要在你的代码中你想进入调试器的位置调用断点()。

# 一些有错误的复杂代码
断点()

调用breakpoint()会让你进入pdb，这是默认的Python调试器。在Python 3.6和更老的版本中，
你可以通过显式导入pdb来实现同样的目的。

import pdb; pdb.set_trace()

和breakpoint()一样，pdb.set_trace()会让你进入pdb调试器。它只是没有那么干净，而且要多记一些。

还有其他的调试器，你可能想尝试一下，但pdb是标准库的一部分，所以它总是可用的。无论你喜欢哪种调试器，
在你进入编码面试环境之前，都值得尝试一下，以适应工作流程。

用f-Strings格式化字符串

Python 有很多不同的方法来处理字符串格式化，而且要知道用什么来处理是很棘手的。事实上，我们在两篇单独的
文章中深入探讨了格式化问题：一篇是关于一般的字符串格式化，一篇是专门针对f字符串的。在编码面试中，
你使用Python 3.6+，建议的格式化方法是Python的f-strings。

f-strings支持使用字符串格式化迷你语言，以及强大的字符串插值功能。这些特性允许你添加变量甚至有效的
Python表达式，并在运行时对它们进行评估，然后再添加到字符串中。

'''
def get_name_and_decades(name, age):
    return f"我的名字是{name}，我的年龄是{age / 10:.5f}几十年了。"
get_name_and_decades("Maria", 31)
#我的名字叫Maria，我的年龄是3.10000岁。
'''
f-string允许你将Maria放入字符串中，并在一个简洁的操作中添加她的年龄和所需的格式。

需要注意的一个风险是，如果你输出的是用户生成的值，那么可能会带来安全风险，在这种情况下，
模板字符串可能是一个更安全的选择。

使用 sorted() 对复杂列表进行排序
大量的编码面试问题都需要某种排序，而你有多种有效的方式可以对项目进行排序。除非面试官希望
你实现自己的排序算法，否则通常最好使用 sorted() 。
你可能已经看到了最简单的排序用法，比如按升序或降序对数字或字符串列表进行排序。
'''
sorted([6,5,3,7,2,4,1])
#[1, 2, 3, 4, 5, 6, 7]

sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
#['rhino', 'dog', 'cheetah', 'cat', 'bear]

'''
默认情况下，sorted()已将输入的内容按升序排序，而反向关键字参数则使其按降序排序。
值得了解的是可选的关键字参数key，它可以让你指定一个函数，在排序之前将对每个元素进行调用。
添加一个函数允许自定义排序规则，如果你想对更复杂的数据类型进行排序，这特别有用。
'''
animals = [

    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},

    ]
sorted(animals, key=lambda animal: animal['age'])
answer = [

    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},

]
'''
通过传递一个返回每个元素年龄的lambda函数，你可以很容易地通过每个字典的一个值对字典列表进行排序。在这种情况下，字典现在是按年龄升序排序的。


通过传递一个返回每个元素年龄的lambda函数，你可以很容易地通过每个字典的一个值对字典列表进行排序。在这种情况下，
字典现在是按年龄升序排序的。有效地利用数据结构

在编码面试中，算法备受关注，但数据结构可以说更加重要。在编码面试中，选取合适的数据结构会对性能产生重大影响。
除了理论上的数据结构，Python在其标准数据结构实现中还内置了强大而方便的功能。这些数据结构在编码面试中非常有用，
因为它们默认给了你很多功能，让你把时间集中在问题的其他部分。

用集合存储唯一值：你经常需要从现有的数据集中删除重复的元素。新的开发人员有时会用列表来删除重复的元素，而他们应
该用集合来删除重复的元素，因为集合可以强制所有元素的唯一性。

假设你有一个名为get_random_word()的函数。它总是会从一个小词集中返回一个随机选择。
'''

# Good code
import random
all_words = "all the words in the world".split()
def get_random_word():
   return random.choice(all_words)
'''
你应该反复调用get_random_word()来获取1000个随机词，然后返回一个包含每个唯一词的数据结构。
这里有两种常见的、次优的方法和一种好的方法。
'''
#糟糕的方法:
#get_unique_words()
#将值存储在一个列表中，然后将列表转换成一个集合。
def get_unique_words():
    words = []
    for _ in range(1000):
        words.append(get_random_word())
    return set(words)
get_unique_words()
#{'world', 'all', 'the', 'words'}
'''

这种方法并不可怕，但它不必要地创建一个列表，然后将其转换为一个集合。
面试官几乎总是注意到并询问这种类型的设计选择。


更糟糕的方法:
为了避免从列表转换为集合，现在你可以在不使用任何其他数据结构的情况下将值存储在一个列表中，
然后通过将新的值与当前列表中的所有元素进行比较来测试唯一性。然后，你可以通过将新的值与当前
列表中的所有元素进行比较来测试其唯一性。
'''
def get_unique_words():
    words = []
    for _ in range(1000):
        word = get_random_word()
        if word not in words:
            words.append(word)
    return words
print(get_unique_words())
#['world', 'all', 'the', 'words']

'''
除了从一开始就使用了一个集合之外，这可能看起来和其他方法没有什么不同。如果你考虑一下.add()中发生的事情，
它甚至听起来像第二种方法：获取单词，检查它是否已经在集合中，如果没有，就把它添加到数据结构中。

那么为什么使用集合和第二种方法不同呢？
之所以不同，是因为集合存储元素的方式可以近乎恒定时间地检查一个值是否在集合中，而不像列表，需要线性时间的查找。
查找时间的不同意味着向集合中添加的时间复杂度以O(N)的速度增长，在大多数情况下，这比第二种方法的O(N²)要好得多。

使用生成器节省内存
列表理解是方便的工具，但有时会导致不必要的内存使用。
想象一下，你被要求找出前1000个完全平方的总和，从1开始。你知道列表理解，所以你很快就写出了一个可行的解决方案。
'''
sum([i * i for i in range(1, 1001)])
#333833500

'''
换掉括号，你的列表理解就会变成生成器表达式。生成器表达式非常适合于当你知道你想从一个序列中检索数据，但你不需要同时
访问所有的数据。
生成器表达式不是创建一个列表，而是返回一个生成器对象。该对象知道它在当前状态下的位置（例如，i = 49），并且只在被
要求时计算下一个值。
所以当sum通过反复调用.__next__()对生成器对象进行迭代时，生成器会检查i等于什么，计算i * i，在内部递增i，并返回
适当的值给sum。这种设计允许生成器用于海量数据序列，因为每次内存中只存在一个元素。
使用.get()和.setdefault()在字典中定义默认值。
最常见的编程任务之一涉及到添加、修改或检索一个可能在字典中存在或不存在的项目。Python 字典有优雅的功能来使这些
任务变得干净和简单，但开发人员经常在没有必要的时候明确地检查值。
想象一下，你有一个名为 cowboy 的字典，你想得到那个牛仔的名字。一种方法是用一个条件来显式检查键。
'''

print(sum((i * i for i in range(1, 1001))))
#333833500

cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}

if 'name' in cowboy:
    name = cowboy['name']
else:
    name = 'The Man with No Name'

print(name)
#'The Man with No Name'

'''
这种方法首先检查名称键是否存在于字典中，如果存在，则返回相应的值。否则，它就返回一个默认值。
虽然显式检查键确实有效，但如果你使用.get()，可以很容易地用一行来代替。
'''

name = cowboy.get('name', 'The Man with No Name')
'''
get()执行与第一种方法中相同的操作，但现在它们被自动处理。如果键存在，那么将返回适当的值。否则，将返回默认值。
但是如果你想在访问名称键的同时用默认值更新字典呢？.get()在这里并不能帮助你，所以你只能再次明确地检查值。​
'''

if 'name' not in cowboy:
    cowboy['name'] = 'The Man with No Name'
name = cowboy['name']

'''
换掉括号，你的列表理解就会变成生成器表达式。生成器表达式非常适合于当你知道你想从一个序列中检索数据，但你不需要同时访问所有的数据。



生成器表达式不是创建一个列表，而是返回一个生成器对象。该对象知道它在当前状态下的位置（例如i = 49），并且只在被要求时计算下一个值。



所以当sum通过反复调用.__next__()对生成器对象进行迭代时，生成器会检查i等于什么，计算i * i，在内部递增i，并返回适当的值给sum。这种设计允许生成器用于海量数据序列，因为每次内存中只存在一个元素。



使用.get()和.setdefault()在字典中定义默认值。

最常见的编程任务之一涉及到添加、修改或检索一个可能在字典中存在或不存在的项目。
Python 字典有优雅的功能来使这些任务变得干净和简单，但开发人员经常在没有必要的时候明确地检查值。

想象一下，你有一个名为 cowboy 的字典，你想得到那个牛仔的名字。一种方法是用一个条件来显式检查键。
检查值并设置默认值是一种有效的方法，而且很容易读懂，但Python又提供了一种更优雅的方法，
即.setdefault()
'''

name = cowboy.setdefault('name', 'The Man with No Name')

'''
.setdefault()完成的事情和上面的代码段完全一样，它检查cowboy中是否存在name，如果存在，则返回该值。它检查cowboy中是否存在name，如果存在，则返回该值。否则，它将 cowboy['name'] 设置为 The Man with No Name 并返回新值。
利用 Python 的标准库
默认情况下，Python自带了很多功能，只需要一个importstatement就可以了。它本身就很强大，但知道如何利用标准库可以让你的编码面试技巧超常发挥。
很难从所有可用的模块中挑选出最有用的部分，所以本节将只关注其实用功能的一小部分子集。希望这些功能能证明在编码面试中对你有用，同时也能激起你的欲望，了解更多关于这些模块和其他模块的高级功能。
用collections.defaultdict()处理缺失的字典密钥
.get()和.setdefault()在为单个键设置默认值时很好用，但通常希望为所有可能的未设置的键设置一个默认值，特别是在编码面试环境下编程时。
假设你有一组学生，你需要跟踪他们的家庭作业成绩。输入值是一个格式为(student_name，grade)的tuples列表，但你想轻松地查找单个学生的所有成绩，而不需要遍历列表。
一种存储成绩数据的方法是使用一个字典，将学生姓名映射到成绩列表中。

'''
student_grades = {}
grades = [
     ('elliot', 91),
     ('neelam', 98),
     ('bianca', 81),
     ('elliot', 88),
 ]
for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)
print(student_grades)
#{'elliot': [91, 88], 'neelam': [98], 'bianca': [81]}
'''
在这种方法中，你迭代学生，并检查他们的名字是否已经是字典中的属性。如果没有，你将他们添加到字典中，
并以一个空列表作为默认值。然后，你将他们的实际成绩追加到该学生的成绩列表中。

但还有一种更简洁的方法，那就是使用 defaultdict，它扩展了标准 dict 的功能，允许你设置一个默认值，
如果键不存在，就会被操作。
'''
from collections import defaultdict
student_grades = defaultdict(list)
for name, grade in grades:
    student_grades[name].append(grade)
'''
在这种情况下，你正在创建一个defaultdictthat使用没有参数的list()构造函数作为默认的工厂方法。没有参数的list()
会返回一个空列表，所以defaultdict在名称不存在的情况下调用list()，然后允许附加等级。如果你想搞得很花哨，你也可以
使用一个lambda函数作为你的工厂值来返回一个任意的常量。
利用defaultdict可以使应用程序的代码更加简洁，因为你不必担心键级的默认值。相反，你可以在defaultdict级别处理它
们一次，之后就像键一直存在一样。关于这个技术的更多信息，请查看使用 Python defaultdict 类型处理缺失的键。
用 collections.Counter 来计算可哈希对象
你有一长串没有标点符号或大写字母的单词，你想计算每个单词出现的次数。
你可以使用字典或defaultdictand递增计数，但collections.Counter提供了一个更干净、更方便的方法来完成这个任务。
Counter是dict的一个子类，对于任何缺失的元素，它都使用0作为默认值，这使得计算对象的出现次数变得更加容易。
'''
from collections import Counter
words = "if there was there was but if \
#there was not there was not".split()
counts = Counter(words)
print(counts)
Counter({'if': 2, 'there': 4, 'was': 4, 'not': 2, 'but': 1})

'''

.most_common()是一个方便的方法，只是简单地按计数返回n个最频繁的输入。
使用stringConstants访问普通字符串组
小知识时间到了! 'A'>'a'是真还是假？
是假的，因为A的ASCII码是65，但a是97，而65不大于97。
为什么答案很重要？因为如果你想检查一个字符是否是英文字母表的一部分，一个常用的方法是看它是否在A和z之间
（ASCII表上的65和122）。
检查ASCII码是可行的，但是很笨拙，在编码面试中很容易出错，尤其是当你记不住是小写还是大写ASCII字符在先的时候。
使用字符串模块中定义的常量就容易多了。
你可以在is_upper()中看到一个使用的常量，它返回一个字符串中的所有字符是否都是大写字母。
'''
print(counts.most_common(2))
#[('there', 4), ('was', 4)]

import string
def is_upper(word):
     for letter in word:
         if letter not in string.ascii_uppercase:
             return False
     return True

print(is_upper('Thanks Geir'))
#False
print(is_upper('LOL'))
#True
'''
is_upper() 遍历 word 中的字母，并检查这些字母是否是 string.ascii_uppercase 的一部分。
如果你打印出string.ascii_uppercase，你会发现它只是一个低级的字符串。
其值被设置为字面的'ABCDEFGHIJKLMNOPQRSTUVWXYZ'。
所有的字符串常量都只是经常引用的字符串值的字符串。它们包括以下内容。

string.ascii_letters
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.printable
string.whitespace
'''

'''
itertools有多种工具用于生成输入数据的可迭代序列，但现在我们只关注两个常用函数：
itertools.permutations()和itertools.combinations()。
itertools.permutations()建立了一个所有permutations的列表，这意味着它是一个长度
与count参数相匹配的所有可能的输入值分组的列表。
rkeyword参数让我们指定每个分组中的数值数量。
'''
import itertools

friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
list(itertools.permutations(friends, r=2))
#[('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
# ('Ashish', 'Monique'), ('Ashish', 'Devon'), ('Ashish', 'Bernie'),
# ('Devon', 'Monique'), ('Devon', 'Ashish'), ('Devon', 'Bernie'),
# ('Bernie', 'Monique'), ('Bernie', 'Ashish'), ('Bernie', 'Devon')]
'''
在组合中，元素的顺序很重要，所以('sam', 'devon')和('devon', 'sam')是不同的配对，这意味着它们都会被包含在列表中。
itertools.combinations()建立组合。这些也是输入值的可能分组，但现在值的顺序并不重要。
因为('sam', 'devon')和('devon', 'sam')代表同一对，所以只有其中一个会被包含在输出列表中。
'''
list(itertools.combinations(friends, r=2))
#[('Monique'，'Ashish')，('Monique'，'Devon')，('Monique'，'Bernie')。
#('Ashish', 'Devon'), ('Ashish', 'Bernie'), ('Devon', 'Bernie')]

'''
由于值的顺序对组合并不重要，所以对于同一个输入列表，组合比排列组合要少。同样，因为我们将r设为2，所以每个分组中都有两个名字。
.combinations()和.permutations()只是一个强大库的小例子，但当你试图快速解决一个算法问题时，即使是这两个函数也是相当有用的。
结束语 编码面试超能力
现在你可以在下一次编码面试中自如地使用Python的一些不常见，但更强大的标准特性。关于这门语言的整体知识有很多，
但本文应该已经给了你一个深入的起点，同时让你在面试时更有效地使用Python。
在这篇文章中，你已经学会了不同类型的标准工具，为你的编码面试技巧加分。
强大的内置函数
为处理常见场景而构建的数据结构，几乎不需要任何代码。
标准库包，对具体问题有丰富的功能解决方案，让你更快地写出更好的代码。
面试可能不是真实软件开发的最佳近似，但值得了解如何在任何编程环境中取得成功，甚至面试。值得庆幸的是，在编码面试中
学习如何使用Python可以帮助你更深入地理解这门语言，这将在日常开发中得到回报。
 立即观看 本教程有一个由 Real Python 团队创建的相关视频课程。将其与书面教程一起观看，以加深你的理解。Python 
 编码面试。技巧和最佳实践
🐍Python技巧 💌
每隔几天向您的收件箱发送一个短小精悍的Python窍门。没有垃圾邮件。随时可以退订。由 Real Python 团队策划。
'''