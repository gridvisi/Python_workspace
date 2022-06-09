

if __name__=='__main__':
	a,c=map(int,input("Please enter 2 numbers: ").split())
	b=a&c
	print(b)
#  &是按位逻辑运算符，比如5 & 6，5和6转换为二进制是101和110，此时101 & 110=100，100转换为十进制是4，所以5 & 6=4

a,b=map(int,input("Please enter 2 numbers: ").split(' '))
c=a|b
print(c)
#  |是按位或逻辑运算符，比如5|6，就是101|110，得到111=7，所以最后结果为7

a,b=map(int,input("Please enter 2 numbers: ").split(' '))
c=a^b
print(c)
# ^是按位异或逻辑运算符，比如5^6，其实是101^110，结果是011，所以5^6的答案是3


def oddCount(n):
    return n // 2
print(11 == 11.00000000000000009)
print(len('0000000000000000'))
a = 1.00000000000001
b = 1
print(a == b)
print(len(str(a)),str(a))