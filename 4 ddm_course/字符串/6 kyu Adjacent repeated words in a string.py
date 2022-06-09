'''
https://www.codewars.com/kata/5245a9138ca049e9a10007b8/train/python

"dog cat"                 --> 0
"dog DOG cat"             --> 1
"apple dog cat"           --> 0
"pineapple apple dog cat" --> 0
"apple     apple dog cat" --> 1
"apple dog apple dog cat" --> 0
"dog dog DOG dog dog dog" --> 1
"dog dog dog dog cat cat" --> 2
"cat cat dog dog cat cat" --> 3
'''

st = "cat cat dog dog cat cat"
print(st.index('cat'))
def count_adjacent_pairs(st):
    first,st = {}, st.split(' ')
    s = set(st)
    for n in set(st):
        first[n] = ''.join([str(i) if e == n else ' ' for i,e in enumerate(st)])
    return first  #,index_dic


# Top 2nd solution
from itertools import groupby
def count_adjacent_pairs(st):
    return len([name for name,group in groupby(st.lower().split(' ')) if len(list(group))>=2])

st = "dog dog DOG dog dog dog"
st = "dog dog DOG"

# Top 3rd solution
def count_adjacent_pairs(st):
    s, one, two, c = st.lower().split(' '), None, None, 0
    print(s)
    for w in s:
        print(w,two,one,w == one, w != two,w == one and w != two)
        c += w == one and w != two
        two = one
        one = w
    return c
print(count_adjacent_pairs(st))

'''
def count_adjacent_pairs(st):
    st,i,j = ' '.split(st),0,1
    cn = 0
    while i < len(st):
        if st[i] == st[j]:
            j += 1
            cn += 1
        else:
            i = j
    return 
'''