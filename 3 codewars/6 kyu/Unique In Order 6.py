'''
但是当我们在具体实现时很可能会遇到意想不到的错误，代码有的时候能够达到预期的删除所有重复元素的效果，有的时候只能删除部分重复元素，
如上例所示。比较两个列表，发现，列表x中所有的1都是不相邻的，列表y中有的1是相邻的。出现以上问题的原因在于，列表的内存自动管理功能，
在删除列表中的元素时，python会自动对列表内存进行收缩，并移动列表中的元素以保证元素之间没有间隙，所以使用“循环+remove（）方法”来
删除列表中某一重复元素时，如果存在相邻的该元素，在删除前面一个元素后，后一个元素会被移动到刚被删除的这个元素的位置，
这样这个元素就“躲过了删除”
————————————————
版权声明：本文为CSDN博主「no_error_no_warn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_39514033/article/details/80807227
'''
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
def unique_in_order(iterable,re = []):  #
    i,j = 0,0
    #print(iterable,i,j)
    while iterable[i] == iterable[j]:
            j += 1
            if j >= len(iterable):
                re.append(iterable[i])
                return ''.join(re)
    re.append(iterable[i])
    #print(i, j, len(iterable))
    i = j
    #print(re, len(iterable))
    return unique_in_order(iterable[i:])

st = "AAAABBBCC##777DAABBB   AHTRDE$$$$E&&ESSJH"

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

from itertools import groupby
def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

print(unique_in_order(st))

def unique_in_order(iterable):  #
    iter = set(list(iterable))
    output = []
    cam = ''
    for i in set(iter):
        if i not in output:
            output.append(i)
    return output

L = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
L.remove(2)
print(L)    #[1, 2, 3, 4, 5, 6, 7, 8, 9]
L.remove(2)
print(L)    #[1, 3, 4, 5, 6, 7, 8, 9]

x = ['a', 'b', 'c', 'd']
y = ['b', 'c']
for i in x:
    if i in y:
        x.remove(i)
print(x)

x = ['a', 'b', 'c', 'd']
y = ['b', 'c']
x_new = []
for i in x:
  if i not in y:
    x_new.append(i)
x = x_new
print (x)