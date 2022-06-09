'''
https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec/train/python
'''

print(float('-inf'),float('-inf')+5,float('-inf')-5)
print(max(float('-inf')+5,float('-inf')-5))

prices = [10, 7, 5, 4, 1]
def max_profit(prices):
    m = best = float('-inf')
    for v in reversed(prices):
        m, best = max(m, best-v), max(best,v)
        print(m,best)
    return m
print(max_profit(prices))


def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i in prices[1:]:
        if i - min_price > out:
            out = i - min_price
        if i < min_price:
            min_price = i
    return out

s = 1
print(bin(s)[-1],bin(s+1)[-1],bin(s+2)[-1])

prices = [10, 7, 5, 8, 11, 9]
#prices = [10, 7, 5, 4, 1]
prices = [9,9]
prices = [3,6,2,4,9,4,2,6,3]
prices = [10, 7, 5, 4, 1]
print(sorted(prices))
def max_profit(prices):
    s,gap = sorted(prices),len(prices)
    i,j = 0,len(prices)-1
    r,re = 0,[]
    #print(s[j] - s[i],i,j)
    while i < j:
        if prices.index(s[i]) < prices.index(s[j]):
            re.append(s[j] - s[i])
        else:
            re.append(s[i] - s[j])
            #print(re)
        i += int(bin(r)[-1])
        r += 1
        gap -= int(bin(r)[-1])
        j = i + gap-1  #ls-1 - r + int(bin(r-1)[-1])

        print(i,j,re)
    return max(re)
#print(max_profit(prices))


'''
def max_profit(prices):
    s = []
    if prices.index(min(prices)) < prices.index(max(prices)):
        return max(prices) - min(prices)
    for i in range(1,len(prices)):
        s.append(max([x - prices[i-1] for x in prices[i:]]))
    return max(s)

       if step//2 == 0:
            i += 1
            step += 1
        elif step//2 == 1:
            j -= 1
            step += 1
            
        i += int(bin(r)[-1])
        r += 1
        j -= int(bin(r)[-1])
'''


'''
def max_profit(prices):
    if prices.index(min(prices)) < prices.index(max(prices)):
        return max(prices) - min(prices)
    else:
        sl = min(prices[:prices.index(min(prices))-1])
        lr = max(prices[prices.index(min(prices)):])
        return sl,lr,min(prices)-sl,(lr-min(prices))
'''