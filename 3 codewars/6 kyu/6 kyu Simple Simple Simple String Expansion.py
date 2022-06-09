'''
https://www.codewars.com/kata/simple-simple-simple-string-expansion/train/python
'''
s = '3D2a5d2f'
s = '0d0a0v0t0y'
s = 'abcde'

s = '3d332f2a'
s = '3abc'
s = 'abcde'
s = '3d332f2a'
print((s[0:3]))
def string_expansion(s):
    #res = map(lambda x:int(x),if i.isdigit() == 0  for i in s)
    re,res,st = [],[],''
    for i in s:
        if i.isdigit() == True:
            re.append(int(i))
        else:re.append(i)
    j = 0
    while j < len(re):
        if isinstance(re[j], int) and isinstance(re[j+1], str):
            res.append(j)
        j += 1
    print(res[:2])
    for k,e in enumerate(res):
        print(s[res[k]])
        if k+1 < len(res):
            st += int(s[res[k]]) * (s[res[k]+1 : res[k+1]])
    return st,res

print(string_expansion(s))

'''
        while isinstance(re[j + k], str):
                st += re[j] * re[j + k]
                k += 1
                if isinstance(re[j + k], int):
                    pass
            j = j + k    
'''