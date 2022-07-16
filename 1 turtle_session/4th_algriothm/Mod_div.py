
'''
在晨练中，你要求你的士兵排成5排。您注意到最后一排有3名士兵。
然后你让它们以8个为一排重新形成，最后一行留下7个，
然后是9个人一行，留下2个。
x % 5 == 3
x % 8 == 7
x % 9 == 2
你从来没有计算过你所有的士兵，但现在你有足够的信息来确
定总数，而不必明确说明，避免泄露给敌人可以拦截的士兵数量。
'''

# 暴力枚举
ans = [] #
for n in range(1,200):
    if n%5==3 and n%8==7 and n%9==2:
        ans = n
        ans.append(n)
print('1st solve:',ans)


ans = []
answer = 0
total = 10000
for n in range(total):
    if n%5==3 and n%8==7 and n%9==2:
        ans.append(n)
        answer = n
print(answer)

#
def my_function(): # This is a function definition. Note the colon (:)
    a = 2 # This line belongs to the function because it's indented
    return a # This line also belongs to the same function
print('my_function:',my_function()) # This line is OUTSIDE the function block


a,b = 14,15
if a < b: # If block starts here
    print(a) # This is part of the if block
else: # else must be at the same level as if
    print(b) # This line is part of the else block

x = True # HOLIDAY
y = False # COVID

print(x or y) # if x is False then y otherwise x
print(x and y) # if x is False then x otherwise y
print(not x) # if x is True then False, otherwise True

'''
普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
世纪闰年：必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。
'''

start = 2000
year = 1900

def isRun(year):
    if not year%4 and year%100:   #True
        return "闰年"
    elif not year%400:
        return '闰年'
    return 'not'

print(f"{year}",isRun(year))

print([f"{year}:{isRun(year)}" for year in range(start,year)])


#3 while

def coco(rmb=100,price=3,bonus=3):  #rmb,price,bonus refer to/
    bot = 0
    drink = 0
    empty = 0
    while rmb > 0:
        rmb = rmb-price
        bot += 1
        drink += 1
        empty += 1
        if empty == bonus:
            bot += 1
            empty = 0

    return drink,bot
rmb,price,bonus = 100,3,3
print(coco(rmb,price,bonus))


range(1,10,2)
#print('1'+ 2)

