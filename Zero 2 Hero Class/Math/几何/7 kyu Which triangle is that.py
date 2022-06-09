'''
https://www.codewars.com/kata/564d398e2ecf66cec00000a9/train/python

Build a function that will take the length of each side of a
triangle and return if it's either an Equilateral, an Isosceles,
a Scalene or an invalid triangle.

It has to return a string with the type of triangle.
For example:

type_of_triangle(2, 2, 1) --> "Isosceles"


@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(type_of_triangle(1,1,1), "Equilateral""等边")
        test.assert_equals(type_of_triangle(3,2,4), "Scalene")
        test.assert_equals(type_of_triangle(2,2,1), "Isosceles")
        test.assert_equals(type_of_triangle('.',5,82), "Not a valid triangle")

Equilateral等边形
Scalene斜边
Isosceles等腰三角形
Not a valid triangle不是一个有效的三角形
'''

def type_of_triangle(a, b, c):
    if not all([type(i)==int for i in (a,b,c)]):
        return "Not a valid triangle"

    if sum(sorted([a,b,c])[:2]) < max([a,b,c]):
        return "Not a valid triangle"
    else:
        if a == b == c:return "Equilateral"
        if a == b or a == c or b == c:return "Isosceles"
    return "Scalene"

#1st
def type_of_triangle(a, b, c):
    if any(not isinstance(x, int) for x in (a, b, c)):
        return "Not a valid triangle"
    a, b, c = sorted((a, b, c))
    if a + b <= c:
        return "Not a valid triangle"
    if a == b and b == c:
        return "Equilateral"
    if a == b or a == c or b == c:
        return "Isosceles"
    return "Scalene"

#2nd
def type_of_triangle(*S):
    try :
        S = sorted(S)
        if sum(S[:2])<=S[2]:                     return "Not a valid triangle"
        if all(e == S[0] for e in S[1:]) :       return "Equilateral"
        if any(a==b for a, b in zip(S, S[1:])) : return "Isosceles"
        else :                                   return "Scalene"
    except :                                     return "Not a valid triangle"

import math
# Class solution
class Triangle(object):
    '''判断三角形的类型以及面积方法'''
    #定义三角形三边啊a,b,c,;
    def __init__(self,a,b,c):
        self.a=a; self.b=b; self.c=c

    #判断是否构成三角形的方法；
    def isTriangle(self):
        self.a ,self.b, self.c = sorted([self.a ,self.b, self.c])
        if self.a+self.b >= self.c:
            return "能构成三角形"
        else:
            return "不能构成三角形"

    def isEquilateral(self):
        if self.a == self.b == self.c:
            return "Equilateral:等边三角形"
        else:
            return "不能构成等边三角形"

    def isIsosceles(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles：等腰三角形"
        else:
            return "不能构成等腰三角形"

    def isRight_angle(self):
        self.a, self.b, self.c = sorted([self.a, self.b, self.c])
        if round(self.a**2,10) + round(self.b**2,10) == round(self.c**2,10):
            return "能构成直角三角形"
        else:
            return "不能构成直角三角形"

    def area_of_triange(self):
        a,b,c = self.a,self.b,self.c
        return 0.25* math.sqrt((a + b + c)*(a + b - c)*(a + c - b)*(b + c - a))



trianges = [(3,4,5),(5,9,4)]
s = (3,4,5)
s = 2,2*math.sqrt(2),2
s = math.sqrt(3),math.sqrt(3),math.sqrt(6)
print(2**2 + 2**2 == 2**2 * round(math.sqrt(2)**2,10),math.sqrt(2)**2)
if __name__ == '__main__':
    delta = Triangle(*s)
    print(delta.isRight_angle())
    print(delta.isEquilateral())
    print(delta.isIsosceles())
    print(delta.area_of_triange())