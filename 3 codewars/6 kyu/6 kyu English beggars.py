'''
https://www.codewars.com/kata/english-beggars/train/python
'''

values,n = [1,2,3,4,5],3

def beggars(values, n):
    beg_res,l = [],len(values)
    for st in range(0,n):
        arr = values[st:l:n]
        beg_res.append(sum(arr))
    return beg_res

def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]

def beggars(a, n):
    return [sum(a[i::n]) for i in range(n)]

def beggars(values, n):
    if n == 0:
        return []
    i=0
    take=[]
    for x in range(n):
        take.append(0)
    for val in values:
        take[i%n]=take[i%n]+val
        i= i + 1
    return take

print(beggars(values, n))
