
if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

d = {'a': 0, 'b': 1, 'c': 0}

if d.get('b') > 0:
   print('ok',d['b'])

#if d['d'] > 0:
#   print('ok')


if d['a'] > 0:
   print('ok')

elif d['b'] > 0:
   print('ok')

elif d['c'] > 0:
   print('ok')

elif d['d'] > 0:
   print('ok')
else:
    print('not ok')

# case 2nd
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
   print('Hello Xander')
elif name == 'Joe':
   print('Hello Joe')
elif name == 'Arnold':
   print('Hello Arnold')
else:
    print("I don't know who you are!")

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
