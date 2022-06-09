
print("coffee" or "tea")

print("coffee" and "tea")

# 100 内所有能被3，7整除数？
ans = []
for n in range(1,101):
    if n % 3 == 0 or n % 7 == 0:
        ans.append(n)
print(ans)

'''
公历年份是4的倍数的，一般都是闰年。
但公历年份是整百数的，必须是400的倍数才是闰年。
”要判断某一年是不是闰年，一般方法是用4或400去除
这一年的年份数，如果除得的商是整数而没有余数，
那么这一年是闰年；如果有余数，那么这一年是平年。
'''
year = 2100
# 能整除100，再看能不能整除400

def hundred(n):
    return n % 100 == 0
#n = 101
#print('1、能整除100？',hundred(n))

def fourhundred(n):
    return n % 400 == 0
#n = 800
#print('1、能整除100？',hundred(n))

def four(n):
    return n % 4 == 0

n = 2000



print(year)
if year % 4 == 0 or year % 400 <= 100:
    print("是闰年")
else:
    print("不是闰年")
