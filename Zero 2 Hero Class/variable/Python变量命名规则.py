#常用的命名法：骆驼（Camel）、帕斯卡（pascal）、匈牙利（Hungarian）、下划线（_）

#骆驼：是指混合使用大小写字母来构成变量和函数的名字
#帕斯卡：与骆驼命名法类似只不过骆驼命名法是首字母小写，而帕斯卡命名法是首字母大写
'''
总结：对于常量的定义一般习惯全用大字，并用下划线 ' _ ' 作为分割，通常每种语言都有自己的
Coding Style, 比如 C/C++ 和 python 是下划线,java 和 go 是驼峰。

所以，对于要使用哪种命名法可以根据个人的代码编写风格，也是可使用不同的命名规范混合使用。
如：骆驼+下划线 （int temperature_Sensor;）


'''
'''
在使用标识符时，需要注意如下规则：
标识符可以由字母、数字、下画线（_）组成，其中数字不能打头。
标识符不能是 Python 关键字，但可以包含关键字。
标识符不能包含空格。

例如下面变量，有些是合法的，有些是不合法的：
abc_xyz：合法。
HelloWorld：合法。
abc：合法。
xyz#abc：不合法，标识符中不允许出现“#”号。
abc1：合法。
1abc：不合法，标识符不允许数字开头。

1.只能包含字母、数字和下划线，且不能以数字开头

2.区分字母大小写

3.禁止使用保留字(关键字)

命名惯例：

1.以单一下下划线开头的变量名（_x）不会被 from module import * 语句导入

2.前后有下划线的变量名（__x__）是系统定义的变量名，对python 解释器有特殊意义

3.以两个下划线开头但结尾没有下划线的变量名（__x）是类的成员变量

4.交互式模式下，变量名 ”_“ 用于保存最后表达式的结果

5.变量是弱类型
'''

#导入keyword 模块
import keyword
#显示所有关键字
print(keyword.kwlist)

'''
文件名
全小写,可使用下划线


包
应该是简短的、小写的名字。如果下划线可以改善可读性可以加入。如mypackage。


模块
与包的规范同。如mymodule。


类
总是使用首字母大写单词串。如MyClass。内部类可以使用额外的前导下划线。

函数&方法
函数名应该为小写，可以用下划线风格单词以增加可读性。如：myfunction，my_example_function。
*注意*：混合大小写仅被允许用于这种风格已经占据优势的时候，以便保持向后兼容。


函数和方法的参数
总使用“self”作为实例方法的第一个参数。总使用“cls”作为类方法的第一个参数。
如果一个函数的参数名称和保留的关键字冲突，通常使用一个后缀下划线好于使用缩写或奇怪的拼写。


全局变量
对于from M import *导入语句，如果想阻止导入模块内的全局变量可以使用旧有的规范，在全局变量上加一个前导的下划线。
*注意*:应避免使用全局变量


变量
变量名全部小写，由下划线连接各个单词。如color = WHITE，this_is_a_variable = 1
*注意*：
1.不论是类成员变量还是全局变量，均不使用 m 或 g 前缀。
2.私有类成员使用单一下划线前缀标识，多定义公开成员，少定义私有成员。
3.变量名不应带有类型信息，因为Python是动态类型语言。如 iValue、names_list、dict_obj 等都是不好的命名。


常量
常量名所有字母大写，由下划线连接各个单词如MAX_OVERFLOW，TOTAL。


异常
以“Error”作为后缀。


缩写
命名应当尽量使用全拼写的单词，缩写的情况有如下两种：
1.常用的缩写，如XML、ID等，在命名时也应只大写首字母，如XmlParser。
2.命名中含有长单词，对某个单词进行缩写。这时应使用约定成俗的缩写方式。
例如：
function 缩写为 fn
text 缩写为 txt
object 缩写为 obj
count 缩写为 cnt
number 缩写为 num，等。
前导后缀下划线
一个前导下划线：表示非公有。
一个后缀下划线：避免关键字冲突。
两个前导下划线：当命名一个类属性引起名称冲突时使用。
两个前导和后缀下划线：“魔”（有特殊用图）对象或者属性，例如__init__或者__file__。绝对不要创造这样的名字，而只是使用它们。
*注意*：关于下划线的使用存在一些争议。



特定命名方式
主要是指 __xxx__ 形式的系统保留字命名法。项目中也可以使用这种命名，它的意义在于这种形式的变量是
只读的，这种形式的类成员函数尽量不要重载。如
class Base(object):
def __init__(self, id, parent = None):
self.__id__ = id
self.__parent__ = parent
def __message__(self, msgid):
# …略
其中 __id__、__parent__ 和 __message__ 都采用了系统保留字命名法。
附:Google Python命名规范
module_name, package_name, ClassName, method_name, ExceptionName, function_name, 
GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.
'''