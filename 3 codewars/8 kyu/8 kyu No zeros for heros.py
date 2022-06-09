'''
https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
'''
n = 13400
n = 0
def no_boring_zeros(n):
    for i in range(len(str(n))):
        n = n/10
        if n == 0:return 0
        if int(n) != n:
            return int(n*10)

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

#int(''.join([i for i in str(n)[::-1] if i != 0][::-1]))

print(no_boring_zeros(n))

'''
def no_boring_zeros(n):
    i = 1
    while n/(10**i) == int(n/(10**i)):
        i += 1
    return n//(10**(i-1))
    
    for i,e in enumerate(str(n)[::-1]):
        if e != 0:
            pass
        return str(n)[:len(str(n)) - i]
'''