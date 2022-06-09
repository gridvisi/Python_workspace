__author__ = 'Administrator'
#https://www.cnpython.com/pypi/word2number



#The above is a long addition with some numbers hidden in the boxes. Each box represents a distinct digit from 0 to 9.
#Fill up all the boxes and find the digit not used.

x = [x for x in range(0,10)]
print (",".join(str(i) for i in x))
print(x)

print(2555/9)
print(2555%9)

print((sum([2,5,5,5]))%9)

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
'''