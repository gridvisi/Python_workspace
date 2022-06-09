'''
https://www.codewars.com/kata/5ee044344a543e001c1765b4/train/python


Nicky has had Myopia (Nearsightedness) since he was born.
Because he always wears glasses, he really hates digits 00 and he
loves digits 1 and 2. He calls numbers, that don't contain 00 (two consecutive zeros),
 the Blind Numbers. He will give you n, the digit-length of number in 10-adic system,
  and you need to help him to count how many numbers are there of length n, that only
  consist of digits 0, 1 and 2 and are not Blind Numbers.

Note📝
We include 0 in the begin of number also.

The numbers will be very huge, so return the answer modulo 1000000007

Example
n = 3

The answer is 22.
The below list is all 27 possible numbers of length 3, with digits 0-2, and there 5 numbers that contain 00 so we not include those.

[000, 001, 002, 010, 011, 012, 020, 021, 022, 100,
101, 102, 110, 111, 112, 120 121,
122, 200, 201, 202, 210 , 211, 212, 220, 221, 222]
Constraints
1 ≤ n ≤ 500000
'''
#print(len([000, 001, 002, 010, 011, 012, 020, 021, 022, 100, 101, 102, 110, 111, 112, 120 121, 122, 200, 201, 202, 210 , 211, 212, 220, 221, 222]))


def blind_number(n):
    a, b = 1, 3
    for _ in range(n):
        a, b = b, (a + b) * 2 % 1000000007
    return a

'''
大数相乘，大数的排列组合等为什么要取模

1000000007是一个质数（素数），对质数取余能最大程度避免结果冲突/重复
int32位的最大值为2147483647，所以对于int32位来说1000000007足够大。
int64位的最大值为2^63-1，用最大值模1000000007的结果求平方，不会在int64中溢出。
所以在大数相乘问题中，因为(a∗b)%c=((a%c)∗(b%c))%c，所以相乘时两边都对1000000007取模，
再保存在int64里面不会溢出。

这道题为什么要取模，取模前后的值不就变了吗？

确实：取模前 f(43) = 701408733, f(44) = 1134903170, f(45) = 1836311903, 但是 f(46) > 2147483647结果就溢出了。

_____，取模后 f(43) = 701408733, f(44) = 134903163 , f(45) = 836311896, f(46) = 971215059没有溢出。

取模之后能够计算更多的情况，如 f(46)

这道题的测试答案与取模后的结果一致。

总结一下，这道题要模1000000007的根本原因是标准答案模了1000000007。不过大数情况下为了防止溢出，模1000000007是通用做法，原因见第一点。

关于为什么要取素数作为模
————————————————
版权声明：本文为CSDN博主「想想柯西会怎么做」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43849266/article/details/113246560
'''

print('10010000'.count('00')) #[1:2]) #[i:i+2]
#C(n,2) + C(n,3) ... C(n,n)

def blind_number(n):
    cunt = 0
    for i in range(10 ** n + 1):
        if all([str(i).count('00')>=1 for i in str(i)]):
            cunt += 1
    return cunt
n = 3
print(blind_number(n))



def blind_number(n): # bruce is not good
    ans = []
    if len(str(n).split("00")) >= 2:
        ans.append(n)
    return ans