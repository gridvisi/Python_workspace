'''
(1 - ¼) * r = ¼ * ½ R  so that r = 1/6 R
L = R+1/6R   = 70/6 cm = 7/60 m
2 pi * sqrt(L/g) = 0.746    2pi*sqrt(0.1m / g) =
https://brilliant.org/practice/simple-harmonic-motion-level-3-4-challenges/?p=2
'''
import math
g = 9.81
R = 10
L = (1 + 1/6) * R
s = 2*math.pi*(math.sqrt(L/g) - math.sqrt(R/g))
print(s)