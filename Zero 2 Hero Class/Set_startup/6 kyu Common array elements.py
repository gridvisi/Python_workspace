'''
https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python

Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example:

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
More examples in the test cases.

Test.it("Basic tests")
Test.assert_equals(common([1,2,3],[5,3,2],[7,3,2]),5)
Test.assert_equals(common([1,2,2,3],[5,3,2,2],[7,3,2,2]),7)
'''

#1st
from collections import Counter
def common(a,b,c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

#2nd
def common(a,b,c):
    a.sort() ; b.sort() ; c.sort()
    i = j = k = c1 = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            c1 += a[i]
            i += 1 ; j += 1 ; k += 1
        elif a[i] < b[j] : i += 1
        elif b[j] < c[k] : j += 1
        else : k += 1
    return c1

#fail try
from collections import Counter
def common(a,b,c):
    setabc = set(a) & set(b) & set(c)
    A = Counter([i for i in a if i in setabc])
    B = Counter([i for i in b if i in setabc])
    C = Counter([i for i in c if i in setabc])
    return sum([n[0]*n[1] for n in min([[(k,v) for k,v in A.items()],[(k,v) for k,v in B.items()],[(k,v) for k,v in C.items()]],key=lambda x:x[1])])
a,b,c = [1,2,2,3,3],[5,3,2,2],[7,3,2,2,2]
print(common(a,b,c))
print((Counter(a) & Counter(b) & Counter(c))  )
'''
Test Results:
Execution Timed Out
STDERR
Execution Timed Out (12000 ms)

#all([x in a and x in b and x in c for x in setabc])
# sum([x==y==z for x,y,z in zip(a,b,c)])
#print([(x,y,z) for x,y,z in zip(a,b,c)])

    print([[(k,v) for k,v in A.items()],[(k,v) for k,v in B.items()],[(k,v) for k,v in C.items()]])

    print(A,B,C)
max([A.items(),B.items(),C.items()],key=lambda x:x.values())
    return max([A.items(),B.items(),C.items()],key=lambda x:x.values())
AttributeError: 'dict_items' object has no attribute 'values'
'''