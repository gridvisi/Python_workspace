'''
https://www.codewars.com/kata/5b707fbc8adeaee7ac00000c/train/python

Given two forces (F1 and F2 ) and the angle F2 makes with F1 find the resultant force R and the angle it makes with F1.

input
Three values :

F1
F2 making an angle θ with F1
angle θ
output
An array consisting of two values :

R (the resultant force)
angle R makes with F1 (φ)
notes
Units for each of the following are given as under :

F1 = Newton
F2 = Newton
angle θ = degree
R = Newton
φ = degree
ALGORITHMSPHYSICSGEOMETRYALGEBRAMATHEMATICS

Test.describe("Tests")
Test.it("Sample tests")
R1, P1 = solution(20, 10, 120)
test.assert_approx_equals(R1, 17.320508075688775)
test.assert_approx_equals(P1, 29.999999999999996)
R2, P2 = solution(110, 45, 45)
test.assert_approx_equals(R2, 145.34564710973225)
test.assert_approx_equals(P2, 12.645904708568862)
'''
import math
#print(math.atan(1/math.sqrt(3)),math.tan(1),math.sin(math.pi))

x = 1/math.sqrt(3)
x = -120
#角度转 -》弧度
print('角度转 -》弧度:',math.radians(x))
print(math.sin(x),math.cos(x),math.cos(180-x))
x = math.radians(x)
print(math.sin(x),math.cos(x),math.cos(180-x))
#弧度转 -》角度
print('弧度转 -》角度:',math.degrees(x))
'''
已知：三角形ABC，边长为a,b,c,三个角为A、B、C
则a*a=b*b + c*c - 2bc*cosA,是余弦定理,税后开根得出第三条边长
'''

def solution(force1, force2, theta) :
    theta = math.radians(theta)
    #fx = force2*math.cos(theta) + force1
    #fy = force2*math.sin(theta)
    f = math.sqrt(force1**2 + force2**2 - 2*force1*force2*math.cos(math.pi-theta))
    #p = theta - math.asin(force1*math.sin(theta)/f) if f != 0 else 0
    p = math.acos((force1**2 + f**2 - force2**2)/(2*force1*f))
    print(f,p,theta)
    return f,math.degrees(p) if theta > 0 else math.degrees(p)
force1, force2, theta = 20, 20, -120
print(solution(force1, force2, theta))

'''

def solution(force1, force2, theta) :
    theta = math.radians(theta)
    fx = force2*math.cos(theta) + force1
    fy = force2*math.sin(theta)
    f = math.sqrt(fx**2 + fy**2) if fx > 0 else -math.sqrt(fx**2 + fy**2)

    p = math.acos(abs(fx)/f)
    print(f, fx, fy,p)
    return f,math.degrees(p)
'''

#1st
from math import cos, radians, sin, atan2, degrees, hypot

def solution(f1, f2, theta):
    r = radians(theta)
    x = f1 + f2 * cos(r)
    y = f2 * sin(r)
    return hypot(x, y), degrees(atan2(y, x))

