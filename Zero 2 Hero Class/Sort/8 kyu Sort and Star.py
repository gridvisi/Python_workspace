'''
https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
你将会得到一个字符串的向量，你必须按字母顺序对其进行排序（区分大小写，并基于字符的ASCII值），然后返回第一个值。你必须按字母顺序对其进行排序（区分大小写，并基于字符的ASCII值），然后返回第一个值。

返回的值必须是一个字符串，并且在每个字母之间有 "***"。

你不应该从数组中删除或添加元素。
Test.assert_equals(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
Test.assert_equals(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
Test.assert_equals(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
Test.assert_equals(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
Test.assert_equals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')
'''

def two_sort(array):
    return '***'.join(list(sorted(array)[0]))

array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
print(two_sort(array))

#1st
def two_sort(lst):
    return '***'.join(min(lst))

#2nd
def two_sort(arr):
    return '***'.join(sorted(arr)[0])

#sorted
# .sort()

ages = [10,13,8,19]
print('ages_sort:',sorted(ages,reverse=True))
print(ages)
ages.sort()
print(ages)

c = ['chicken','eggs']
c = ['egges','chicken']
c.sort()
print(c)