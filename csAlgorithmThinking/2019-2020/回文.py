
def func(n):  # 方法 2  数组切片
    return str(n) == str(n)[::-1]  # str(n) ==
    # 巧妙地运用切
n = "油灯少灯油"
print(func(n))


def reverse(s):   # 探究下for 循环机制
    re = ''
    for i in range(len(s)-1,  -1,  -1):
        re += s[i]
        print(i)
    return re,i
s = '我爱重庆'
s = 'i am liyanjin'

print(reverse(s))    # 发现没有i == 0 ？ why 迭代终点end is not as same as start


def foo(s):             # 方法 3 递归写法
	if s == "":return s
	else:return foo(s[1:]) + s[0]
#print (foo("Happy New Year"))
#print (reverse("Happy New Year"))

