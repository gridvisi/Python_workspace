'''
https://www.codewars.com/kata/57a77726bb9944d000000b06/train/python

There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
For a given quantity and price (per mango), calculate the total
cost of the mangoes.

Examples
mango(3, 3) ==> 6    # 2 mangoes for 3 = 6; +1 mango for free
mango(9, 5) ==> 30   # 6 mangoes for 5 = 30; +3 mangoes for free
'''

# 判断3送2，2送1哪个方案优惠更大？
# 共有10个, 买6个送4个，
# 或者买7个，送3个，

def mango(quantity, price):
    res = ((quantity%5)//3)*2+(quantity%5)%3 if (quantity%5)//3 else quantity%5
    total_32 = ((quantity//5)*3 + res)*price
    total_21 = ((quantity//3)*2 + quantity%3)*price
    return min([total_21,total_32]),total_21,total_32
quantity,price = 10, 1
print(mango(quantity,price))

p = 1
print([mango(q,p) for q in range(1,100)])

def mango(quantity, price):
    if quantity % 5 == 0:
        return (quantity // 5)*3 * price
    elif quantity % 3 == 0:
        return (quantity // 3)*2 * price

quantity,price = 9, 5
quantity,price = 5, 1
print(mango(quantity,price))


#1st
def mango(quantity, price):
    return (quantity - quantity // 3) * price