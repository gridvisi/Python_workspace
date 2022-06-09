#print('a'&'b','a'&'o','b'&'o') TypeError: unsupported operand type(s) for &: 'str' and 'str'
print('a'* 0,set('aa'))
print('&:',1&1,0&0,0&1,'^:',0^0,0^1,1^0,1^1)
print('w[x]!=w[y]:', 1+(1 != 0))
print('~~',~(0|0),(~0|~0))



blood = ['A','B','O','AB']

def parent_kids(father,mother):
    f,m = father,mother
    blood = ['A', 'B', 'O', 'AB']
    rule = {
        'O':['o','o'],
    'A':['a','o'],
    'B':['b','o'],
    'AB':['a','b']
    }
    w = {'a': 1, 'b': 1, 'o': 0}  # weight
    comb = [(x+y) for x in rule[f] for y in rule[m]]
    #it = iter([i.upper() for i in comb])
    return set([x[0].upper() if x[0]==x[1] else (x[0]*w[x[0]]+x[1]*w[x[1]]).upper() for x in comb])

father,mother = 'B','AB'
father,mother = 'O','O'
father,mother = 'A','A'
father,mother = 'A','B'
father,mother = 'A','AB'
#father,mother = 'O','AB'

print(parent_kids(father,mother))

#[x*w[x]+y*w[y] for x in rule[f] for y in rule[m]]
#[(x*w[x]+y*w[y])*(w[x]|w[y])+'o'*(w[x]^w[y]) for x in rule[f] for y in rule[m]]
#[(next(it)).upper() if n!='' else 'O'for n in comb]
#[next(it) if it.upper()==x else x for x in blood],comb
#[next(comb).upper() if len(x)==2 for x in next(comb) else ]
# #set(rule[father] + rule[mother]),comb
'''
    odds = iter(sorted((n for n in arr if n & 1)))
    return [next(odds) if n & 1 else n for n in arr]
'''



def parent_kids_blood():
    re = {}
    rule = {
        'O':['o'],
    'A':['a','o'],
    'B':['b','o'],
    'AB':['a','b']
    }
    for i in blood:
        for j in blood:
            key = f"{i}"+'+'+f"{j}"
            print(key)
            re[key] = sorted([x+y for x in rule[i] for y in rule[j]])
    return re,len(re)
father,mother = 'A','AB'
print(parent_kids_blood())

# O为隐性基因
'''
ao = A
bo = B
oo = O 
'''
element = 'oa'
blood_type = [x.upper() for x in element if x != 'o']
if blood_type == []:blood_type.append('O')
print("blood type:",blood_type)

#list(map(lambda x,y:set(rule[x] + rule[y]),(x for x in blood),(y for y in blood)))
#list(map(lambda x: x,(x for x in element if x != 'o' else "O")))