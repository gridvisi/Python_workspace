
from namedlist import namedlist
nl = namedlist('myList', 'a b c d')

L = ['A', 'B', 'C', 'D']
D = dict(zip(nl._fields,L))
NL = nl(**D)

print(NL)
#myList(a='A', b='B', c='C', d='D')