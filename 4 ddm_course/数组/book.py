price = [28.9, 32.7, 45.6, 78, 35, 86.2, 27.8, 43, 56, 65]
num = []
str_in = input('请以空格为间隔连续输入一个数组:')
num = [int(n) for n in str_in.split()]
#print(num)
total=[]
for i in range(10):
    total.append(num[i]*price[i])
#print(total)
print(sum(total))

# 1 5 8 10 5 1 1 2 3 4
