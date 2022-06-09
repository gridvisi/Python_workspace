'''
int(x [,base ])         将x转换为一个整数
long(x [,base ])        将x转换为一个长整数
float(x )               将x转换到一个浮点数
complex(real [,imag ])  创建一个复数
str(x )                 将对象 x 转换为字符串
repr(x )                将对象 x 转换为表达式字符串
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )               将序列 s 转换为一个元组
list(s )                将序列 s 转换为一个列表
chr(x )                 将一个整数转换为一个字符
unichr(x )              将一个整数转换为Unicode字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串
Given an array of numbers, you must return a string. The numbers correspond to the letters
of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' '
that are represented by '27', '28' and '29' respectively.

>>> import string
>>> string.ascii_lowercase[:14]
'abcdefghijklmn'
>>> string.ascii_lowercase[:14:2]
'acegikm'
'''
import time
import string
print(string.ascii_lowercase[:26])

s = '64'
print(chr(int(s)))
num = [i for i in range(27,1,-1)]
alpha = string.ascii_lowercase[:26][::-1]
print(alpha)
arr = ['24', '12', '23', '22', '4', '26', '9', '8','28']
def switcher(arr):
    alpha = string.ascii_lowercase[:26][::-1]+'!? '
    #return ''.join([alpha[int(x)-1] for x in arr])
    s = [alpha[int(x) - 1] for x in arr]
    return s
st = time.time()
print(switcher(arr*500))
end = time.time()
print('join的耗时：',end - st)

st2 = time.time()
res = ''
for x in switcher(arr*500):
    res = f'{res}{x}'
print('f:',res)
end2 = time.time()
print('f的耗时：',end2 - st2)

def switcher(arr):
    d = {str(i): chr(123-i) for i in range(1,27)}
    d.update({'27':'!'})
    d.update({'28':'?'})
    d.update({'29':' '})
    d.update({'0':''})
    return ''.join([d[str(i)] for i in arr])

import string
letters = string.ascii_lowercase[::-1] + '!? '
def switcher(arr):
    return ''.join([letters[ch-1] for ch in map(int, arr) if ch])
print(ord('a'),ord('z'))
s = 'WhAt! FiCK! DaMn CAke?'
def borrow(s):
    return ''.join([x.lower() for x in s if ord(x.lower()) >= 97 and ord(x.lower()) <= 122])
#not in ['?','!',' ']])

def borrow(s):
    return ''.join(filter(str.isalpha, s.lower()))

def borrow(s):
    return "".join(c for c in s.lower() if c.islower())

def borrow(s):
    return ''.join([x.lower() for x in s if x.isalpha()])
print(borrow(s))


'''

from xpinyin import Pinyin
pin = Pinyin()
def get(self):
    owner_info = db.query(User).all()
    # 定义一个列表, 将用户的字典信息包含在列表当中
    a = []
    if user_info:
        user = []
        for i in user_info:
            dic = {}
            dic['user_id'] = i.user_id
            dic['user_name'] = i.user_name
            user_name = pin.get_pinyin(i.user_name)  # 默认分割符为-
            a.append({user_name: dic})
        a = sorted(a, key=lambda x: x)
        for i in a:
            # print i.keys()
            user.append(i.values()[0])
        # print(owner)
        return jsonify(code=200, message='ok', data=user)
    else:
        return jsonify(code=404, message='no info', data='')


#原文链接：https: // blog.csdn.net / bin_1022 / article / details / 82229315
'''