'''
https://www.codewars.com/kata/5b358a1e228d316283001892/train/python
Test.assert_equals(get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")
Test.assert_equals(get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*")
Test.assert_equals(get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")
'''

city = "Chicago"  # "c:**,h:*,i:*,a:*,g:*,o:*")
def get_strings(city):
    res = []
    for i in city.lower().replace(' ',''):
        if i not in res:
            res.append(i)
    re = [f'{i}:'+city.lower().count(i)*'*'+',' for i in res]
    return ''.join(re)[:-1]

print(get_strings(city))
print(city.lower().count('c'))
print(set(list(city.lower())))
#print(sorted(set(list(city.lower())),key = list(city)))
#print(getattr(city))

def get_strings(city):
    counts = {}

    for c in city.lower():
        if c.isalpha():
            counts[c] = counts[c] + "*" if c in counts else "*"

    return ",".join([f"{c}:{a}" for (c, a) in counts.items()])