'''
https://www.codewars.com/kata/59a818191c55c44f3900053f/train/python
a = 0011 1100
b = 0000 1101
-----------------

a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011
'''
print(bin(25),bin(28),int(('0b11111'),2))
a = 0b00111100
b = 0b00001101
print(a&b)
print(int(a), int(b))
print(int(a) & int(b))
n = 25
print(int(bin(28),2),bin(25))

n = 1234567  #
def true_binary(n):
    top = ['1']*(len(bin(n))-2)
    minu = (int('0b'+''.join(top),2) - n)//2
    x,y = [int(i) for i in bin(minu)[2:]],[int(i) for i in ''.join(top)]
    s = len(y)-len(x)
    x = s*[0] + x
    print(x)
    for i,e in enumerate(y):
        if x[i] == 1:
            y[i] = -1
    return y
n = 25
def true_binary(n):
    return [(c == '1') * 2 - 1 for c in '1' + bin(n)[2:-1]]
print('top:',true_binary(n))

#print(''.join(re))
m = [int(i) for i in list('0b110010110101101000011')[2:]]


for i,e in enumerate(m):
    if e == 0:
        m[i] = -1
    else:pass

print('mop:',m)
re = [1,1,-1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,1,1]
print('m==re:',m == re)
print(n&(25-2))
print(2&25)
print(bin(32),bin(25))
print(bin(6)[2:])
print(all(i == '1' for i in (bin(6))[2:]))


def true_binary(n):
    if n == 1:return [1]
    elif n <= 3:return [1,1]
    elif n%2 == 1 and n > 3:
        for x in range(2,2**len(bin(n))+1):
            #print('x',x)
            if x & (x + n) == 0 and all(i == '1' for i in bin(x*2 + n)[2:]):
                re = list(bin(x+n)[2:])

                for i, e in enumerate(re):
                    if e == '0':
                        re[i] = -1
                    else:
                        re[i] = 1
                return re   #x,x+n,bin(x+n),bin(x)
n = 1234567
#print(n//431292,n%431292)
#print(true_binary(n))

'''
def true_binary(n):
    re = []
    for i in str(bin(n))[2:]:
        if int(i) == 0:
            re.append(int(i)+1)
        else:
            i = 0
            re.append(i)
    return re
    

    for i,e in enumerate(str(bin(n))[2:]):
        if int(e) == 0:
            re = '1'* i + '0'*(len(str(bin(n))[2:])-i)
    print(re,bin(int('0b'+re,2) - n))
    nav = bin(int('0b'+re,2) - n)[2:]
    res = [int(i) for i in re]
    bench = len(re) - len(nav)
    for i,e in enumerate(nav):
        res[i+bench] = - (int(e))
'''