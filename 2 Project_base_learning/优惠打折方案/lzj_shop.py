

def lzjshop(n:int,c:str): #
    price_sheet = {'bread':3.5,}

    return price_sheet[c] * n

#get
def yournameshop(n: int, c: str):  #
    #n, c = 4, "bread"
    price_sheet = {'bread': 3.5, "coke":3,'water':2,'Sausage':6}
    ans = price_sheet.get(c,f"抱歉没有{c}") * n
    print('ans',ans)
    return ans if isinstance(ans,float) else f"抱歉没有{c}"
n,c = 3,"bread"
n,c = 3,"cup"
n,c = 4,"bread"
n,c = 3,"coke"
#print(yournameshop(n,c))


# discount:d = 80%,

def lzjshop(n,c,d): #d=80%=0.8
    return 10*d


# icecream price zip
icecream = ["ha gendasi","Cold Stone","VIVOLI GELATO",
       "COPPELIA ","Dairy Queen(DQ)","Wall's","que chao",
       "wu yangpai","ba xi","yi li","le keke"]

priceic = [15,5,9,7,11,8,10,4,12,13,14]

price_sheet = list(zip(icecream,priceic))
print('1',price_sheet) #生成价格表
price_sheet = dict(zip(icecream,priceic))
print('2',price_sheet) #生成价格表

#字典：dict = {key：value}"
call = {119:"火警",110:"警察",120:"救护车"}
print(call[119])
print(call.get(911,'i do know'))


#get
def icecreamshop(c: str,n: int):  #
    ans = price_sheet.get(c)
    #print('ans',ans)
    if ans:return ans * n*1.0
    return 0 #f"抱歉没有{c}"


n,c = 3,"cup"
n,c = 4,"bread"
n,c = 3,"ha gendasi"
n,c = 3,"bread"
print(icecreamshop(c,n))




price_sheet = {'ha gendasi': 15, 'Cold Stone': 5, 'VIVOLI GELATO': 9,
               'COPPELIA ': 7,'Dairy Queen(DQ)': 11, "Wall's": 8,
               'que chao': 10, 'wu yangpai': 4,
               'ba xi': 12, 'yi li': 13, 'le keke': 14}

print('Dairy Queen(DQ)',price_sheet['Dairy Queen(DQ)'])


percentage = [17,14,12,11,10,8,7,7,6,5,3]  #销量
sales = [icecreamshop(n, c) for c,n in price_sheet.items()]
print(sales)


percentage.append(11)
print(percentage)

print(price_sheet.keys())
print(price_sheet.values())
print(price_sheet)