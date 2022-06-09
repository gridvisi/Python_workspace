'''
https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]

output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
'''

def to_csv_text(array):
    ans = ''
    for arr in array:
        ans += ','.join([str(i) for i in arr])+"\n"
    return ans[:-1]
array =  [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]
print(to_csv_text(array))

#1st
def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)

'''
import string

print(string.ascii_letters)     # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)            # '0123456789'
print(string.hexdigits)         # '0123456789abcdefABCDEF'
print(string.octdigits)         # '01234567'
print(string.printable)         # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
print(string.punctuation)       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)        # ' \t\n\r\x0b\x0c'
————————————————
版权声明：本文为CSDN博主「YUAYU-」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43835542/article/details/104016897
'''