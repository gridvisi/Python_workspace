'''
https://www.codewars.com/kata/double-sort/train/python
Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, or a mix of both. You will not get an empty array, nor a sparse one.
很简单-你将得到一个数组。数组中的值可以是数字或字符串，也可以是两者的混合。不会得到空数组，也不会得到稀疏数组。

Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings sorted in alphabetic order. The values must maintain their original type.
您的任务是返回一个数组，该数组首先按升序排序数字，然后按字母顺序排序字符串。值必须保持其原始类型。

Note that numbers written as strings are strings and must be sorted with the other strings.
请注意，作为字符串写入的数字是字符串，必须与其他字符串一起排序。
'''

print(ord('!'),ord('1'))
print('!'.isdigit())
arr = ['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]
def db_sort(arr):
    restr,re = [],[]
    for e in arr:
        if e == str(e):
            restr.append(e)
        else:re.append(e)
    return sorted(re) + sorted(restr)

def db_sort(arr):
    return sorted(arr, key=lambda x:(isinstance(x,str),x))
print(db_sort(arr))

x = 1
print((isinstance(x,str),x))
key = (isinstance(x,str),x)
s = lambda x:(isinstance(x,str),x)
print(key,s)

'''
>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(students, key=lambda s: s[2])            # 按年龄排序
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
 
>>> sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


def db_sort(arr):
    return sorted([str(i) for i in arr])
arr = ['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6] #[5,6,6,7,10,15,110,"!","2500","come","on"]

'''