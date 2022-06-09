'''
‘and’ ‘or’和‘not’的优先级是not>and>or。

对一批编号为1～100，全部开关朝上(开)的灯进行以下*作：
凡是1的倍数反方向拨一次开关；
2的倍数反方向又拨一次开关；
3的倍数反方向又拨一次开关……
问：最后为关熄状态的灯的编号。
#print(1^0)  #^运算符为异或运算
a异或b = (a and (not b) ) or ( (not a) and b)
'''
print(5&7)  #与（&）返回101（5=101,7=111，按位与，相同得同，相异为0）
print(5|7)  #或（|）返回111（5=101,7=111，按位或，有1得1，全0得0
print(5^7)  #异或（^（shift+6）） 返回010（5=101,7=111，按位异或，相同得0，不同得1）
print(~5^7) #返回010（5=101,按取反）
print(~5)
a,b = bin(0),bin(1)
print(a and b)
print(a or b)
a,b = 1,0
print(a and b)

str1 = 'python'
str2 = ''
list1 = ['python']
list2 = []
tup1 = ('python')
tup2 = ()
dic1 = {'python':1}
dic2 = {}

print('1 ',str1 and list1)
print('2 ',str1 and list1 and list2)
print('3 ',str2 and list2)
print('4 ',str1 and str2)
print('5 ',str1 or list2)
print('6 ',str2 or list2)
print('7 ',str1 or str2)
print('8 ',str1 or str2 and list1 or list2)

print('9-1 ',str2 or tup2)
print('9-2 ',tup2 or str2)
print('9-3 ',str2 and tup2)
print('9-4 ',tup2 and str2)

print('10-1 ',list2 or tup2)
print('10-2 ',tup2 or list2)
print('10-3 ',list2 and tup2)
print('10-4 ',tup2 and list2)

print('11-1 ',str2 or dic2)
print('11-2 ',dic2 or str2)
print('11-3 ',str2 and dic2)
print('11-4 ',dic2 and str2)

print('12-1 ',list2 or dic2)
print('12-2 ',dic2 or list2)
print('12-3 ',list2 and dic2)
print('12-4 ',dic2 and str2)

print(([] or {}),({} or []))

print((0 or 1),(1 or 0),(0 and 1),(1 and 0))
print((1 or 0),(0 or 1),(1 and 0),(0 and 1))

print((2 or 1),(1 or 2),(2 and 1),(1 and 2))