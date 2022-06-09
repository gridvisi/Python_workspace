'''
https://www.codewars.com/kata/5e98712b7de14f0026ef1cc1/train/python

Task
Create a function that given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases.

In the event that an element appears more than once in the input sequence, only one
of them will be taken into account for the result, discarding the rest.

Input
Sequence of strings. Valid characters for those strings are uppercase and lowercase
characters from the alphabet and whitespaces.

Output
Sequence of elements. Each element is the group of inputs that can be obtained by
rotating the strings.

Sort the elements of each group alphabetically.

Sort the groups descendingly by size and in the case of a tie, by the first element
of the group alphabetically.

Examples
['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] -->
[['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
'''



print('Capital'.lower())
sl = [['Tokyo', 'Kyoto', 'Okyot'], ['Rome'], ['Paris'], ['London', 'Donlon']]
print(list(map(sorted,sl)))


from collections import Counter
def group_cities(seq):
    sl = [i for i in set(seq)]
    key = [''.join(sorted(list(i.lower()))) for i in sl]
    seqdict = dict([(k,[]) for k,v in Counter(key).items() if v])
    for i in seq:
        ki = ''.join(sorted(list(i.lower())))
        seqdict[ki].append(i)
    ans = sorted(list(map(sorted,seqdict.values())),key= lambda x:(len,[0]),reverse=True)
    return ans
seq = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
print(group_cities(seq))


#1st
def group_cities(seq):
    result = []
    sort_result =[]
    seq = list(dict.fromkeys(seq)) #removing  duplicates
    for e, i in enumerate(seq):
        sort_result = [j for j in seq if len(j)==len(i) and j.lower() in 2*(i.lower())]
        if not sorted(sort_result) in result :
            result.append(sorted(sort_result))
    return(sorted(sorted(result),key=len,reverse=True))


#2st
from collections import defaultdict

def group_cities(seq):
    key = lambda s: min(s[i:]+s[:i] for i in range(len(s)))
    d = defaultdict(set)
    for e in seq: d[key(e.lower())].add(e)
    return sorted((sorted(v) for v in d.values()), key=lambda x: (-len(x),x))

students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
print(sorted(students, key=newgrades.__getitem__))
#['jane', 'dave', 'john']


#3nd
def group_cities(seq):
    res = {}
    for w in seq:
        temp = [str(w[i:] + w[:i]).title() for i in range(1, len(w))
                if str(w[i:] + w[:i]).title() in seq]
        temp.append(w)
        res[frozenset(temp)] = sorted(set(temp))
    return sorted(res.values(), key=lambda x: (-len(x), x[0]))

#4th
from collections import defaultdict

def key(s):
    s = s.lower().replace(' ', '')
    return min(s[i:] + s[:i] for i in range(len(s)))

def group_cities(seq):
    result = defaultdict(list)
    for city in set(seq):
        result[key(city)].append(city)
    for cities in result.values():
        cities.sort()
    return sorted(result.values(), key=lambda cities: (-len(cities), cities[0]))



'''
def group_cities(seq):
    key = [''.join(sorted(list(i.lower()))) for i in set(seq)]
    key = [i for i in set(key)]
    seqdict = dict(zip(key,[[]]*len(key)))

    #for k, v in seqdict.items():
    for i in seq:
        ki = ''.join(sorted(list(i.lower())))
        seqdict[ki] = i

    return seqdict

'''
sl = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']
s = sl[0]
def keys(s):
    s = s.lower().replace(' ', '')
    return min(s[i:] + s[:i] for i in range(len(s)))
print('key:',keys(s))

# python按值的长度和字母顺序对字典进行排序
db = {'Carl': [('Intel', 30, 40), ('Dell', 20, 50), ('Intel', -10, 60), ('Apple', 20, 55)],
      'Barb': [('Intel', 20, 40), ('Intel', -10, 45), ('IBM', 40, 30), ('Intel', -10, 35)],
      'Alan': [('Intel', 20, 10), ('Dell', 10, 50), ('Apple', 80, 80), ('Dell', -10, 55)],
      'Dawn': [('Apple', 40, 80), ('Apple', 40, 85), ('Apple', -40, 90)]}
print(sorted(db, key = lambda k: (-len(db[k]), k)))

