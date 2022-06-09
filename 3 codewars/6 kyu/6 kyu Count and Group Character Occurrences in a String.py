'''
https://www.codewars.com/kata/count-and-group-character-occurrences-in-a-string/train/python
'''
s= "Mississippi"
def get_char_count(s):
    n,re,num,dic,value = list(s),{},[],{},[]
    for i,e in enumerate(s):
        if s.count(e) not in num:
            num.append(s.count(e))
        dic.update({e:s.count(e)})
    for j in num:
        for k,v in dic.items():
            if v == j:
                re.update()

    return dic,num,re

def get_char_count(s):
    counts = {}
    for c in (c.lower() for c in s if c.isalnum()):
        print(counts)
        counts[c] = counts[c] + 1 if c in counts else 1
        print(counts,counts[c],c)
    m = {}
    for k, v in counts.items():
        m[v] = sorted(m[v] + [k]) if v in m else [k]
    return m

print(get_char_count(s)) #

res = {1:'m',4:['i','s']}
ls = [1,'b',3]
print(res[4])

'''
   for i in num:
        for k,v in dic.items():
            if v == i:
                value.append([i,k])        
    for k,v in dic.items():
        if v in num:
            print({v:k})
            re.update({v:k})
'''