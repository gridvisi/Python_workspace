import math
print(bin(10),bin(100),bin(1000))

print(bin(100),bin(100//2 -2),bin((100//2 -2)//8))
# 0b1100100 -> 0b110010 -> 0b110000 -> 0b110 -> 2+2+2
print("以上逆运算过程: ")
print((int('0b110',2) * 2*2*2 + 2) * 2) # 7

#1000 == 0b1111101000
print("1000 分解运算过程: ")
#1 // 2**2, 确保结果末尾数是0，而不是 1
print(bin(1000//2**2))   # 0b11111010
print(bin(1000//2**2 - 2))  # 0b11111000

#2  // 2**2, 确保结果末尾数是0，而不是 1
print(bin((1000//2**2 - 2) // 2**2 ))  #0b111110

#3 无法做 //2 运算，否则商的结果奇数，而通过对 2 加法或者乘法无法获得奇数
#  但可以做减法后
print(bin((1000//2**2 - 2) // 2**2 - 2))
#0b111100

#4 末尾有'00'。继续 //2 运算
print(bin(((1000//2**2 - 2) // 2**2 - 2)//2))
# 0b11110

#5 可做减法
print(bin(((1000//2**2 - 2) // 2**2 - 2)//2 - 2))
# 0b11100

#6 '00' 可以 //2，
print(bin((((1000//2**2 - 2) // 2**2 - 2)//2 - 2) // 2))
# 0b1110

#7 '0' 减去 2
print(bin((((1000//2**2 - 2) // 2**2 - 2)//2 - 2) // 2 - 2))
# 0b1100

#8 '00' // 2
print(bin(((((1000//2**2 - 2) // 2**2 - 2)//2 - 2) // 2 - 2) // 2))
# 0b110

#9 '0' - 2
print(bin(((((1000//2**2 - 2) // 2**2 - 2)//2 - 2) // 2 - 2) // 2 - 2))
# 0b100

#10 '00' // 2
print(bin((((((1000//2**2 - 2) // 2**2 - 2)//2 - 2) // 2 - 2) // 2 - 2) // 2))
# 0b10

#11 '0' - 2
print(bin((((((1000//2*2 - 2) // 2*2 - 2)//2 - 2) // 2 - 2) // 2 - 2) // 2 - 2))
# 0b0 == 0
final = "((((((1000//2*2 - 2) // 2*2 - 2)//2 - 2) // 2 - 2) // 2 - 2) // 2 - 2)"

print(final.count('*')+final.count('//')+final.count('-'))

op = ['*',"//","-"]
num = 0
for i in final:
    if i in op:
        num += 1
print(f"有 {num} 个运算符在 {final}")

# 再进一步，可否总结为算法实现？
# 十进制整数求最少次数的2 * +组合
#1 整除2并且商为偶数，则 //, 数组首尾添加"(",")"
#2 否则，减去 2 即二进制的'10'

from collections import deque
def shortcut(num):

    s = str(num)
    n = num
    s = deque(s)
    while n != 0:
        if (n//2) % 2 == 0:

            s.append('//2')
            n //= 2
        else:
            n -= 2
            s.appendleft('(')
            s.append('-2'+')')
    s = ''.join(s)
    total = s.count('*')+s.count('//')+s.count('-')
    return s,eval(''.join(s)),total
num = 1000
print('short:',shortcut(num))





print((2**2+2) * 2**4 + 2*2) # 6
# = 2**6 + 2**5 + 2**2

print(math.sqrt(500))
print((20 * 24 + 20) * 2)
print('www',((((2**6 + 2)*2 + 2) * 2)+2) * 2)

print((2**(2+2))**2)
print((((2+2+2)*2*2*2 + 2) * 2))  #   = 100  total_op = 7

#print((((2+2+2)*2*2*2 + 2) * 2))
print(62 * 16 + 8)
#print(((2**3 + 2)*(2+2+2) + 2) * 2*2*2 + 2*2*2)
print((14 * 16 + 2**3 + 18) * 2 * 2)
#print((2**3+2 * 2**3+ + 2**3 + 18) * 2 * 2)

print((((2+2+2)*2*2*2 + 2) * 2)*2 * 2*2)

def divTwo(n):
    op = []
    ans = n
    while ans >= 0:
        ans /= 2
        op.append("/")
        ans -= 2
        op.append("-")
    return ans,op
n = 1000
print('divTwo:',divTwo(n))



def binCal(n):
    ans = 0
    b = bin(n)[2:][::-1]
    print(b)
    for i, e in enumerate(b):
        if e == '1':
            ans += i-1
    return ans
s = [10,100,1000]
print([binCal(n) for n in s])


while True:  #
    for i in range(1,5):
        if i == 2:
            print('nest:',i)
    break #


for i in (0, 1, 2, 3, 4, 5, 6):
    if i == 5 or i == 6 or i == 3:
        print(f'现在已经停靠 {i} 层')
        continue
    print('for 循环：',i)



i = 1 # 第一层  input
while i <= 7:   #
    print("电梯指示灯",i)
    if i == 8:  #目的地到丁丁猫 8 层
        print("Breaking from loop, 停止循环，靠停")
        #break
    i += 1 #i = i-1
print('***************',"\n")

# ID identify

age = 10
name = "zhou"

import math
PI = math.pi
print(id(PI)) #PI存在地址 2522348890128

name1 = "ada"
name2 = "zhou"
name3 = "ada"
print(id(name1),id(name2),id(name3))
#print(len(PI))
print(PI,len(str(PI)),str(PI))

#S数据类型
#float  int  complex 复数 1 + j
R = 0.5
R = 1
AREA = str(PI) * R**2
print(AREA)


# User pick two numbers to sum

num1 = float(input("Number 1:"))
num2 = float(input("Number 2:"))

# Add two numbers
plus = num1 + num2
mul = num1 * num2
div = num1 / num2
min = num1 - num2
sum = sum([num1 , num2]) #,num3,num4,
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print(f"plus num1 + num2 = {num1} + {num2} = ", int(num1 + num2))
