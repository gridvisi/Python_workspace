'''
https://www.codewars.com/kata/5865a28fa5f191d35f0000f8/train/python


编写一个函数take_umbrella()，它需要两个参数：一个代表当前天气的字符串和一个代表今天下雨机会的浮点数。

你的函数应该根据以下标准返回True或False。

如果目前正在下雨，或者多云，并且下雨的几率超过0.20，你应该打伞。
如果是晴天，你不应该打伞，除非下雨的可能性比不下雨的可能性大。
当前天气的选项是晴天、阴天和雨天。

例如，take_umbrella('sunny', 0.40)应该返回False。

作为一个额外的挑战，可以考虑只用逻辑运算符来解决这个卡塔，不使用任何if语句。
给你一个布尔函数（即一个接受布尔参数并返回布尔值的函数）。你必须返回一个代表该函数真值表的字符串。

格式化规则:
变量应该被命名为A、B、C、D......，以此类推，与传递给布尔函数的顺序相同。
不会有超过26个（A...Z）的参数
布尔值将用1（真）或0（假）表示
如果该函数是匿名的，则使用字母f作为名称。
第一行将包括，按顺序。
变量的名称，用空格（ ）分隔

​​思路梳理：
返回True，意味着带伞​；
返回False，意味着不必带伞

共有几个条件触发？

1、晴天带伞的触发条件​：
    ​ rain_chance >=0.5，return True

2、多云带伞的触发条件​：
     ​rain_chance >=0.2，return True

3、下雨天带伞的触发条件​：
    ​    ​rain_chance ==0.0，return True

    ​    ​#意即无论rain_chance多少，都带伞​；​
​
'''

def take_umbrella(weather, rain_chance):
    # need not take umbrella should meet follow condition -> True
    s = weather=="sunny" and rain_chance > 0.5
    c = weather=="cloudy" and rain_chance > 0.2
    r = rain_chance >= 0.0 and weather=="rainy"
    return s or c or r

#test: Time: 542msPassed: 5Failed: 98
'''
True should equal False
False should equal True
Test Passed
'''

#1st
def take_umbrella(weather, rain_chance):
    # Your code here.
    return (weather=='cloudy' and rain_chance>0.20) or weather=='rainy' or (weather=='sunny' and rain_chance>0.5)

#2nd
def take_umbrella(weather, rain_chance):
    return rain_chance > {'sunny': 0.5, 'cloudy': 0.2, 'rainy': -1}[weather]