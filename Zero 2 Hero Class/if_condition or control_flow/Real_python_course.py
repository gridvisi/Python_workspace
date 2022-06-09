d = {'a': 0, 'b': 1, 'c': 0}

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

#2
x,y = 9,11
print('foo') if x < y else print('bar') #good
#if x < y: print('foo') else: print('bar') #wrong

if x < y and x > 10:print('foo')   #good
#if x < y: if x > 10: print('foo')  #wrong

#请问下面输出是多少？
if x < y: print('foo')
elif y < x: print('bar')
else: print('baz')

#2nd solution

x = y = 40
z = 1+x if x > y else y+2
print(z)
#42

z = (1+x) if x > y else (y+2)
print(z)
#42

#3rd solution
s = ('foo' if (x == 1) else
    'bar' if (x == 2) else
    'baz' if (x == 3) else
    'qux' if (x == 4) else
    'quux'
    )
print(s)
'quux'