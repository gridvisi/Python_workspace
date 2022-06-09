#https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python

s = "codewars"

def capitalize(s): #Top 1
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]

def capitalize(s):#fault
    re = []
    for i,e in enumerate(list(s)):
        if i%2 == 0:
            re.append(e.upper())
        else:
            re.append(e)
    return [''.join(re),''.join(re).swapcase()]
print(capitalize(s))



def capitalize(s):#fault
    re = ''
    it = iter(s)
    while it:
        re += next(it).upper()
        re += next(it)
    return [re,''.join([x.swapcase() for x in re])]
print(capitalize(s))

def capitalize(s): #fault
    re = ''
    it = iter(s)
    for i in range(len(s)//2):
        re += next(it).upper()
        re += next(it)
    return [re,''.join([x.swapcase() for x in re])]
print(capitalize(s))

#fault reason :['AbRaCaDaBr', 'aBrAcAdAbR'] should equal ['AbRaCaDaBrA', 'aBrAcAdAbRa']
def capitalize(s): #fault
    it = [s[i].upper()+s[i+1] for i in range(len(s)) if i%2 == 0]
    return [''.join(it),''.join([i.swapcase() for i in it])]

print(capitalize(s))

def capitalize(s): #fault
    it = [(s[i].upper()+s[i+1]) for i in range(0,len(s)-1,2)]
    return [''.join(it),''.join([i.swapcase() for i in it])]

def capitalize(s):  #fault
    it = iter(list(s))
    #sr = (next(it).upper if s.index(next(it))%2 == 0 else next(it))
    return list(it)
print(capitalize(s))

'''
name_list = ['kzd','ysy','kcw','scr','ky']
name_li = map(upper(), name_list)
print name_l
'''


#TypeError: 'builtin_function_or_method' object is not iterable
#如果遇到object is not iterable这样的的报错，一般是所迭代的对象或者所迭代的对象里面有不可以支持迭代的对象，
# 请把这里的对象进行转换成可以迭代解析的对象即可，我这里遇到的是把对象转化成张量就好了