'''
https://www.codewars.com/kata/5235c913397cbf2508000048/train/python
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression
创建一个简单的计算器，该计算器给定一个由运算符（）、+、-、*、/组成的字符串，用空格分隔的数字返回该表达式的值
Example:
例子：
Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Calculator（）.evaluate（“2/2+3*4-6”）#=>7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
记住操作顺序！乘法和除法具有更高的优先级，应该从左到右执行。加法和减法的优先级较低，也应该从左到右执行。
ALGORITHMSPARSINGSTRINGSEXPRESSIONSBASIC LANGUAGE FEATURESFUNDAMENTALS
基本语言特征
'''

class Calculator(object):
  def evaluate(self, string):
    return 0