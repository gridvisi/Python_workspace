'''
  Python's f-strings are amazingly fast!

 f-strings有着神奇的执行效率
'''
x,y = 1,2
def add(x, y, *args, **kwargs):
    print(f"x={x}, y={y}")
print(add(x, y))

add(y=2, x=1)
print(add(x, y))  #x=1, y=2

'''
第二种方式看似更灵活，出错的风险也增加了，特别是多人合作的项目中。
那么如何从语法层面上禁止这样调用，避免出错呢？
这里就可以使用Python3.8中的仅位置参数语法了，在函数定义时，参数之间可指定一个斜杠（/），
斜杠前的参数严格遵守仅位置参数的定义，例如：
'''
'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：857662006 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
def add(x, y, /, *args, **kwargs):
    print(f"x={x}, y={y}")
print('/',add(1,2))  #x=1, y=2

def increment_1 (amt, discount, /):
    return amt+1+discount
amt,discount = 1,0.5
print(increment_1(amt, discount))

import time
s,t = 'hello','world'
'''
f'{s} {t}'               # 78.2 ns
s + '  ' + t             # 104 ns
' '.join((s, t))         # 135 ns
'%s %s' % (s, t)         # 188 ns
'{} {}'.format(s, t)     # 283 ns
#Template('$s $t').substitute(s=s, t=t)  # 898 ns
'''

st = time.time()
print(f'{s} {t}')
end = time.time()
print(st - end)


'''
海象表达式 :=
新的语法 := 将给变量赋值, 这个变量是更大的表达式的一部分.

'''
a = 'hello world'
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
elif (n := len(a)) <= 10:
    print(f"List is short ({n} elements, expected <= 10)")
#用在 if 判断中, 避免调用 len() 两次.

import re
discount = '80%'
advertisement = '=70%'
if (mo := re.search(r'(\d+)% discount', advertisement)):
    print(mo.group(1), mo.group(0))
    discount = float(mo.group(1)) / 100.0
print(discount)
#正则表达式匹配和获取结果的时候.

#https://www.cnblogs.com/awakenedy/articles/9182036.html
#https://www.cnblogs.com/huigebj/p/11259449.html
from how_to_time import how_to_time
from how_to_time import time
import how_to_time
user = 'eric_idle'
member_since = how_to_time.date(1975, 7, 31)
print(f'{user=} {member_since=}')
"user='eric_idle' member_since=datetime.date(1975, 7, 31)"

#通常的 f - 字符串格式说明符 允许更细致地控制所要显示的表达式结果:

delta = how_to_time.date.today() - member_since
f'{user=!s} {delta.days=:,d}'
'user=eric_idle delta.days=16,075'

# 说明符将输出整个表达式，以便详细演示计算过程:
import math
theta=30
print(f'{theta=} {math.cos(radians(theta))=:.3f}')
#math.cos(radians(theta))=0.866



'''
# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)
#用在 while 循环中, 可以同时取值, 并判断是否为空.

clean_name.title() for name in names
 if (clean_name := normalize('NFC', name)) in allowed_names
'''

