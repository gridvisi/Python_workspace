'''
https://www.codewars.com/kata/59bf97cd4f98a8b1cd00007e/train/python

The sum of divisors of 6 is 12 and the sum of divisors of 28 is 56. You will notice
that 12/6 = 2 and 56/28 = 2. We shall say that (6,28) is a pair with a ratio of 2.
Similarly, (30,140) is also a pair but with a ratio of 2.4.
These ratios are simply decimal representations of fractions.

(6,28) and (30,140) are the only pairs in which every member of a pair is 0 <= n < 200.
The sum of the lowest members of each pair is 6 + 30 = 36.

You will be given a range(a,b), and your task is to group the numbers into pairs with
the same ratios. You will return the sum of the lowest member of each pair in the range.
If there are no pairs. return nil in Ruby, 0 in python. Upper limit is 2000.

solve(0,200) = 36
Test.it("Basic tests")
Test.assert_equals(solve(1,100),6)
Test.assert_equals(solve(1,200),36)
Test.assert_equals(solve(1,300),252)
Test.assert_equals(solve(200,1000),1104)

'''

def divsorSum(x):
    divs = [1]
    for i in range(2,x+1//2):
        if x%i == 0:
            divs.append(i)
    divs.append(x)
    return sum(divs)
x = 6
print(divsorSum(x))

from collections import Counter
def solve(a,b):
    valueNum = {}
    tap,tapp = [],[]
    ans = []
    for i in range(a,b+1):
        value = str(divsorSum(i)/i)
        #tap.append((i,value))
        

        tap.append(value)

    for x in tap:
        for k,v in res.items():
            if v == x:
                ans.append(k)
    return ans,tap

a, b = 1,200
print(solve(a,b))




