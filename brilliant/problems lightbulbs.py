'''
https://brilliant.org/problems/lightbulbs/
'''



def bulb_bit(l):
    step, re = 1, []
    while step <= l:
        ind = [0 for i in range(l)]
        for i in range(0,l-step+1):
            slice = range(i,i+step) #[i for i in range(i,i+step)]
            t = ''.join(['1' if i in slice else '0' for i,e in enumerate(ind)])
            re.append(t)
        step += 1
    return re
l = 8
#print(bulb_bit(l))

def flip(x,y):
    re =''
    for i in range(len(x)):
        if x[i] == y[i]: #== '0' or x[i] == y[i] == '1':
            re += '0'
        elif x[i] != y[i]: #(x[i] == '1' and y[i] == '0') or (x[i] == '0' and y[i] == '1'):
            re += '1'
    return re

st = ['0' for i in range(l)]
x, y, z, m = '10000000', '10000000', '11110000', '00001111'

print('xtobin',int('0b'+y,2))

def bflip(x,y):
    re = ''
    for i in range(len(x)):
        re += str(int(x[i]) ^ int(y[i]))
    return ''.join(re)
print(bflip(x,y))

st = bflip(st, x)
st = bflip(st, y)
st = bflip(st, z)
st = bflip(st, m)
print(st)


def status(start,end,l):
    re,st = [],start
    coll = bulb_bit(l)
    for x in coll:
        for y in coll:
            for z in coll:
                for m in coll:
                    #print(x,y,z,m)
                    st = flip(st, x)
                    st = flip(st, y)
                    st = flip(st, z)
                    if st == end:
                        re.append([''.join(x),''.join(y),''.join(z)])
                    else:
                        st = flip(st, m)
                        if st == end:
                            re.append((''.join(x),''.join(y),''.join(z),''.join(m)))

    print('re:',len(re),re)
    final = []
    for i,e in enumerate(re):
        if e[0] == '01010101':
            final.append(e[1:])
    return 'sxyzm:'+f'{len(final)}' + f'{final}'

start,end = '1010','0101'
l = 4
print(status(start,end,l))

'''

def recur(start, x):
    print(start, x)
    it = iter([y, z, m])
    st = flip(start, x)
    if st == end:
        re.append((st, x))
        print(re)
        return re
    else:
        recur(st, next(it))

s = ''.join(['0' for n in range(l)])
coll = bulb_bit(l)                    
'''

def status(start,coll,most,end):
    step,res = 0,[]
    re = []
    st = start
    while step < most:
        for x in coll:
            st = flip(st, x)

            re.append((st,''.join(st),''.join(x),''.join(y),''.join(z)))
    #print('re:'+f'{len(re)}'+f'{re}')
    final = []
    for i,e in enumerate(re):
        if e[0] == '01010101':
            final.append(e[1:])
        #else:return None
    return 'len(final)='+f'{len(final)}' + ' final='+f'{final}'+ ' len(re):'+f'{len(re)}'

start,end = '00000000','01010101'
most = 4
#print(status(s,coll,most,end))



