#1 运用切片，截取字符串s中的'python'，下列哪两个写法是对的？
s = "Life is short, I love python"

print('1:',s[-6:])
print('2:',s[len(s)-6:])
print('3:',s[-1:-6])
print('4:',s[1:6:3])

if 1:
    print('no 1st','lhf')

if 0:  # 0 == False
    print('no 2nd','teacher li')
else:
    print('no 3rd','zhang')

if not(12%3 and 12%4):
    print('apple can be divide by 3 and 4 evently')

if 0 and 0:print('')
if 0 or 1: print('0 or 1')
print('coffee' and 'tea')
print('coffee' or 'tea')

print('---- ----------- --------- -------')


print('4:',s[::6])

#2、对上面的s 操作，想将字符串中的字母：I，改为：you，如何实现？中文意思是“我”改为“你”
s = list(s)
#s.replace('I',"You")

ans = ''              # ans 是一个空字符串的变量，用以接受s里的字符串
for i in list(s):     #注意 字符串里的字母是无法直接修改，需要改为列表格式list
    if i == 'I':
        ans += 'You'  # 条件判断找到I，在相同位置的ans直接添加为you
    else:
        ans += i      # 不符合if条件的，不做改动，原封不动追加到ans
print(ans)


'''
3、变量的命名常见的有三种写法，哪一个是python提倡的写法：

distance_to_nearest_town (Snake Case)
DistanceToNearestTown (Pascal Case)
distanceToNearestTown (Camel Case)

下面的变量命名哪些是错误的？
4square
route66
return
Age
home_address
ver1.3

'''

#4 all() any()的坑记
num = [6,12,18]
num = [6,12,18,24,30,32]
print('2&3:',all([not(i%2) and not(i%3) for i in num]))

#找出1-100内个位和十位都不含素数的，如：14的个位是4，十位是1，都不是素数
#14、10，8都符合要求，但27不是，2和7都是素数

print('------ -----all() ------ any()------ ---')
prim = '2357'
ans = 44
print('1:',all([i in prim for i in str(ans)]))
print('2:',all([i for i in str(ans) if i in prim]))
print('3:',all([1 if i in prim else 0 for i in str(ans)]))
print('4:',[i for i in str(ans) if i in prim])
print('5:',all([[[]]]))

# 高级函数写法：
print(set(str(ans))&set(prim))