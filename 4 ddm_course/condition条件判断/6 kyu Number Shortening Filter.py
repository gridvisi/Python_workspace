'''
https://www.codewars.com/kata/56b4af8ac6167012ec00006f/train/python
在这个kata中，我们将创建一个函数，它将返回另一个函数（或Ruby中的过程），以缩短很长的数字。给定一个初始值数组，
替换给定基数的X次幂。如果返回函数的输入不是数字字符串，它应该将输入本身作为字符串返回。

这里有一个例子，胜过千言万语。

Test.describe("Basic tests")
filter1 = shorten_number(['','k','m'],1000)
Test.assert_equals(filter1('234324'), '234k')
Test.assert_equals(filter1('98234324'), '98m')
Test.assert_equals(filter1([1,2,3]), '[1, 2, 3]')
Test.assert_equals(filter1(''), '')
Test.assert_equals(filter1('32424234223'), '32424m')
filter2 = shorten_number(['','KB','MB','GB'],1024)
Test.assert_equals(filter2('32'), '32')
Test.assert_equals(filter2('2100'), '2KB')
Test.assert_equals(filter2('pippi'), 'pippi')
Test.assert_equals(filter2('2100k'), '2100k')
Test.assert_equals(filter2('1073741823'), '1023MB')
'''


def shorten_number(suffixes, base):
    if base == 1000:
