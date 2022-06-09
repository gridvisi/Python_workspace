'''
https://brilliant.org/daily-problems/exclusive-or/

使用assert断言是学习python一个非常好的习惯，python assert 断言句语格式及用法很简单。在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助。本文主要是讲assert断言的基础知识。

python assert断言的作用

python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。

assert断言语句的语法格式

    assert python 怎么用？
    expression assert 表达式
1
2
assert语句用来声明某个条件是真的。
如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
当assert语句失败的时候，会引发一AssertionError。
下面做一些assert用法的语句供参考：
'''
# 什么是XOR？
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

today = "Tuesday"
#True表示今天是周四判断成立

left = right = 'Jack'
bool_date = (today == "Tuesday")
bool_left = (left == 'Jack' or not 'Jack')
bool_right = (right == 'Jack' or not 'Jack')

#1 bool_left, bool_right 只有一个为真，恰好可以用^: XOR表达
#2
for bool_left in (True,False):
    for bool_right in (True,False):
        Purple = bool_date or bool_left
        Gray = bool_date ^ bool_right
        if Purple ^ Gray == True:
            # Purple和Gray两人只有一个陈述为真：XOR 用 ^ 表达
            if bool_left ^ bool_right == True:
                #bool_left, bool_right只有一个为真：XOR 用 ^ 表达

                if bool_left:print('left is Jack')
                if bool_right:print('right is Jack')



#先看紫色衣服的声明
Purple = bool_date or bool_left
Gray = bool_date ^ bool_right
print(Purple,Gray)

#Purple 和 Gray有一个为True


left = 'Jack'     # 先假定left为Jack
#right = 'Jack'



assert today == "Tuesday"
#assert left == 'mike'


'''

class ShortInputException(Exception):
    #自定义的异常类
    
    def __init__(self, length, atleast):
        #super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:#x这个变量被绑定到了错误的实例
        print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
    else:
        print('没有异常发生.')

main()
'''