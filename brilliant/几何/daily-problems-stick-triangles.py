'''
https://brilliant.org/daily-problems/stick-triangles/

If a triangle has sides 1 cm and 6 cm long, which of the following could be
the third side?

Select one or more

2 cm
4 cm
6 cm
8 cm
Actually, none of these could be the other side.
'''

a,b = 1,6

def triangele(a,b):
    #output the integer third side
    return [i for i in range(1,a+b+1) if i < a+b and min(a,b)+i>b]

print(triangele(a,b))