
import string
item = 'This , is a demo.'
item = item.strip(string.punctuation)
print(item)
s = '   '
print(s.isspace())
'''
去除标点符号方式多种多样，这里介绍两种自己常用的。

1、python自带punctuation包，可以消除所有中文标点符号。

import re,string
from zhon.hanzi import punctuation
text = " Hello, world! 这，是：我;第!一个程序\?()（）<>《》 "
print(re.sub(r"[%s]+" %punctuation, "",text))
Hello world 这是我第一个程序



2、自己定义标点符号集，即可以消除中文标点符号也可以消除英文标点符号。

import re,string
text = " Hello, world! 这，是：我;第!一个程序\?()（）<>《》 "
punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
print(re.sub(r"[%s]+" %punc, "",text))
'''


ss = '我的电话是18827038663，也是微信号，\n 请加入，谢谢\n\n\n'
print(ss.strip('\n'))
print(ss.replace('\n', ''))

import string
delset = string.punctuation
print('string.punctuation:',delset)

line = 'good at python!'
l = line.translate(delset)
print(l)

import re
punctuation = '!,;:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

text = " Hello, world!  "
print(removePunctuation(text))

