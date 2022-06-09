
'''
case 2nd
python 字符串补全填充固定长度（补0）的三种方法
原字符串左侧对齐， 右侧补零:
'''
s = '100'  #input: '100'.ljust(32,'0')
width = 8
#str.ljust(width,'0')
print(s.ljust(width,'*'))
print(s.rjust(width,'*'))
#output: '78900000000000000000000000000000'

#方法二：
'''
input: '123'.zfill(32)
output:'00000000000000000000000000000123'
'''
s = '200'
width = 10
s.zfill(width)
print(s)

#方法三：
'''
'%07d' % n
input: '%032d' % 89
output:'00000000000000000000000000000089'
'''


n = int(input())
print(len(str(n)))

n = int(input('请输入：'))
s = 1
for i in range(1,n+1):
    s *= i
print(s)
#res = lambda x,y:x*y,[i for i in range(1,n)]
print(s)


#print(sum([i for i in range(1,100,2)]))

start = 0
i = 1
end = 'l'

name1 = 'ucas'
name2 = 'eric'
for i in range(0,4):
    end = end + name1[i]
    print(end)
print(end)
