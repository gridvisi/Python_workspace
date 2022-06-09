'''
位与运算符运算规则：0&0=0&1=1&0=0，1&1=1

位或运算符运算规则：0|1=1|0=1|1=1，0|0=0

位求反运算符运算规则：~0=1，~1=0，对于整数x有~x=-(x+1)

位异或运算符运算规则：0^0=1^1=0，0^1=1^0=1

左移位运算符运算规则：原来的所有位左移，最低位补0，相当于乘以2

右移位运算符运算规则：原来的所有位右移，最低位丢弃，最高位使用符号位填充，相当于整除2 
————————————————
版权声明：本文为CSDN博主「放下扳手&amp;拿起键盘」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/william_hehe/article/details/85005630
'''
b = 11
print('b',b << 1)
def add_without_plus_op(a,b):
    while b!=0:
        data = a&b
        print(data)
        a = a ^ b
        print(a)
        b = data << 1
        print(b)
    return a

a,b = 7,11
print(add_without_plus_op(a,b))