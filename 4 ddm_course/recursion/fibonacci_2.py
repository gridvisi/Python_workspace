__author__ = 'Administrator'

def max_min(x, y, z):
    max = min = x
    if y > max:
        max = y
    else:
        min = y
    if z > max:
        max = z
    else:
        min = z
    return (max, min)
print(max_min(15, 10, 39))
print( 3< 5< 55<66)


def smart_fibonacci(n):
    a, b = 0, 1
    for i in range(1,n):
        a, b = b, a+b
    return b

print(smart_fibonacci(10))

def num_operations_fibonacci(n):
    if n in [1, 2]:
        return 0

    else:
        return num_operations_fibonacci(n - 1) + num_operations_fibonacci(n - 2) + 1#?

print(num_operations_fibonacci(10))

#num = [' ','A','B','C','D','E','F','G']
#num = [' ','c','d','e','f','a','b','G']
loop = 'abcdefg'
print(list(loop))

def looper(loop):
    i = 0
    num = list(loop)
    i+=1
    load = num[i]
    num[i] = num[i+2]
    num[i+2] = load

    while i < 4:
        looper(loop)
        loop+=1
        str = num[1]+num[2]+num[3]+num[4]+num[5]+num[6]+num[7]
    return str
print("result :",looper(loop))
#str_loop = list(str)
#print(str_loop)
'''
i = 0
loop = looper(num)
while i < 100:
    arr = looper(loop)
    print(arr)
    #str = list(arr)
    result = looper(str)
print(result)
'''