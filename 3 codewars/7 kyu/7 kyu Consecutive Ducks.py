'''
https://www.codewars.com/kata/consecutive-ducks/train/python
if i element sum is n, min of element is ?
suppose min num is x
x*i + sum[i for i in range(0,i)] = n
x = (n - sum[i for i in range(0,i)])/i
so key is that iter i make above left equal to right


 test.assert_equals(consecutive_ducks(69), True)
        test.assert_equals(consecutive_ducks(8), False)
        test.assert_equals(consecutive_ducks(57), True)
        test.assert_equals(consecutive_ducks(6), True)
        test.assert_equals(consecutive_ducks(13), True)
        test.assert_equals(consecutive_ducks(16), False)
        test.assert_equals(consecutive_ducks(91), True)
        test.assert_equals(consecutive_ducks(75), True)
        test.assert_equals(consecutive_ducks(38), True)
        test.assert_equals(consecutive_ducks(25), True)
        test.assert_equals(consecutive_ducks(32), False)
        test.assert_equals(consecutive_ducks(65), True)
        test.assert_equals(consecutive_ducks(13), True)
        test.assert_equals(consecutive_ducks(16), False)
        test.assert_equals(consecutive_ducks(99), True)
    @test.it("Check Medium Values")
    def __():
        test.assert_equals(consecutive_ducks(522), True)
        test.assert_equals(consecutive_ducks(974), True)
        test.assert_equals(consecutive_ducks(755), True)
        test.assert_equals(consecutive_ducks(512), False)
        test.assert_equals(consecutive_ducks(739), True)
        test.assert_equals(consecutive_ducks(1006), True)
        test.assert_equals(consecutive_ducks(838), True)
        test.assert_equals(consecutive_ducks(1092), True)
        test.assert_equals(consecutive_ducks(727), True)
        test.assert_equals(consecutive_ducks(648), True)
        test.assert_equals(consecutive_ducks(1024), False)
        test.assert_equals(consecutive_ducks(851), True)
        test.assert_equals(consecutive_ducks(541), True)
        test.assert_equals(consecutive_ducks(1011), True)
        test.assert_equals(consecutive_ducks(822), True)
    @test.it("Check Large Values")
    def __():
        test.assert_equals(consecutive_ducks(382131), True)
        test.assert_equals(consecutive_ducks(118070), True)
        test.assert_equals(consecutive_ducks(17209), True)
        test.assert_equals(consecutive_ducks(32768), False)
        test.assert_equals(consecutive_ducks(161997), True)
        test.assert_equals(consecutive_ducks(400779), True)
        test.assert_equals(consecutive_ducks(198331), True)
        test.assert_equals(consecutive_ducks(325482), True)
        test.assert_equals(consecutive_ducks(88441), True)
        test.assert_equals(consecutive_ducks(648), True)
        test.assert_equals(consecutive_ducks(65536), False)
        test.assert_equals(consecutive_ducks(323744), True)
        test.assert_equals(consecutive_ducks(183540), True)
        test.assert_equals(consecutive_ducks(65271), True)
        test.assert_equals(consecutive_ducks(5263987), True)

solution 2nd
square = 2*n
(st + st + i) * i == 2*n  judge st is integer
st = 0.5*(2*n - i*i)/i
'''
import math
n = 2048
def consecutive_ducks(n):
    i = 2
    while i <= int(math.sqrt(n))+1:
        s = sum([j for j in range(i)])
        #print(s)
        if (n - s) % i == 0:
            #print(n-s)
            return True, i, [int((n - s) / i + j) for j in range(i)]
        else:i += 1
    return False

print(consecutive_ducks(n))

import math
def consecutive_ducks(n):
    return math.ceil(math.log(n,2))!=math.floor(math.log(n,2))

from math import log2
def consecutive_ducks(n):
    return not log2(n).is_integer()

def consecutive_ducks(n):
    return bin(n).count('1') != 1

def consecutive_ducks(n):
    return bool(n & (n - 1))

a,b = 10,5
print('bin:',bin(a),bin(b))
print('and:',a and b)
print('&:',a & b,bool(a & b))

#https://blog.csdn.net/weixin_43946756/article/details/86565014
#https://www.cnblogs.com/goddog1024/p/11236884.
'''
& 是位运算；and 是逻辑运算。
>>> a = 1
>>> b = 2
>>> #1 的二进制是 1，2的二进制是 10
>>> a&b
0
>>> a and b
2

注：a,b分别是整数1和2，以二进制表示分别为：01，10。
&运算结果的二进制为：00，即十进制的 0（按位逻辑运算）。
再如 ：2&3，二进制表示为 10&11，所以结果是 10，即十进制的 2。
1 是真，2是真（整数0是否），所以 1 and 2 是真， 0 and 2 是否
'''
print(bool(2))

consecutive_ducks=lambda n:not __import__("math").log2(n).is_integer()

n = 32 #323744
# from zero to x , if sum[i for i in range(x)] = n
# what is x?  x*(1+x) = n so i should be less than x

def consecutive_ducks(n):   #time out 12000ms
    if n%2 == 1:
        return True
    else:
        for i in range(3,int(math.sqrt(n)),2):
            if n%i == 0:
                return True
    return False,i

print(consecutive_ducks(n))

'''

    i = 2
    while i < int(math.sqrt(n)):
        if (2*n - i*i) % (2*i) == 0:
            st = (2*n - i*i)//(2*i)
            if sum([st+j for j in range(i)]) == n:
                return True#st,[st+j for j in range(i)],sum([st+j for j in range(i)])
        i += 1
    else:return False
'''