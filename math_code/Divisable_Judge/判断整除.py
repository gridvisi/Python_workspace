'''
1.能被9整除的数，各个位之和能被9整除。
2.能被11整除的数，奇数位数字之和与偶数位数字之和的差，能被11整除。
3.一个3位以上的数字，能被7（9或11）整除的特征是，a = 他的后三位，b = 除了后3位以外的数字，
两者差的绝对值能被7（9或11）整除。

'''
def div_seven(n,move=[]):
    next_n = n//10 - 2*(n%10)
    print(next_n)
    move.append(next_n)
    if next_n <= 10:return move
    return div_seven(next_n,move)
n = 28282863
print(div_seven(n,move=[]))



print (divmod(6,3))
print('test',divmod(1000,3))
print('test',divmod(1000,17))

three_div = []
for i in range(100,1000+1,100):
    three_div.append([i,i // 3,i % 3])
print(three_div)

three_div_pow = []
ans = []
for i in range(10):
    three_div_pow.append([10**i,10**i // 3,10**i % 3])
    ans.append(divmod(10**i,3))
print(all(i[1] == 1 for i in ans))
print(three_div_pow,ans)

# x * 10**digit == x * (9*(digit-1) +1) == divmod(x*10**digit,3) == 1 #True
# 整除3的判断：等价于10**digit除以3的余数是x*1，推导可得，判断sum(x)可否整除3是等价问题

# 整除7的判断：等价于10除以7余数为3，10的n倍的余数是3*n，推导可得，判断sum(3*n + unit)可否整除7是等价问题
# 对于整数N=ma=10*m+a；a为个位。若m-2a=7b，即可以被7整除
