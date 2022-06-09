'''
https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3,
"Boom" if it is divisible by 5,
"BangBoom" if it divisible by 3 and 5, and
"Miss" if it isn't divisible by any of them.
Note: Your program should only return one value

Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 -->
Output: "Boom"

FUNDAMENTALS
Test.assert_equals(multiple(30), "BangBoom")
Test.assert_equals(multiple(3), "Bang")
Test.assert_equals(multiple(98),"Miss")
Test.assert_equals(multiple(65),"Boom")
Test.assert_equals(multiple(23),"Miss")
Test.assert_equals(multiple(15),"BangBoom")
'''

def multiple(x):
    if x % 5 == 0 and x%3 != 0:return 'Boom'
    if x % 5 == 0 and x % 3 == 0: return 'BangBoom'
    if x % 5 != 0 and x % 3 == 0: return 'Bang'
    if x % 5 != 0 and x % 3 != 0: return 'Miss'

#1st
def multiple(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'


start = '1:30'
end = '2:30'

def shijian(start,end):  #函数
    return end - start

def red_green_yellow(light):
    if light == 'red':
        return 'stop'

    if light == 'green':
        return 'go through'

    if light == 'yellow':
        return 'depend on' #

light = 'red'
light = 'yellow'
print(red_green_yellow(light))