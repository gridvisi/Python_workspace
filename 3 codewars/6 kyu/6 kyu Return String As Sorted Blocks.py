'''
https://www.codewars.com/kata/5e0f6a3a2964c800238ca87d/train/python

Test.assert_equals(blocks("21AxBz"), "xzAB12")
Test.assert_equals(blocks("abacad"), "abcd-a-a")
Test.assert_equals(blocks(""), "")

heyitssampletestkk
'heyitsampletestkks' should equal 'aehiklmpsty-ekst-est'
'''
from itertools import groupby
from collections import Counter
s = "abacad"
sl = Counter(s) - Counter('abc')
print(sl)

xl = 'dingdingmao12PYTHON'

sort = lambda c: (c,c.isupper(),c.isdigit())
xlsort = Counter(xl)
print('xl:',sorted(xlsort,key=sort))



#s = "21AxBz"
#s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#print(list(group) for c, group in groupby(list(s)))
#print('group:',list(''.join(group) for c, group in groupby(list(s))))


from collections import Counter

def blocks(s):
    sort = lambda c: (c.isdigit(), c.isupper(), c)
    answer, counter = [], Counter(s)
    while counter:
        block = ''.join(sorted(counter, key=sort))
        print('block:',block)
        answer.append(block)
        counter = counter - Counter(block)
        print('counter:',counter,Counter(block))
    return '-'.join(answer)

s = ''
s = "21AxBz"  #"xzAB12"
#s = 'heyitssampletestkk'  # 'aehiklmpsty-ekst-est'
s = "abacad"
#print('all:',all([i==1 for i in Counter(s).values()])) #Counter(s).values())
print(blocks(s))

# sort
  
sort = lambda c: (c.isdigit(), c.isupper(), c)



def blocks(s):
    if len(s) == 0:
        return ''
    ls = sorted(s, key=lambda c: c.lower() if c.isupper() else c.upper())
    ls = sorted(ls, key=lambda i:i.isdigit())
    #key = sorted([i for i in ls if ls.count(i)>1])
    ans = []
    res = dict([[k,v] for k,v in Counter(ls).items()])
    if all([i==1 for i in Counter(s).values()]):
        return ''.join(res)

    minloop = min([v for k,v in Counter(ls).items()])
    print(minloop,res)
    i = 0
    while i < minloop+2:
        ans.append('-')
        for k,v in res.items():
            if v > 0:
                ans.append(k)
                res[k] -= 1
            print(ans)
        i += 1
    return ''.join(ans)[1:]                  #''.join(sorted(set(ls))) + ''.join(ans)

#"abacad", "21AxBz" : "xzAB12")
s = ''
s = "21AxBz"  #"xzAB12"
#s = 'heyitssampletestkk'  # 'aehiklmpsty-ekst-est'
s = "abacad"
print('all:',all([i==1 for i in Counter(s).values()])) #Counter(s).values())
print(blocks(s))

s = "123ABCabc"
s = "21AxBz"
s = sorted(s, key=lambda c: c.lower() if c.isupper() else c.upper())
print(sorted(s, key=lambda i:i.isdigit()))



# 3rd try by eric
def blocks(s):
    if len(s) == 0:
        return ''
    ls = sorted(s, key=lambda c: c.lower() if c.isupper() else c.upper())
    ls = sorted(ls, key=lambda i:i.isdigit())
    #key = sorted([i for i in ls if ls.count(i)>1])

    res = [[k,v-1] for k,v in Counter(ls).items() if v >= 2]
    ans,minloop = [],min([v[1] for v in res])
    print(minloop)
    i = 0
    while i <= minloop:
        for v in res:
            if v[1] > 0:
                ans.append(v[0])
                v[1] -= 1
                print('ans',ans)
        i += 1
    return ''.join(sorted(set(ls))) + ''.join(ans)


# 2nd try by eric
def blocks(s):
    if len(s) == 0:
        return ''
    ls = sorted(s, key=lambda c: c.lower() if c.isupper() else c.upper())
    #print(sorted(ls))
    #ls.sort(key=str.lower)

    ls = sorted(ls, key=lambda i:i.isdigit())
    key = sorted([i for i in ls if ls.count(i)>1])
    #print(key)

    re_l,re_r = ls,[]
    res = [[k,v-1] for k,v in Counter(ls).items() if v >= 2]
    #print(res)
    round = 0
    while round <= min([i[1] for i in res]):
        print(min([i[1] for i in res]))
        re_r.append('-')
        for e in res:

            if e[1] > 1:
                e[1] -= 1
                re_r.append(e[0])
        round += 1
    print('r', re_r, res)
    return ''.join(sorted(set(ls))) + ''.join(re_r)

# 1st try by eric
def blocks(s,re_l=[]):
    ls = sorted(s, key=lambda c: c.lower() if c.isupper() else c.upper())
    print(sorted(ls))
    #ls.sort(key=str.lower)
    ls = sorted(ls, key=lambda i:i.isdigit())
    print(ls)
    i,j,re_l,re_r = 0,1,ls,['-']
    while i+j < len(ls)-1:
        j = 1
        if ls[i] == ls[i+j]:
            re_r.append(f"{ls[i+j]}")
            print(ls[i],ls[i+j],re_r)
            re_l[i] = ''
            j += 1
        else:
            i += 1
    if len(set(list(re_r))) != len(list(re_r)):
        return blocks(re_r,re_l)
    return ''.join(re_l + re_r),ls