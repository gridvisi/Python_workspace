
"""方法一"""
str_ = "[[1,2,344],[323,3,34]]"
list_ = eval(str_)
print([i for k in list_ for i in k])

""""方法二"""
import re
string = "[[1,2,344],[323,3,34]]"
regex = re.compile('\d+')
print([int(i) for i in re.findall(regex, string)])
