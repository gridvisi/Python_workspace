'''
https://www.codewars.com/kata/5a906c895084d7ed740000c2/train/python

1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
'''
'''
Test Results:
Basic tests
 (6 of 6 Assertions)
Random tests
 (57 of 57 Assertions)
STDERR
Execution Timed Out (12000 ms)
'''
def solve(n):
    s = 0
    sl = [1]
    for i in range(0,n):

        sl = [sum(sl[:i+1]) for i in range(i+1)]
        print(sl)
        s = sum(sl)
    return s
n = 5
print(solve(n))



#2nd
def solve(n):
    t = []
    s = 0
    a,b,c = 1,0,0
    for i in range(0,n):
        t.append((a,b,c))
        #t.append(b)
        #t.append(c)
        b = a+c
        c = b+c
        #c,b = b+c,c
        #t.append(a+b+b)
        s += sum([a,b,c])
    return s,t
n = 5
print(solve(n))
'''
test.assert_equals(solve(4),14)
test.assert_equals(solve(5),42)
test.assert_equals(solve(6),132)
test.assert_equals(solve(7),429)
test.assert_equals(solve(8),1430)
test.assert_equals(solve(20),6564120420)
'''