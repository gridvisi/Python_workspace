icecream = ["ha gendasi","Cold Stone","VIVOLI GELATO",
       "COPPELIA ","Dairy Queen(DQ)","Wall's","que chao",
       "wu yangpai","ba xi","yi li","le keke"]

print('damele' in icecream)
print("Dairy Queen(DQ)" in icecream)

priceic = [15,5,9,7,11,8,10,4,12,13,14]

price_sheet = list(zip(icecream,priceic))
price_sheet = dict(zip(icecream,priceic))
print(price_sheet) #生成价格表
#get
def icecreamshop(c: str,n: int):  #
    ans = price_sheet.get(c) #f"抱歉没有{c}"
    #ans = price_sheet[c]
    #print('ans:',ans)

    if ans: #if True: True,1==True, 0==False
        return f"顾客购买{c}了,总共是:",ans * n*1.0
    else:
        return f"抱歉没有{c}"

n,c = 3,"bread"
n,c = 3,"cup"

n,c = 3,"ha gendasi"
n,c = 4,"bread"

#n,c = 4,"bread"
#f"顾客购买{c}了,总共是:"
print(icecreamshop(c,n))

print(True + True)
print(True + False)
print(False + False)

answer = 0
if answer:print('OKAY')
else:print('no')


print(abs(-1))
print(int(0.01))
print(len("chongqing"))

#if else
#while for loop
#try except

#算法
#递推，