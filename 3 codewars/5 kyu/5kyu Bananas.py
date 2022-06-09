'''
https://www.codewars.com/kata/bananas/train/python
> "What is your name" said Tim.
"My name" said the mouse "Is Dinglemouse".

> "What were you before the witch turned you into a mouse" said Rose.
"I was a banana" said Dingle the mouse, "So be careful. If you see her, run away!".
- Badjelly the Witch (12:32), Spike Milligan

Kata Task
Given a string of letters a, b, n how many different ways can you
make the word "banana" by crossing out various letters and then
reading left-to-right?
'''
import itertools
s = 'bbananana'

def bananas(s):
    res,f,g = [],[],[]
    l = ls = list(s)
    c = [j for j in range(len(ls))]
    s_dic = dict(zip([i for i in range(len(s))],ls))
    st = list(itertools.combinations([i for i in range(len(s))],len(s) - len('banana')))
    for i in st:
        re = [ls[j] for j in c if j not in i]
        if ''.join(re) == 'banana':
            res.append(i)
    print(res)
    for j in res:
        l = list(s)
        x = convert(l,j,'-')
        g.append(x)
    return g


s = 'bbananana'
l = list(s)
d = (0,2,7)
rep = '-'
def convert(l,d,rep):
    f = l
    for i in d:
        f[i] = '-'
    return ''.join(f)
print(convert(l,d,rep))

print(bananas(s))

'''

def bananas(s):
    st = '0b'+'1'*(len(s) - len('banana'))
    nd = st + '0'* len('banana')
    for i in range(int(st,2),int(nd,2)+1):
        print((i))
        if sum(int(i) for i in list(str(bin(i))[2:])) == len(s) - len('banana'):
            c.append(bin(i))
    
    return c,len(c)   #st,int(st,2),nd,int(nd,2)

print(bananas(s))
'''