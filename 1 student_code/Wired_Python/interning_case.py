#1 interning
# is, ==, 'phil'.split("") ?

name = 'phil'
n,a,m,e = list(name)

x = ['p', 'h', 'i', 'l']
y = ''.join(['p', 'h', 'i', 'l'])
z = 'p' + 'h' + 'i' + 'l'
print(n,a,m,e,list(name),x,y,z)

print('x is list(name):',x is list(name))
print('name is y:',name is y)
print('name is z:',name is z)



#2 in or not in
a = True

b = False
print(not a == b)

#print(a == not b)


m = []
n = []
print(m == n, m is n)
print('m in n:',m in n)
p = ''
print('p in m:',p in m)

#print(True==1,True is 1)
# #SyntaxWarning: "is" with a literal. Did you mean "=="?

print(True == 1,False == 0)
print((1 == 1) in [1])
print(1 == (1 in [1]))
print('True in [1]:',True in [1])

print(1 <= (0 < 1))
print(1 < 0 < 1)
print(1 < 2 < 3)

#3 [[]]

print('3 [[]]:',[] == False, [[]] == True)
#if []:
#    print('not ')

print('what happen when we use nest list?')
boo = []
print('[]:',all(boo)) #'type' object is not iterable
print('[]+[]:',all(boo + []))
print('[]+[]+False:',all(boo + [] + [False]))
print('[]+[]+ZERO:',all(boo + [] + [0]))
print('[]+[]+True:',all(boo + [] + [1]))

boo = [[]]
print('[[]]:',all(boo))

# Very tricky ???
boo = [[[]]]
print('[[[]]]',all(boo))

boo = [[[[[]]]]]
print('[[[[]]]]',all(boo))

if boo:
    print('yes, trigger if statment')
else:
    print('Do not trigger if statment')

print(all(boo))





#4 {}

d = {0:'hello',1:'world'}
d[1.0] = 'china'

print(d)
print(hash(1) == hash(1.0))