'''
https://blog.csdn.net/wuhui_gdnt/article/details/88887664
'''

def getNum(n):
    i = 0
    while i <= n:
        yield i
        i += 1
x = getNum(10)
print(getNum(x))


def getNum(n):
    i = 0
    while i <= n:
        yield i
        i += 1
x = getNum(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

'''
#for循环本身就是一个生成器。当我们运行如下所示的代码时，非常占内存，会卡。
a = [x for x in range(10000000)]
print(a)
#换种方式，把它变成生成器：
a = (x for x in range(10000000))
print(a)
#用一下生成一个，不占内存。这里的括号和元祖没关系
'''


name = " Albert Einstein"
str = "If All the bees die on earth, we would die due to not enough food sustain the living"

def name_in_str(str, name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())
#运行程序后，返回是True，说明str这句话恰好顺序包含了
print(name_in_str(str, name))

import string
print(string.ascii_letters[:26])
letter = string.ascii_letters[:26]
letter = letter + ' '
str = "The qick brown fox jumps over a lazy dog"
it = iter(letter)
print('一个都不能少：',all(c in it for c in str.lower()))

def letter_in_str(str, name):

    print(letter,len(str))
    num = (i for i in range(1,28))
    it = iter(letter.lower())
    #f"{next(it)}"
    print(next(num),next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num),next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    print(next(num), next(it) in str.lower())
    return all(c in it for c in str.lower())
#运行程序后，返回是True，说明str这句话恰好顺序包含了a-z
print(letter_in_str(str, name))

letter = string.ascii_letters[:26]
print('t' in letter.lower())

'''

    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
    print(next(num),next(it), next(it) in letter.lower())
    print(next(num),next(it),next(it) in letter.lower())
'''


'''
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())
    print(next(num),next(it), next(it) in str.lower())
    print(next(num),next(it),next(it) in str.lower())

'''