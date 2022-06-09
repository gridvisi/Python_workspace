'''
https://www.codewars.com/kata/55aea0a123c33fa3400000e7/train/python

Sort array by last character
Complete the function to sort a given array or list by last character of elements.
Element can be an integer or a string.
例子
['acvd'，'bcc'] --> ['bcc'，'acvd']
字符串的最后一个字符是d和c，由于c在d之前，所以按最后一个字符排序会有
给['bcc', 'acvd']。

如果两个元素在最后一个字符上没有区别，那么应该按照它们的顺序进行排序。
阵列中来。
Example:
['acvd', 'bcc']  -->  ['bcc', 'acvd']
The last characters of the strings are d and c. As c comes before d, sorting by last character will
give ['bcc', 'acvd'].

If two elements don't differ in the last character, then they should be sorted by the order they
come in the array.

test.assert_equals(sort_me(['acvd','bcc']), ['bcc','acvd'])
test.assert_equals(sort_me(["asdf", 14, "13","asdf"]), ["13", 14, "asdf", "asdf"])
'''

def sort_me(arr):
    arrs = sorted([str(i) for i in arr],key=lambda x:x[-1])
    return [i if i in arr else int(i) for i in arrs]

arr = ["asdf", 14, "13","asdf"]
print(sort_me(arr))


#1st solution
def sort_me(arr):
    return sorted(arr, key=lambda elem: str(elem)[-1])


