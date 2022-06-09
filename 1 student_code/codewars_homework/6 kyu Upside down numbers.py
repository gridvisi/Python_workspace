'''
https://www.codewars.com/kata/59f7597716049833200001eb/train/python

Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down),
these numbers remain the same.

To clarify, if we write them down on a paper and turn the paper upside down,
the numbers will be the same.

Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range.
For example, solve(0,10) = 3,
because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

from random import randrange as ran
@test.describe('Fixed Tests')
def fixed_tests():

    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(solve(0,10),3)
        test.assert_equals(solve(10,100),4)
        test.assert_equals(solve(100,1000),12)
        test.assert_equals(solve(1000,10000),20)
        test.assert_equals(solve(10000,15000),6)
        test.assert_equals(solve(15000,20000),9)
        test.assert_equals(solve(60000,70000),15)
        test.assert_equals(solve(60000,130000),55)
'''


def solve(a, b):
    exc = '23457'
    cunt = 0
    dic = {'6':'9','9':'6','0':'0','1':'1','8':'8'}
    for i in range(a,b+1):
        s = str(i)
        if len(s) == 1:
            if all([d not in exc for d in s]):
                if ''.join([dic[i] for i in s[::-1]]) == s:
                    cunt += 1
        elif all([d not in exc for d in s]) and s[-1] !="0":
            if ''.join([dic[i] for i in s[::-1]]) == s:
                cunt += 1
    return cunt
a, b = 0,10
#a,b = 60000,130000

print(solve(a,b))


#1st
REV = {'6':'9', '9':'6'}
BASE = set("01869")

def isReversible(n):
    s = str(n)
    return ( not (set(s) - BASE)                                                          # contains only reversible characters
             and (not len(s)%2 or s[len(s)//2] not in "69")                               # does not contain 6 or 9 right in the middle (only for odd number of digits)
             and all( REV.get(c, c) == s[-1-i] for i,c in enumerate(s[:len(s)//2]) ))     # symmetric repartition

def solve(a, b):
    return sum( isReversible(n) for n in range(a,b) )

#2nd
def solve(a, b):
    return sum(str(n) == str(n)[::-1].translate(str.maketrans('2345679', 'XXXX9X6')) for n in range(a, b))


#3rd
table = str.maketrans("69", "96", "23457")

def solve(a, b):
    return sum(1 for n in range(a, b) if f"{n}"[::-1] == f"{n}".translate(table))



#4th
solve=lambda a,b:sum(n==n.translate(n.maketrans('2345679','----9-6'))[::-1]for n in map(str,range(a,b)))



#5th
dictio = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
def solve(a, b):
    return sum(1 for i in range(a,b) if transf(i))

def transf(n):
    n = str(n)
    for i,j in enumerate(n):
        if j not in dictio:
            return False
        elif dictio[j] != n[-i-1]:
            return False
    return True


