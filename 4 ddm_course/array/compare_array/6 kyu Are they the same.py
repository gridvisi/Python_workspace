'''
https://www.codewars.com/kata/550498447451fbbd7600041c/train/python


Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
'''

def comp(array1, array2):
    if array2==None or array1 == None:return False
    arr = [i*i for i in array1]
    return sorted(arr)==sorted(array2)


def comp(array1, array2):
    if not array2 or not array1:return False
    arr = [i*i for i in array1]
    return sorted(arr)==sorted(array2)
array1, array2 = [],[]
array1, array2 = None,[]
print(comp(array1, array2))


#1st solution
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

def comp(a1, a2):
    return None not in (a1,a2) and sorted(x*x for x in a1) == sorted(a2)

# right code:
def test():
    if value == 1:
        a = b = 1
        return a, b
    else:
        a = None
        b = None
value = 0
a, b = test(),test()

#wrong code:
def test():
    if value == 1:
        a = b = 1
        return a, b

value = 0
a, b = test()

'''
复制代码
执行这段测试程序会报错："TypeError: 'NoneType' object is not iterable"
这里是没有考虑到else的情况，在if条件不满足时，函数默认返回None。
调用时，将None赋给
a, b

等价于a, b = None

就出现了这样的错误提示。【结论】
1.将None赋给多个值时，会出现提示：TypeError: 'NoneType'
object is not iterable

2.函数返回值一定要考虑到条件分支的覆盖

3.在没有return语句时，python默认会返回None
'''