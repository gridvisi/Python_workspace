#100 以内
#1 整除3 或者整除 7

result = []
for i in range(101):
    if i % 3 or i % 11:
        result.append(i)
print(result)

print("************************************")

#2 整除3 同时还要整除 7
#code




card = 15
if card % 2 == 0: #it's an even-numbered card: 伪代码
    print("It's even") #announce

if card % 3 == 0: #it's divisible by 3:
    print('announce:',"It's a multiple of 3")

if card % 5 == 0: #it's divisible by 5:
            print('announce',"It's a multiple of 5")

print("************************************")
card = 15
if card % 2 == 0: #it's an even-numbered card: 伪代码
    print("It's even") #announce

else:
    if card % 3 == 0: #it's divisible by 3:
        print('announce:',"It's a multiple of 3")
    else:
        if card % 5 == 0: #it's divisible by 5:
            print('announce',"It's a multiple of 5")

'''

print(3/2,3//2,7%4) #

for i in range(10):
    if i % 2==0 and i % 3==0:
        print(i)

print([u for u in range(1,10,3) if u%2==0 and u%3==0])

print(list(range(0,10,2*3)))

'''