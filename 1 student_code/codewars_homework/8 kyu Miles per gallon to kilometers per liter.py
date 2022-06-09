'''
https://www.codewars.com/kata/557b5e0bddf29d861400005d/train/python

Sometimes, I want to quickly be able to convert miles per
imperial gallon into kilometers per liter.

Create an application that will display the number of kilometers
per liter (output) based on the number of miles per imperial
gallon (input).

Make sure to round off the result to two decimal points.
If the answer ends with a 0, it should be rounded off without
 0. So instead of 5.50, we should get 5.5.

Some useful associations relevant to this kata:
1 Imperial Gallon = 4.54609188 litres
1 Mile = 1.609344 kilometres

有时，我希望能够快速地将每英制加仑的英里数转换成每升的公里数。

创建一个应用程序，根据每英制加仑的英里数（输入）来显示每升的公里数（输出）。

请确保将结果四舍五入到小数点后两位数。如果答案以0结尾，则应舍去0。
因此，我们应得到5.5，而不是5.50。

一些与此卡塔相关的有用的关联：
1英制加仑=4.54609188升
1英里=1.609344公里
'''

def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188,2)

#lambda
converter = lambda x: round(x * 0.354006043538, 2)