'''
https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples
divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
'''

#Time: 517msPassed: 107Failed: 0

import math
def divisors(n):
    bench = int(math.sqrt(n))+1

    #n恰好是完全平方数 if int(math.sqrt(n)) = math.sqrt(n)+1
    #那么,n的因子成对出现：(1,n),(2,n/2) ...直到sqrt(n)是唯一不成对
    #理由是 n/sqrt(n) == sqrt(n)
    #结论是只需对完全平方数做特判

    factor = [i for i in range(1,bench) if n%i==0]
    return 2*len(factor)-1 if bench == math.sqrt(n)+1 else 2*len(factor)

'''
Time: 590msPassed: 107Failed: 0
Test Results:
Fixed Tests
Basic Test Cases (7 of 7 Assertions)
Completed in 0.08ms
Random Tests
Testing: 439768, expecting: 16
Testing: 494209, expecting: 9
Testing: 43545, expecting: 8
Testing: 123806, expecting: 8
Testing: 206200, expecting: 24
Testing: 240833, expecting: 8
Testing: 108241, expecting: 9
Testing: 191844, expecting: 27
Testing: 222953, expecting: 2
Testing: 32761, expecting: 3
Testing: 115805, expecting: 16
Testing: 427716, expecting: 27
Testing: 1369, expecting: 3
Testing: 163031, expecting: 4
Testing: 32512, expecting: 18
Testing: 403122, expecting: 8
Testing: 140923, expecting: 4
Testing: 489618, expecting: 16
Testing: 321821, expecting: 2
Testing: 152298, expecting: 12
Testing: 454825, expecting: 24
Testing: 13241, expecting: 2
Testing: 404496, expecting: 45
Testing: 492622, expecting: 8
Testing: 122500, expecting: 45
Testing: 452107, expecting: 4
Testing: 65329, expecting: 4
Testing: 269891, expecting: 2
Testing: 26423, expecting: 2
Testing: 175492, expecting: 12
Testing: 166535, expecting: 8
Testing: 67483, expecting: 8
Testing: 413781, expecting: 4
Testing: 67460, expecting: 12
Testing: 359106, expecting: 16
Testing: 194481, expecting: 25
Testing: 260861, expecting: 2
Testing: 471012, expecting: 12
Testing: 91688, expecting: 16
Testing: 3025, expecting: 9
Testing: 441607, expecting: 2
Testing: 3025, expecting: 9
Testing: 14132, expecting: 6
Testing: 7921, expecting: 3
Testing: 274964, expecting: 12
Testing: 442007, expecting: 2
Testing: 369748, expecting: 12
Testing: 218306, expecting: 8
Testing: 156275, expecting: 24
Testing: 376205, expecting: 8
Testing: 455235, expecting: 32
Testing: 32945, expecting: 8
Testing: 491722, expecting: 32
Testing: 283527, expecting: 8
Testing: 132355, expecting: 8
Testing: 428756, expecting: 12
Testing: 408598, expecting: 4
Testing: 215518, expecting: 8
Testing: 484, expecting: 9
Testing: 103763, expecting: 4
Testing: 458329, expecting: 3
Testing: 138457, expecting: 8
Testing: 470820, expecting: 96
Testing: 464057, expecting: 4
Testing: 473599, expecting: 8
Testing: 183926, expecting: 8
Testing: 178821, expecting: 16
Testing: 338075, expecting: 6
Testing: 175094, expecting: 4
Testing: 109551, expecting: 12
Testing: 224736, expecting: 24
Testing: 341346, expecting: 8
Testing: 75625, expecting: 15
Testing: 205165, expecting: 8
Testing: 197136, expecting: 45
Testing: 4489, expecting: 3
Testing: 100679, expecting: 4
Testing: 330339, expecting: 8
Testing: 430523, expecting: 4
Testing: 330012, expecting: 36
Testing: 453223, expecting: 4
Testing: 283911, expecting: 8
Testing: 442968, expecting: 16
Testing: 164087, expecting: 8
Testing: 473882, expecting: 8
Testing: 451003, expecting: 8
Testing: 480255, expecting: 16
Testing: 333958, expecting: 4
Testing: 143315, expecting: 4
Testing: 173864, expecting: 16
Testing: 1764, expecting: 27
Testing: 86966, expecting: 16
Testing: 3969, expecting: 15
Testing: 54840, expecting: 32
Testing: 110008, expecting: 8
Testing: 377073, expecting: 6
Testing: 267857, expecting: 2
Testing: 308532, expecting: 24
Testing: 175874, expecting: 8
Testing: 85798, expecting: 4
Completed in 9.49ms
You have passed all of the tests! :)
'''

n = 4096
print(divisors(n))

print(math.sqrt(n))
